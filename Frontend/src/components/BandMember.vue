<template>
  <div id="e3" style="max-width: 38%; margin: auto;" center>
    <!--
         <v-card>
          <v-container
            class ="container"
            fluid
            grid-list-lg
          ><h2>멤버 <span class="membernum">3</span></h2>
        <div class="text-xs-right">
          <v-btn outline color="black" onclick="location.href=`http://localhost:8080/invite`">멤버 초대하기</v-btn>
        </div>
    
          </v-container>
         </v-card>
     
    
        <div>
          <v-toolbar
            color="#FFF59D"
            tabs
          >
            <v-text-field
            class="search"
              flat
              label="멤버 검색"
              prepend-inner-icon="search"
            ></v-text-field>
          </v-toolbar>
        </div>
    
        <hr class="one">
      -->
  
    <v-layout row>
      <v-flex xs12>
        <v-card>
          <v-list subheader>
            <v-subheader><h5>멤버</h5></v-subheader>
            <v-list-tile v-for="member in members" :key="member.username" avatar>
              <!-- @click="" 위에 이거 넣자-->
              <v-list-tile-avatar>
                <img :src="member.avatar">
              </v-list-tile-avatar>
  
              <v-list-tile-content>
                <v-list-tile-title v-html="member.username"></v-list-tile-title>
  
              </v-list-tile-content>
  
              <v-list-tile-action>
                <v-icon :color="member.active ? 'orange' : 'grey'">chat_bubble</v-icon>
              </v-list-tile-action>
            </v-list-tile>
          </v-list>
        </v-card>
      </v-flex>
    </v-layout>
  </div>
</template>


<script>
  import axios from "axios";
  import {
    PLATFORM_SERVER_HOST_URL
  } from "../settings"
  
  export default {
    data() {
  
      return {
        members: [],
        items2: [{
            active: true,
            title: 'Jason Oner',
            avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg'
          },
          {
            active: true,
            title: 'Ranee Carlson',
            avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg'
          },
          {
            title: 'Cindy Baker',
            avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg'
          },
          {
            title: 'Ali Connors',
            avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg'
          }
        ],
        items: []
      }
    },
  
    props: [
      'bandId'
    ],
  
    created() {
  
      axios.get(`${PLATFORM_SERVER_HOST_URL}/band/${this.bandId}/member`)
        .then(result => {
          this.members = result.data;
  
          // this.members.forEach(function (member) {
          //   tempArray.push(item)
          // })
        });
    },
  
  }
</script>



<style>
  
  .membernum {
    text-decoration-color: #FF9436
  }
  
  .search {
    color: #FF9436
  }
</style>

