<template>
  <div class="sub_menu">
      <v-tabs

        slot="extension"
        v-model="model"
        centered
        color="#FFA648"
        slider-color="yellow"
      >
        <v-tab 
          :href="`http://localhost:8080/band`"
        >
          전체글
        </v-tab>
        <v-tab
          :href="`http://localhost:8080/gallery`"
        >
          사진첩
        </v-tab>

        <v-tab
          :href="`http://localhost:8080/member`"
        >
          멤버
        </v-tab>
      </v-tabs>


  </div>
</template>

<script>
  export default {
    data () {
      return {
        model: 'tab-1',
        text : 'test'
        }
    }
  }
</script>

<style>
.sub_menu{
z-index: -100;
}
</style>
