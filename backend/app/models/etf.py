from sqlalchemy import Column, String, Integer, Float, Date, DateTime, BigInteger, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base


class Etf(Base):
    """ETF 기본 정보"""

    __tablename__ = "etfs"

    code = Column(String(10), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category = Column(String(50))
    manager = Column(String(50))
    listed_at = Column(Date)
    fee = Column(Float)
    nav = Column(BigInteger)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


class EtfPrice(Base):
    """ETF 가격 히스토리"""

    __tablename__ = "etf_prices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    etf_code = Column(String(10), ForeignKey("etfs.code"), nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)
    close_price = Column(Integer)
    volume = Column(BigInteger)


class EtfHolding(Base):
    """ETF 구성 종목"""

    __tablename__ = "etf_holdings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    etf_code = Column(String(10), ForeignKey("etfs.code"), nullable=False, index=True)
    stock_name = Column(String(100), nullable=False)
    weight = Column(Float)
    updated_at = Column(DateTime, server_default=func.now())
