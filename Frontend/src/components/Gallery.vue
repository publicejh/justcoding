<template>
  <div>
      <band-header></band-header>
      <band-sub-header></band-sub-header>
      <band-gallery></band-gallery>
  </div>
</template>

<script>
import BandHeader from './BandHeader.vue';
import BandSubHeaderVue from './BandSubHeader.vue';
import BandContents from './BandContents.vue';
import BandMemberVue from './BandMember.vue';
import BandGallery from './BandGallery.vue';
export default {
  components: {
    'BandHeader' : BandHeader,
    'BandSubHeader' : BandSubHeaderVue, 
    'BandContents' : BandContents,
    'BandMember' : BandMemberVue,
    'BandGallery' : BandGallery
  }
}
</script>