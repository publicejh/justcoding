<template>
  <v-list subheader>
    <v-subheader>Chats</v-subheader>
  <!--  <v-list-tile avatar v-for="(chat, index) in chats" v-bind:key="chat.name" @click="test" :to="/chat/ + chat.id" target="_blank"> -->
    <v-list-tile avatar v-for="(chat, index) in chats" v-bind:key="chat.name" @click="openChat(chat.id)">
      <v-list-tile-content>
        <v-list-tile-title v-html="chat.participants"></v-list-tile-title>
      </v-list-tile-content>
    </v-list-tile>
  </v-list>
</template>

<script>
  export default{
    data () {
      return {
        Chats: 'Chats'
      }
    },
    created () {
      this.$store.dispatch('loadChats')
    },
    computed: {
      chats () {
        return this.$store.getters.chats
      }
    },
    methods: {
      openChat (chat_id) {
        
        window.open('/#/chat/' + chat_id,'targetWindow',
        'location=no, scrollbars=yes, status=no, toolbar=no, menubar=no, resizable=yes, width=400, height=622, left=200, top=100')
      }
    },
  }
</script>
