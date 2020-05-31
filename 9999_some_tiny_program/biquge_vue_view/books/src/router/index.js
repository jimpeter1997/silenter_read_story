import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import HomeCate from "../views/HomeCate.vue";
import BookIndex from "../views/BookIndex.vue";
import BookDetail from "../views/BookDetail.vue";

Vue.use(VueRouter);

const routes = [
  // 网站首页路径
  {
    path: "/",
    name: "Home",
    component: Home
  },
  // 网站分类路径
  {
    path: "/:cate",
    name: "HomeCate",
    component: HomeCate
  },

  // 图书首页路径
  {
    path: "/book/:book_id",
    name: "BookIndex",
    component: BookIndex
  },

  // 图书详情页路径
  {
    path: "/book/:book_id/:cap_id",
    name: "BookDetail",
    component: BookDetail
  },

  // {
  //   path: "/about",
  //   name: "About",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/About.vue")
  // }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
