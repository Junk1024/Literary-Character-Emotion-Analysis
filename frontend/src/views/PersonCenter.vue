<template>
  <el-row>
    <el-col :span="8" style="padding-right: 10px">
      <el-card class="box-card">
        <div class="user">
          <img src="../assets/images/user.png" alt="" />
          <div class="userinfo">
            <p class="name">{{ showUserName }}</p>
          </div>
        </div>
        <!-- <div class="login-info">
          <p>上次登录时间: <span>2022-10-30</span></p>
          <p>上次登录地点: <span>郑州</span></p>
        </div> -->
      </el-card>
      <el-card style="margin-top: 20px; height: 475px">
        <el-table :data="tableData" style="width: 100%">
          <!-- <el-table-column prop="name" label="课程"> </el-table-column>
          <el-table-column prop="todayBuy" label="今日购买"> </el-table-column>
          <el-table-column prop="monthBuy" label="本月购买"> </el-table-column>
          <el-table-column prop="totalBuy" label="总共购买"> </el-table-column> -->
          <el-table-column v-for="(val, key) in tableLabel" :prop="key" :label="val" />
        </el-table>
      </el-card>
    </el-col>
    <el-col :span="16" style="padding-left: 10px">
      <!-- <div class="num">
        <el-card v-for="item in countData" :key="item.name" :body-style="{ display: 'flex', padding: 0 }">
          <i class="icon" :class="`el-icon-${item.icon}`" :style="{ background: item.color }"></i>
          <div class="detail">
            <p class="price">￥{{ item.value }}</p>
            <p class="desc">{{ item.name }}</p>
          </div>
        </el-card>
      </div> -->
      <el-card style="height: 380px">
        <!-- 折线图 -->
        <div ref="echarts1" style="height: 380px"></div>
      </el-card>
      <div class="graph">
        <el-card style="height: 320px">
          <div ref="echarts2" style="height: 320px"></div>
        </el-card>
        <el-card style="height: 320px">
          <div ref="echarts3" style="height: 320px"></div>
        </el-card>
      </div>
    </el-col>
  </el-row>
</template>

