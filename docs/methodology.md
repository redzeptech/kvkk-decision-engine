\# Metodoloji



Bu proje, kişisel veri ihlali olaylarında “ilk değerlendirme” amacıyla \*\*risk skorlaması + gerekçeli karar izi + aksiyon önerileri\*\* üretir.



\## 1. Girdi Kategorileri

Aşağıdaki alanlar temel alınır:



\- \*\*Olay türü:\*\* yanlış alıcıya iletim, yetkisiz erişim, kayıp cihaz, misconfiguration vb.

\- \*\*Veri türleri:\*\* kimlik, iletişim, finans, sağlık, biyometrik, kimlik doğrulama verisi (parola/token) vb.

\- \*\*Özel nitelikli veri:\*\* var/yok (veya sağlık/biyometrik işaretinden türetim)

\- \*\*Etkilenen kişi sayısı:\*\* tahmini ölçek

\- \*\*Veri dışarı çıkışı:\*\* yok / şüpheli / doğrulandı

\- \*\*Şifreleme durumu:\*\* şifreli / şifresiz / bilinmiyor

\- \*\*Log/delil durumu:\*\* mevcut / yok / bilinmiyor



\## 2. Skorlama Mantığı (MVP)

Skor 0–100 aralığında tutulur. Skoru artıran başlıca unsurlar:



\- Özel nitelikli veri riski

\- Finansal veri veya kimlik doğrulama verisi (parola/token) sızıntısı

\- Etkilenen kişi sayısının büyüklüğü

\- Veri dışarı çıkışının doğrulanması

\- Belirsizlik (log yokluğu, şifreleme durumunun bilinmemesi)



Skoru azaltan başlıca unsur:

\- Verinin güçlü biçimde şifrelenmiş olması



\## 3. Risk Seviyeleri

\- 0–19: \*\*Düşük\*\*

\- 20–39: \*\*Orta\*\*

\- 40–69: \*\*Yüksek\*\*

\- 70–100: \*\*Kritik\*\*



\## 4. Karar İzi (Trace)

Araç, sonuç üretirken hangi etkenlerin skoru artırdığı/azalttığını maddeler halinde döndürür. Böylece uyum/hukuk ekipleri çıktıyı gerekçelendirebilir ve iç onay süreçlerinde kullanabilir.



\## 5. Aksiyon Önerileri

Aksiyonlar risk seviyesine göre önerilir ve şu başlıkları kapsar:

\- delil bütünlüğü ve kayıt altına alma

\- erişim kontrolü ve hasar azaltma

\- kapsam/etki analizi

\- iç bildirim/koordinasyon

\- (gerekiyorsa) bildirim hazırlıkları için hızlandırılmış değerlendirme



\## 6. Güncelleme Gereksinimi

Mevzuat, Kurul kararları ve kurum içi politika/prosedürler doğrultusunda kural seti ve metinler periyodik olarak güncellenmelidir.



