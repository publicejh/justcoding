<template>
 <div id="e3" style="max-width: 60%; margin: auto;" center>

    <v-form>
      <v-container>
        <div>
            <h3>밴드 개설하기</h3>
        </div>
          <v-flex>
            <v-text-field
              label="밴드 이름을 입력하세요."
              color="orange"
              name="bandtitle"
              v-model="bandtitle"
            ></v-text-field>
          </v-flex>
        <div style="float:right;">
           <v-btn color="orange" flat @click="dialog = false">취소</v-btn>
           <v-btn color="orange" flat v-on:click="bandCreate">완료</v-btn>
        </div>
     
      </v-container>
    </v-form>


 </div>
</template>

<script>
import axios from "axios";
import { PLATFORM_SERVER_HOST_URL } from "../settings"
export default {
      data: () => ({
  
      bandtitle: [],
     
     }),
methods: {
  
      bandCreate() {
        axios
          .post(`${PLATFORM_SERVER_HOST_URL}/band/create/`, {
            band_name: this.bandtitle,
            band_leader : this.$store.getters.user.userId, 
            //image : this.ImageUpload,
          })
  
          .then(response => {})
          // .then(console.log(this.postBody))
          // .then(console.log(response.postBody))
          .catch(e => {
            this.errors.push(e);
          });
  
      },
}




}
</script>


<style>

</style>


