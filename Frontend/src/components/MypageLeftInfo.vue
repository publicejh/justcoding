<!-- <template>
    <div id="app">

    <v-layout row style="width: 300px; margin: 20px 30px auto 100px">
      <v-flex >
        
        <v-layout align-center justify-center column fill-height/>
        내 정보
        </v-layout>
      </v-flex>
    </v-layout>

</div>
</template>

<script>
  import axios from 'axios'
  import { PLATFORM_SERVER_HOST_URL } from "../settings"

  export default {
    data () {
      return {
        bandName: '',
        memberCnt: 0
      }
    },

    props: [
      'bandId'
    ],

    created() {
      console.log('zzzzz: ', this.bandID)

      axios.get(`${PLATFORM_SERVER_HOST_URL}/band/${this.bandId}`).then(result => {
        this.bandName = result.data.band_name;
        // this.memberCnt = result.data;

      }).catch((e)=>{
        console.log(e)
      })

    },

    computed: {
      bandId () {
        return this.bandId
      },
      bandName () {
        return this.bandName
      }
    },
  }
</script> -->
