<template>
<div >
  <v-layout id="list_view">

    <router-link to="/band-create" tag="span" style="cursor: pointer">
      <v-hover >
        <v-card
          slot-scope="{ hover }"
          :class="`elevation-${hover ? 12 : 2}`"
          width="250"
          height="250"
          color="#FFF59D"
          style="align:center; padding:45px; margin: 30px"
        >
          <v-card-title>
            <div style="margin : auto">
              <span class="headline">밴드만들기</span>
              <div class="d-flex" style="align:center; margin:auto">
                  <i class="material-icons">add</i>
              </div>
            </div>
            <v-spacer></v-spacer>
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

