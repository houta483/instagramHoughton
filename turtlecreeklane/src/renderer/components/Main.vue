<template>
  <div class='parent' v-if="this.$store.state.followers === true">
    <p class='selectData'> Please select the file containing your followers' data </p>
    <input class='file' id="file" ref="file" type="file" v-on:change="handleFile('followers')"/>
    <button class='runPythonButton' @click="myMethod"> Analyze Follower Data </button>
    <p v-if="this.$store.state.showFilesProcessed == true">Files Processed: {{this.$store.state.filesProcessed}}</p>
  </div>

  <div class='parent' v-else-if="this.$store.state.storyEngagement === true">
    <p class='selectData'> Please select the file containing your story engagement data </p>
    <input class='file' type="file"/>
    <button class='runPythonButton'> Analyze Story Engagement </button>
  </div>

  <div class='parent' v-else-if="this.$store.state.stickerResponses === true">
    <p class='selectData'> Please select the screenshots containing your sticker response data </p>
    <input class='file' id="file" ref="file" type="file" v-on:change="handleFile('stickers')" multiple />
    <button class='runPythonButton'> Analyze Sticker Responses </button>
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
    handleFile(type){
      if (type === 'followers') {
        this.file = this.$refs.file.files[0];
      }
      else if (type === 'stickers') {
        this.file = this.$refs.file.files;
      }
    },
    myMethod () {
      this.$store.state.showFilesProcessed = true;
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
      )
      .then((data) => console.log(data))
      .catch((e) => console.log(e))
    }
  },
};
</script>

<style scoped>
.parent {
  display: inline-block;
}
.file {
  width: 200px;
  height: 30px;
  justify-self: center;
}
.selectData {
  height: 20px;
}
.runPythonButton {
  width: 190px;
  height: 20px;
}
</style>