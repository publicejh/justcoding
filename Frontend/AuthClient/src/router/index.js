import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import SignUp from '@/components/signup1'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SignUp',
      component: SignUp
    }
  ]
})
