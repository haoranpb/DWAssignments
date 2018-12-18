<template>
  <div>
    <div class="time">
      <h2>每个请求占一秒的百分比</h2>
      <div class="label">
        <el-tag type="success">标签二</el-tag>
        <el-tag type="info">标签三</el-tag>
        <el-tag type="warning">标签四</el-tag>
        <el-tag type="danger">标签五</el-tag>
      </div>
      <el-progress style="margin-top:15px;" :text-inside="true" :stroke-width="20" :percentage="10"></el-progress>
      <el-progress :text-inside="true" :stroke-width="20" :percentage="80" color="rgba(142, 113, 199, 0.7)"></el-progress>
      <el-progress :text-inside="true" :stroke-width="20" :percentage="100" status="success"></el-progress>
      <el-progress :text-inside="true" :stroke-width="20" :percentage="50" status="exception"></el-progress>
    </div>
  </div>
</template>

<script>
export default {
  
}
</script>

<style scoped>
.time{
  width: 40%;
  float: right;
}
.label{
  height: 40px;
}
.el-tag{
  margin-right: 10px;
  margin-left: 10px;
  margin-bottom: 0;
}
.el-progress{
  margin-top: 30px;
  margin-bottom: 20px;
}
h2{
  font-size: 1.2em;
}
</style>
