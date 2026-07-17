# DAHI - Embedding Engine Design

## Amaç

Bu doküman, Feature Vector'ların AI modelleri tarafından kullanılabilecek
Dense Embedding'lere nasıl dönüştürüleceğini tanımlar.

Embedding Engine;

- Similarity Engine
- Recommendation Engine
- AI Modelleri

tarafından kullanılacaktır.

---

# Pipeline

Video

↓

Feature Extraction

↓

Feature Vector

↓

Normalization

↓

Embedding Model

↓

Dense Embedding

↓

Similarity Engine

↓

Recommendation Engine

---

# Embedding Nedir?

Embedding, bir nesnenin matematiksel olarak temsil edildiği
yoğun (Dense) sayısal vektördür.

Benzer içeriklere sahip videolar,
Embedding uzayında birbirine yakın konumlanacaktır.

---

# Embedding Girdisi

Embedding Engine'in girdisi

Feature Vector'dır.

Örnek

[
13.13,
394,
1,
1,
1,
7,
7,
0.755
]

---

# Normalization

Embedding oluşturulmadan önce
Feature Vector normalize edilir.

İlk sürümde

- Min-Max Normalization

kullanılması planlanmaktadır.

İlerleyen sürümlerde

- StandardScaler
- RobustScaler

desteklenecektir.

---

# Embedding Model

Embedding üretimi doğrudan
Embedding Model tarafından yapılacaktır.

İlk sürüm

Rule-Based Dense Vector

İkinci sürüm

MLP

Üçüncü sürüm

AutoEncoder

Dördüncü sürüm

Transformer

---

# Embedding Boyutu

İlk sürüm

Feature Vector ile aynı boyutta olacaktır.

İlerleyen sürümlerde

64

128

256

512

boyutlu Embedding üretilebilecektir.

---

# Similarity

Embedding'ler

Cosine Similarity

ile karşılaştırılacaktır.

---

# Tasarım Prensipleri

- Modüler olmalıdır.
- Embedding Model değiştirilebilir olmalıdır.
- Feature Vector bağımsız kalmalıdır.
- Yeni modeller mevcut sistemi bozmamalıdır.

---

# Sonraki Aşama

Bu tasarım

normalizer.py

embedding_models.py

embedding_engine.py

tarafından gerçekleştirilecektir.