<template>
    <div class="hello">
        <h1>{{ msg }}</h1>
        <form @submit.prevent="signin">
            <b-form-group>
                <b-form-input v-model="uid" type="text" placeholder="이메일"></b-form-input>
            </b-form-group>
            <b-form-group>
                <b-form-input v-model="password" type="password" placeholder="비밀번호"></b-form-input>
            </b-form-group>
            <b-button size="lg" variant="success" type="submit">확인</b-button>
        </form>
        <br>
        <p>
          비밀번호를 잊으셨나요?
          <b><u>비밀번호 재설정</u></b>
        </p>
        <p>
          밴드가 처음이신가요?
          <router-link :to="{ name:'Signup' }"><b><u>회원가입</u></b></router-link>
        </p>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'Signin',
        data () {
            return {
                msg: '로그인',
                uid: '',
                password: '',
            };
        },
        methods: {
            signin () {
                const uid = this.uid;
                const password = this.password;

                if (!uid || !password) {
                    return false;
                }

                axios.post('http://localhost:3000/auth/signin', { uid, password })
                    .then(res => {
                        if (res.status === 200) {
                            alert('로그인 성공');
                            document.cookie = `accessToken=${res.data.data.accessToken}`;
                            document.cookie = `refreshToken=${res.data.data.refreshToken}`;
                            axios.defaults.headers.common['x-access-token'] = res.data.data.accessToken;
                            this.$router.push({ name: 'Home' });
                        }
                    })
                    .catch(err => {
                        alert('로그인 실패');
                    })
            }
        }
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

    h1, p {
      text-align: center;
    }

    h1, h2 {
        font-weight: normal;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }

    .btn-lg {
        width: 100%;
    }
</style>
