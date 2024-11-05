from fastapi import FastAPI
import uvicorn
from api_v1 import router
from fastapi.responses import HTMLResponse
from fastui import prebuilt_html
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(router, tags=["API"])

@app.get("/")
async def root() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title="Тестовое задание"))


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="localhost",
        port=8000,
    )