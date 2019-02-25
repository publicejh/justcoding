<template>
  <div style="margin-top:5px">
    <v-flex style="position: relative;">
      <div class="chat-container" v-on:scroll="onScroll" ref="chatContainer" >
        <message :username="username" :messages="messages" @imageLoad="scrollToEnd"></message>
      </div>
      <emoji-picker :show="emojiPanel" @close="toggleEmojiPanel" @click="addMessage"></emoji-picker>
      
      <div class="typer">
          <v-btn icon class="blue--text emoji-panel" @click="toggleEmojiPanel">
            <v-icon>insert_emoticon</v-icon>
          </v-btn>
          <span>
            <label style="margin:0;">
              <form id="myForm" enctype="multipart/form-data"> 
                <input style="display: none;" type="file" id="file" ref="myFiles" class="custom-file-input" @change="previewFiles">
              </form>
              <v-icon>add_a_photo</v-icon>
            </label>
          </span>
          <input type="text" placeholder="Type here..." v-on:keyup.enter="sendMessage" v-model="content">
      </div>
    </v-flex>
  </div>
</template>

<script>
  import Message from './Message.vue'
  import EmojiPicker from './EmojiPicker.vue'
  import WebSocketInstance from '@/websocket'
  import jwt_decode from 'jwt-decode' 
  import axios from "axios";
  import {
    FILE_SERVER_HOST_URL
  } from "@/settings"

  export default {
    data () {
      return {
        content: '',
        chatMessages: [],
        emojiPanel: false,
        currentRef: {},
        loading: false,
        totalChatHeight: 0,
        userId: jwt_decode(localStorage.getItem("token")).user_id
      }
    },
    props: [
      'id'
    ],
    created() {
      this.loadChat()
    },
    mounted () {
      this.totalChatHeight = this.$refs.chatContainer.scrollHeight
    },
    components: {
      'message': Message,
      'emoji-picker': EmojiPicker
    },
    computed: {
      messages () {
        return this.chatMessages
      },
      username () {
        return localStorage.getItem("username")
      },
      onChildAdded () {
        const that = this
        let onChildAdded = function (snapshot, newMessage = true) {
          // let message = snapshot.val()
          let message = snapshot
          message.id = snapshot.id
          /*eslint-disable */
          var urlPattern = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig
          /*eslint-enable */
          if(message.content){
            message.content = message.content
              .replace(/&/g, '&amp;')
              .replace(/</g, '&lt;')
              .replace(/>/g, '&gt;')
              .replace(/"/g, '&quot;')
              .replace(/'/g, '&#039;')
            message.content = message.content.replace(urlPattern, "<a href='$1'>$1</a>")
          }
          if (!newMessage) {
            that.chatMessages.unshift(that.processMessage(message))
            that.scrollTo()
          } else {
            that.chatMessages.push(that.processMessage(message))
            that.scrollToEnd()
          }
        }
        return onChildAdded
      },
      fetchMessages () {
        return this.$store.getters.fetchedMessages
      },
      newMessage () {
        return this.$store.getters.newMessage
      }
    },
    watch: {
      fetchMessages (val, oldVal) {
        console.log('watched fetchMessages: ', val)
        const that = this
        let tempArray = []
        val.forEach(function (item) {
          tempArray.push(item)
        })
        // if (tempArray[0].key === tempArray[1].key) return
        tempArray.forEach(function (child) { that.onChildAdded(child, false) })
        that.loading = false
      },
      newMessage (val, oldVal) {
        console.log('watched newMessage: ', val)
        const that = this
        that.onChildAdded(val)
      }

    },
    methods: {
      loadChat () {
        this.loading = false
        if (this.id !== undefined) {
          this.chatMessages = []
          let chatID = this.id
          this.waitForSocketConnection(() => {
            WebSocketInstance.fetchMessages(
              '',
              chatID
            );
          });
          WebSocketInstance.connect(chatID);
        }
      },
      waitForSocketConnection(callback) {
        const component = this;
        setTimeout(function() {
          if (WebSocketInstance.state() === 1) {
            console.log("Connection is made");
            callback();
            return;
          } else {
            console.log("wait for connection...");
            component.waitForSocketConnection(callback);
          }
        }, 100);
      },
      onScroll () {
        let scrollValue = this.$refs.chatContainer.scrollTop
        const that = this
        if (scrollValue < 100 && !this.loading) {
          this.totalChatHeight = this.$refs.chatContainer.scrollHeight
          this.loading = true
          let chatID = this.id
          let currentTopMessage = this.chatMessages[0]
          if (currentTopMessage === undefined) {
            this.loading = false
            return
          }

          WebSocketInstance.fetchMessages(
            '',
            chatID,
            currentTopMessage.id
          );
        }
      },
      processMessage (message) {
        /*eslint-disable */
        var imageRegex = /([^\s\']+).(?:jpg|jpeg|gif|png)/i
        /*eslint-enable */
        if (imageRegex.test(message.content)) {
          message.image = imageRegex.exec(message.content)[0]
        }
        var emojiRegex = /([\u{1f300}-\u{1f5ff}\u{1f900}-\u{1f9ff}\u{1f600}-\u{1f64f}\u{1f680}-\u{1f6ff}\u{2600}-\u{26ff}\u{2700}-\u{27bf}\u{1f1e6}-\u{1f1ff}\u{1f191}-\u{1f251}\u{2934}-\u{1f18e}])/gu
        if (emojiRegex.test(message.content)) {
          message.content = message.content.replace(emojiRegex, '<span class="emoji">$1</span>')
        }
        return message
      },
      sendMessage () {
        if (this.content !== '') {
          this.$store.dispatch('sendMessage', { username: this.username, content: this.content, date: new Date().toString(), chatID: this.id })
          this.content = ''
        }
      },
      scrollToEnd () {
        this.$nextTick(() => {
          var container = this.$el.querySelector('.chat-container')
          container.scrollTop = container.scrollHeight
        })
      },
      scrollTo () {
        this.$nextTick(() => {
          let currentHeight = this.$refs.chatContainer.scrollHeight
          let difference = currentHeight - this.totalChatHeight
          var container = this.$el.querySelector('.chat-container')
          container.scrollTop = difference
        })
      },
      addMessage (emoji) {
        this.content += emoji.value
      },
      toggleEmojiPanel () {
        this.emojiPanel = !this.emojiPanel
      },
      previewFiles() {
        var self = this;

        this.files = this.$refs.myFiles.files
        var formID = "myForm";
  
        var form = document.getElementById(formID);
        var formData = new FormData(form);

        formData.append('file', this.files[0]);
        formData.append('userId', this.userId);
        formData.append('chatId', this.id);
  
        axios({
            method: 'post',
            url: `${FILE_SERVER_HOST_URL}/file_manage/chat/upload/image/`,
            contentType: false,
            processData: false,
            data: formData,
            config: {
              headers: {
                'Content-Type': 'multipart/form-data'
              }
            }
          })
          .then(function(response) {
            //handle success
            console.log(response)
  
          })
          .catch(function(response) {
            //handle error
            console.log(response);
          });
      },
    }
  }
</script>

<style>
  .scrollable {
    overflow-y: auto;
    height: 90vh;
  }
  .typer{
    box-sizing: border-box;
    display: flex;
    align-items: center;
    bottom: 0;
    height: 4.9rem;
    width: 100%;
    background-color: #fff;
    box-shadow: 0 -5px 10px -5px rgba(0,0,0,.2);
  }
  .typer .emoji-panel{
    /*margin-right: 15px;*/
  }
  .typer input[type=text]{
    left: 2.5rem;
    padding: 1rem;
    width: 80%;
    background-color: transparent;
    border: none;
    outline: none;
    font-size: 1.25rem;
  }
  .chat-container{
    box-sizing: border-box;
    height: calc(100vh - 9.5rem);
    overflow-y: auto;
    padding: 10px;
    background-color: #f2f2f2;
  }
  .message{
    margin-bottom: 3px;
    text-align: left;
  }
  .message.own{
    text-align: right;
  }
  .message.own .content{
    background-color: lightskyblue;
  }
  .chat-container .username{
    font-size: 18px;
    font-weight: bold;
  }
  .chat-container .content{
    padding: 8px;
    background-color: lightgreen;
    border-radius: 10px;
    display:inline-block;
    box-shadow: 0 1px 3px 0 rgba(0,0,0,0.2), 0 1px 1px 0 rgba(0,0,0,0.14), 0 2px 1px -1px rgba(0,0,0,0.12);
    max-width: 50%;
    word-wrap: break-word;
    }
  @media (max-width: 480px) {
    .chat-container .content{
      max-width: 60%;
    }
  }

</style>
