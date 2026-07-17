import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


#==================================================
# ROUTERS
#==================================================

from .api.search import router as search_router
from .api.video import router as video_router
from .api.analysis import router as analysis_router


#==================================================
# FAST API
#==================================================

app = FastAPI(

    title="DAHI API",

    version="1.0.0",

)


#==================================================
# CORS
#==================================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


#==================================================
# API ROUTERS
#==================================================

app.include_router(search_router)

app.include_router(video_router)

app.include_router(analysis_router)


#==================================================
# STATIC IMAGES
#==================================================

KEYFRAME_DIR = (

        ROOT_DIR
        / "data"
        / "keyframes"
        / "images"

)


app.mount(

    "/images",

    StaticFiles(
        directory=KEYFRAME_DIR
    ),

    name="images",

)


#==================================================
# STATIC VIDEOS
#==================================================

VIDEOS_DIR = (

        ROOT_DIR
        / "data"
        / "videos"

)


app.mount(

    "/videos",

    StaticFiles(
        directory=VIDEOS_DIR
    ),

    name="videos",

)


#==================================================
# HOME
#==================================================

@app.get("/")
def home():

    return {

        "project":"DAHI",

        "status":"running"

    }