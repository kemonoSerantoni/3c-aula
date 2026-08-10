import js from '@eslint/js'
import globals from 'globals'

export default [
  js.configs.recommended,
  {
    languageOptions: {
      globals: {
        ...globals.browser
      }
    },
    rules: {
      quotes: ['error', 'single'],
      semi: ['error', 'never']
    }
  },
]