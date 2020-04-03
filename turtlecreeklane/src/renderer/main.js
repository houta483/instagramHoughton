import Vue from 'vue'
import App from './App'
import Vuex from "vuex"

Vue.use(Vuex)

Vue.config.productionTip = false

const store = new Vuex.Store({
  state: {
    followers: false,
    stickerResponses: true,
    storyEngagement: false,
  }
});

/* eslint-disable no-new */
new Vue({
  store,
  components: { App },
  template: '<App/>'
}).$mount('#app')
