<template>
  <div>
    <div class="time">
      <h2>每个请求占一秒的百分比</h2>
      <el-progress style="margin-top:15px;" :text-inside="true" :stroke-width="20" :percentage="usedtime.redis"></el-progress>
      <el-progress :text-inside="true" :stroke-width="20" :percentage="usedtime.neo4j" color="rgba(142, 113, 199, 0.7)"></el-progress>
      <el-progress :text-inside="true" :stroke-width="20" :percentage="usedtime.influxdb" status="success"></el-progress>
      <el-progress :text-inside="true" :stroke-width="20" :percentage="usedtime.zonghedb" status="exception"></el-progress>
    </div>
    <div class="label">
      <p>Redis</p>
      <p>Neo4j</p>
      <p>Influxdb</p>
      <p>综合DB</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ['usedtime']
}
</script>

<style scoped>
.time{
  width: 40%;
  float: right;
}
.label{
  float: right;
  width: 8%;
  margin-top: 5.5%;
}
.label p{
  height: 35px;
}
.el-progress{
  margin-top: 30px;
  margin-bottom: 20px;
}
h2{
  font-size: 1.2em;
  margin-bottom: 8%;
}
</style>
