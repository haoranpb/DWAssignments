<template>
  <div id="movie-querier">
    <div class="rule">
      <h1>Please Set Searching Rules</h1>
      <hr />
      <div class="content">
        <div class="myform">
          <el-form ref="form" :model="form" label-width="100px">
            <el-form-item label="电影名称">
              <el-input v-model="form.name" placeholder="电影名称">
              </el-input>
            </el-form-item>
            <el-form-item label="电影类别">
              <el-input v-model="form.genre" placeholder="电影类别">
              </el-input>
            </el-form-item>
            <el-form-item label="上映时间">
              <el-date-picker v-model="form.date" type="daterange" range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期">
              </el-date-picker>
            </el-form-item>
            <el-form-item label="导演名字">
              <el-input v-model="form.director" placeholder="导演名字">
              </el-input>
            </el-form-item>
            <el-form-item label="演员名字">
              <el-input v-model="form.actor" placeholder="演员名字">
              </el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submit">Search</el-button>
            </el-form-item>
          </el-form>
        </div>
        <Time />
      </div>
    </div>
    <result />
  </div>
</template>

<script>
import Result from '@/components/Result.vue'
import Time from '@/components/Time.vue'

export default {
  components: {
    Result,
    Time
  },
  data() {
    return {
      form: {
        name: '',
        date: '',
        director: '',
        actor: '',
        genre: ''
      }
    }
  },
  methods: {
    submit(){
      console.log(this.form);
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
.myform{
  float: left;
}
</style>
