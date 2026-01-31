from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class ScoreResult:
    score: int
    level: str
    trace: List[str]
    actions: List[str]


def _risk_level(score: int) -> str:
    if score < 20:
        return "Düşük"
    if score < 40:
        return "Orta"
    if score < 70:
        return "Yüksek"
    return "Kritik"


def _actions_for(level: str) -> List[str]:
    base = [
        "Olay kaydı oluşturulması ve olay sorumlularının atanması",
        "Delil bütünlüğünün korunması (log, e-posta, dosya vb.)",
        "Erişim kontrolü uygulanması (oturum sonlandırma, parola sıfırlama vb.)",
        "Kapsam/etki analizinin başlatılması (veri envanteri eşleştirmesi)",
    ]
    if level == "Düşük":
        return base + [
            "Ön değerlendirme raporunun tamamlanması ve iç onaya sunulması",
        ]
    if level == "Orta":
        return base + [
            "Bildirime ilişkin gerekliliğin uyum/hukuk tarafından değerlendirilmesi",
            "İlgili kişilere bilgilendirme ihtiyacının değerlendirilmesi",
        ]
    if level == "Yüksek":
        return base + [
            "Olay müdahale planının devreye alınması",
            "Hızlandırılmış karar süreci ile bildirim hazırlıklarının başlatılması",
            "Kök neden analizi ve kalıcı önlemler",
        ]
    return base + [
        "Üst yönetime acil bilgilendirme ve kriz koordinasyonu",
        "Bildirim/bilgilendirme taslaklarının hazırlanması",
        "Kapsamlı kök neden analizi ve zorunlu kontrol iyileştirmeleri",
    ]


def calculate_risk(incident: Dict[str, Any]) -> ScoreResult:
    score = 0
    trace: List[str] = []

    data_types = [str(x).lower() for x in incident.get("data_types", [])]
    affected = int(incident.get("affected_count", 0) or 0)

    # Özel nitelikli veri
    if bool(incident.get("special_category", False)) or ("health" in data_types) or ("biometric" in data_types):
        score += 35
        trace.append("Özel nitelikli veri riski (+35)")

    # Kimlik + finans
    if "identity" in data_types:
        score += 15
        trace.append("Kimlik verisi (+15)")
    if "financial" in data_types:
        score += 25
        trace.append("Finansal veri (+25)")

    # Kimlik doğrulama (parola/token)
    if "auth" in data_types or bool(incident.get("password_leak", False)):
        score += 30
        trace.append("Kimlik doğrulama verisi (parola/token) (+30)")

    # Ölçek
    if affected >= 1000:
        score += 20
        trace.append("Etkilenen kişi sayısı 1000+ (+20)")
    elif affected >= 100:
        score += 12
        trace.append("Etkilenen kişi sayısı 100-999 (+12)")
    elif affected >= 10:
        score += 6
        trace.append("Etkilenen kişi sayısı 10-99 (+6)")
    elif affected >= 1:
        score += 2
        trace.append("Etkilenen kişi sayısı 1-9 (+2)")

    # Dışarı çıkış
    exf = str(incident.get("exfiltration_status", "unknown")).lower()
    if exf == "confirmed":
        score += 25
        trace.append("Veri dışarı çıkışı doğrulandı (+25)")
    elif exf == "suspected":
        score += 12
        trace.append("Veri dışarı çıkışı şüpheli (+12)")

    # Belirsizlik
    log_status = str(incident.get("log_status", "unknown")).lower()
    if log_status in ("missing", "unknown"):
        score += 8
        trace.append("Log/delil belirsizliği (+8)")

    # Şifreleme indirimi
    enc = str(incident.get("encryption_status", "unknown")).lower()
    if enc == "encrypted":
        score -= 15
        trace.append("Veri şifreli (-15)")
    elif enc == "unknown":
        score += 5
        trace.append("Şifreleme durumu belirsiz (+5)")

    score = max(0, min(int(score), 100))
    level = _risk_level(score)
    actions = _actions_for(level)

    return ScoreResult(score=score, level=level, trace=trace, actions=actions)


# Geriye dönük uyumluluk: eski adla çağıran olursa
def calculate_risk_score(incident: Dict[str, Any]):
    r = calculate_risk(incident)
    return r.score, r.level, r.trace
