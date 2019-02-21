<template>
  <v-list subheader>
    <v-subheader>
      Chats
      <v-dialog v-model="dialog" scrollable max-width="300px">
        <v-btn slot="activator" color="primary" dark>+</v-btn>
        <v-card>
          <v-card-title>Select Country</v-card-title>
          <v-divider></v-divider>
          <v-card-text style="height: 300px;">
            {{selected}}
            <v-list-tile v-for="member in members" :key="member.username">
              <v-list-tile-content>
                <v-checkbox :value="member.username" 
                            :key="member.username"
                            :label="member.username"
                            v-model="selected">
                </v-checkbox>
              </v-list-tile-content>
            </v-list-tile>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn color="blue darken-1" flat @click="dialog = false">Close</v-btn>
            <v-btn color="blue darken-1" flat @click="createChat">Create</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-subheader>
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
        Chats: 'Chats',
        dialogm1: '',
        dialog: false,
        selected: []
      }
    },
    created () {
      this.$store.dispatch('loadChats')
    },
    computed: {
      chats () {
        return this.$store.getters.chats
      },
      members () {
        let items = [
          { title: '전체글' },
          { title: '전체1글'}
        ]


        items = this.$store.getters.sigMembers
        console.log('rrrrrrr: ', items)


        return items
      }
    },
    methods: {

      createChat () {
        this.$store.dispatch('createChat', {bandId: parseInt(this.$store.getters.sigId), participants: this.selected})

      },

      openChat (chat_id) {
        
        window.open('/#/chat/' + chat_id,'targetWindow',
        'location=no, scrollbars=yes, status=no, toolbar=no, menubar=no, resizable=yes, width=400, height=622, left=200, top=100')
      }
    },
  }
</script>
