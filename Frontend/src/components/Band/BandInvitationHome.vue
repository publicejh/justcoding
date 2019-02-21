<template>

      <v-dialog v-model="dialog" scrollable max-width="300px">
        <v-card>
          <v-card-title>SIG Invitation</v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            {{sigName}}
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn flat @click="">Refuse</v-btn>
            <v-btn color="blue darken-1" flat @click="acceptInvitation">Accept</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
</template>

<script>
  export default {

    data () {
      return {
        token: null,
        dialog: true,
      }
    },
    // props: [
    //   'token'
    // ],

    created() {
      this.token = this.$route.params.token
      this.$store.dispatch('validateInvitationToken', this.token).then((res => {
        // ...

        if(this.$store.getters.isInvitationTokenValid === false){
            alert('invalid invitation url')
            // this.$router.go(-1)
            this.$router.push("/")
        }
      }), error => {
            console.error("Got nothing from server. Prompt user to check internet connection and try again")
        })
    },

    mounted() {
    },

    computed: {
        sigName () {
            return this.$store.getters.sigName
        }
    },

    methods: {
  
      acceptInvitation() {
          this.$store.dispatch('acceptInvitation').then((res => {
            alert('yyyyinvitation succeed')
            this.$router.push(`/band/${this.$store.getters.invitationSigId}`)
              
            }), error => {
                console.error("Got nothing from server. Prompt user to check internet connection and try again")
            })
      }
    }

  }
</script>

<style>
  .left{
    float: left;
    margin : auto;
  }
</style>