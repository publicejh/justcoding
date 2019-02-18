<template>
    <div id="app">
        <img src="./assets/logo_SIG.png">
        <div id="contents">
            <router-view/>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'app'
    };
</script>

<style>
    #app {
        width: 600px;
        margin: 60px auto 0;
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50; /* 글자 색 */
    }

    #contents {
        text-align: left;
    }

    body {
      background-color: #F6F6F8;
    }


</style>
