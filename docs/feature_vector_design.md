# DAHI - Feature Vector Design

## Amaç

Bu doküman, Feature Extraction aşamasında üretilen Feature'ların
AI modelleri tarafından kullanılabilecek ortak bir Feature Vector'a
nasıl dönüştürüleceğini tanımlar.

Feature Vector;

- Similarity Engine
- Embedding Engine
- Recommendation Engine

tarafından kullanılacaktır.

---

# Pipeline

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

Embedding Engine

↓

Similarity Engine

↓

Recommendation Engine

---

# Neden Feature Vector?

Feature Extraction sonucunda elde edilen Feature'lar farklı veri tiplerine sahiptir.

Örnek:

```json
{
    "duration": 13.13,
    "frame_count": 394,
    "scene_count": 1,
    "dominant_object": "person",
    "total_words": 7
}