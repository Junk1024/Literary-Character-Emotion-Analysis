import axios from 'axios'

const http = axios.create({
  baseURL: '/api',
  timeout: 10000
})
// 添加请求拦截器
http.interceptors.request.use(
  function (config) {
    // 发送请求之前做的事
    return config
  },
  function (error) {
    // 请求错误时要做的事
    return Promise.reject(error)
  }
)
// 添加响应拦截器
http.interceptors.response.use(
  function (response) {
    return response
  },
  function (error) {
    return Promise.reject(error)
  }
)

export default http
