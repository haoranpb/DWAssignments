<template>
  <div id="result">
    <el-table
      :data="movieData"
      height="550"
      border
      style="width: 100%">
      <el-table-column
        prop="date"
        label="日期"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="姓名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="address"
        label="地址">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  data(){
    return {
      movieData: [{

      }]
    }
  }
}
</script>

<style scoped>
h1{
  margin: 0;
  padding: 0;
  margin-top: 30%;
  font-size: 1.2em;
  font-weight: 600;
  position: relative;
  right: 40%;
  display: block;
}
#result{
  display: block;
}
hr{
  display: block;
  margin-top: 2%;
  margin-bottom: 2%;
}
</style>

