import { AUTH_SERVER_HOST_URL } from "@/settings";
import { PLATFORM_SERVER_HOST_URL } from "@/settings";
import { CHAT_SERVER_HOST_URL } from "@/settings";
import axios from 'axios'
import jwt_decode from 'jwt-decode'

const SigModule = {
  state: {
    sigId: null,
    invitationSigId: null,
    sigMembers: [],
    isInvitationTokenValid: false,
    sigName: '',
    sigMemberCnt: '',
    sigCoverImgPath: ''
  },
  mutations: {
    setSigId (state, payload) {
      state.sigId = payload
    },
    setInvitationSigId (state, payload) {
      state.invitationSigId = payload
    },
    setSigMembers (state, payload) {
      state.sigMembers = payload
    },
    setSigName (state, payload) {
      state.sigName = payload
    },
    setSigMemberCnt (state, payload) {
      state.sigMemberCnt = payload
    },
    setSigCoverImgPath (state, payload) {
      state.sigCoverImgPath = payload
    },
    setIsInvitationTokenValid (state, payload) {
      state.isInvitationTokenValid = payload
    }
  },
  actions: {
    setSigAll ({commit}, payload) {
      return new Promise((resolve, reject) => {
        axios.get(`${PLATFORM_SERVER_HOST_URL}/band/${payload}`).then(res => {
            
            commit('setSigId', res.data.id)
            commit('setSigName', res.data.band_name)
            commit('setSigCoverImgPath', res.data.band_cover_img_path)
            commit('setSigMemberCnt', res.data.members.length)
            resolve(res);
    
          }).catch((e)=>{
            console.log('errrrr: ', e)
            reject(e);
          })
      })
    },
    setSig ({commit}, payload) {
      commit('setSigId', payload)
    },
    setSigName ({commit}, payload) {
      commit('setSigName', payload)
    },
    setSigCoverImgPath ({commit}, payload) {
      commit('setSigCoverImgPath', payload)
    },
    loadSigMembers ({commit}, payload) {
      axios({
        method: 'GET',
        url: `${PLATFORM_SERVER_HOST_URL}/band/${payload}/member`
      }).then((response) => {
        // state.sigMembers = response.data
        commit('setSigMembers', response.data)
      }).catch((ex) => {
        console.log(ex)
      })
    },
    generateInvitationToken ({commit}, payload) {
      axios.post(`${PLATFORM_SERVER_HOST_URL}/band/${this.getters.sigId}/invitation-token/`, {
        band: parseInt(this.getters.sigId),
        token: payload
      }).then(res => {
        console.log('invitation token created: ', res.data)
      }).catch((ex)=>{
        console.log(ex)
        commit('setIsInvitationTokenValid', false)
      })
    },
    validateInvitationToken ({commit}, payload) {
        return new Promise((resolve, reject) => {
            // Do something here... lets say, a http call using vue-resource
            axios({
                method: 'GET',
                url: `${PLATFORM_SERVER_HOST_URL}/band/n/${payload}`
              }).then((response) => {
                console.log('validate token: ', response.data)
                if(response.data.band){
                    commit('setIsInvitationTokenValid', true)
                    commit('setInvitationSigId', response.data.band)
                    commit('setSigName', response.data.band_name)
                }
                else{
                  commit('setIsInvitationTokenValid', false)
                }
                resolve(response);
              }).catch((ex) => {
                console.log(ex)
                reject(ex);
              })
        })
    },
    acceptInvitation ({commit}, payload) {
        return new Promise((resolve, reject) => {
          console.log('xxx: ', payload)
            // Do something here... lets say, a http call using vue-resource
            axios.post(`${PLATFORM_SERVER_HOST_URL}/band/${payload.sigId}/invite/`, {
                user: jwt_decode(localStorage.getItem("token")).user_id,
                band: payload.sigId,
                is_band_leader: payload.isLeader
              }).then(res => {
                console.log('invitation succeed')
                resolve(res)
              }).catch((ex)=>{
                console.log(ex)
                reject(ex)
              })
        })
    },

      
  },
  getters: {
    sigId (state) {
      return state.sigId
    },
    invitationSigId (state) {
      return state.invitationSigId
    },
    sigMembers (state) {
      return state.sigMembers
    },
    sigName (state) {
      return state.sigName
    },
    sigMemberCnt (state) {
      return state.sigMemberCnt
    },
    sigCoverImgPath (state) {
      return state.sigCoverImgPath
    },
    isInvitationTokenValid (state) {
      return state.isInvitationTokenValid
    }
  }
}

export default SigModule
