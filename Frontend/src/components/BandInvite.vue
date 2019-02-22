<template>

 <div
    id="e3"
    style="max-width: 40%; margin: auto;"
    class="grey lighten-3"
    center
  >
  <div>
     <v-card>
      <v-container
        class ="container"
        fluid
        grid-list-lg
      ><h2>멤버초대</h2> 
      <!-- <v-spacer></v-spacer>이거 쓰면 공간 벌릴 수 있음 -->
    <div class="text-xs-right">

      <v-dialog v-model="dialog" scrollable max-width="50%">
        <!--<v-btn slot="activator" color="primary" dark>+</v-btn>-->
        <v-btn slot="activator" @click="createInvitationToken"  color="#FFCC80">초대링크생성</v-btn>
        <v-card>
          <v-card-title>멤버초대하기</v-card-title>
          <v-divider></v-divider>
          <v-card-text style="height: 300px;">

            <v-form>
              <v-container>
                <v-layout row wrap>
          
                  <v-flex>
                    <v-text-field
                      label="아래 링크를 복사하여 멤버를 초대하세요."
                      outline
                      readonly
                      id = "invitationUrl"
                      :value="invitationUrl"
                    >
                    {{token}}
                    </v-text-field>
                  </v-flex>
          
                </v-layout>
              </v-container>
            </v-form>

            <v-btn outline color="black" @click.stop.prevent="copyTestingCode">링크복사하기</v-btn>
          
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn color="orange" flat @click="dialog = false">Close</v-btn>
            <v-btn color="orange" flat @click="">Create</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      
    </div>

      </v-container>
     </v-card>
 



    


</div>


</div>
</template>


<script>
import axios from "axios";
import { PLATFORM_SERVER_HOST_URL } from "../settings"
export default {

  data() {
      
    return {
      // members :[],
      dialog: false,
      token: null,
      invitationUrl: "",
      items: [
        { active: true, title: 'Jason Oner', avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg' },
        { active: true, title: 'Ranee Carlson', avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg' },
        { title: 'Cindy Baker', avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg' },
        { title: 'Ali Connors', avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg' }
      ],
      items2: [
        { title: 'Travis Howard', avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg' }
      ]
    }
  },
    
  created() {

    axios.get(`${PLATFORM_SERVER_HOST_URL}/band/1/member`)
    .then(result => {
      console.log(result);
      this.members = result.data;
      console.log("XXXX")
      console.log(this.members);
    });


  },
  computed: {
    invitationToken() {
      return this.token
    }
  },
  watch: {
    invitationToken (val, oldVal) {
      console.log('watched invitationToken: ', val)
      this.invitationUrl = `http://localhost:8080/#/n/${val}`
    }
  },

  methods: {
      copyTestingCode () {
        let testingCodeToCopy = document.querySelector('#invitationUrl')
        testingCodeToCopy.setAttribute('type', 'text') 
        testingCodeToCopy.select()

        try {
          var successful = document.execCommand('copy');
          var msg = successful ? 'successful' : 'unsuccessful';
          alert('링크가 복사되었습니다.');
        } catch (err) {
          alert('링크복사 실패');
        }
        testingCodeToCopy.setAttribute('type', 'text')
        window.getSelection().removeAllRanges()
      },

      createInvitationToken() {
        this.token = Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15)
        this.$store.dispatch('generateInvitationToken', this.token)
      },

      createInvitationLink () {
        let testingCodeToCopy = document.querySelector('#URL')
        testingCodeToCopy.setAttribute('type', 'text') 
        testingCodeToCopy.select()

        try {
          var successful = document.execCommand('copy');
          var msg = successful ? 'successful' : 'unsuccessful';
          alert('링크가 복사되었습니다.');
        } catch (err) {
          alert('링크복사 실패');
        }
        testingCodeToCopy.setAttribute('type', 'text')
        window.getSelection().removeAllRanges()
      },

  },
    
}
</script>



<style>
.container{
    background-color: #FFF59D
}
.membernum{
    text-decoration-color: #FF9436
}
.search{
  color: #FF9436
}
</style>

  