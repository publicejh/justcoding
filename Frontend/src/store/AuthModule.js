import { CHAT_SERVER_HOST_URL } from "@/settings";
import axios from 'axios'

const AuthModule = {
  state: {
    user: null
  },
  mutations: {
    setUser (state, payload) {
      state.user = payload

      localStorage.setItem("username", payload.username);
    //   const userListRef = firebase.database().ref('presence')
    //   const myUserRef = userListRef.push()

    //   firebase.database().ref('.info/connected')
    //     .on(
    //       'value', function (snap) {
    //         if (snap.val()) {
    //           // if we lose network then remove this user from the list
    //           myUserRef.onDisconnect()
    //             .remove()
    //           // set user's online status
    //           let presenceObject = {user: payload, status: 'online'}
    //           myUserRef.set(presenceObject)
    //         } else {
    //           // client has lost network
    //           let presenceObject = {user: payload, status: 'offline'}
    //           myUserRef.set(presenceObject)
    //         }
    //       }
    //     )
    }
  },
  actions: {
    // signUserUp ({commit}, payload) {
    //   commit('setLoading', true)
    //   commit('clearError')
    //   firebase.auth().createUserWithEmailAndPassword(payload.email, payload.password)
    //     .then(
    //       user => {
    //         firebase.database().ref('users').child(user.uid).set({
    //           name: payload.username
    //         })
    //           .then(
    //             message => {
    //               commit('setLoading', false)
    //               const newUser = {
    //                 id: user.uid,
    //                 username: payload.username
    //               }
    //               commit('setUser', newUser)
    //             }
    //           )
    //           .catch(
    //             error => {
    //               commit('setLoading', false)
    //               commit('setError', error)
    //             }
    //           )
    //       }
    //     )
    //     .catch(
    //       error => {
    //         commit('setLoading', false)
    //         commit('setError', error)
    //       }
    //     )
    // },
    signUserIn ({commit}, payload) {
      commit('setLoading', true)
      commit('clearError')

      
      axios.post(`${CHAT_SERVER_HOST_URL}/rest-auth/login/`, {
        username: payload.email,
        password: payload.password
      }).then(res => {
          commit('setLoading', false)
          const newUser = {
            username: payload.email
          }
          commit('setUser', newUser)
      }).catch((ex)=>{
        console.log(ex)
        commit('setLoading', false)
        commit('setError', ex)
      })
    }
  },
  getters: {
    user (state) {
      return state.user
    }
  }
}

export default AuthModule
