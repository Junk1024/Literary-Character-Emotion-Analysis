<template>
  <div class="box">
    <div class="grid-content bg-purple">
      <div class="title-style" @click="openUrl(url)">{{ title }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: '基于Github-Pages和Github-Action实现的自动化部署博客(点击跳转)'
    },
    url: {
      type: String,
      default: 'https://junk1024.github.io/'
    }
  },
  methods: {
    openUrl(url) {
      window.open(url, '_blank')
      //_blank : 在新窗口打开
      //_self : 在当前窗口打开

      //window.location.href = url : 当前页面重定向
    }
  }
}
</script>

<style lang="less" scoped></style>
