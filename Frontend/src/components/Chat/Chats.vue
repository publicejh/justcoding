<template>
<div id="app" style="width: 250px; position: fixed; right: 20px; top:150px">
<v-layout row style="width: 250px; margin: 0px 100px auto 30px; float: right;">
  <v-flex>
    <v-card>
      
      
  <v-list style="padding:30px">
   
      <span class="headline">채팅</span>
      <div style="float:right">
      <v-dialog v-model="dialog" scrollable max-width="300px">
         <v-btn slot="activator" color="orange" flat>New Chat</v-btn>
       <v-card>
          <v-card-title>멤버선택</v-card-title>
          <v-divider></v-divider>
          <v-card-text style="height: 300px;">
            <p>{{selected}}</p>
            <v-list-tile v-for="member in members" :key="member.username">
              <v-list-tile-content>
                <v-checkbox :value="member.username" 
                            :key="member.username"
                            :label="member.username"
                            v-model="selected"
                            color="orange">
                </v-checkbox>
              </v-list-tile-content>
            </v-list-tile>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn color="orange" flat @click="dialog = false">Close</v-btn>
            <v-btn color="orange" flat @click="createChat">Create</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      </div>
   <v-divider></v-divider>
  <!--  <v-list-tile avatar v-for="(chat, index) in chats" v-bind:key="chat.name" @click="test" :to="/chat/ + chat.id" target="_blank"> -->
    <v-list-tile avatar v-for="(chat, index) in chats" v-bind:key="chat.name" @click="openChat(chat.id)">
      <v-list-tile-content>
        <v-list-tile-title v-html="chat.participants"></v-list-tile-title>
      </v-list-tile-content>
    </v-list-tile>
  </v-list>
       
    
    </v-card>
  </v-flex>

</v-layout>
</div>
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
