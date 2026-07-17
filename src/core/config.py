from pathlib import Path

# ==================================================
# PROJE KÖK DİZİNİ
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent


# ==================================================
# DATA KLASÖRLERİ
# ==================================================

DATA_FOLDER = BASE_DIR / "data"

VIDEOS_FOLDER = DATA_FOLDER / "videos"

METADATA_FOLDER = DATA_FOLDER / "metadata"
METADATA_FILE = METADATA_FOLDER / "metadata.csv"

SCENES_FOLDER = DATA_FOLDER / "scenes"

KEYFRAMES_FOLDER = DATA_FOLDER / "keyframes"
KEYFRAMES_IMAGES_FOLDER = KEYFRAMES_FOLDER / "images"
KEYFRAMES_METADATA_FOLDER = KEYFRAMES_FOLDER / "metadata"

OBJECTS_FOLDER = DATA_FOLDER / "objects"
OBJECTS_METADATA_FOLDER = OBJECTS_FOLDER / "metadata"

TEXT_FOLDER = DATA_FOLDER / "texts"
TEXT_METADATA_FOLDER = TEXT_FOLDER / "metadata"

SPEECH_FOLDER = DATA_FOLDER / "speech"

FEATURES_FOLDER = DATA_FOLDER / "features"

REPORTS_FOLDER = DATA_FOLDER / "reports"


# ==================================================
# MODEL KLASÖRLERİ
# ==================================================

MODELS_FOLDER = BASE_DIR / "models"


# ==================================================
# SCENE DETECTION
# ==================================================

SCENE_THRESHOLD = 27.0


# ==================================================
# KEYFRAME EXTRACTION
# ==================================================

MIN_KEYFRAMES_PER_SCENE = 1
MAX_KEYFRAMES_PER_SCENE = 5

KEYFRAME_SEARCH_RADIUS = 10

KEYFRAME_IMAGE_EXTENSION = ".jpg"


# ==================================================
# OBJECT DETECTION
# ==================================================

YOLO_MODEL = "yolo11s.pt"

YOLO_CONFIDENCE = 0.35

YOLO_DEVICE = "cpu"


# ==================================================
# OCR
# ==================================================

OCR_LANGUAGES = [
    "tr",
    "en"
]

OCR_GPU = False

OCR_MIN_CONFIDENCE = 0.40


# ==================================================
# SPEECH RECOGNITION
# ==================================================

WHISPER_MODEL = "base"


# ==================================================
# DESTEKLENEN VİDEO FORMATLARI
# ==================================================

SUPPORTED_VIDEO_EXTENSIONS = [
    ".mp4",
    ".mov",
    ".avi",
    ".mkv"
]


# ==================================================
# PIPELINE STATUS
# ==================================================

STATUS_METADATA_DONE = "metadata_done"

STATUS_SCENE_DONE = "scene_done"
STATUS_SCENE_ERROR = "scene_error"

STATUS_KEYFRAME_DONE = "keyframe_done"
STATUS_KEYFRAME_ERROR = "keyframe_error"

STATUS_OBJECT_DONE = "object_done"
STATUS_OBJECT_ERROR = "object_error"

STATUS_FEATURE_DONE = "feature_done"
STATUS_FEATURE_ERROR = "feature_error"

STATUS_FEATURE_VECTOR_DONE = "feature_vector_done"
STATUS_FEATURE_VECTOR_ERROR = "feature_vector_error"

STATUS_VISUAL_DONE = "visual_done"
STATUS_VISUAL_ERROR = "visual_error"

STATUS_SPEECH_DONE = "speech_done"
STATUS_SPEECH_ERROR = "speech_error"

STATUS_SPEECH_EMBEDDING_DONE = "speech_embedding_done"
STATUS_SPEECH_EMBEDDING_ERROR = "speech_embedding_error"

STATUS_OCR_DONE = "ocr_done"
STATUS_OCR_ERROR = "ocr_error"

STATUS_OCR_EMBEDDING_DONE = "ocr_embedding_done"
STATUS_OCR_EMBEDDING_ERROR = "ocr_embedding_error"

STATUS_FUSION_DONE = "fusion_done"
STATUS_FUSION_ERROR = "fusion_error"

STATUS_SIMILARITY_DONE = "similarity_done"
STATUS_SIMILARITY_ERROR = "similarity_error"


# ==================================================
# PIPELINE
# ==================================================

PIPELINE_NAME = "DAHI"

PIPELINE_VERSION = "1.0.0"


# ==================================================
# PIPELINE STAGES
# ==================================================

