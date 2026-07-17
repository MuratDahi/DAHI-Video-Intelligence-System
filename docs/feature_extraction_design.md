# DAHI - Feature Extraction Design

## Amaç

Bu doküman, DAHI Framework içerisinde video analizinden elde edilen ham verilerin
anlamlı Feature'lara nasıl dönüştürüleceğini tanımlar.

Feature Extraction katmanı;

- Video Metadata
- Scene Detection
- Object Detection
- OCR

çıktılarını kullanarak video hakkında anlamlı özellikler üretir.

Bu özellikler daha sonra tek bir **Feature Representation** içerisinde birleştirilerek;

- Embedding Engine
- Similarity Engine
- Recommendation Engine

tarafından kullanılacaktır.

---

# Phase 2 Pipeline

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

Embedding

↓

Similarity Engine

↓

Recommendation Engine

---

# 1. Video Features

## Kaynak

metadata.csv

## Amaç

Videonun genel yapısını temsil eden özellikleri üretmek.

## İlk Versiyonda Üretilecek Feature'lar

- duration
- frame_count

## Gelecek Versiyonlar

- fps
- resolution
- aspect_ratio
- bitrate

---

# 2. Scene Features

## Kaynak

scene.json

## Amaç

Videonun sahne yapısını temsil etmek.

## İlk Versiyonda Üretilecek Feature'lar

- scene_count

## Gelecek Versiyonlar

- average_scene_duration
- minimum_scene_duration
- maximum_scene_duration
- scene_change_rate

---

# 3. Object Features

## Kaynak

object.json

## Amaç

Videodaki nesne dağılımını temsil etmek.

## İlk Versiyonda Üretilecek Feature'lar

- total_objects
- unique_objects
- dominant_object

## Gelecek Versiyonlar

- object_frequency
- people_count
- vehicle_count
- furniture_count

---

# 4. Text Features

## Kaynak

text.json

## Amaç

Videoda bulunan yazıları temsil etmek.

## İlk Versiyonda Üretilecek Feature'lar

- total_words
- unique_words
- average_confidence

## Gelecek Versiyonlar

- contains_brand
- contains_price
- contains_number
- contains_url
- contains_email
- contains_phone

---

# Feature Extraction Architecture

Her Feature grubu kendi modülünde işlenecektir.

```
feature_extraction/

├── video_features.py
├── scene_features.py
├── object_features.py
├── text_features.py
└── extract_features.py
```

---

## video_features.py

```
extract_video_features(video_id)

↓

get_video(video_id)

↓

get_duration()

↓

get_frame_count()

↓

Video Feature Dictionary
```

---

## scene_features.py

```
extract_scene_features(video_id)

↓

load_scene_json(video_id)

↓

Scene Feature Dictionary
```

---

## object_features.py

```
extract_object_features(video_id)

↓

load_object_json(video_id)

↓

Object Feature Dictionary
```

---

## text_features.py

```
extract_text_features(video_id)

↓

load_text_json(video_id)

↓

Text Feature Dictionary
```

---

## extract_features.py

Bu modül;

- Video Feature
- Scene Feature
- Object Feature
- Text Feature

çıktılarını tek bir Feature Representation içerisinde birleştirir.

---

# Feature Lifecycle

Ham Veri

↓

Raw Feature

↓

Derived Feature

↓

Feature Representation

↓

Embedding

↓

Similarity

↓

Recommendation

---

# Feature Extraction Principles

- Ham veri Feature değildir.
- Her Feature tek bir anlam taşımalıdır.
- Feature üretimi modüler olmalıdır.
- Her Feature kendi modülünde hesaplanmalıdır.
- Feature'lar birbirinden bağımsız olmalıdır.
- Yeni Feature eklemek mevcut sistemi bozmamalıdır.
- Feature isimleri açık ve anlaşılır olmalıdır.
- Koddan önce veri modeli tasarlanmalıdır.

---

# Design Principles

- Single Responsibility Principle uygulanmalıdır.
- Modüller birbirinden bağımsız olmalıdır.
- Yardımcı fonksiyonlar tekrar kullanılabilir olmalıdır.
- Her Feature test edilebilir olmalıdır.
- Kod okunabilirliği performanstan önce gelir.
- Genişletilebilir (Scalable) mimari hedeflenmelidir.

---

# Roadmap

Phase 2

- Video Feature Extraction
- Scene Feature Extraction
- Object Feature Extraction
- Text Feature Extraction
- Feature Representation

↓

Phase 3

- Embedding Engine
- Similarity Engine

↓

Phase 4

- Recommendation Engine
- Search Engine
- AI Knowledge Layer