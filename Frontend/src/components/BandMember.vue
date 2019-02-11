<template>

 <div
    id="e3"
    style="max-width: 60%; margin: auto;"
    class="grey lighten-3"
    center
  >
  <div>
     <v-card>
      <v-container
        class ="container"
        fluid
        grid-list-lg
      ><h2>멤버 <span class="membernum">3</span></h2> 
      <!-- <v-spacer></v-spacer>이거 쓰면 공간 벌릴 수 있음 -->
    <div class="text-xs-right">
      <v-btn outline color="black">멤버 초대하기</v-btn>
    </div>

      </v-container>
     </v-card>
 

    <div>
      <v-toolbar
        color="#DBBC68"
        dark
        tabs
      >
        <v-text-field
          class="mx-3"
          flat
          label="멤버 검색"
          prepend-inner-icon="search"
          solo-inverted
        ></v-text-field>
      </v-toolbar>
    </div>

    <hr class="one">


<v-layout row>
    <v-flex xs12 >
      <v-card>
        
        <v-list subheader>
          <v-subheader>멤버</v-subheader>
          <v-list-tile
            v-for="item in items"
            :key="item.title"
            avatar
          > 
          <!-- @click="" 위에 이거 넣자-->
            <v-list-tile-avatar>
              <img :src="item.avatar">
            </v-list-tile-avatar>

            <v-list-tile-content>
              <v-list-tile-title v-html="item.title"></v-list-tile-title>
            </v-list-tile-content>

            <v-list-tile-action>
              <v-icon :color="item.active ? 'orange' : 'grey'">chat_bubble</v-icon>
            </v-list-tile-action>
          </v-list-tile>
        </v-list>
      </v-card>
    </v-flex>
  </v-layout>
    


</div>




  </div>
</template>


<script>
export default {
      data () {
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
    }
    
}
</script>



<style>
.container{
    background-color: #D6C8A1
}
.membernum{
    text-decoration-color: #FF9436
}
</style>

  