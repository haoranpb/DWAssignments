<template>
  <div class="graph">
    <div>
      <div class="pie">
        <canvas id="pie" width="400" height="400"></canvas>
      </div>
      <div class="bar">
        <canvas id="bar" width="600" height="400"></canvas>
      </div>
    </div>
    <div class="line">
      <canvas id="line" width="1500" height="400"></canvas>
    </div>
  </div>
</template>

<script>
import Chart from 'chart.js'
import axios from 'axios'

export default {
  data(){
    return {
      month: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      backgroundColor: ['rgba(255, 99, 132, 0.3)', 'rgba(54, 162, 235, 0.3)', 'rgba(255, 206, 86, 0.3)', 'rgba(75, 192, 192, 0.3)', 'rgba(153, 102, 255, 0.3)', 'rgba(255, 159, 64, 0.3)'],
      borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)', 'rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)', 'rgba(255, 159, 64, 1)'],
      pie: {
        data: [10, 20, 30],
        labels: ['Red', 'Yellow', 'Blue']
      },
      bar: {
        data: [12, 19, 3, 5, 15, 3, 4, 7, 4, 3, 9, 20]
      },
      line: {
        data: [0, 10, 5, 2, 20, 30, 45],
        labels: ["January", "February", "March", "April", "May", "June", "July"]
      }
    }
  },
  mounted: function(){
    let obj = this;
    let pie = document.getElementById("pie");
    let myPieChart = new Chart(pie,{
      type: 'pie',
      data: {
        datasets: [{
          data: obj.pie.data,
          backgroundColor: obj.backgroundColor,
        }],
        labels: obj.pie.labels
      },
      options: { 
        responsive: true,
        title: {
          display: true,
          text: 'Genres'
        }
      }
    });

    let bar = document.getElementById("bar");
    let myBarChart = new Chart(bar, {
        type: 'bar',
        data: {
          labels: obj.month,
          datasets: [{
            label: 'Movies per Month',
            data: obj.bar.data,
            backgroundColor: obj.backgroundColor.concat(obj.backgroundColor),
            borderColor: obj.borderColor.concat(obj.borderColor),
            borderWidth: 1
          }]
        },
        options: { 
          responsive: true,
          title: {
            display: true,
            text: 'Month'
          }
        }
    });

    let line = document.getElementById('line');
    let myLineChart = new Chart(line, {
      type: 'line',
      data: {
        labels: obj.line.labels,
        datasets: [{
          label: "Movies per Year",
          backgroundColor: 'rgb(255, 99, 132)',
          borderColor: 'rgb(255, 99, 132)',
          data: obj.line.data,
          fill: false,
        }]
      },
      options: { 
        responsive: true,
        title: {
          display: true,
          text: 'Year'
        }
      }
    });

    axios.get('http://127.0.0.1:5000/diagram')
    .then(function (response) {
      myPieChart.data.labels = response.data['diagramlabels'];
      myPieChart.data.datasets[0].data = response.data['diagramdata'];
      
      myLineChart.data.labels = response.data['chart2labels'];
      myLineChart.data.datasets[0].data = response.data['chart2data'];
      // console.log(response.data['monthlabels']);
      // console.log(response.data['monthdata']);
      myBarChart.data.labels = response.data['monthlabels'];
      myBarChart.data.datasets[0].data = response.data['monthdata'];

      myLineChart.update();
      myPieChart.update();
      myBarChart.update();
    })
    .catch(function () {
      obj.$message.error('糟糕，哪里出了点问题！');
    });
  }
}
</script>


<style scoped>
.pie, .bar{
  margin: 0;
  display: inline;
}
.bar{
  float: right;
}
.pie{
  float: left;
}
.line{
  width: 100%;
}
</style>

