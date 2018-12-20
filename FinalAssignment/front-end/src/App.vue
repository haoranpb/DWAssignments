<template>
  <div id="app">
    <el-container>
      <el-header>
        <movie-header />
      </el-header>
      <el-main style="padding-left: 15%; padding-right: 15%; padding-top: 3%">
        <router-view/>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import MovieHeader from './components/MovieHeader'

export default {
  components: {
    MovieHeader
  }
}
</script>


<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
html, body{
  margin: 0;
  padding: 0;
}
.el-header{
  background-color: black;
  text-align: center;
  line-height: 60px;
}
.el-main {
  background-color: rgb(255, 255, 255);
  color: #333;
  text-align: center;
}
</style>
