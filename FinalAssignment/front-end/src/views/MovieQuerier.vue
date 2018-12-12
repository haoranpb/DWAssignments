<template>
  <div id="movie-querier">
    <div class="rule">
      <h1>Please Set Searching Rules</h1>
      <hr />
      <el-form ref="form" :model="form" label-width="100px">
        <el-form-item label="电影名称">
          <el-input
            v-model="form.name"
            placeholder="电影名称">
          </el-input>
        </el-form-item>
        <el-form-item label="上映时间">
          <el-date-picker
            v-model="form.date"
            type="daterange"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="导演名字">
          <el-input
            v-model="form.director"
            placeholder="导演名字">
          </el-input>
        </el-form-item>
        <el-form-item label="演员名字">
          <el-input
            v-model="form.actor"
            placeholder="演员名字">
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
import Result from '@/components/Result.vue'

export default {
  components: {
    Result
  },
  data() {
    return {
      form: {
        name: '',
        date: '',
        director: '',
        actor: '',
      }
    }
  },
  methods: {
    submit(){
      console.log('hahah');
    }
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
.rule{
  height: 100%;
}
.el-form{
  float: left;
}

</style>