PIPELINE_STAGES = {

    "metadata": {
        "previous_status": None,
        "current_status": STATUS_METADATA_DONE,
        "count_column": None
    },

    "scene": {
        "previous_status": STATUS_METADATA_DONE,
        "current_status": STATUS_SCENE_DONE,
        "count_column": "scene_count"
    },

    "keyframe": {
        "previous_status": STATUS_SCENE_DONE,
        "current_status": STATUS_KEYFRAME_DONE,
        "count_column": "keyframe_count"
    },

    "object": {
        "previous_status": STATUS_KEYFRAME_DONE,
        "current_status": STATUS_OBJECT_DONE,
        "count_column": "object_count"
    },

    "feature": {
        "previous_status": STATUS_OBJECT_DONE,
        "current_status": STATUS_FEATURE_DONE,
        "count_column": None
    },

    "feature_vector": {
        "previous_status": STATUS_FEATURE_DONE,
        "current_status": STATUS_FEATURE_VECTOR_DONE,
        "count_column": None
    },

    "visual": {
        "previous_status": STATUS_FEATURE_VECTOR_DONE,
        "current_status": STATUS_VISUAL_DONE,
        "count_column": None
    },

    "speech": {
        "previous_status": STATUS_VISUAL_DONE,
        "current_status": STATUS_SPEECH_DONE,
        "count_column": None
    },

    "speech_embedding": {
        "previous_status": STATUS_SPEECH_DONE,
        "current_status": STATUS_SPEECH_EMBEDDING_DONE,
        "count_column": None
    },

    "ocr": {
        "previous_status": STATUS_SPEECH_EMBEDDING_DONE,
        "current_status": STATUS_OCR_DONE,
        "count_column": None
    },

    "ocr_embedding": {
        "previous_status": STATUS_OCR_DONE,
        "current_status": STATUS_OCR_EMBEDDING_DONE,
        "count_column": None
    },

    "fusion": {
        "previous_status": STATUS_OCR_EMBEDDING_DONE,
        "current_status": STATUS_FUSION_DONE,
        "count_column": None
    },

    "similarity": {
        "previous_status": STATUS_FUSION_DONE,
        "current_status": STATUS_SIMILARITY_DONE,
        "count_column": None
    }

}

# ==================================================
# KLASÖRLERİ OLUŞTUR
# ==================================================

TEXT_METADATA_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)

# ==================================================
# VECTOR OUTPUT
# ==================================================

VECTORS_FOLDER = DATA_FOLDER / "vectors"

# ==================================================
# EMBEDDING OUTPUT
# ==================================================

EMBEDDINGS_FOLDER = DATA_FOLDER / "embeddings"

# ==================================================
# SIMILARITY OUTPUT
# ==================================================

SIMILARITY_FOLDER = DATA_FOLDER / "similarity"

# ==================================================
# SEMANTIC OUTPUT
# ==================================================

SEMANTIC_FOLDER = DATA_FOLDER / "semantic"

VISUAL_EMBEDDINGS_FOLDER = SEMANTIC_FOLDER / "visual"

SPEECH_EMBEDDINGS_FOLDER = SEMANTIC_FOLDER / "speech"

OCR_EMBEDDINGS_FOLDER = SEMANTIC_FOLDER / "ocr"

FUSION_EMBEDDINGS_FOLDER = SEMANTIC_FOLDER / "fusion"


# ==================================================
# SEMANTIC SIMILARITY
# ==================================================

SEMANTIC_SIMILARITY_FOLDER = DATA_FOLDER / "semantic_similarity"

# ==================================================
# SPEECH OUTPUT
# ==================================================

SPEECH_FOLDER = DATA_FOLDER / "speech"

SPEECH_METADATA_FOLDER = SPEECH_FOLDER / "metadata"

# ==================================================
# WHISPER
# ==================================================

WHISPER_MODEL = "base"

# ==================================================
# SPEECH
# ==================================================

SPEECH_FOLDER = DATA_FOLDER / "speech"

SPEECH_METADATA_FOLDER = SPEECH_FOLDER / "metadata"

# ==================================================
# SPEECH EMBEDDINGS
# ==================================================

SPEECH_EMBEDDINGS_FOLDER = (
    SEMANTIC_FOLDER /
    "speech"
)

# ==================================================
# OCR
# ==================================================

OCR_FOLDER = DATA_FOLDER / "ocr"

OCR_METADATA_FOLDER = OCR_FOLDER / "metadata"


# ==================================================
# OCR EMBEDDINGS
# ==================================================

OCR_EMBEDDINGS_FOLDER = (
    SEMANTIC_FOLDER /
    "ocr"
)

SEARCH_EMBEDDINGS_FOLDER = (
    DATA_FOLDER / "search"
)


STATUS_SEARCH_EMBEDDING_DONE = "search_embedding_done"

STATUS_SEARCH_EMBEDDING_ERROR = "search_embedding_error"