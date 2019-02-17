<template>

 <div
    id="e3"
    style="max-width: 40%; margin: auto;"
    class="grey lighten-3"
    center
  >
  <div>
     <v-card>
      <v-container
        class ="container"
        fluid
        grid-list-lg
      ><h2>멤버초대</h2> 
      <!-- <v-spacer></v-spacer>이거 쓰면 공간 벌릴 수 있음 -->
    <div class="text-xs-right">
      <v-btn outline color="black" @click.stop.prevent="copyTestingCode">링크복사하기</v-btn>
      
    </div>
      <v-form>
      <v-container>
        <v-layout row wrap>
  
          <v-flex>
            <v-text-field
              value="http://localhost:8080/invite" 
              label="아래 링크를 복사하여 멤버를 초대하세요."
              id="URL"
              outline
              readonly
            ></v-text-field>
          </v-flex>
  
        </v-layout>
      </v-container>
    </v-form>


      </v-container>
     </v-card>
 



    


</div>


</div>
</template>


<script>
import axios from "axios";
import { PLATFORM_SERVER_HOST_URL } from "../settings"
export default {
      data: () => ({
        members :[],
      }),
      data(){
          
        return {
        items: [
          { active: true, title: 'Jason Oner', avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg' },
          { active: true, title: 'Ranee Carlson', avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg' },
          { title: 'Cindy Baker', avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg' },
          { title: 'Ali Connors', avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg' }
        ],
        items2: [
          { title: 'Travis Howard', avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg' }
        ]
      }
      },
       
        created() {
  
      axios.get(`${PLATFORM_SERVER_HOST_URL}/band/1/member`)
      .then(result => {
        console.log(result);
        this.members = result.data;
        console.log("XXXX")
        console.log(this.members);
      });


    },


    methods: {
        copyTestingCode () {
          let testingCodeToCopy = document.querySelector('#URL')
          testingCodeToCopy.setAttribute('type', 'text') 
          testingCodeToCopy.select()

          try {
            var successful = document.execCommand('copy');
            var msg = successful ? 'successful' : 'unsuccessful';
            alert('링크가 복사되었습니다.');
          } catch (err) {
            alert('링크복사 실패');
          }
          testingCodeToCopy.setAttribute('type', 'text')
          window.getSelection().removeAllRanges()
        },
    },
    
}
</script>



<style>
.container{
    background-color: #FFF59D
}
.membernum{
    text-decoration-color: #FF9436
}
.search{
  color: #FF9436
}
</style>

  