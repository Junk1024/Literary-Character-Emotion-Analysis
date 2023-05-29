<template>
  <div class="login">
    <h1>手机注册</h1>

    <div class="account">
      <phone-login :rule-form="phoneForm" @send="send" @submit="submit" @errHandle="errHandle"> </phone-login>
    </div>
  </div>
</template>

<script>
import PhoneLogin from '../components/PhoneLogin.vue'

export default {
  components: { PhoneLogin },
  props: {},
  data() {
    return {
      phoneForm: {
        phone: '',
        code: ''
      }
    }
  },
  methods: {
    submit() {
      this.$message.success('提交成功')
      console.log('成功')
    },
    errHandle() {
      this.$message.error('表单填写有误，请检查')
      console.log('失败')
    },
    send() {
      this.$message.info('发送验证码成功')
    }
  },
  mounted() {}
}
</script>

<style scoped lang="less">
.login {
  width: 750px;
  border: 1px solid #eaeaea;
  margin: 180px auto;
  padding: 35px 35px 35px 35px;
  background-color: #fff;
  border-radius: 15px;
  box-shadow: 0 0 50px #cac6c6;
  box-sizing: border-box;
  h1 {
    text-align: center;
  }
}
.account {
  margin: auto;

  width: 500px;
}
</style>
