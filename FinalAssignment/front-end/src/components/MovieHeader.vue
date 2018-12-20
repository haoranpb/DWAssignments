<template>
  <div id="nav">
    <router-link to="/">MovieQuerier</router-link> | 
    <router-link to="/relation">RelationQuerier</router-link> | 
    <router-link to="/graph">Graph</router-link>
  </div>
</template>

<script>
export default {
  
}
</script>

<style scoped>
#nav{
  float: left;
  font-size: 1.2em;
  font-weight: 600;
  padding-left: 15%;
}
a{
  text-decoration: none;
  color: white;
}
</style>
