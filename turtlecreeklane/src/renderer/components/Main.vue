<template>
  <div v-if="this.$store.state.followers === true">
    <p class='selectData'> Please select the file containing your followers' data </p>
    <input class='file' id="file" ref="file" type="file" v-on:change="handleFile"/>
    <button style="width: 100px; height: 100px;" @click="myMethod"> Click here </button>
  </div>

  <div v-else-if="this.$store.state.storyEngagement === true">
    <p class='selectData'> Please select the file containing your story engagement data </p>
    <input class='file' type="file"/>
  </div>

  <div v-else-if="this.$store.state.stickerResponses === true">
    <p class='selectData'> Please select the file containing your sticker response data </p>
    <input class='file' type="file" />
  </div>

</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

export default {
  name: "Main",
  props: {
    msg: String
  },
  methods: {
    handleFile(){
      this.file = this.$refs.file.files[0];
    },
    myMethod () {
      let form_data =  new FormData();
      form_data.append('file', this.file)
      axios.post(
        'http://localhost:5000/submit/',
        form_data,
        {
          headers: {
            'Content-type': 'multipart/form-data'
          }
        } 
      ).then(function(){
        console.log('SUCCESS');
      }).catch(function (e){
        console.log(e)
      })
    }
  }
};
</script>

<style scoped>
.file {
  width: 200px;
  height: 30px;
  margin-top: -280px;
  justify-self: center;
}
.selectData {
  height: 20px;
}
</style>