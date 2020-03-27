<template>
  <div id="app">
    <Header class='header' />
    <Main class='main' />
    <Navbar class='navbar' />
  </div>
</template>

<script>
import Main from "./components/Main.vue";
import Header from "./components/Header.vue"
import Navbar from "./components/Navbar.vue"

export default {
  name: "App",
  components: {
    Main, Header, Navbar
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
  display: grid;
  grid-template-columns: 20% 80%;
  grid-template-rows: 20% 80%;
  height: 800px;
}

.main {
  display: grid;
  grid-column: 2 / 3;
  grid-row: 2;
}

.header {
  display: grid;
  grid-column: 1 / 3;
  grid-row: 1 / 1;
  border-bottom: .5px solid gray;
  padding-top: 15px;
}

.navbar {
  display: grid;
  grid-column: 1 / 1;
  grid-row: 2 / 3;
  border-right: .5px solid gray;
}
</style>
