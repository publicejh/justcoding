<template>
  <div class="image">
    <img :src="imgSrc">
  </div>
</template>

<script>
  import {
    FILE_SERVER_HOST_URL
  } from "@/settings"

  export default {
    props: [
      'imgPath'
    ],
    data () {
      return {
        imgSrc: `${FILE_SERVER_HOST_URL}` + this.imgPath
      }
    },
    mounted () {
      var img, that
      img = new Image()
      that = this
      img.onload = function () {
        that.imgSrc = that.imgsrc
        that.$emit('imageLoad')
      }
      img.src = this.imgsrc
    }
  }
</script>

<style>
  .image{
    margin: 0;
    background-color: white;
    box-shadow: 0px 0px 34px -7px rgba(0,0,0,0.75);
    width: 200px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-right: auto;
  }
  .message.own .image{
    margin-right: 0;
    margin-left: auto;
  }
  .image img{
    width: 150px;
  }
  @media (max-width: 480px) {
    .image{
      width: 100px;
    }
    .image img{
      width: 100px;
    }
  }
</style>
