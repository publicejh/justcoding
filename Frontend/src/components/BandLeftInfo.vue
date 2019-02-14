<template>
    <div id="app">

    <v-layout row style="width: 300px; margin: 20px 30px auto 100px">
      <v-flex >
        <v-card>
          <v-img
            src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
            height="200px"
          >
          </v-img>
  
          <v-card-title primary-title>
            <div>
              <div class="headline">밴드이름</div>
              <span class="grey--text">멤버수 : 3</span>
            </div>
          </v-card-title>
  
          <v-card-actions>
            <v-btn  color="#FFCC80" onclick="location.href=`http://localhost:8080/invite`">멤버초대하기</v-btn>
            <v-spacer></v-spacer>

          </v-card-actions>
  
          <v-slide-y-transition>

          </v-slide-y-transition>
        </v-card>
      </v-flex>
    </v-layout>

</div>
</template>
