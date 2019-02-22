<template>
<div >
  <v-layout id="list_view">

    <router-link to="/band-create" tag="span" style="cursor: pointer">
      <v-hover class="text-xs-center" style="display:flex">
        <v-card
          slot-scope="{ hover }"
          :class="`elevation-${hover ? 12 : 2}`"
          width="250"
          height="250"
          color="#FFF59D"
          style="align:center; margin: 30px"
          class="text-xs-center"
        >
          <v-card-title class="text-xs-center" style="margin:auto">
            <div style="margin : auto" class="text-md-center">
              <h2 class="text-xs-center" >밴드 생성</h2>
              <div class="d-flex" style="align:center; margin:auto">
                  <i class="material-icons">add</i>
              </div>
            </div>
            
          </v-card-title>
        </v-card>
      </v-hover>
    </router-link>
<v-layout row wrap style="align:center; padding:10px">
    <v-card flat row tile
    v-for="band in bands" v-bind:key="band.id"
      width="250"
      height="250"
      style="align:center; padding:10px; margin:auto"
    >
      <router-link :to="/band/ + band.id" tag="span" style="cursor: pointer">
      <v-img
        :aspect-ratio="16/9"
        src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
      ></v-img>
      <v-card-title>
        <div>
          <span class="headline">{{band.band_name}}</span>
          <div class="d-flex">
            <div class="ml-2 grey--text text--darken-2">
              <span>{{ value }}</span>
            </div>
          </div>
        </div>
        <v-spacer></v-spacer>
      </v-card-title>
      </router-link>
    </v-card>

  </v-layout>

  </v-layout>  
</div>

</template>

<script>
import axios from "axios";
import { PLATFORM_SERVER_HOST_URL } from "../settings"

  export default {
    data: () => ({
      value: 4.5,
      bands:[],
    }),
      
    created() {
      axios.get(`${PLATFORM_SERVER_HOST_URL}/band/`).then(result => {
        console.log('xxxx: ', result);
        this.bands = result.data;
        console.log(this.bands);
      }).catch((e)=>{
        console.log(e)
      })
  
    },
  }
</script>

<style>
/* #list_view{
  display: flex;
  justify-content: center;
  align-items: center;
} */
</style>

