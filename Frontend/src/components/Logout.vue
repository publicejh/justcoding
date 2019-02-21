<!-- <template>
  <v-container>
    <v-layout row v-if="error">
      <v-flex xs12 sm6 offset-sm3>
        <app-alert @dismissed="onDismissed" :text="error.message"></app-alert>
      </v-flex>
    </v-layout>
    <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
        <v-card>
          <v-card-text>
            <v-container>
              <form @submit.prevent="onLogin">
                <v-layout row>
                  <v-flex xs12>
                    <v-text-field
                      name="username"
                      label="Username"
                      id="username"
                      v-model="username"
                      required></v-text-field>
                  </v-flex>
                </v-layout>
                <v-layout row>
                  <v-flex xs12>
                    <v-text-field
                      name="password"
                      label="Password"
                      id="password"
                      v-model="password"
                      type="password"
                      required></v-text-field>
                  </v-flex>
                </v-layout>
                <v-layout>
                  <v-flex xs12>
                    <v-btn type="submit" :loading="loading">Login</v-btn>
                  </v-flex>
                </v-layout>
              </form>
            </v-container>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template> -->

<template>

</template>


<script>
  export default {
    data () {
      return {
        // username: '',
        // password: ''
      }
    },
    computed: {
      user () {
        return this.$store.getters.user
      },
      error () {
        return this.$store.getters.error
      },
      loading () {
        return this.$store.getters.loading
      }
    },
    watch: {
      user (value) {
        // if (value !== null && value !== undefined) { //
        //   this.$router.push('/')
        // }
        if (value == null || value == undefined) { // 로그아웃 된 상태로 업데이트 되면, 첫 화면으로 돌리기
          this.$router.push('/')
        }
      }
    },
    methods: {
      // onLogin () {
      //   this.$store.dispatch('signUserIn', {username: this.username, password: this.password})
      // },
      onLogout () {
        // //여기
        // this.$store.dispatch('signUserout')
        //
        //this.$store.de
        


      },


      onDismissed () {
        this.$store.dispatch('clearError')
      }
    }
  }
</script>
