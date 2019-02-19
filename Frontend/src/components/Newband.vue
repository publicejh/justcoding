<template>
  <div>
    <band-create></band-create>
  </div>
</template>

<script>
import BandHeader from './BandHeader.vue';
import BandSubHeaderVue from './BandSubHeader.vue';
import BandContents from './BandContents.vue';
import BandMemberVue from './BandMember.vue';
import BandLeftInfoVue from './BandLeftInfo.vue'
import BnadInvite from './BandInvite.vue'
import BandCreate from './BandCreate.vue'
export default {
  components: {
    'BandHeader' : BandHeader,
    'BandSubHeader' : BandSubHeaderVue, 
    'BandContents' : BandContents,
    'BandMember' : BandMemberVue,
    'BandLeftInfo' : BandLeftInfoVue,
    'BnadInvite' : BnadInvite,
    'BandCreate' : BandCreate,
  }
}
</script>

</style>