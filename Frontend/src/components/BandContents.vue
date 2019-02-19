<template>
  <!--전체 화면 비율설정-->
  
  <div id="e3" style="max-width: 40%; margin: auto;" class="grey lighten-3" center>
  
    <!--검색 툴바-->
    <div>
      <div>
        <v-toolbar color="#FBC02D" dark tabs>
          <v-text-field  flat label="글 내용 검색" prepend-inner-icon="search" solo-inverted></v-text-field>
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
                  <div>새로운 소식을 남겨보세요.</div>
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
                      <v-text-field
                       label="제목을 입력하세요"
                       name="postTitle" 
                       v-model="postTitle"
                      ></v-text-field>
                      </v-flex>
                        <v-flex xs12>
                          <v-textarea full-width placeholder="새로운 소식을 남겨보세요" name="postBody" v-model="postBody">{{postBody}}</v-textarea>
                          <!-- <v-tooltip top><i class="material-icons Brown600" slot="activator" >perm_media</i><span>사진첨부</span></v-tooltip>
  
                            <v-tooltip right><i class="material-icons Brown600" slot="activator">attachment</i><span>파일첨부</span></v-tooltip>-->
                             <div v-if="!image">
    <input type="file"  @change="onFileChange">
     
  </div>
  <div v-else>
    <img class="InsertImage" :src="image" />
    <button @click="removeImage">Remove image</button>
  </div><button v-on:click="submitFile()">Submit</button>


            
                          <upload-btn icon
                          v-model="ImageUpload"> 
                            <template slot="icon">
                                <i class="material-icons Brown600" slot="activator">perm_media</i>
                            </template>
                          </upload-btn>
                          <upload-btn icon>
                          <template slot="icon">
                           <i class="material-icons Brown600" slot="activator">attachment</i>
                          </template>
                          </upload-btn>
                        </v-flex>
                      </v-layout>
                    </v-container>
                  </v-card-text>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="orange" flat @click="dialog = false">Close</v-btn>
                    <v-btn color="orange" flat v-on:click="postPost" @click="dialog = false">Save</v-btn>

                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-layout>
          </div>
        </v-card-title>
      </v-card>
    </v-flex>

    <v-card>
      <v-container class="container" fluid grid-list-lg>
        <v-layout row wrap>
          <v-flex xs12 class="post" v-for="post in posts" v-bind:key="post.id" v-model="postnum">
            <v-card color="white" class="black--text">
              <v-card-title primary-title>
                <div>
                  <div class="headline">{{post.title}}</div>
                  <span>작성시간 : {{post.created_at | formatDate}}</span>
                  <p></p>
                 
                  <div v-if="post.image !== null" >
                    <img 
                    v-bind:src="post.image" 
                    height="150px"
                    contain>
                  </div >                
                  <p>{{post.content}}</p>

                </div>
              </v-card-title>

              <v-expansion-panel>
                <v-expansion-panel-content>
                  <div slot="header">댓글보기</div>

                  <v-card v-for="comments in post.comments" v-bind:key="comments.id">
                    <v-card-text>
                      <h3>{{comments.author}} : {{comments.message}}</h3>
                      <span>{{comments.created_at | formatDate}}</span>

                      <hr>
                    </v-card-text>
                  </v-card>

                  <!--text입력란-->
                  <v-flex xs12>
                    <v-text-field
                      placeholder="댓글을 남겨주세요."
                      color="orange"
                      name="CommentCreateMsg"
                      v-model="CommentCreateMsg"
                    ></v-text-field>
                  </v-flex>
                  <v-btn
                    flat
                    color="orange"
                    style="float:right"
                    v-on:click="createComment(post.id)"
                  >댓글입력</v-btn>

                </v-expansion-panel-content>
              </v-expansion-panel>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
   
  </div>
</template>






<script>
  import axios from "axios";
  import UploadButton from "vuetify-upload-button";
  import { PLATFORM_SERVER_HOST_URL } from "../settings"
 
  export default {
    components: {
      "upload-btn": UploadButton
    },
  
    data: () => ({
  
      dialog: false,
      posts: [],
      //comments:[],
      postBody: "",
      postTitle: "",
      errors: [],
      image: "",
      index: "",
      CommentCreateMsg: "",
      postnum: "",
      ImageUpload:"",
      file:'',

     }),

    props: [
      'bandId'
    ],
  
    created() {
      console.log('yyyy: ', this.bandId)
  
      axios.get(`${PLATFORM_SERVER_HOST_URL}/post/`,{
        params: {
          bandId: this.bandId
        }
      }).then(result => {
        console.log(result);
        this.posts = result.data;
        console.log(this.posts);
      });
  
    },


  
    methods: {
  
      postPost() {
  
        axios
  
          .post(`${PLATFORM_SERVER_HOST_URL}/post/create/`, {
            title: this.postTitle,
            content: this.postBody,
            band_id: this.bandId,
            author: this.$store.getters.user.userId,
            //image : this.ImageUpload,
          })
  
          .then(response => {})
          // .then(console.log(this.postBody))
          // .then(console.log(response.postBody))
          .catch(e => {
            this.errors.push(e);
  
          });
  
      },
  
      createComment(post_id) {
        axios
          .post(`${PLATFORM_SERVER_HOST_URL}/post/comments/create`, {
            message: this.CommentCreateMsg,
            author: this.$store.getters.user.userId,
            post: post_id
          })
          .then(response => {})
          .catch(e => {
            this.errors.push(e);
          });  
      },

        onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length)
        return;
      this.createImage(files[0]);
    },
    createImage(file) {
      var image = new Image();
      var reader = new FileReader();
      var vm = this;

      reader.onload = (e) => {
        vm.image = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    removeImage: function (e) {
      this.image = '';
    },

    submitFile(){
                //Initialize the form data
            let formData = new FormData();
               // Add the form data we need to submit
            formData.append('file', this.file);
 console.log('xxxxx');
            axios.post( '/post/comments/create',
                formData,
                {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
              }
            ).then(function(){
          console.log('SUCCESS!!');
        })
        .catch(function(){
          console.log('FAILURE!!');
        });
      },

      //  handleFileUpload(){
      //   this.file = this.$refs.file.files[0];
      // },
  
    }

    
  
    // createPost(post){
    //     const url = `${API_URL}/post/`;
    //     return axios.post(url,post);
    // }
  
    // mounted(){
    //   axios.get(`${PLATFORM_SERVER_HOST_URL}/api/`+result.id+'/comments')
    //   .then((result) => {
    //         console.log(result)
    //         this.comments = result.data
    // })
    // }


    //   methods: {
    //   searchTerm: function () {
    //     // using JSONPlaceholder
    //     const baseURI = `${PLATFORM_SERVER_HOST_URL}`;
    //     this.$http.get(`${baseURI}/api`)
    //     .then((result) => {
    //       console.log(result)
    //       this.posts = result.data
    //     })
  
    //   }
  
    // }
  
  };

</script>








<style>
  .container {
    background-color: #FFF59D;
  }
  .material-icons.Brown600 {
    color: #6d4c41;
  }
  .InsertImage {
  width: 30%;
  margin: auto;
  display: block;
  margin-bottom: 10px;
}
</style>

