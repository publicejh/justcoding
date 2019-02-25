<template>
  <!--전체 화면 비율설정-->
  
  <div style="max-width: 40%; margin:auto;" class="grey lighten-3" center>
    <!--검색 툴바-->
    <v-toolbar color="white" flat>
      <v-text-field label="글 내용 검색" prepend-inner-icon="search" color="orange"></v-text-field>
    </v-toolbar>
    <v-flex xs12 style="margin: 12px auto 12px auto;">
      <v-card color="white" class="black--text" flat>
        <v-card-title primary-title>
          <div>
            <v-layout>
              <v-dialog v-model="dialog" persistent max-width="600px">
                <div slot="activator" class="headline">
                  <h5 style="color: grey;">새로운 소식을 남겨보세요.</h5>
                </div>
                <!--글쓰기 팝업생성-->
                <v-card max-height="400px">
                  <v-card-title>
                    <span class="headline" style="padding-right:10px;">글쓰기</span>
                    <label style="margin:0;">
                              <form id="myForm" enctype="multipart/form-data"> 
                                <input style="display: none;" type="file" id="file" ref="myFiles" class="custom-file-input" @change="previewFiles">
                              </form>
                              <v-icon>add_a_photo</v-icon>
                            </label>
                  </v-card-title>
                  <ckeditor :editor="editor" v-model="postBody"></ckeditor>
  
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="orange" flat @click="dialog = false">Close</v-btn>
                    <v-btn color="orange" flat v-on:click="postPost" @click="dialog = false">Save</v-btn>
  
                  </v-card-actions>
                </v-card>
              </v-dialog>
  
              <v-dialog v-model="updatedialog" persistent max-width="600px">
                <v-card max-height="400px">
                  <v-card-title>
                    <span class="headline" style="padding-right:10px;">수정하기</span>
                    <label style="margin:0;">
                              <form id="myFormE" enctype="multipart/form-data"> 
                                <input style="display: none;" type="file" id="fileE" ref="myFilesE" class="custom-file-input" @change="previewFiles('edit')">
                              </form>
                              <v-icon>add_a_photo</v-icon>
                            </label>
                  </v-card-title>
                  <ckeditor :editor="editor" v-model="postBodyEdit"></ckeditor>
                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <!-- <v-btn color="orange" flat @click="updatedialog[index] = false">Close</v-btn> -->
                    <v-btn color="orange" flat @click="updatedialog = false">Close</v-btn>
                    <v-btn color="orange" flat v-on:click="updatePost(postIdEdit)" @click="updatedialog = false">Save</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-layout>
          </div>
        </v-card-title>
      </v-card>
    </v-flex>
  
    <v-flex xs12 class="post" v-for="post in posts" v-bind:key="post.id" v-model="postnum">
      <v-card color="white" class="black--text" flat>
        <v-card-title primary-title>
          <div style="margin-left: 10px;">
            <v-layout row wrap style="margin-left: 0;">
              <v-flex>
                <v-icon x-large>account_circle</v-icon>
              </v-flex>
              <v-flex style="position: absolute; margin-left: 50px;">
                <h5>{{post.author_name}}</h5>
                <span style="color:grey;">{{post.created_at | formatDate}}</span>
              </v-flex>
            </v-layout>
            <p></p>
            <p v-html="post.content"></p>
          </div>
        </v-card-title>
  
        <div style="float:right">
          <v-btn flat color="orange" style="float:right" slot="activator" @click="updatedialogFunc(post.id, post.content)">
            수정
          </v-btn>
          <!--수정하기 팝업생성-->
          <v-btn flat color="orange" style="float:right" v-on:click="deletePost(post.id)">삭제</v-btn>
        </div>
  
        <v-expansion-panel>
          <v-expansion-panel-content>
            <div slot="header">댓글 {{post.comments.length}}</div>
  
            <v-card v-for="comments in post.comments" v-bind:key="comments.id">
              <v-card-text class="grey lighten-4" style="padding-bottom:0; height:100px;">
                <v-layout row wrap style="margin-left: 0;">
                  <v-flex>
                    <v-icon medium>account_circle</v-icon>
                  </v-flex>
                  <v-flex style="position: absolute; margin-left: 48px;">
                    <h5>{{comments.author_name}}</h5>
                    <p style="margin-bottom: 5px;">{{comments.message}}</p>
                    <span style="color:grey;">{{comments.created_at | formatDate}}</span>
                  </v-flex>
                </v-layout>
              </v-card-text>
              <v-divider style="margin:0;"></v-divider>
            </v-card>
            <!--text입력란-->
            <div style="padding-left:25px">
              <v-layout row wrap>
                <v-flex xs9>
                  <v-text-field style="margin: auto 12px auto 12px;" placeholder="댓글을 남겨주세요." color="orange" v-model="CommentCreateMsg[index]"></v-text-field>
                </v-flex>
                <v-flex xs3 style="margin-top:10px">
                  <v-btn flat color="orange" style="float:right;margin: auto 12px auto 12px;" v-on:click="createComment(post.id, index)">댓글입력</v-btn>
                </v-flex>
              </v-layout>
            </div>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-card>
    </v-flex>
  
  
  
  
  
  
  </div>
