import Vue from 'vue';
import VueRouter from 'vue-router';
// import Register from '../components/Register.vue';
import Login from '../components/Login.vue';
import Register from '../components/Register.vue';


Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Register,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
  ],
});
