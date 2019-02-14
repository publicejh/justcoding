import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home.vue'
import member from '../components/member.vue'
import Gallery from '../components/Gallery.vue'
import invite from '../components/invite.vue'
import List from '../components/List.vue'
import Newband from '../components/Newband.vue'


Vue.use(Router)

export default new Router({
    routes: [
      {
        path: '/band',
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
      {
        path: '/',
        name: 'list',
        component: List
      },
      {
        path: '/band-create',
        name: 'band-create',
        component: Newband
      },
    ],
    mode: 'history'
  })