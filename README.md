<img width="470" height="805" alt="image" src="https://github.com/user-attachments/assets/7109f610-0677-4c8d-b681-9e03c6af69e7" /># DAHI
### Deep Artificial Hybrid Intelligence

<p align="center">

Multimodal AI Framework for Intelligent Video Understanding and Recommendation

</p>

---

# Overview

DAHI is a modular Artificial Intelligence framework designed to understand short-form videos by combining multiple AI models into a single semantic representation.

Instead of relying on only visual information, DAHI analyzes different modalities including:

- Visual Appearance
- Video Statistics
- Speech
- OCR Text
- Object Information

These modalities are fused into a unified semantic embedding which enables semantic search, recommendation, similarity analysis and future AI applications.

The project is designed as an end-to-end pipeline where every stage is independent, reusable and scalable.

---

# Main Features

✅ Scene Detection

✅ Keyframe Extraction

✅ Object Detection

✅ Feature Extraction

✅ Feature Embedding

✅ Visual Embedding (OpenCLIP)

✅ Speech Extraction (Whisper)

✅ Speech Embedding (Sentence Transformers)

✅ OCR Extraction (EasyOCR)

✅ OCR Embedding

✅ Multimodal Semantic Fusion

✅ Semantic Similarity Search

✅ Recommendation Engine

✅ End-to-End Pipeline

---

# AI Models

| Module | Model |
|---------|------|
| Scene Detection | PySceneDetect |
| Object Detection | YOLO |
| Visual Understanding | OpenCLIP |
| Speech Recognition | OpenAI Whisper |
| OCR | EasyOCR |
| Text Embedding | Sentence Transformers |
| Similarity | Cosine Similarity |

---

# Pipeline

```text
Video

↓

Scene Detection

↓

Keyframe Extraction

↓

Object Detection

↓

Speech Extraction

↓

OCR Extraction

↓

Feature Extraction

↓

Feature Embedding

↓

Visual Embedding

↓

Speech Embedding

↓

OCR Embedding

↓

Semantic Fusion

↓

Semantic Similarity

↓

Recommendation Engine
```

---

# Multimodal Architecture

```text
                VIDEO
                   │
     ┌─────────────┼─────────────┐
     │             │             │
     │             │             │
Visual        Speech         OCR Text
     │             │             │
     │             │             │
 OpenCLIP      Whisper    Sentence Transformer
     │             │             │
     └─────────────┼─────────────┘
                   │
                   │
          Feature Extraction
                   │
                   ▼
          Semantic Fusion
                   │
                   ▼
          Semantic Embedding
                   │
                   ▼
       Similarity & Recommendation
```

---

# Project Goals

The primary objective of DAHI is to understand videos semantically instead of treating them as raw pixels.

The framework combines information from multiple AI systems into a single embedding representation which can later be used for:

- Video Recommendation
- Semantic Search
- Video Classification
- Content Understanding
- Duplicate Detection
- Video Retrieval
- AI Assistants
- Future Large Vision Models

---

# Project Structure

```
DAHI/

│

├── data/

│   ├── videos/

│   ├── scenes/

│   ├── keyframes/

│   ├── objects/

│   ├── features/

│   ├── embeddings/

│   ├── speech/

│   ├── ocr/

│   ├── semantic/

│   │      ├── visual/

│   │      ├── speech/

│   │      ├── ocr/

│   │      └── fusion/

│   └── semantic_similarity/

│

├── src/

│   ├── core/

│   ├── pipeline/

│   ├── scene/

│   ├── keyframe/

│   ├── object_detection/

│   ├── features/

│   ├── embedding/

│   ├── semantic/

│   ├── speech/

│   ├── ocr/

│   ├── recommendation/

│   └── run_pipeline.py

│

├── requirements.txt

├── README.md

└── .gitignore
```

---

# Data Flow

The complete processing pipeline is shown below.

```
Raw Video

↓

Scene Detection

↓

Keyframe Extraction

↓

Object Detection

↓

Speech Extraction

↓

OCR Extraction

↓

Feature Extraction

↓

Feature Embedding

↓

Visual Embedding

↓

Speech Embedding

↓

OCR Embedding

↓

Semantic Fusion

↓

Semantic Similarity

↓

Recommendation Engine
```

---

# Embedding Dimensions

| Embedding | Dimension |
|------------|----------:|
| Feature | 8 |
| Visual (CLIP) | 512 |
| Speech | 384 |
| OCR | 384 |
| Final Semantic Embedding | 1288 |

---

# Technologies

## Programming

- Python

---

## Deep Learning

- PyTorch

- OpenCLIP

- Sentence Transformers

- OpenAI Whisper

- EasyOCR

---

## Computer Vision

- OpenCV

- PySceneDetect

- YOLO

---

## Scientific Computing

- NumPy

- Pandas

---

## Storage

- JSON

- NumPy (.npy)

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/DAHI.git
```

Enter the project

```bash
cd DAHI
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run the complete pipeline

