<template>
  <div v-if="this.$store.state.followers === true">
    <p class='selectData'> Please select the file containing your followers' data </p>
    <input class='file' type="file"/>
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

export default {
  name: "Main",
  props: {
    msg: String
  },
  methods: {
    
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