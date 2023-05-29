<template>
  <div>
    <el-container>
      <el-aside width="auto">
        <common-aside />
      </el-aside>
      <el-container>
        <el-header><CommonHeader /></el-header>
        <common-tag />
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import CommonTag from '../components/CommonTag.vue'
import CommonAside from '../components/CommonAside.vue'
import CommonHeader from '../components/CommonHeader.vue'
export default {
  components: { CommonAside, CommonHeader, CommonTag }
}
</script>

<style lang="less" scoped>
.el-header {
  padding: 0;
}
</style>