```bash
python src/run_pipeline.py
```

Run only semantic pipeline

```python
MODE = "semantic"
```

Run full pipeline

```python
MODE = "full"
```

---

# Output Files

After execution DAHI automatically generates

```
Scene Metadata

Keyframes

Object Metadata

Speech Metadata

OCR Metadata

Feature Vectors

Visual Embeddings

Speech Embeddings

OCR Embeddings

Fusion Embeddings

Similarity Results

Recommendations
```

---

# Example Output

```
Top 10 Similar Videos

1. Video_032

2. Video_011

3. Video_006

4. Video_044

5. Video_015

...

Similarity : 0.9874
```

---

# Performance

The framework is designed to process videos independently.

Advantages

- Modular Architecture

- Scalable Design

- Easy Model Replacement

- Fast Embedding Search

- Reusable Components

- Production Ready Structure

- Easy Integration

- Future AI Expansion

---

# Why DAHI?

Most recommendation systems rely on user interactions such as likes, comments or watch history.

DAHI follows a different approach.

Instead of learning only from user behavior, DAHI attempts to understand the actual content of videos.

The framework combines multiple artificial intelligence models into a unified semantic representation that captures visual, textual and contextual information.

This allows future applications such as semantic search, intelligent recommendation, duplicate detection and multimodal understanding.

---

# Future Roadmap

## Version 1.0

- ✅ Scene Detection
- ✅ Keyframe Extraction
- ✅ Object Detection
- ✅ Feature Extraction
- ✅ Feature Embedding
- ✅ Visual Embedding
- ✅ Speech Extraction
- ✅ Speech Embedding
- ✅ OCR Extraction
- ✅ OCR Embedding
- ✅ Semantic Fusion
- ✅ Semantic Similarity
- ✅ Recommendation Engine

---

## Version 2.0

- FAISS Vector Database
- FastAPI REST API
- Batch Processing
- GPU Optimization
- Docker Support
- Cloud Deployment
- Automatic Dataset Builder
- Metadata Validation
- Logging System

---

## Version 3.0

- Natural Language Search

Example

```
Find me funny cat videos.
```

```
Show me luxury car videos.
```

```
Find educational videos about mathematics.
```

---

Version 3 will introduce semantic retrieval powered by multimodal embeddings.

---

## Version 4.0

- Large Language Model Integration

Examples

```
Summarize this video.
```

```
Explain this content.
```

```
Recommend similar educational videos.
```

```
Generate video tags.
```

---

Version 4 aims to transform DAHI into a complete AI Video Understanding Platform.

---

# Research Motivation

DAHI is designed to explore multimodal representation learning for short-form videos.

Instead of depending on a single AI model, the framework combines different modalities into one semantic representation.

The objective is to build a scalable architecture suitable for future research in

- Computer Vision

- Natural Language Processing

- Recommendation Systems

- Semantic Search

- Video Retrieval

- Artificial Intelligence

---

# Design Principles

The project follows several software engineering principles.

- Modular Design

- Separation of Concerns

- Reusable Components

- Scalable Architecture

- Easy Maintenance

- Independent Pipelines

- Configurable Models

- Production-Oriented Development

---

# Possible Applications

DAHI can be extended into many AI products.

Examples include

- TikTok Recommendation

- Instagram Reels Analysis

- YouTube Shorts Recommendation

- Semantic Video Search

- AI Video Assistant

- Intelligent Dataset Builder

- Video Classification

- Duplicate Video Detection

- AI Moderation Systems

- Video Analytics Platform


---

# Author

**Murat**

Computer Engineering Student

Artificial Intelligence

Computer Vision

Deep Learning

Python Development

---

# Acknowledgements

This project makes use of several outstanding open-source projects.

- OpenAI Whisper

- OpenCLIP

- Sentence Transformers

- EasyOCR

- PyTorch

- OpenCV

- PySceneDetect

- YOLO

- NumPy

- Pandas

The authors of these projects deserve full credit for their excellent work.

---

# Final Note

DAHI is more than a recommendation engine.

It is an extensible multimodal AI framework designed to understand videos through the combination of vision, language and semantic representations.

The long-term vision of the project is to build an intelligent video understanding platform capable of powering next-generation recommendation systems and AI applications.

<img width="470" height="424" alt="image" src="https://github.com/user-attachments/assets/4b0a1b6e-dfd8-4fae-8fa3-04e4ee729ba9" />

*************************************************************************
<img width="481" height="524" alt="image" src="https://github.com/user-attachments/assets/6e2c611c-1d90-4095-874f-c0abfd48c3ca" />


************************************************************************

<img width="474" height="458" alt="image" src="https://github.com/user-attachments/assets/f7b6cde1-b583-40fa-b6c3-49fec476af3a" />

*************************************************************************


<img width="479" height="135" alt="image" src="https://github.com/user-attachments/assets/89b652e6-ae7b-40a7-a901-bdf1007b35e7" />

NOT : The OCR data for this system is stored in JSON format.





