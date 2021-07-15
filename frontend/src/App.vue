<template>
  <div id="app">
    <Header />
    <Welcome />
    <Trending />
    <Latest />
  </div>
</template>

<script>
import Header from "@/components/base/Header";
import Welcome from "@/components/Welcome";
import Trending from "@/components/Trending";
import Latest from "@/components/Latest";

export default {
  name: 'App',
  components: {
    Latest,
    Trending,
    Welcome,
    Header,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
