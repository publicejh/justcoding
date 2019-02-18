import Vue from 'vue';
import Router from 'vue-router';

import Signin from '@/pages/Signin/Signin.vue';
import Signup from '@/pages/Signup/Signup.vue';
import Home from '@/pages/Home/Home.vue';


import Findpw1 from '@/pages/Signin/Findpw1.vue';
import Findpw2 from '@/pages/Signin/Findpw2.vue';

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/home',
            name: 'Home',
            component: Home
        },
        {
            path: '/',
            name: 'Signup',
            component: Signup
        },
        {
            path: '/signin',
            name: 'Signin',
            component: Signin
        },
        {
            path: '/findpw1',
            name: 'Findpw1',
            component: Findpw1
        },
        {
            path: '/findpw2',
            name: 'Findpw2',
            component: Findpw2
        }
    ]
});
