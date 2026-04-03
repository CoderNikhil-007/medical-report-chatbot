from fastapi import FastAPI
from app.routes import upload, query
import warnings

# Ignore only specific warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

app = FastAPI()

app.include_router(upload.router)
app.include_router(query.router)