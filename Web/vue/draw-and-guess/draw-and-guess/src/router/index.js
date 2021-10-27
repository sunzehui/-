import Vue from 'vue'
import VueRouter from 'vue-router'


//解决编程式路由往同一地址跳转时会报错的情况
const originalPush = VueRouter.prototype.push;
const originalReplace = VueRouter.prototype.replace;
//push
VueRouter.prototype.push = function push(location, onResolve, onReject) {
    if (onResolve || onReject)
        return originalPush.call(this, location, onResolve, onReject);
    return originalPush.call(this, location).catch(err => err);
};
//replace
VueRouter.prototype.replace = function push(location, onResolve, onReject) {
    if (onResolve || onReject)
        return originalReplace.call(this, location, onResolve, onReject);
    return originalReplace.call(this, location).catch(err => err);
};


Vue.use(VueRouter)

const routes = [
    {path: '/', redirect: '/login'},
    {path: '/login', component: () => import('@/views/Login/index')},
    {path: '/home', component: () => import('@/views/Game/index')}
]

const router = new VueRouter({
    routes
})


router.beforeEach((to, from, next) => {
    const nickname = localStorage.getItem('nickname')

    // 缓存中有昵称
    if (nickname) {
        // 当前是登录页
        if (to.path === '/login') {
            next({path: '/home'})
        } else {
            next()
        }
    } else {
        // 当前是登录页
        if (to.path === '/login') {
            next()
        } else {
            next({path: '/login'})
        }
    }
})

export default router
