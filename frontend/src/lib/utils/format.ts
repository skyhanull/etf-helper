/**
 * 숫자를 원화 형식으로 포맷
 */
export const formatKRW = (value: number): string => {
  return new Intl.NumberFormat('ko-KR', {
    style: 'currency',
    currency: 'KRW',
  }).format(value)
}

/**
 * 숫자를 콤마 포함 형식으로 포맷
 */
export const formatNumber = (value: number): string => {
  return new Intl.NumberFormat('ko-KR').format(value)
}

/**
 * 퍼센트 포맷 (+/- 포함)
 */
export const formatPercent = (value: number): string => {
  const sign = value >= 0 ? '+' : ''
  return `${sign}${value.toFixed(2)}%`
}

/**
 * 날짜 포맷 (YYYY.MM.DD)
 */
export const formatDate = (date: string | Date): string => {
  const d = new Date(date)
  return `${d.getFullYear()}.${String(d.getMonth() + 1).padStart(2, '0')}.${String(d.getDate()).padStart(2, '0')}`
}
