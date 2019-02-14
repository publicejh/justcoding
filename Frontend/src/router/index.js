import Vue from 'vue'
import Router from 'vue-router'
import Signin from '@/components/User/Signin'
import Home from '@/components/Band/Home'
import Chats from '@/components/Chat/Chats'
import Chat from '@/components/Chat/Chat'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Signin',
      component: Signin
    },
    {
      path: '/main',
      name: 'Home',
      component: Home
    },
    {
      path: '/chat',
      name: 'Chats',
      component: Chats
    },
    {
      path: '/chat/:id',
      name: 'Chat',
      component: Chat,
      props: true
      // beforeEnter: AuthGuard
    }
  ]
})
