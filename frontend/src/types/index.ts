// ETF 관련 타입
export interface Etf {
  code: string
  name: string
  category: string
  manager: string
  listedAt: string
  fee: number
  nav: number
  price: number
  return1m: number
  return3m: number
  return6m: number
  return1y: number
  volume: number
  updatedAt: string
}

export interface EtfDetail extends Etf {
  holdings: EtfHolding[]
}

export interface EtfHolding {
  name: string
  weight: number
}

export interface PriceHistory {
  date: string
  price: number
}

// 포트폴리오 관련 타입
export interface PortfolioItem {
  id: string
  etfCode: string
  etfName: string
  quantity: number
  avgPrice: number
  currentPrice?: number
}

// API 응답 타입
export interface ApiResponse<T> {
  success: boolean
  data?: T
  error?: {
    code: string
    message: string
    details?: unknown
  }
  meta?: {
    page?: number
    limit?: number
    total?: number
    totalPages?: number
  }
}

// 쿼리 파라미터 타입
export interface EtfListParams {
  category?: string
  manager?: string
  search?: string
  sort?: string
  page?: number
  limit?: number
}
