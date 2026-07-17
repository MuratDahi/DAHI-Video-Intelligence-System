# DAHI - Feature Dictionary

## Amaç

Bu doküman, DAHI Framework tarafından üretilen tüm Feature'ların teknik tanımlarını içerir.

Her Feature aşağıdaki bilgileri içerir:

- Category
- Description
- Source
- Data Type
- Example
- Usage

Bu sözlük, Feature Extraction, Feature Fusion ve Similarity Engine tarafından ortak referans olarak kullanılacaktır.

---

# Video Features

## VF001 - duration

**Category**

Raw Feature

**Description**

Videonun toplam süresi (saniye cinsinden).

**Source**

metadata.csv

**Data Type**

Float

**Example**

13.13

**Usage**

- Video uzunluğunu temsil eder.
- Tempo analizinde kullanılabilir.
- Benzer videoların karşılaştırılmasında kullanılabilir.

---

## VF002 - frame_count

**Category**

Raw Feature

**Description**

Videodaki toplam kare (frame) sayısı.

**Source**

metadata.csv

**Data Type**

Integer

**Example**

394

**Usage**

- Video yoğunluğunu temsil eder.
- FPS hesaplamalarında kullanılabilir.
- Zaman tabanlı Feature'ların hesaplanmasına yardımcı olur.

---

# Scene Features

Bu bölüm Scene Detection modülünden üretilecek Feature'ları içerir.

(Henüz tasarlanmadı.)

---

# Object Features

Bu bölüm Object Detection modülünden üretilecek Feature'ları içerir.

(Henüz tasarlanmadı.)

---

# Text Features

Bu bölüm OCR modülünden üretilecek Feature'ları içerir.

(Henüz tasarlanmadı.)

---

# Notlar

- Raw Feature'lar doğrudan mevcut veriden elde edilir.
- Derived Feature'lar bir veya daha fazla Feature kullanılarak hesaplanır.
- Her Feature yalnızca tek bir anlamı temsil etmelidir.
- Feature isimleri mümkün olduğunca açık ve anlaşılır olmalıdır.
- Yeni Feature eklemek mevcut Feature'ları etkilememelidir.