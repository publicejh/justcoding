import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home.vue'
import member from '../components/member.vue'
import Gallery from '../components/Gallery.vue'
import invite from '../components/invite.vue'


Vue.use(Router)

export default new Router({
    routes: [
      {
        path: '/',
        name: 'Home',
        component: Home
        //beforeEnter: AuthGuard
      },
      {
        path: '/member',
        name: 'member',
        component: member
      },
      {
        path: '/gallery',
        name: 'gallery',
        component: Gallery
      },
      {
        path: '/invite',
        name: 'invite',
        component: invite
      },
    ],
    mode: 'history'
  })