// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import { store } from './store'
import Vue from 'vue'
import App from './App.vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import axios from 'axios'
import moment from 'moment'
import router from './router'
import PictureInput from 'vue-picture-input'

Vue.use(PictureInput);

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

Vue.config.productionTip = false
Vue.use(Vuetify)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
