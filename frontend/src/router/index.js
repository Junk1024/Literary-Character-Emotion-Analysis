import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
// import User from '../views/User.vue'
import MyMain from '../views/MyMain.vue'
// import Mall from '../views/Mall.vue'
// import PageOne from '../views/PageOne.vue'
// import PageTwo from '../views/PageTwo.vue'
import MyLogin from '../views/Login.vue'
import Resiter from '../views/Resiter.vue'

Vue.use(VueRouter)
// 1.创建路由组件
// 2.将路由于组件进行映射
// 3.创建路由实例
const routes = [
  {
    path: '/',
    component: MyMain,
    name: 'Main',
    // redirect: '/home',
    children: [
      // { path: 'home', name: 'home', component: Home },
      // { path: 'user', name: 'user', component: User },
      // { path: 'mall', name: 'mall', component: Mall },
      // { path: 'page1', name: 'page1', component: PageOne },
      // { path: 'page2', name: 'page2', component: PageTwo }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: MyLogin
  },
  {
    path: '/resiter',
    name: 'resiter',
    component: Resiter
  }
]

const router = new VueRouter({
  mode: 'hash',

  routes // (缩写) 相当于 routes: routes
})
export default router