</template>






<script>
  import axios from "axios";
  import UploadButton from "vuetify-upload-button";
  import {
    PLATFORM_SERVER_HOST_URL,
    FILE_SERVER_HOST_URL
  } from "../settings"
  import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
  import jwt_decode from 'jwt-decode'
  
  
  
  
  
  export default {
    components: {
      "upload-btn": UploadButton,
  
    },
  
    data: () => ({
      userId: jwt_decode(localStorage.getItem("token")).user_id,
      files: [],
      imageUrl: "",
      dialog: false,
      // updatedialog: false,
      updatedialog: false,
      posts: [],
      //comments:[],
      editPost: "",
      postBody: "",
      postBodyEdit: "",
      postIdEdit: null,
      postTitle: "",
      errors: [],
      // image: "",
      index: "",
      // CommentCreateMsg: "",
      CommentCreateMsg: [],
      postnum: "",
      // ImageUpload:"",
      // file:'',
      editorText: '',
      editor: ClassicEditor,
      editorData: '',
  
      temptemp: "<b>test</b>",
      customEditor: ClassicEditor.defaultCoonfig = {
  
        toolbar: ['heading', '|', 'bold', 'italic', 'custombutton']
      }
    }),
  
    props: [
      'bandId'
    ],
  
    created() {
      axios.get(`${PLATFORM_SERVER_HOST_URL}/post/`, {
        params: {
          bandId: this.bandId
        }
      }).then(result => {
        this.posts = result.data;
      });
  
    },
  
    methods: {
      previewFiles(state) {
        var self = this;
  
        if (state === 'edit') {
          console.log('editeeeee')
          this.files = this.$refs.myFilesE.files
          var formID = "myFormE";
        } else {
  
          this.files = this.$refs.myFiles.files
          var formID = "myForm";
        }
  
        var form = document.getElementById(formID);
        var formData = new FormData(form);
        formData.append('file', this.files[0]);
        formData.append('userId', this.userId);
        formData.append('bandId', this.$store.getters.sigId);
  
        axios({
            method: 'post',
            url: `${FILE_SERVER_HOST_URL}/file_manage/upload/image/`,
            contentType: false,
            processData: false,
            data: formData,
            config: {
              headers: {
                'Content-Type': 'multipart/form-data'
              }
            }
          })
          .then(function(response) {
            //handle success
            console.log(response)
            self.imageUrl = `${FILE_SERVER_HOST_URL}` + response.data
            console.log(self.imageUrl);
  
            var imgElement = '<br/><img src="' + self.imageUrl + '" width="100%"/>';
  
            if (state === 'edit') {
              console.log('editeeeee')
              self.postBodyEdit += imgElement
            } else {
              self.postBody += imgElement
            }
          })
          .catch(function(response) {
            //handle error
            console.log(response);
          });
  
      },
  
      updatedialogFunc(postId, content) {
        this.updatedialog = true
        this.postBodyEdit = content
        this.postIdEdit = postId
      },
  
      getPost(post_id) {
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
            author: this.userId,
            //image : this.ImageUpload,
          })
  
          .then(response => {
            var content = this.postBody
            this.$router.push(`/band/${this.bandId}?new-post=${response.data.id}`)
            // return content
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
            author: this.userId,
            //image : this.ImageUpload,
          })
  
          .then(response => {
  
            this.$router.push(`/band/${this.bandId}?mod-post=${response.data.id}`)
          }).catch(e => {
            this.errors.push(e);
  
          });
  
      },
  
      deletePost(post_id) {
  
        axios.delete(`${PLATFORM_SERVER_HOST_URL}/post/delete/${post_id}`, {})
  
          .then(response => {
            // this.result.splice(id, 1)
            this.$router.push(`/band/${this.bandId}?delete-post=${post_id}`)
  
          }).catch(e => {
            this.errors.push(e);
  
          });
  
      },
  
      createComment(post_id, index) {
        axios
          .post(`${PLATFORM_SERVER_HOST_URL}/post/comments/create`, {
            message: this.CommentCreateMsg[index],
            author: this.userId,
            post: post_id
          })
          .then(response => {
            this.$router.push(`/band/${this.bandId}?new-comment=${response.data.id}`)
  
          }).catch(e => {
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
      removeImage: function(e) {
        this.image = '';
      },
  
      submitFile() {
        //Initialize the form data
        let formData = new FormData();
        // Add the form data we need to submit
        formData.append('file', this.file);
        console.log('xxxxx');
        axios.post('/post/comments/create',
            formData, {
              headers: {
                'Content-Type': 'multipart/form-data'
              }
            }
          ).then(function() {
            console.log('SUCCESS!!');
          })
          .catch(function() {
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
  .material-icons.Brown600 {
    color: #6d4c41;
  }
  
  .InsertImage {
    width: 30%;
    margin: auto;
    display: block;
    margin-bottom: 10px;
  }
  
  .ck-content {
    height: 200px;
  }
</style>

