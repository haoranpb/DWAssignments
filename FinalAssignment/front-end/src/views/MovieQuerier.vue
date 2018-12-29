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
        <Time :usedtime="dbtime"/>
      </div>
    </div>
    <div id="result">
      <el-table :data="movieData" height="550" stripe style="width: 100%">
        <el-table-column prop="title" label="电影名称" width="150"></el-table-column>
        <el-table-column prop="id" label="电影ID" width="100"></el-table-column>
        <el-table-column prop="actor" label="演员" width="150"></el-table-column>
        <el-table-column prop="director" label="导演" width="150"></el-table-column>
        <el-table-column prop="genre" label="分类" width="120"></el-table-column>
        <el-table-column prop="reviewnum" sortable label="评论数" width="100"></el-table-column>
        <el-table-column prop="time" sortable label="上映时间"></el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import Time from '@/components/Time.vue'
import axios from 'axios'

export default {
  components: {
    Time
  },
  data() {
    return {
      dbtime:{
        redis: 40,
        neo4j: 30,
        influxdb: 20,
        zonghedb: 10,
      },
      form: {
        name: '',
        date: '',
        director: '',
        actor: '',
        genre: ''
      },
      movieData: []
    }
  },
  methods: {
    submit(){
      let obj = this;
      this.$message('正在查询，请稍后！');
      let start = '';
      let end = '';
      if(this.form.date){
        start = this.form.date[0];
        end = this.form.date[1];
      }
      axios.get('http://127.0.0.1:5000/moviesearch', {
        params: { 
          title: obj.form.name,
          genre: obj.form.genre,
          starttime: start,
          endtime: end,
          actor: obj.form.actor,
          director: obj.form.director
        }
      })
      .then(function (response) {
        obj.$message({
          message: '恭喜你，成功了！',
          type: 'success'
        });
        obj.movieData = [];
        // console.log(response.data['redis']);
        // console.log(response.data['influxdb']);
        // console.log(response.data['neo4j']);
        // console.log(response.data['zonghedb']);
        console.log(response.data);

        for(let key of Object.keys(response.data)){
          if(key!='length'&&key!='redis'&&key!='neo4j'&&key!='zonghedb'&&key!='influxdb'){
            obj.movieData.push(response.data[key]);
          }
        }
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    }
  }
}
</script>

<style scoped>
#result{
  display: block;
  margin-top: 20px;
}
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
