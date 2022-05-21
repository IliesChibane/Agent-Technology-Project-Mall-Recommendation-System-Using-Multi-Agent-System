import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import Agent1 from "../views/Agent1View.vue";
import Agent2 from "../views/Agent2View.vue";
import Agent3 from "../views/Agent3View.vue";


Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/agent1",
    name: "agent1",
    component: Agent1,
  },
  {
    path: "/agent2",
    name: "agent2",
    component: Agent2,
  },
  {
    path: "/agent3",
    name: "agent3",
    component: Agent3,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;