# DAHI - Semantic AI Design

## Amaç

Bu doküman, DAHI Framework içerisinde videoların yalnızca yapısal özelliklerini değil,
anlamsal (Semantic) içeriğini de temsil edecek yapay zeka katmanını tanımlar.

Semantic AI katmanı;

- Videonun ne anlattığını
- Videonun konusunu
- Videonun bağlamını
- Videonun içeriğini

anlamaya çalışacaktır.

Bu katman sayesinde DAHI;

- Video Search
- Recommendation
- Similarity
- Video Classification
- Video Understanding

gibi sistemlerin temelini oluşturacaktır.

---

# Mevcut Pipeline

Video

↓

Metadata Extraction

↓

Scene Detection

↓

Keyframe Extraction

↓

Object Detection

↓

OCR

↓

Feature Extraction

↓

Feature Vector

↓

Embedding

↓

Similarity

↓

Recommendation

Bu yapı videoların yapısal benzerliğini hesaplamaktadır.

---

# Semantic Pipeline

Video

↓

Visual Encoder

↓

Speech Encoder

↓

OCR Encoder

↓

Scene Encoder

↓

Object Encoder

↓

Semantic Fusion

↓

Semantic Embedding

↓

Semantic Similarity

↓

Recommendation Engine

Bu yapı videoların anlamsal benzerliğini hesaplayacaktır.

---

# Semantic AI Katmanları

## 1. Visual Encoder

Amaç

Videonun görsel içeriğini temsil eden embedding üretmek.

Girdi

- Keyframe görüntüleri

Çıktı

Visual Embedding

İlk sürüm

OpenAI CLIP

İlerleyen sürümler

- SigLIP
- EVA-CLIP
- DINOv2

---

## 2. Speech Encoder

Amaç

Videoda konuşulan metnin anlamını temsil etmek.

Girdi

Speech Transcript

Çıktı

Speech Embedding

İlk sürüm

SentenceTransformer

İlerleyen sürümler

- OpenAI Embedding
- Instructor XL

---

## 3. OCR Encoder

Amaç

Videoda bulunan yazıların anlamını temsil etmek.

Girdi

OCR Text

Çıktı

Text Embedding

İlk sürüm

SentenceTransformer

---

## 4. Object Encoder

Amaç

Nesnelerin sadece sayısını değil,
hangi nesnelerin birlikte bulunduğunu öğrenmek.

Örnek

Person

Laptop

Desk

↓

Office Scene

---

## 5. Scene Encoder

Amaç

Videonun sahne yapısını temsil etmek.

Kullanılacak Bilgiler

- Scene Count
- Scene Duration
- Scene Transition
- Scene Order

---

# Semantic Fusion

Amaç

Tüm Semantic Encoder çıktılarının
tek bir temsil haline getirilmesi.

Fusion

Visual Embedding

+

Speech Embedding

+

OCR Embedding

+

Object Embedding

+

Scene Embedding

↓

Semantic Vector

---

# Semantic Embedding

Semantic Fusion sonucunda oluşan
yüksek boyutlu Dense Vector'dır.

Bu vektör;

- Similarity Engine
- Recommendation Engine
- Search Engine

tarafından kullanılacaktır.

---

# Semantic Similarity

İki Semantic Embedding

Cosine Similarity

ile karşılaştırılacaktır.

---

# Recommendation

Recommendation Engine artık
Feature Vector yerine

Semantic Embedding

kullanacaktır.

Bu sayede sistem;

"aynı nesneye sahip"

videolar yerine

"aynı konuyu anlatan"

videoları önerecektir.

---

# Semantic AI Prensipleri

- Modüler olmalıdır.
- Her Encoder bağımsız olmalıdır.
- Yeni Encoder eklenebilmelidir.
- Fusion değiştirilebilir olmalıdır.
- Similarity Engine bağımsız kalmalıdır.
- Recommendation Engine bağımsız kalmalıdır.

---

# Klasör Yapısı

src/

semantic/

clip_encoder.py

speech_encoder.py

ocr_encoder.py

object_encoder.py

scene_encoder.py

semantic_fusion.py

semantic_engine.py

---

# Gelişim Yol Haritası

Version 2.0

- Semantic Encoder
- Semantic Similarity
- Semantic Recommendation

Version 3.0

- Video Captioning
- Video Classification
- Multi-Modal Learning

Version 4.0

- User Behavior Learning
- Personalized Recommendation
- Ranking Model

---

# Nihai Hedef

DAHI'nın amacı yalnızca videoları karşılaştırmak değildir.

DAHI'nın amacı;

Videoların ne anlattığını anlayan,

Anlamsal olarak temsil eden,

Benzer içerikleri bulabilen,

Öneriler oluşturabilen,

Modüler bir Video Understanding Framework geliştirmektir.