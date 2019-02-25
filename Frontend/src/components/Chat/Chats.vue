<template>
  <div id="app" style="width: 250px; position: fixed; right: 20px; top:101px">
    <v-layout row style="width: 250px; margin: 0px 143px auto 30px; float: right;">
      <v-flex>
        <v-card flat>
  
  
          <v-list style="padding:20px">
            <span class="">채팅</span>
            <div style="float:right">
              <v-dialog v-model="dialog" scrollable max-width="300px">
                <v-btn style="margin-top:0;padding-bottom:10px;" small slot="activator" color="orange" flat>새 채팅</v-btn>
                <v-card>
                  <v-card-title>멤버선택</v-card-title>
                  <v-divider></v-divider>
                  <v-card-text style="height: 300px;">
                    <p>{{selected}}</p>
                    <v-list-tile v-for="member in members" :key="member.username">
                      <v-list-tile-content>
                        <v-checkbox :value="member.username" :key="member.username" :label="member.username" v-model="selected" color="orange">
                        </v-checkbox>
                      </v-list-tile-content>
                    </v-list-tile>
                  </v-card-text>
                  <v-divider></v-divider>
                  <v-card-actions>
                    <v-btn color="orange" flat @click="dialog = false">Close</v-btn>
                    <v-btn color="orange" flat v-on:click="createChat" @click="dialog = false">Create</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </div>
            <v-divider></v-divider>
            <div style="max-height: 250px; overflow-y: scroll;">
              <v-list-tile avatar v-for="(chat, index) in chats" v-bind:key="chat.name" @click="openChat(chat.id)">
                <v-list-tile-content>
                  <v-layout row wrap style="padding-left: 13px;">
                    <v-flex>
                      <v-icon medium>account_circle</v-icon>
                    </v-flex>
                    <v-flex style="position: absolute; margin-left: 48px;">
                      <v-list-tile-title v-html="String(chat.participants).split(',').join(', ')"></v-list-tile-title>
                    </v-flex>
                  </v-layout>
                </v-list-tile-content>
              </v-list-tile>
            </div>
          </v-list>
  
  
        </v-card>
      </v-flex>
  
    </v-layout>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        Chats: 'Chats',
        dialogm1: '',
        dialog: false,
        selected: []
      }
    },
  
    props: [
      'bandid'
    ],
  
    created() {
      this.$store.dispatch('loadChats', this.bandid)
      this.$store.dispatch('loadSigMembers', this.bandid)
  
    },
    computed: {
      chats() {
        return this.$store.getters.chats
      },
      members() {
  
        let items = this.$store.getters.sigMembers
  
  
        return items
      }
    },
    methods: {
      createChat() {
        this.$store.dispatch('createChat', {
          bandId: parseInt(this.$store.getters.sigId),
          participants: this.selected
        }).then((res => {
          console.log('createafdsfa: ', res)
          window.open('/#/chat/' + res.data.id, 'targetWindow',
            'location=no, scrollbars=yes, status=no, toolbar=no, menubar=no, resizable=yes, width=400, height=622, left=200, top=100')
        }), error => {
          console.error("Got nothing from server. Prompt user to check internet connection and try again")
        })
  
      },
      openChat(chat_id) {
        window.open('/#/chat/' + chat_id, 'targetWindow',
          'location=no, scrollbars=yes, status=no, toolbar=no, menubar=no, resizable=yes, width=400, height=622, left=200, top=100')
      }
    },
  }
</script>
