# KVKK Decision Engine
![CI](https://github.com/redzeptech/kvkk-decision-engine/actions/workflows/ci.yml/badge.svg)


KVKK kapsamındaki kişisel veri ihlali olaylarında; olayın niteliğine göre **risk derecelendirmesi**, **gerekçeli değerlendirme (karar izi)** ve **rapor taslağı** üreten karar destek aracıdır.

> **Uyarı:** Bu araç hukuki görüş yerine geçmez. Çıktılar karar destek amaçlıdır. Nihai değerlendirme kurumun uyum/hukuk birimlerince yapılmalıdır.

---

## Amaç
- Uyum / hukuk ekipleri için hızlı ön değerlendirme
- Risk skoru ve risk seviyesi üretimi (0–100)
- Gerekçeli değerlendirme (hangi etkenler skoru etkiledi?)
- Kurumsal rapor taslağı üretimi (Markdown)

## Kimler için?
- KVKK uyum ekipleri
- Hukuk birimleri
- Bilgi güvenliği / BT operasyon ekipleri
- İç denetim / risk ekipleri

---

## Kurulum
Python 3.10+ önerilir.

```bash
pip install -r requirements.txt
py app/cli.py -i data/incident_examples.json -o out/report.md
Bu komut, örnek olay dosyasını kullanarak `out/report.md` yolunda bir rapor taslağı üretir.
## Kullanım (Rapor üretimi)

```bash
py app/cli.py -i data/incident_examples.json -o out/report.md
Risk Skoru: 62/100
Risk Seviyesi: Yüksek
Gerekçeli Değerlendirme:
- Finansal veri (+25)
- Veri dışarı çıkışı şüpheli (+12)
Önerilen Aksiyonlar:
- Olay kaydı oluşturulması
- Etkilenen hesapların kontrolü
