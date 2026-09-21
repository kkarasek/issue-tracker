from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.issues import router as issues_router
from app.middleware.timer import timing_middleware


app = FastAPI()

app.middleware("http")(timing_middleware)

app.add_middleware(CORSMiddleware, allow_origins=[
                   "*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(issues_router)


@app.get('/healthz')
def health_check():
    return {"status": "ok"}
