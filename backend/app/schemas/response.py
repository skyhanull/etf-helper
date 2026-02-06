from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class PaginationMeta(BaseModel):
    page: int
    limit: int
    total: int
    total_pages: int


class ErrorDetail(BaseModel):
    code: str
    message: str
    details: Optional[dict] = None


class ApiResponse(BaseModel, Generic[T]):
    """표준 API 응답"""

    success: bool
    data: Optional[T] = None
    error: Optional[ErrorDetail] = None
    meta: Optional[PaginationMeta] = None


def success_response(data: T, meta: Optional[dict] = None) -> dict:
    """성공 응답 생성"""
    response = {"success": True, "data": data}
    if meta:
        response["meta"] = meta
    return response


def error_response(code: str, message: str, details: Optional[dict] = None) -> dict:
    """에러 응답 생성"""
    return {
        "success": False,
        "error": {"code": code, "message": message, "details": details},
    }


def paginated_response(data: list, page: int, limit: int, total: int) -> dict:
    """페이지네이션 응답 생성"""
    total_pages = (total + limit - 1) // limit
    return {
        "success": True,
        "data": data,
        "meta": {
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": total_pages,
        },
    }
