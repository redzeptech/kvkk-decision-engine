def calculate_risk_score(incident):
    score = 0
    trace = []

    if incident.get("special_category"):
        score += 35
        trace.append("Özel nitelikli veri (+35)")

    if "financial" in incident.get("data_types", []):
        score += 25
        trace.append("Finansal veri (+25)")

    if incident.get("password_leak"):
        score += 30
        trace.append("Kimlik doğrulama verisi sızmış (+30)")

    if incident.get("affected_count", 0) > 1000:
        score += 20
        trace.append("1000+ kişi etkilenmiş (+20)")

    if incident.get("exfiltration_status") == "confirmed":
        score += 25
        trace.append("Veri dışarı çıkmış (+25)")

    if incident.get("encryption_status") == "encrypted":
        score -= 15
        trace.append("Veri şifreli (-15)")

    score = max(0, min(score, 100))

    if score < 20:
        level = "Düşük"
    elif score < 40:
        level = "Orta"
    elif score < 70:
        level = "Yüksek"
    else:
        level = "Kritik"

    return score, level, trace
    return score, level, trace


def calculate_risk(incident):
    # CI ve diğer modüller calculate_risk bekliyor
    return calculate_risk_score(incident)

