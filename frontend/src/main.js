import Vue from 'vue'
import App from './App.vue'
// import { Row, Button } from 'element-ui';
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import router from './router'
import store from './store'
import './api/mock'
import Cookie from 'js-cookie'
import debounce from './utils/debounce'
import axios from 'axios'
Vue.use(debounce)

Vue.config.productionTip = false
Vue.prototype.$axios = axios

// 全局引入
Vue.use(ElementUI)

// 按需引入
// Vue.use(Row)
// Vue.use(Button)

// 添加全局前置导航守卫
router.beforeEach((to, from, next) => {
  // 判断token存不存在
  const token = Cookie.get('token')
  // if (!token && to.name == 'resiter') {
  //   next({ name: 'resiter' })
  // }
  // token不存在，说明当前用户是未登录，应该跳转至登录页
  if (!token && to.name !== 'login' && to.name !== 'resiter') {
    // console.log(1)
    next({ name: 'login' })
  } else if (token && to.name === 'login') {
    // token存在，说明用户登录，此时跳转至首页
    // console.log(2)
    next({ name: 'home' })
  } else {
    // console.log(3)
    next()
  }
})

new Vue({
  router,
  store,
  axios,
  render: h => h(App),
  created() {
    store.commit('addMenu', router)
  }
}).$mount('#app')
