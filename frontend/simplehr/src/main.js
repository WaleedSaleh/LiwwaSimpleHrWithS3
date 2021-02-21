import Vue from 'vue';
import Vuelidate from 'vuelidate';
import 'bootstrap/dist/css/bootstrap.css';
import App from './App.vue';
import router from './router';

Vue.use(Vuelidate);
Vue.config.productionTip = false;


new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
