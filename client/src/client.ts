import createClient from 'openapi-fetch'
import type { paths } from './types/api'

const client = createClient<paths>({
  baseUrl: import.meta.env.VITE_API_URL,
})

export default client
