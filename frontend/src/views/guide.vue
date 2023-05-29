<template>
  <div class="card content-box">
    <el-alert title="引导页对于一些第一次进入项目的人很有用，你可以简单介绍下项目的功能。本 Demo 是基于 driver.js." type="warning" :closable="false" />
    <div><el-button type="primary" @click.prevent.stop="guide">打开引导页 🤹‍♂️</el-button></div>
  </div>
</template>

<script>
import Driver from 'driver.js'
import 'driver.js/dist/driver.min.css'
export default {
  data() {
    return {
      driver: null,
      steps: [
        {
          element: '#a',
          popover: {
            title: '这是菜单折叠按钮',
            description: '点击可实现左侧菜单的折叠与否',
            position: 'right'
          }
        },
        {
          element: '#b',
          popover: {
            title: '头像下拉菜单',
            description: '鼠标放在头像上即可显示下拉菜单',
            position: 'left'
          }
        }
      ]
    }
  },
  methods: {
    guide() {
      this.driver.defineSteps(this.steps)
      this.driver.start()
    }
  },
  mounted() {
    this.driver = new Driver()
  }
}
</script>

<style scoped lang="less">
.el-button {
  margin-top: 20px;
}
</style>
