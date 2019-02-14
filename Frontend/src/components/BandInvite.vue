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
      <v-btn outline color="black">링크들어가야함</v-btn>
    </div>

      </v-container>
     </v-card>
 



    


</div>


</div>
</template>


<script>
import axios from "axios";
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
  
      axios.get("http://localhost:8000/band/1/member")
      .then(result => {
        console.log(result);
        this.members = result.data;
        console.log("XXXX")
        console.log(this.members);
      });
  
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

  