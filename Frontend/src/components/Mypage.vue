<template>
  <div>
    <v-btn @click="logOut">logout</v-btn>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        
      }
    },

    methods: {
      logOut () {
        this.$store.dispatch('signUserOut')
        this.$router.push('/')
      }
    }
  }
</script>
