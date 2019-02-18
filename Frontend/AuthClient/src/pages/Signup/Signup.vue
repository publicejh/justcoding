<template>
    <div>
        <br>
        <h1>모임이 쉬워진다! <br>우리끼리 SIG</h1>
        <p>당신의 모임도 SIG로 시작하세요</p>
        <form @submit.prevent="signup">
            <b-form-group>
                <b-form-input type="email" v-model="email" placeholder="이메일로 가입"></b-form-input>
            </b-form-group>
            <!-- <b-form-group label="Enter your password"> -->
            <b-form-group>
                <b-form-input type="password" v-model="password" placeholder="비밀번호"></b-form-input>
            </b-form-group>
            <b-form-group>
                <b-form-input type="text" v-model="uid" placeholder="이름"></b-form-input>
            </b-form-group>
            <!-- <b-form-group label="Enter your position">
                <b-select v-model="position" :options="positionOptions"></b-select>
            </b-form-group>
            <b-form-group label="Enter your role">
                <b-select v-model="role" :options="roleOptions"></b-select>
            </b-form-group> -->
            <b-button size="lg" variant="success" type="submit">Signup</b-button>
        </form>
        <br>
        <p>이미 가입하셨나요? <router-link :to="{ name:'Signin' }"><b><u>로그인하기</u></b></router-link></p>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'Signup',
        data () {
            return {
                uid: '',
                password: '',
                email: '',

                // role: '',
                // position: '',

                // positionOptions: [
                //     { text: '개발자', value: 'developer' },
                //     { text: '기획자', value: 'director' },
                //     { text: '디자이너', value: 'designer' },
                // ],
                // roleOptions: [
                //     { text: '일반', value: 'member' },
                //     { text: '관리자', value: 'admin' },
                // ]
            };
        },
        methods: {
            signup () {
                const uid = this.uid;
                const password = this.password;
                const email = this.email;

                // const position = this.position;
                // const role = this.role;

                if (!uid || !password || !email) {
                    return false;
                }

                // axios.post('http://localhost:3000/auth/signup', { uid, password, position, role })
                axios.post('http://localhost:3000/auth/signup', { uid, password, email })
                    .then(res => {
                        if (res.status === 200) {
                            // 성공적으로 회원가입이 되었을 경우
                            this.$router.push({ name: 'Signin' });
                        }
                    });
            }
        }
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
