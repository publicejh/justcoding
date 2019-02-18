<template>
    <div class="hello">
        <h1>{{ msg }}</h1>
        <p>인증 메일을 발송했습니다.<br>
          이메일로 받은 인증번호를 입력하세요.
        </p>
        <form @submit.prevent="findpw2">
            <b-form-group>
                <b-form-input v-model="vnum" type="text"></b-form-input>
            </b-form-group>
            <b-button size="lg" variant="success" type="submit">확인</b-button>
        </form>
        <p>인증 번호가 오지 않는다면?</p>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'Findpw2',
        data () {
            return {
                msg: 'bong',
                uid: '',
                vnum: '',
            };
        },
        methods: {
            findpw2 () {
                const uid = this.uid;
                //const msgs = this.msg;
                const vnum = this.vnum;

                if (!uid) {
                    return false;
                }

                axios.post('http://localhost:3000/auth/findpw2', { uid })
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
                        //alert('존재하지 않는 이메일입니다');
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
