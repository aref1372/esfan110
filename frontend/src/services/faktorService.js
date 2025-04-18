import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000'  // آدرس backend شما

export async function createFaktor(data) {
  return axios.post(`${API_BASE_URL}/api/faktor`, data)
}