<script>
import { getData } from '../api'
import Cookie from 'js-cookie'
import * as echarts from 'echarts'
export default {
  computed: {
    showUserName() {
      return Cookie.get('username')
    }
  },
  data() {
    return {
      username: 'info.username',
      tableData: [
        // {
        //   name: 'oppo',
        //   todayBuy: 100,
        //   monthBuy: 300,
        //   totalBuy: 800
        // },
        // {
        //   name: 'vivo',
        //   todayBuy: 100,
        //   monthBuy: 300,
        //   totalBuy: 800
        // },
        // {
        //   name: '苹果',
        //   todayBuy: 100,
        //   monthBuy: 300,
        //   totalBuy: 800
        // },
        // {
        //   name: '小米',
        //   todayBuy: 100,
        //   monthBuy: 300,
        //   totalBuy: 800
        // },
        // {
        //   name: '三星',
        //   todayBuy: 100,
        //   monthBuy: 300,
        //   totalBuy: 800
        // },
        // {
        //   name: '魅族',
        //   todayBuy: 100,
        //   monthBuy: 300,
        //   totalBuy: 800
        // }
      ],
      tableLabel: {
        name: '标签',
        todayBuy: '数据集',
        monthBuy: '训练集',
        totalBuy: '验证集'
      }
    }
  },
  mounted() {
    getData().then(({ data }) => {
      const { tableData } = data.data
      console.log(data.data)
      this.tableData = tableData

      // 基于准备好的dom，初始化echarts实例
      const echarts1 = echarts.init(this.$refs.echarts1)
      // 指定图表的配置项和数据
      var echarts1Option = {
        xAxis: {
          type: 'category',
          data: ['Epoch1', 'Epoch2', 'Epoch3', 'Epoch4']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            legend: 'loss',
            data: [0.63462, 0.60624, 0.68506, 0.78905],
            type: 'line',
            smooth: true
          },
          {
            legend: 'accu',
            data: [0.7805, 0.793, 0.7865, 0.782],
            type: 'line',
            smooth: true
          }
        ]
      }
      // 处理数据xAxis
      const { userData, videoData } = data.data
      // const xAxis = Object.keys(orderData.data[0])
      // const xAxisData = {
      //   data: xAxis
      // }
      // console.log(xAxisData)
      // echarts1Option.xAxis = xAxisData
      // echarts1Option.yAxis = {}
      // echarts1Option.legend = { label: ['loss', 'acc'] }
      // echarts1Option.series = []
      // xAxis.forEach(key => {
      //   echarts1Option.series.push({
      //     name: key,
      //     data: orderData.data.map(item => item[key]),
      //     type: 'line'
      //   })
      // })
      console.log(echarts1Option)
      // 使用刚指定的配置项和数据显示图表。
      echarts1.setOption(echarts1Option)

      // 柱状图
      const echarts2 = echarts.init(this.$refs.echarts2)
      const eachrts2Option = {
        legend: {
          // 图例文字颜色
          textStyle: {
            color: '#333'
          }
        },
        grid: {
          left: '20%'
        },
        // 提示框
        tooltip: {
          trigger: 'axis'
        },
        xAxis: {
          type: 'category', // 类目轴
          data: userData.map(item => item.date),
          axisLine: {
            lineStyle: {
              color: '#17b3a3'
            }
          },
          axisLabel: {
            interval: 0,
            color: '#333'
          }
        },
        yAxis: [
          {
            type: 'value',
            axisLine: {
              lineStyle: {
                color: '#17b3a3'
              }
            }
          }
        ],
        color: ['#2ec7c9', '#b6a2de', 'yellow'],
        series: [
          {
            name: '训练集',
            data: userData.map(item => item.new),
            type: 'bar'
          },
          {
            name: '验证集',
            data: userData.map(item => item.active),
            type: 'bar'
          },
          {
            name: '测试集',
            data: userData.map(item => item.test),
            type: 'bar'
          }
        ]
      }
      echarts2.setOption(eachrts2Option)

      // 饼状图
      const echarts3 = echarts.init(this.$refs.echarts3)
      const eachrts3Option = {
        tooltip: {
          trigger: 'item'
        },
        color: ['#0f78f4', '#dd536b', '#9462e5', '#a6a6a6', '#e1bb22', '#39c362', '#3ed1cf'],
        series: [
          {
            data: videoData,
            type: 'pie'
          }
        ]
      }
      echarts3.setOption(eachrts3Option)
    })
  }
}
</script>

//
<style lang="less" scoped>
.user {
  padding-bottom: 20px;
  margin-bottom: 20px;
  border-bottom: 1px solid #ccc;
  display: flex;
  align-items: center;
  img {
    margin-right: 40px;
    width: 150px;
    height: 150px;
    border-radius: 50%;
  }
  .userinfo {
    .name {
      font-size: 32px;
      margin-bottom: 10px;
    }
    .access {
      color: #999999;
    }
  }
}
.login-info {
  p {
    line-height: 28px;
    font-size: 14px;
    color: #999999;
    span {
      color: #666666;
      margin-left: 60px;
    }
  }
}
.num {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  .icon {
    width: 80px;
    height: 80px;
    font-size: 30px;
    text-align: center;
    line-height: 80px;
    color: #fff;
  }
  .detail {
    margin-left: 15px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    .price {
      font-size: 30px;
      margin-bottom: 10px;
      line-height: 30px;
      height: 30px;
    }
    .desc {
      font-size: 14px;
      color: #999;
      text-align: center;
    }
  }
  .el-card {
    width: 32%;
    margin-bottom: 20px;
  }
}
.graph {
  margin-top: 20px;
  display: flex;
  justify-content: space-between;
  .el-card {
    width: 48%;
  }
}
</style>
