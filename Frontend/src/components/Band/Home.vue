<template>
  <div>
      <band-header></band-header>
      <band-sub-header></band-sub-header>
      <div>
        <div style="max-width: 60%; margin: auto; display: inline-block; padding: 10px">
            <band-contents></band-contents>
        </div>
        <div style="max-width: 20%; display: inline-block; margin: auto; padding: 10px">
            <chats></chats>
        </div>
      </div>
  </div>
</template>

<script>
import BandHeader from './BandHeader.vue';
import BandSubHeaderVue from './BandSubHeader.vue';
import BandContents from './BandContents.vue';
// import BandMemberVue from './BandMember.vue';

import Chats from '../Chat/Chats.vue'


export default {
  components: {
    'BandHeader' : BandHeader,
    'BandSubHeader' : BandSubHeaderVue, 
    'BandContents' : BandContents,
    // 'BandMember' : BandMemberVue

    'Chats' : Chats,
  }
}
</script>