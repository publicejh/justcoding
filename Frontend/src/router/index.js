import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Signin from '@/components/Signin'
import Signup from '@/components/Signup'
import Band from '../components/Band.vue'
import BandMember from '../components/BandMember.vue'
import BandGallery from '../components/BandGallery.vue'
import invite from '../components/invite.vue'
import Home from '../components/Home.vue'
import Newband from '../components/Newband.vue'
import BandContents from '../components/BandContents.vue';
import BandInvite from '../components/BandInvite.vue';
import AuthGuard from './auth-guard';
// import Mypage from '../components/Mypage.vue';
// import MypageContents from '../components/MypageContents.vue';
// import MypageMenu from '../components/MypageMenu.vue';
import Logout from '../components/Logout.vue';
import IsLogined from './is-logined.js'

Vue.use(Router)

export default new Router({
  routes: [
    // {
    //   path: '/',
    //   name: 'HelloWorld',
    //   component: HelloWorld
    // },
    {
      path: '/',
      name: 'Home',
      component: Home,
      beforeEnter: AuthGuard
    },
    {
      path: '/signin',
      name: 'Signin',
      component: Signin
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup
    },
    {
      path: '/logout',
      name: 'Logout',
      component: Logout,
      beforeEnter: IsLogined
    },
    {
      path: '/band/:id',
      name: 'Band',
      component: Band,
      props: true,
      //beforeEnter: AuthGuard

      // 중첩된 라우트는 children 속성으로 하위 라우트를 정의할 수 있다.
      children: [
        { path: 'content', component: BandContents },
        { path: 'gallery', component: BandGallery },
        { path: 'member', component: BandMember },
        { path: 'invite', component: BandInvite },
      ]
    },
    // {
    //   path: '/member',
    //   name: 'member',
    //   component: member
    // },
    // {
    //   path: '/gallery',
    //   name: 'gallery',
    //   component: Gallery
    // },
    {
      path: '/invite',
      name: 'invite',
      component: invite
    },
    {
      path: '/band-create',
      name: 'band-create',
      component: Newband
    },

  ]
})
