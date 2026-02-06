import type { Config } from 'tailwindcss'

const config: Config = {
  darkMode: ['class'],
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/features/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))',
          // 디자인 시스템 색상
          palette: '#3b82f6', // 파란색
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary))',
          foreground: 'hsl(var(--secondary-foreground))',
          // 디자인 시스템 색상
          palette: '#6b7280', // 회색
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive))',
          foreground: 'hsl(var(--destructive-foreground))',
        },
        muted: {
          DEFAULT: 'hsl(var(--muted))',
          foreground: 'hsl(var(--muted-foreground))',
        },
        accent: {
          DEFAULT: 'hsl(var(--accent))',
          foreground: 'hsl(var(--accent-foreground))',
        },
        popover: {
          DEFAULT: 'hsl(var(--popover))',
          foreground: 'hsl(var(--popover-foreground))',
        },
        card: {
          DEFAULT: 'hsl(var(--card))',
          foreground: 'hsl(var(--card-foreground))',
        },
        // 디자인 시스템 색상 팔레트
        success: {
          DEFAULT: '#10b981', // 초록색
          light: '#34d399',
          dark: '#059669',
        },
        warning: {
          DEFAULT: '#f59e0b', // 노란색
          light: '#fbbf24',
          dark: '#d97706',
        },
        error: {
          DEFAULT: '#ef4444', // 빨간색
          light: '#f87171',
          dark: '#dc2626',
        },
        // 커스텀 색상
        profit: 'hsl(var(--profit))',
        loss: 'hsl(var(--loss))',
        chart: {
          1: 'hsl(var(--chart-1))',
          2: 'hsl(var(--chart-2))',
          3: 'hsl(var(--chart-3))',
          4: 'hsl(var(--chart-4))',
          5: 'hsl(var(--chart-5))',
        },
      },
      spacing: {
        // 디자인 시스템 간격 (기존 Tailwind 간격 유지 + 추가)
        '1': '4px',   // $1
        '2': '8px',   // $2
        '3': '12px',  // $3
        '4': '16px',  // $4
        '6': '24px',  // $6
        '8': '32px',  // $8
      },
      fontSize: {
        // 디자인 시스템 폰트 크기 (기존 Tailwind 크기 유지 + 추가)
        'xs': '12px',   // $xs
        'sm': '14px',   // $sm
        'base': '16px', // $base
        'lg': '18px',   // $lg
        'xl': '20px',   // $xl
        '2xl': '24px',  // $2xl
        '3xl': '30px',  // $3xl
        '4xl': '36px',  // $4xl
        '5xl': '48px',  // $5xl
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
      screens: {
        // 디자인 시스템 반응형 브레이크포인트
        'mobile': '640px',   // Mobile: < 640px (기본값이 max-width)
        'tablet': '640px',   // Tablet: 640px - 1024px
        'desktop': '1024px', // Desktop: > 1024px
        // Tailwind 기본값과 호환
        'sm': '640px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
        '2xl': '1536px',
      },
    },
  },
  plugins: [require('tailwindcss-animate')],
}

export default config
