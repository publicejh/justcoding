<template>
  <div v-if="dataReady" id="container">
    <v-toolbar color="#FFA648" style="position: fixed; top:50px; z-index: 10000000;" height="34px" flat>
      <v-toolbar-items>
        <v-btn flat :key="1" :to="`/band/${this.id}`" style="margin-left: 550px;">
          <div class="hidden-xs-only">전체글</div>
        </v-btn>
        <v-btn flat :key="2" :to="`/band/${this.id}/gallery`">
          <div class="hidden-xs-only">사진첩</div>
        </v-btn>
        <v-btn flat :key="3" :to="`/band/${this.id}/member`">
          <div class="hidden-xs-only">멤버</div>
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>
  
    <div row id="wrapper">
      <!--<band-sub-header :bandId="bandId"></band-sub-header>-->
      <div class="left">
        <!--<band-left-info :bandId="bandId"></band-left-info>-->
        <band-left-info v-bind:bandid="id"></band-left-info>
      </div>
  
      <!-- <div style="max-width: 20%; display: inline-block; margin: auto; padding: 10px"> -->
      <div class="right">
        <chats v-bind:bandid="id"></chats>
      </div>
      <div style="margin-top:35px">
        <router-view :bandId="id" :key="$route.fullPath"></router-view>
        <!-- <band-contents :bandId="id"></band-contents> -->
      </div>
      <!-- </div> -->
    </div>
  </div>
</template>

<script>
  import BandHeader from './BandHeader.vue';
  import BandSubHeaderVue from './BandSubHeader.vue';
  import BandContents from './BandContents.vue';
  import BandMemberVue from './BandMember.vue';
  import BandLeftInfoVue from './BandLeftInfo.vue';
  import Chats from './Chat/Chats.vue';
  
  export default {
    components: {
      'BandHeader': BandHeader,
      'BandSubHeader': BandSubHeaderVue,
      'BandContents': BandContents,
      'BandMember': BandMemberVue,
      'BandLeftInfo': BandLeftInfoVue,
      'Chats': Chats,
    },
  
    data() {
      return {
        dataReady: false
      }
    },
    props: [
      'id'
    ],
  
    created() {
      this.$store.dispatch('setSigAll', this.id).then((res => {
        
        this.dataReady = true
      }), error => {
        console.error("Got nothing from server. Prompt user to check internet connection and try again")
      })
  
    },
  
  
    mounted() {
      if(this.dataReady){
      this.$store.dispatch('loadSigMembers', this.id)
      }
      // this.$router.push("/band/1/content")
    },
  
    computed: {
      // id () {
      //   return this.id
      // },
      menuItems() {
        let items = [{
            title: '전체글',
            route: `/band/${this.id}`
          },
          {
            title: '사진첩',
            route: `/band/${this.id}/gallery`
          },
          {
            title: '멤버',
            route: `/band/${this.id}/member`
          }
        ]
        return items
      }
    }
  
  }
</script>

<style>
  .left {
    float: left;
    margin: auto;
  }
  
  .right {
    float: right;
    margin: auto;
  }
  
  #wrapper {
    padding: 10px;
  }
</style>
