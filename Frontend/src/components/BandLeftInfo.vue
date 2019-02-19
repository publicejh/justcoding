<template>
    <div id="app">

    <v-layout row style="width: 300px; margin: 20px 30px auto 100px">
      <v-flex >
        <v-card>
          <v-img
            src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
            height="200px"
          >
          </v-img>
  
          <v-card-title primary-title>
            <div>
              <div class="headline">{{bandName}}</div>
              <span class="grey--text">멤버수 : 3</span>
            </div>
          </v-card-title>
  
          <v-card-actions>
            <!--<v-btn  color="#FFCC80" onclick="location.href=`http://localhost:8080/invite`">멤버초대하기</v-btn>-->
            <v-btn  color="#FFCC80" :to="bandID + /invite/">멤버초대하기</v-btn>
            <v-spacer></v-spacer>

          </v-card-actions>
  
          <v-slide-y-transition>

          </v-slide-y-transition>
        </v-card>
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
</script>
