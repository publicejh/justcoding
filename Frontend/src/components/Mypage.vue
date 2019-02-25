<template>
  <v-container>
    <v-layout justify-center>
      <v-flex xs6>
        <v-card>
          <v-list subheader>
            <v-list-tile>
              내정보
            </v-list-tile>
          </v-list>
          <v-divider></v-divider>
          <v-list subheader>
            <v-subheader>멤버</v-subheader>
            <v-list-tile>
  
              <v-list-tile-content>
                <v-list-tile-title></v-list-tile-title>
  
              </v-list-tile-content>
  
              <v-list-tile-action>
                <v-icon>chat_bubble</v-icon>
              </v-list-tile-action>
            </v-list-tile>
          </v-list>
          <v-divider></v-divider>
          <v-list subheader>
            <v-subheader>멤버</v-subheader>
            <v-list-tile>
  
              <v-list-tile-content>
                <v-list-tile-title></v-list-tile-title>
  
              </v-list-tile-content>
  
              <v-list-tile-action>
                <v-icon>chat_bubble</v-icon>
              </v-list-tile-action>
            </v-list-tile>
          </v-list>
        </v-card>
      </v-flex>
      <v-btn @click="logOut">logout</v-btn>
  
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    data() {
      return {
  
      }
    },
  
    methods: {
      logOut() {
        this.$store.dispatch('signUserOut')
        this.$router.push('/')
      }
    }
  }
</script>
