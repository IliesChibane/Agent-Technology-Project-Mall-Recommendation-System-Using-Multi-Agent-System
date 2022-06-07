import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/Products.vue'
import Vehicles from '../views/Vehicles.vue'
import Rules from '../views/Rules.vue'
import Facts from '../views/Facts.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/vehicles',
    name: 'vehicles',
    component: Vehicles,
  },
  {
    path: '/facts',
    name: 'facts',
    component: Facts,
  },
  {
    path: '/rules',
    name: 'rules',
    component: Rules,
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
