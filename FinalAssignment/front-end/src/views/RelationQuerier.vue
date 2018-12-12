<template>
  <div id="relation-querier">
    <div class="rule">
      <h1>Please Set Search Rule</h1>
      <hr />
      <el-form ref="form" :model="form" label-width="120px">
        <el-form-item label="请输入导演名称">
          <el-input
            v-model="form.director"
            placeholder="导演名称">
          </el-input>
        </el-form-item>
        <el-form-item label="请输入演员名称">
          <el-input
            v-model="form.actor"
            placeholder="演员名称">
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submit">Search</el-button>
        </el-form-item>
      </el-form>
    </div>
    <result />
  </div>
</template>

<script>
import Result from '@/components/Result'

export default {
  data(){
    return {
      form: {
        actor: '',
        director: ''
      }
    }
  },
  components: {
    Result
  }
}
</script>

<style scoped>
h1{
  margin: 0;
  padding: 0;
  font-size: 1.2em;
  font-weight: 600;
  position: relative;
  right: 35%;
  display: block;
}
hr{
  display: block;
  margin-top: 2%;
  margin-bottom: 2%;
}
.el-form{
  float: left;
}
</style>
