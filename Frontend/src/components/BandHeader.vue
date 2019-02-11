<template>
  <v-toolbar
    color="#FF9436"
    dark
    class="user_info"
  >
    <v-toolbar-title ><img style="padding:10px 0px 0px 0px;" src="src/assets/sig_logo.png" width="100" height="80" href="#"></v-toolbar-title>

    <v-divider
      class="mx-3"
      inset
      vertical
    ></v-divider>

    <span class="subheading">My Home</span>

    <v-spacer></v-spacer>

    <v-toolbar-items>
      <v-btn flat>
        Alarm
      </v-btn>

      <v-divider vertical></v-divider>

      <v-btn flat>
        Chat Alarm
      </v-btn>

      <v-divider vertical></v-divider>

    <v-menu open-on-hover top offset-y>
      <v-btn flat
      slot="activator">
        이지영 <!--로그인한 유저이름 보여줌-->
      </v-btn>

      <v-list>
        <v-list-tile
          v-for="(item, index) in items"
          :key="index"
        >
          <v-list-tile-title>{{ item.title }}</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-menu>
    
      

      <v-divider vertical></v-divider>
    </v-toolbar-items>

    <!-- <v-toolbar-side-icon>
  </v-toolbar-side-icon> -->
  </v-toolbar>
</template>


<script>
import axios from 'axios'
  export default {
    data: () => ({
      items: [
        { title: '회원정보' },
        { title: '로그아웃' },
        { title: 'Click Me' },
      ]
    }),
    

  }
</script>

<style>
.user_info{
z-index: 2;
}
</style>
