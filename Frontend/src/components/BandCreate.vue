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
           <v-btn color="orange" flat a href="http://localhost:8080/#/">취소</v-btn>
           <v-btn color="orange" flat v-on:click="bandCreate">완료</v-btn>
        </div>
     
      </v-container>
    </v-form>


 </div>
</template>

<script>
import axios from "axios";
import { PLATFORM_SERVER_HOST_URL } from "../settings"
  import jwt_decode from 'jwt-decode'
export default {
      data: () => ({
  
      bandtitle: [],
     
     }),
methods: {
  
      bandCreate() {
        axios
          .post(`${PLATFORM_SERVER_HOST_URL}/band/create/`, {
            band_name: this.bandtitle,
            band_leader : jwt_decode(localStorage.getItem("token")).user_id, 
            //image : this.ImageUpload,
          }).then(response => {
            this.acceptInvitation(response.data.id)}
          ).catch(e => {
            console.error(e);
          });
  
      },

      acceptInvitation(sigId) {
          this.$store.dispatch('acceptInvitation', {sigId: sigId, isLeader:true}).then((res => {
            alert('invitation succeed')
            this.$router.push(`/band/${sigId}`)
              
            }), error => {
                console.error("Got nothing from server. Prompt user to check internet connection and try again")
            })
      }
}




}
</script>


<style>

</style>


