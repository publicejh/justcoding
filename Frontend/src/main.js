import Vue from 'vue'
import App from './App.vue'
import Vuetify from 'vuetify'
import axios from 'axios'
import moment from 'moment'
// import VueRouter from 'vue-router'
import router from './router'

// Vue.use(VueRouter)

Vue.use(Vuetify, {
  iconfont: 'mdi'
})


Vue.config.productionTip = false
Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('YYYY/MM/DD hh:mm:ss')
  }
});

Vue.use(Vuetify)
Vue.prototype.$http = axios

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
