<template>
    <div id="app" style="position: fixed; top: 101px;">

    <v-layout row style="width: 250px; margin: 0px 30px auto 152px">
      <v-flex >
        <v-card flat>
          <v-img
            :src="sigCoverImgSrc"
            height="200px"
          >
          </v-img>
  
          <v-card-title style="padding-bottom: 0;" primary-title>
            <div>
              <div class="headline">{{this.$store.getters.sigName}}</div>
              <span>멤버 {{this.$store.getters.sigMemberCnt}}</span>
              <v-btn style="min-width: 0;" small flat color="orange" :to="`/band/${bandid}/invite`">
                <v-icon small color="orange">control_point</v-icon>
                초대
              </v-btn>
            </div>
          </v-card-title>
  
          <v-card-actions>
            <v-btn color="grey" small flat :to="`/band/${bandid}/setting`">
             <v-icon color="grey">settings</v-icon>
             시그 설정
            </v-btn>
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
  import { PLATFORM_SERVER_HOST_URL, FILE_SERVER_HOST_URL } from "../settings"

  export default {
    data () {
      return {
        bandName: '',
        memberCnt: 0,
        sigCoverImgSrc: `${FILE_SERVER_HOST_URL}` + this.$store.getters.sigCoverImgPath,
      }
    },

    props: [
      'bandid'
    ],


  }
</script>
