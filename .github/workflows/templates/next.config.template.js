/** @type {import('next').NextConfig} */
const nextConfig = {
  // 환경변수
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL,
  },
  // 이미지 최적화 (필요시 외부 도메인 추가)
  images: {
    remotePatterns: [],
  },
}

module.exports = nextConfig
