import { CHAT_SERVER_HOST_URL } from "@/settings";
import axios from 'axios'
import WebSocketInstance from '../websocket'

const ChatModule = {
  state: {
    chats: [],
    fetchedMessages: [],
    newMessage: null
  },
  mutations: {
    setMessagesEmpty (state) {
      state.messages = []
    },
    setChats (state, payload) {
      state.chats = payload
    },
    setFetchedMessages (state, payload) {
      state.fetchedMessages = payload
    },
    setNewMessage (state, payload) {
      state.newMessage = payload
    }
  },
  actions: {
    sendMessage ({commit}, payload) {
      let chatID = payload.chatID
      const messageObject = {
        from: payload.username,
        content: payload.content,
        chatId: chatID
      };
      WebSocketInstance.newChatMessage(messageObject);
    },
    loadChats ({commit}) {
        axios({
            method: 'GET',
            url: `${CHAT_SERVER_HOST_URL}/chat/`,
            params: { username: this.getters.user.username}
        })
        .then((response) => {
            commit('setChats', response.data)
        })
        .catch((ex) => {
            
        })
    }
    // createChat ({commit}, payload) {
    //   let newPostKey = firebase.database().ref().child('chats').push().key
    //   let updates = {}
    //   updates['/chats/' + newPostKey] = {name: payload.chatName}
    //   firebase.database().ref().update(updates)
    //   return new Promise((resolve, reject) => {
    //     resolve(newPostKey)
    //   })
    // }
  },
  getters: {
    messages (state) {
      return state.messages
    },
    chats (state) {
      return state.chats
    },
    chatUser (state, getters, rootState, rootGetters) {
      return rootState.auth.user
    },
    fetchedMessages (state) {
      return state.fetchedMessages
    },
    newMessage (state) {
      return state.newMessage
    }
  }
}

export default ChatModule
