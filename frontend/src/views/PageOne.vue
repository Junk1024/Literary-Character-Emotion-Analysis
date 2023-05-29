<template>
  <div class="introduce">
    <h2>基于Vue2的情感分析系统</h2>
    <p>---2019级智能科学与技术王漪</p>
    <ul>
      1.技术栈有:vue-router、vuex、axios、element-ui、mock、echarts。
      <li>vue-router：使用vue-router控制页面跳转，在spa中就是组件的切换，并使用了动态路由</li>
      <li>vuex：vuex采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。该项目使用vuex实现了菜单栏的折叠的控制</li>
      <li>axios：通过axios实例二次封装axios，实现数据请求并添加请求拦截器实现用于登陆页面的验证。</li>
      <li>element-ui：使用element-ui进行样式快速的设置，并了解两种引入方式</li>
      <li>mock：拦截请求并使用mock生成相应的模拟数据</li>
      <li>echarts：引入echarts并使用对数据进行多样性直观性展现</li>
    </ul>
    <ul>
      2.模块分配:该项目可分为登录页、注册页、后台首页、用户管理页、分页处理、用户crud、路由守卫等模块
      <li>登录页：使用element-ui快速实现登录页的样式</li>
      <li>注册页：使用setInterval实现验证码按钮</li>
      <li>后台首页：登陆之后进入系统的首页</li>
      <li>用户管理页：用户权限创建，读取，更新，删除的实现</li>
      <li>分页处理：对用户数据的分页处理</li>
      <li>常用组件：一般项目常用的功能实现</li>
      <li>路由守卫：添加路由导航守卫避免错误的跳转</li>
    </ul>
  </div>
</template>

<script>
export default {}
</script>

<style lang="less" scoped>
.introduce {
  h2 {
    text-align: center;
  }
  p {
    text-align: center;
  }
}
</style>
