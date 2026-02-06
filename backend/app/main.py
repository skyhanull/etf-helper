from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.routes import etf, health
from app.core.config import settings
from app.core.exceptions import AppException

app = FastAPI(
    title="ETF Helper API",
    description="국내 ETF 정보 조회 API",
    version="0.1.0",
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 전역 예외 핸들러
@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {"code": exc.code, "message": exc.message},
        },
    )


# 라우터 등록
app.include_router(health.router, tags=["Health"])
app.include_router(etf.router, prefix="/api", tags=["ETF"])


@app.get("/")
async def root():
    return {"message": "ETF Helper API", "docs": "/docs"}
