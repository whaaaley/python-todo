const linearClamp = (min, max, unit = 'rem') => {
  min = min / 16
  max = max / 16

  const minWidth = 425 / 16 // minimum width of mobile
  const maxWidth = 1280 / 16 // maximum width of laptop

  const slope = (max - min) / (maxWidth - minWidth)
  const intercept = min - slope * minWidth
  const value = slope * 100

  return `clamp(${min}${unit}, ${intercept}${unit} + ${value}vw, ${max}${unit})`
}

/** @type {import('tailwindcss').Config} */
export default {
  plugins: [],
  content: [
    './*.html',
    './src/**/*.{css,js,jsx,ts,tsx,vue}',
  ],
  theme: {
    extend: {}
  },
}
