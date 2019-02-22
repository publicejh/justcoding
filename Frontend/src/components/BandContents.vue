<template>
  <!--전체 화면 비율설정-->
    
  <div style="max-width: 40%; margin:auto; " class="grey lighten-3" center>
                <v-dialog v-model="updatedialog" persistent max-width="800px">
                
            
    
                  <v-card>
                    <v-card-title>
                      <span class="headline">수정하기</span>
                    </v-card-title>
                    <ckeditor :editor="editor" v-model="postBodyEdit" ></ckeditor>
                    <v-card-text>
                      <v-container grid-list-md>
                        <v-layout wrap>
                        <v-flex xs12>
                        <v-text-field
                        
                        name="postTitle" 
                        color="orange"
                        v-model="postTitle"
                        
                        ></v-text-field>
                        </v-flex>
                        
                        </v-layout>
                      </v-container>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <!-- <v-btn color="orange" flat @click="updatedialog[index] = false">Close</v-btn> -->
                      <v-btn color="orange" flat @click="updatedialog = false">Close</v-btn>
                      <v-btn color="orange" flat v-on:click="updatePost(postIdEdit)" @click="updatedialog = false">Save</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
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
                  {{updatedialog}}
                  <div>새로운 소식을 남겨보세요.</div>
                </div>
                <!--글쓰기 팝업생성-->
                
                
  
                <v-card>
                  <v-card-title>
                    <span class="headline">글쓰기</span>
                  </v-card-title>
                  <ckeditor :editor="editor" v-model="postBody" ></ckeditor>
                  
                  <v-card-text>
                    <v-container grid-list-md>
                      <v-layout wrap>
                      <v-flex xs12>
                      <v-text-field
                       label="제목을 입력하세요"
                       name="postTitle" 
                       color="orange"
                       v-model="postTitle"
                      ></v-text-field>
                      </v-flex>
                     
                        <v-flex xs12>
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
                  <p>작성자 : {{post.author}}</p>
                  <v-divider></v-divider>
                  <p></p>
                 
                  <div v-if="post.image !== null" >
                    <img 
                    v-bind:src="post.image" 
                    height="150px"
                    contain>
                  </div >                
                  <p v-html="post.content"></p>
                 
                </div>
              </v-card-title>
                

              <div style="float:right">  
                <v-btn
                      flat
                      color="orange"
                      style="float:right"
                      slot="activator"
                      @click="updatedialogFunc(post.id, post.content)"
                    >수정
                  </v-btn>
      <!--수정하기 팝업생성-->
                  

                  
                  <v-btn
                    flat
                    color="orange"
                    style="float:right"
                    v-on:click="deletePost(post.id)"
                  >삭제</v-btn></div>

              <v-expansion-panel>
                <v-expansion-panel-content>
                  <div slot="header">댓글보기</div>

                  <v-card v-for="comments in post.comments" v-bind:key="comments.id">
                    <v-card-text>
                      <h3>{{comments.author}} : {{comments.message}}</h3>
                      <span>[댓글작성] {{comments.created_at | formatDate}}</span>

                      <hr>
                    </v-card-text>
                  </v-card>

                  <!--text입력란-->
                  <v-flex xs12>
                    <v-text-field
                      placeholder="댓글을 남겨주세요."
                      color="orange"
                      v-model="CommentCreateMsg[index]"
                    ></v-text-field>
                  </v-flex>
                  <v-btn
                    flat
                    color="orange"
                    style="float:right"
                    v-on:click="createComment(post.id, index)"
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
  import ClassicEditor from '@ckeditor/ckeditor5-build-classic';

  


 
  export default {
    components: {
      "upload-btn": UploadButton,
       
    },
  
    data: () => ({
  
      dialog: false,
      // updatedialog: false,
      updatedialog: false,
      posts: [],
      //comments:[],
      editPost:"",
      postBody: "",
      postBodyEdit: "",
      postIdEdit: null,
      postTitle: "",
      errors: [],
      image: "",
      index: "",
      // CommentCreateMsg: "",
      CommentCreateMsg: [],
      postnum: "",
      ImageUpload:"",
      file:'',
      editorText: '',
      editor: ClassicEditor,
      editorData: '',

      temptemp: "<b>test</b>",
      customEditor:  ClassicEditor.defaultCoonfig = {
        
    toolbar: [ 'heading', '|', 'bold', 'italic', 'custombutton' ]
      }
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

    mounted() {
      
    },


  
    methods: {
      updatedialogFunc(postId, content) {
        this.updatedialog = true
        this.postBodyEdit = content
        this.postIdEdit = postId
      },

      getPost(post_id){
        var content = this.postBody
        return content

      },
  
      postPost() {
        var content = this.postBody
  
        axios
  
          .post(`${PLATFORM_SERVER_HOST_URL}/post/create/`, {
            title: this.postTitle,
            content: this.postBody,
            band_id: this.bandId,
            author: this.$store.getters.user.userId,
            //image : this.ImageUpload,
          })
  
          .then(response => {
            var content = this.postBody
            console.log(content)
            return content
          })
          // .then(console.log(this.postBody))
          // .then(console.log(response.postBody))
          .catch(e => {
            this.errors.push(e);
  
          });
  
      },
      updatePost(post_id) {
  
        axios
          .put(`${PLATFORM_SERVER_HOST_URL}/post/update/${post_id}/`, {
            title: 'remove',
            content: this.postBodyEdit,
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

           deletePost(post_id) {

        axios.delete(`${PLATFORM_SERVER_HOST_URL}/post/delete/${post_id}`,  {          
          })
  
          .then(response => {
            this.result.splice(id, 1)
        console.log(this.result);
        console.log(xxxxx);

          })
          // .then(console.log(this.postBody))
          // .then(console.log(response.postBody))
          .catch(e => {
            this.errors.push(e);
  
          });
  
      },
  
      createComment(post_id, index) {
        axios
          .post(`${PLATFORM_SERVER_HOST_URL}/post/comments/create`, {
            message: this.CommentCreateMsg[index],
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

