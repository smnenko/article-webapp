import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/auth/Home')
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('@/views/auth/Signup')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/auth/Login')
  },
  {
    path: '/logout',
    name: 'logout',
    component: () => import('@/views/auth/Logout')
  },
  {
    path: '/write',
    name: 'write',
    component: () => import('@/views/article/Write')
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('@/views/auth/Profile')
  },
  {
    path: '/article/:id',
    name: 'article',
    component: () => import('@/views/article/Detail'),
    props: (route) => ({id: route.params.id}),
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
