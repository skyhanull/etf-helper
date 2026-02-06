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
  // SWC 컴파일러 설정 (바이너리 다운로드 문제 해결)
  swcMinify: true,
  // 실험적 기능
  experimental: {
    // SWC 바이너리 다운로드 실패 시 자동 폴백
  },
}

module.exports = nextConfig
