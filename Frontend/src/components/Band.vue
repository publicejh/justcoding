<template>
  <div id="container">
    <v-toolbar color="#FFA648">
      
      <v-toolbar-items v-for="item in menuItems">
        <v-btn flat :key="item.title" :to="item.route">
          <div class="hidden-xs-only">{{ item.title }}</div>
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
        <chats></chats>
      </div>    
       <div>
      <router-view :bandId="id"></router-view>
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
      'BandHeader' : BandHeader,
      'BandSubHeader' : BandSubHeaderVue, 
      'BandContents' : BandContents,
      'BandMember' : BandMemberVue,
      'BandLeftInfo' : BandLeftInfoVue,
      'Chats' : Chats,
    },

    data () {
      return {
        
      }
    },
    props: [
      'id'
    ],

    created() {
      this.$store.dispatch('setSig', this.id)
    },

     
    mounted() {
      this.$store.dispatch('loadSigMembers')
      // this.$router.push("/band/1/content")
    },

    computed: {
      // id () {
      //   return this.id
      // },
      menuItems () {
        let items = [
          { title: '전체글', route: `/band/${this.id}` },
          { title: '사진첩', route: `/band/${this.id}/gallery` },
          { title: '멤버', route: `/band/${this.id}/member` }
        ]
        return items
      }
    }
  
}

</script>

<style>
  .left{
    float: left;
    margin : auto;
  }
  .right{
    float: right;
    margin : auto;
  }
  #wrapper{
    padding: 10px;
  }
</style>
