<template>
  <div id="relation-querier">
    <div class="rule">
      <h1>Please Set Search Rule</h1>
      <hr />
      <el-form ref="form" :model="form" label-width="120px">
        <el-form-item label="请输入导演名称">
          <el-input v-model="form.director" placeholder="导演名称">
          </el-input>
        </el-form-item>
        <el-form-item label="请输入演员名称">
          <el-input v-model="form.actor" placeholder="演员名称">
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submit">Search</el-button>
        </el-form-item>
      </el-form>
      <Time :usedtime="dbtime" />
    </div>
    <div id="result-simple">
      <el-table :data="relationData" height="550" stripe style="width: 100%">
        <el-table-column prop="actor" label="演员" width="180"></el-table-column>
        <el-table-column prop="director" label="导演" width="180"></el-table-column>
        <el-table-column prop="times" sortable label="合作次数"></el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import Time from '@/components/Time'
import axios from 'axios'

export default {
  components:{
    Time
  },
  data(){
    return {
      dbtime:{
        redis: 40,
        neo4j: 30,
        influxdb: 20,
        zonghedb: 10,
      },
      form: {
        actor: '',
        director: ''
      },
      relationData: []
    }
  },
  methods: {
    submit: function(){
      let obj = this;
      this.$message('正在查询，请稍后！');
      axios.get('http://127.0.0.1:5000/collaboration', {
        params: { 
          actor: obj.form.actor,
          director: obj.form.director
        }
      })
      .then(function (response) {
        obj.$message({
          message: '恭喜你，成功了！',
          type: 'success'
        });
        obj.relationData = [];
        // obj.dbtime.redis = response.data['redis']*10;
        // obj.dbtime.influxdb = response.data['influxdb']*10;
        // obj.dbtime.neo4j = response.data['neo4j']*10;
        // obj.dbtime.zonghedb = response.data['zonghedb']*10;
        console.log(response.data);
        for(let key of Object.keys(response.data)){
          if(key!='len'&&key!='redis'&&key!='neo4j'&&key!='zonghedb'&&key!='influxdb'){
            obj.relationData.push(JSON.parse(response.data[key]));
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
  margin-top: 3%;
  float: left;
}
#result-simple{
  display: block;
  margin-top: 20px;
}
</style>
