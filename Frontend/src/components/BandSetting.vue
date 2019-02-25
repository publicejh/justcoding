<template>
    <div id="e3" style="max-width: 40%; margin: auto;" center>
    
        <v-layout justify-center>
            <v-flex xs12>
                <v-card flat>
                    <v-list subheader>
                        <v-list-tile>
                            <v-list-tile-content>
                                <v-list-tile-title>시그 설정</v-list-tile-title>
                            </v-list-tile-content>
                        </v-list-tile>
                    </v-list>
                    <v-divider></v-divider>
                    <v-list subheader>
    
                        <v-list-tile>
    
                            <v-list-tile-content>
                                <v-list-tile-title>시그 이름 및 커버 설정</v-list-tile-title>
    
                            </v-list-tile-content>
    
                            <v-list-tile-action>
                                <v-dialog v-model="dialog" scrollable max-width="50%">
                                    <v-btn depressed slot="activator">변경</v-btn>
                                    <v-card>
                                        <v-card-title>시그 이름 및 커버 설정</v-card-title>
                                        <v-divider></v-divider>
                                        <v-card-text style="height: 350px;">
                                            시그 이름
                                            <v-text-field v-model="modSigName" :value="this.$store.getters.sigName"></v-text-field>
    
                                            <v-layout row wrap>
                                                <v-flex xs6>
                                                    <v-container grid-list-sm fluid>
                                                        현재 커버
                                                        <v-img :src="sigCoverImg" aspect-ratio="1" class="grey lighten-2" height="330px" width="330px">
                                                        </v-img>
                                                    </v-container>
                                                </v-flex>
                                                <v-flex xs6>
                                                    <v-container grid-list-sm fluid>
                                                        커버 선택
                                                        <v-layout row wrap>
                                                            <v-flex v-for="n in 9" :key="n" xs4 d-flex>
                                                                <v-card flat tile class="d-flex">
                                                                    <label v-if="n === 1" style="margin:0;">
                                                                        <form id="myForm" enctype="multipart/form-data">
                                                                            <input style="display: none;" type="file" id="file" ref="myFiles" class="custom-file-input" @change="previewFiles">
                                                                        </form>
                                                                        <v-img :src="addImgSrc">
                                                                        </v-img>
                                                                    </label>
                                                                    <v-img v-else @click="selectImg(`/media/static/t${n}.jpeg`)" :src="`${file_server_host_url_str}/media/static/t${n}.jpeg`" :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`" aspect-ratio="1" class="grey lighten-2">
                                                                        <v-layout slot="placeholder" fill-height align-center justify-center ma-0>
                                                                            <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                                                                        </v-layout>
                                                                    </v-img>
                                                                </v-card>
                                                            </v-flex>
                                                        </v-layout>
                                                    </v-container>
                                                </v-flex>
                                            </v-layout>
    
                                        </v-card-text>
                                        <v-divider></v-divider>
                                        <v-card-actions>
                                            <v-btn color="orange" flat @click="dialog = false">취소</v-btn>
                                            <v-btn color="orange" flat v-on:click="updateSig" @click="dialog = false">완료</v-btn>
                                        </v-card-actions>
                                    </v-card>
                                </v-dialog>
    
                            </v-list-tile-action>
    
                        </v-list-tile>
    
    
                    </v-list>
                    <v-divider></v-divider>
                </v-card>
            </v-flex>
    
        </v-layout>
    </div>
</template>


<script>
    import axios from "axios";
    import {
        PLATFORM_SERVER_HOST_URL,
        FILE_SERVER_HOST_URL
    } from "../settings"
    
    export default {
        data() {
    
            return {
                dialog: false,
                modSigName: this.$store.getters.sigName,
                sigCoverImg: `${FILE_SERVER_HOST_URL}` + this.$store.getters.sigCoverImgPath,
                modSigCovetImg: '',
                addImgSrc: `${FILE_SERVER_HOST_URL}/media/static/upload_image.png`,
                coverImgPath: "",
                uploadImgUrl: "",
                file_server_host_url_str: `${FILE_SERVER_HOST_URL}`
                // files: []
            }
        },
    
        props: [
            'bandId',
            'sigName'
        ],
    
        created() {
    
        },
    
        methods: {
            selectImg(src) {
                this.sigCoverImg = `${FILE_SERVER_HOST_URL}` + src
                this.coverImgPath = src
            },
            previewFiles() {
                var self = this;
    
                var files = this.$refs.myFiles[0].files
                var formID = "myForm";
    
                var form = document.getElementById(formID);
                var formData = new FormData(form);
    
                formData.append('file', files[0]);
                formData.append('userId', this.$store.getters.user.userId);
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
                        self.coverImgPath = response.data
                        self.uploadImgUrl = `${FILE_SERVER_HOST_URL}` + response.data
                        self.sigCoverImg = self.uploadImgUrl
    
                    })
                    .catch(function(response) {
                        //handle error
                        console.log(response);
                    });
    
            },
            updateSig() {
                var self = this;

                axios.put(`${PLATFORM_SERVER_HOST_URL}/band/${this.bandId}/update/`, {
                    band_name: self.modSigName,
                    band_cover_img_path: self.coverImgPath
                }).then(res => {
                    // console.log(res)
                    this.$router.go(`/band/${this.bandId}/setting`)
                    
                }).catch((ex) => {
                    console.log(ex)
                    
                })
            }
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

