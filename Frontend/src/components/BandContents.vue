<template>
<!--전체 화면 비율설정-->
  <div
    id="e3"
    style="max-width: 60%; margin: auto;"
    class="grey lighten-3"
    center
  >
  <!-- <div id="app">
      <button v-on:click="getData">axios 호출</button>
  </div> -->


<!--검색 툴바-->
  <div>
    <div>
      <v-toolbar
        color="#DBBC68"
        dark
        tabs
      >
        <v-text-field
          class="mx-3"
          flat
          label="글 내용 검색"
          prepend-inner-icon="search"
          solo-inverted
        ></v-text-field>
  
      </v-toolbar>
    </div>
</div>


          <v-flex xs12>
            <v-card color="white" class="black--text">
              <v-card-title primary-title>
                <div>
                  
 <v-layout>
    <v-dialog v-model="dialog" persistent max-width="800px">
      <div slot="activator" class="headline">
          <div> 새로운 소식을 남겨보세요.</div>
         
          </div>

     <!--글쓰기 팝업생성-->     
      <v-card>
        <v-card-title>
          <span class="headline">글쓰기</span>
        </v-card-title>


        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>
              <v-flex xs12>
                <!-- <v-text-field v-model="message" label="새로운 소식을 남겨보세요." required></v-text-field> -->
                <v-textarea full-width placeholder="새로운 소식을 남겨보세요" name="postBody" v-model="postBody">{{postBody}}</v-textarea>
               <!-- <v-tooltip top><i class="material-icons Brown600" slot="activator" >perm_media</i><span>사진첨부</span></v-tooltip>
                <v-tooltip right><i class="material-icons Brown600" slot="activator">attachment</i><span>파일첨부</span></v-tooltip> -->
                <upload-btn icon><template slot="icon"> <i class="material-icons Brown600" slot="activator" >perm_media</i></template></upload-btn>
                <upload-btn icon><template slot="icon"> <i class="material-icons Brown600" slot="activator" >attachment</i></template></upload-btn>
               
                


              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" flat @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" flat v-on:click="postPost">Save</v-btn>
                    <!-- <v-btn color="blue darken-1" flat @click="postPost">Save</v-btn> -->
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
                </div>
              </v-card-title>
            </v-card>
          </v-flex>



    <!--<button v-on:click="searchTerm">글 불러오기</button>-->








    <v-card>
      <v-container
        class ="container"
        fluid
        grid-list-lg
      >
      
        <v-layout row wrap>
          <v-flex xs12 class="post" v-for="post in posts" v-bind:key="post.id">
            <v-card color="white" class="black--text">
              <v-card-title primary-title>
                <div>
                  <div class="headline">{{post.title}}</div>
                  <span>작성시간 : {{post.created_at | formatDate}}</span>
                  <p></p>
                  <span>{{post.content}}</span>
                  <!-- <v-img)
                    {{post.image}}
                    height="125px"
                    contain
                  ></v-img> -->
                </div>
              </v-card-title>
              <v-card-actions>
                <v-btn flat dark>Listen now</v-btn>
              </v-card-actions>
              <v-expansion-panel>
    <v-expansion-panel-content>
      <div slot="header">댓글보기</div>
      <v-card v-for="post in posts" v-bind:key="post.id">
        <v-card-text>{{post.comments}}</v-card-text>
      </v-card>
    </v-expansion-panel-content>
  </v-expansion-panel>
            </v-card>
          </v-flex>
          <v-flex xs12>
            <v-card color="white" class="black--text">
              <v-layout row>
                <v-flex xs7>
                  <v-card-title primary-title>
                    <div>
                      <div class="headline">Halycon Days</div>
                      <div>Ellie Goulding</div>
                      <div>(2013)</div>
                    </div>
                  </v-card-title>
                </v-flex>
                <v-flex xs5>
                  <v-img
                    src="https://cdn.vuetifyjs.com/images/cards/halcyon.png"
                    height="125px"
                    contain
                  ></v-img>
                </v-flex>
              </v-layout>
              <v-divider light></v-divider>
              <v-card-actions class="pa-3">
                Rate this album
                <v-spacer></v-spacer>
                <v-icon>star_border</v-icon>
                <v-icon>star_border</v-icon>
                <v-icon>star_border</v-icon>
                <v-icon>star_border</v-icon>
                <v-icon>star_border</v-icon>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </div>
</template>






<script>

import axios from 'axios'
import UploadButton from 'vuetify-upload-button';
const API_URL = 'http://localhost:8000';
  export default {
    components: {
      'upload-btn': UploadButton
    },
    data: () => ({
      dialog: false,
      posts :[],
      comments:[],
      postBody: '',
      errors: [],
      image: ''
    }),
created(){
  axios.get('http://127.0.0.1:8000/post/')
  .then((result) => {
        console.log(result)
        this.posts = result.data
        console.log(this.posts)
        //this.comments = result.data.id.comments
})
},
// methods: {
//     save() {
//       this.$http
//         .post('http://127.0.0.1:8000/post/')
//         .then(response => {
//           console.log(response);
//         }, error => {
//           console.log(error);
//         });
//     }
//   }
methods:{
postPost() {
    axios.post(`http://127.0.0.1:8000/post/create/`, {
      title: 'temptitle',
      content: this.postBody,
      band_id: 1,
      author: 1
    })
    .then(response => {})
    // .then(console.log(this.postBody))
    // .then(console.log(response.postBody))
    
    .catch(e => {
      this.errors.push(e)
    })
},  

}
// createPost(post){

//     const url = `${API_URL}/post/`;
//     return axios.post(url,post);
// }
// mounted(){
//   axios.get('http://127.0.0.1:8000/api/'+result.id+'/comments')
//   .then((result) => {
//         console.log(result)
//         this.comments = result.data
// })
// }

  //   methods: {
  //   searchTerm: function () {
  //     // using JSONPlaceholder
  //     const baseURI = 'http://127.0.0.1:8000';
  //     this.$http.get(`${baseURI}/api`)
  //     .then((result) => {
  //       console.log(result)
  //       this.posts = result.data
  //     })
  //   }
  // }
  //   mounted(){
  //     //var self = this;
  //    // getData: function(){
  //     axios.get('http://127.0.0.1:8000/api/')
  //     .then(function(response){
  //       self.posts = response.data;
  //       console.log(response);
  //     })
  //   //}
  // }


  }

</script>









<style>
.container{
    background-color: #D6C8A1
}
.material-icons.Brown600 { color: #6D4C41; }


</style>


