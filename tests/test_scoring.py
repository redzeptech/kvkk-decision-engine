from app.rules.scoring import calculate_risk


def test_score_is_in_range():
    incident = {
        "data_types": ["identity", "financial"],
        "special_category": False,
        "affected_count": 50,
        "exfiltration_status": "suspected",
        "encryption_status": "unknown",
        "log_status": "available",
    }
    result = calculate_risk(incident)
    assert 0 <= result.score <= 100


def test_level_is_valid():
    incident = {
        "data_types": ["health", "auth"],
        "special_category": True,
        "affected_count": 1500,
        "exfiltration_status": "confirmed",
        "encryption_status": "not_encrypted",
        "log_status": "missing",
    }
    result = calculate_risk(incident)
    assert result.level in {"Düşük", "Orta", "Yüksek", "Kritik"}
    # Skor eşikleri ileride değişebilir; seviyeyi garantiye alıyoruz.
    assert result.level in {"Yüksek", "Kritik"}


