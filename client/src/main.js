import Vue from "vue";
import App from "./App.vue";
import Vuex from "vuex"

Vue.use(Vuex)

Vue.config.productionTip = false

const store = new Vuex.Store({
  state: {
    followers: true,
    storyEngagement: false,
    stickerResponses: false,
  }
});

new Vue({
  store,
  watch: {
    followers() {
      return this.$store.state.followers
    }
  },
  render: h => h(App)
}).$mount("#app");
