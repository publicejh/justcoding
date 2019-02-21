<!-- <template>
  <div id="container">

    <div class="left">
      <mypage-left-info :myId="myId"></mypage-left-info>
    </div>
    <div>
      <router-view :myId="myId"></router-view>
    </div>
  </div>
</template>

<script>
  import BandHeader from './BandHeader.vue';
  import MypageLeftInfoVue from './MypageLeftInfo.vue';
  import MypageContents from './MypageContents.vue';
  // import BandSubHeaderVue from './BandSubHeader.vue';
  // import BandContents from './BandContents.vue';
  // import BandMemberVue from './BandMember.vue';
  // import BandLeftInfoVue from './BandLeftInfo.vue';

  export default {
    components: {
      'BandHeader' : BandHeader,
      'MypageLeftInfo' : MypageLeftInfo,
      'MypageContents' : MypageContents,
      // 'BandSubHeader' : BandSubHeaderVue,
      // 'BandContents' : BandContents,
      // 'BandMember' : BandMemberVue,
      // 'BandLeftInfo' : BandLeftInfoVue,
    },

    data () {
      return {

      }
    },
    props: [
      'id'
    ],

    computed: {


      myId () {
        return this.id
      },
      // menuItems () {
      //   let items = [
      //     { title: '전체글', route: `${this.user_id}/content` },
      //     { title: '사진첩', route: `${this.user_id}/gallery` },
      //     { title: '멤버', route: `${this.user_id}/member` }
      //   ]
      //   return items
      // }
    }
  }
</script>

<style>
  .left{
    float: left;
    margin : auto;
  }
</style> -->
