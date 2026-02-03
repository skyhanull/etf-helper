from fastapi import APIRouter, Query
from typing import Optional
from app.schemas.response import success_response, paginated_response

router = APIRouter()


@router.get("/etfs")
async def get_etf_list(
    category: Optional[str] = Query(None, description="카테고리 필터"),
    manager: Optional[str] = Query(None, description="운용사 필터"),
    search: Optional[str] = Query(None, description="검색어"),
    sort: Optional[str] = Query("-return_1y", description="정렬 기준"),
    page: int = Query(1, ge=1, description="페이지 번호"),
    limit: int = Query(20, ge=1, le=100, description="페이지당 개수"),
):
    """ETF 목록 조회"""
    # TODO: 실제 DB 연동
    mock_data = [
        {
            "code": "069500",
            "name": "KODEX 200",
            "category": "시장",
            "manager": "삼성자산운용",
            "price": 35200,
            "return_1y": 5.1,
        },
        {
            "code": "091160",
            "name": "KODEX 반도체",
            "category": "섹터",
            "manager": "삼성자산운용",
            "price": 12500,
            "return_1y": 15.3,
        },
    ]

    return paginated_response(data=mock_data, page=page, limit=limit, total=2)


@router.get("/etfs/{code}")
async def get_etf_detail(code: str):
    """ETF 상세 정보 조회"""
    # TODO: 실제 DB 연동
    mock_data = {
        "code": code,
        "name": "KODEX 반도체",
        "category": "섹터",
        "manager": "삼성자산운용",
        "listed_at": "2020-01-15",
        "fee": 0.45,
        "nav": 1200000000000,
        "price": 12500,
        "return_1m": 3.2,
        "return_3m": 8.5,
        "return_6m": 12.1,
        "return_1y": 15.3,
        "volume": 1234567,
    }

    return success_response(data=mock_data)


@router.get("/etfs/{code}/prices")
async def get_etf_prices(
    code: str,
    period: str = Query("1y", description="기간 (1m, 3m, 6m, 1y)"),
):
    """ETF 가격 히스토리 조회"""
    # TODO: 실제 DB 연동
    mock_data = [
        {"date": "2024-01-01", "price": 11000},
        {"date": "2024-01-15", "price": 11500},
        {"date": "2024-02-01", "price": 12000},
        {"date": "2024-02-15", "price": 12500},
    ]

    return success_response(data=mock_data)


@router.get("/etfs/{code}/holdings")
async def get_etf_holdings(code: str):
    """ETF 구성 종목 조회"""
    # TODO: 실제 DB 연동
    mock_data = [
        {"name": "삼성전자", "weight": 25.3},
        {"name": "SK하이닉스", "weight": 18.2},
        {"name": "삼성전자우", "weight": 8.5},
        {"name": "DB하이텍", "weight": 5.2},
        {"name": "리노공업", "weight": 4.1},
    ]

    return success_response(data=mock_data)
