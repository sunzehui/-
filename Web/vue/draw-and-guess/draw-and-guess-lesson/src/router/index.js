import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: () => import('@/views/Login/index') },
  { path: '/home', component: () => import('@/views/Game/index') }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  const nickname = localStorage.getItem('nickname')
  if (nickname) {
    // 有昵称，登录过了，没有必要再访问一次登录，直接引导到首页
    if (to.path === '/login') {
      next({ path: '/home' })
    } else {
      next()
    }
  } else {
    // 没有昵称了，不允许访问除了登录页以外的所有页面
    if (to.path === '/login') {
      next()
    } else {
      next({ path: '/login' })
    }
  }
})

export default router
