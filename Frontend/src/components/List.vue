<template>
  <div id="container">
    <div>
      <band-header></band-header>
    </div>
    <div>
    <div>
      <band-list-view></band-list-view>
    </div>
    </div>
      
      
      
  </div>
</template>

<script>
import BandHeader from './BandHeader.vue';
import BandSubHeaderVue from './BandSubHeader.vue';
import BandContents from './BandContents.vue';
import BandMemberVue from './BandMember.vue';
import BandLeftInfoVue from './BandLeftInfo.vue'
import BnadInvite from './BandInvite.vue'
import BandListView from './BandListView.vue'
export default {
  components: {
    'BandHeader' : BandHeader,
    'BandSubHeader' : BandSubHeaderVue, 
    'BandContents' : BandContents,
    'BandMember' : BandMemberVue,
    'BandLeftInfo' : BandLeftInfoVue,
    'BnadInvite' : BnadInvite,
    'BandListView' : BandListView,
  }
}
</script>

<<style>

</style>