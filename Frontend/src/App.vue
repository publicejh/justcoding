<template>
  <!-- <div id="app">
    <band-header></band-header>
    <band-sub-header></band-sub-header>
    <band-contents></band-contents>
    <band-member></band-member>
  </div> -->
  <div>
    <router-view></router-view>
  </div>
</template>

<script>
import BandHeader from './components/BandHeader.vue';
import BandSubHeaderVue from './components/BandSubHeader.vue';
import BandContents from './components/BandContents.vue';
import BandMemberVue from './components/BandMember.vue';
export default {
  components: {
    'BandHeader' : BandHeader,
    'BandSubHeader' : BandSubHeaderVue, 
    'BandContents' : BandContents,
    'BandMember' : BandMemberVue
  }
}
</script>

