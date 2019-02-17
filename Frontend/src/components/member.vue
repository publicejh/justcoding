<template>
  <div id="container">
    <div>
      <band-header></band-header>
      <band-sub-header></band-sub-header>
    </div>
    <div>
    <div class="left">
      <band-left-info></band-left-info>
    </div>
    <div>
      <band-member></band-member>
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
export default {
  components: {
    'BandHeader' : BandHeader,
    'BandSubHeader' : BandSubHeaderVue, 
    'BandContents' : BandContents,
    'BandMember' : BandMemberVue,
    'BandLeftInfo' : BandLeftInfoVue,
  }
}
</script>

<<style>
  .left{
    float: left;
    margin : auto;
  }
</style>