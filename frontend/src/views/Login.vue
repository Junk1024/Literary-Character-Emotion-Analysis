<template>
  <div class="login-index">
    <el-form ref="form" label-width="70px" :inline="true" class="login-container" :model="form" :rules="rules">
      <h3 class="login_title">情感分析系统</h3>
      <h6 class="login_title">2019级智能科学与技术王漪</h6>
      <el-form-item label="用户名" prop="username">
        <el-input v-model="form.username" placeholder="请输入账号"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input show-password type="password" v-model="form.password" placeholder="请输入密码"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button @click="submit" style="margin-left: 68px; margin-top: 10px; width: 198px" type="primary">登录</el-button>
        <el-link style="margin-left: 90px" :underline="false" @click="forget">忘记密码</el-link> |
        <el-link @click="regist" :underline="false"> 注册新账号</el-link>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
import Cookie from 'js-cookie'
import axios from 'axios'
import { getMenu } from '../api'
import { debounce } from '../utils/utils'
export default {
  data() {
    return {
      form: {
        username: '',
        password: ''
      },
      checkform: {},
      rules: {
        username: [{ required: true, trigger: 'blur', message: '请输入用户名' }],
        password: [{ required: true, trigger: 'blur', message: '请输入密码' }]
      }
    }
  },
  methods: {
    regist() {
      // console.log('注册')
      this.$router.push('/resiter')
    },
    forget() {
      alert('该功能待开发')
    },
    submit: debounce(function () {
      this.$refs.form.validate(valid => {
        if (valid) {
          axios
            .get('http://127.0.0.1/list/login', {
              params: {
                name: this.form.username,
                phone: this.form.password
              }
            })
            .then(res => {
              console.log(res.data.data[0].sex)
              this.form = res.data.data[0]
              console.log(this.form.name)
              getMenu(this.form).then(({ data }) => {
                console.log(data)
                if (data.code === 20000) {
                  Cookie.set('token', data.data.token)
                  Cookie.set('username', this.form.name)

                  // 获取菜单数据
                  // data.data.menu获取菜单存入store
                  this.$store.commit('setMenu', data.data.menu)
                  this.$store.commit('addMenu', this.$router)

                  this.$message({
                    message: '登陆成功',
                    type: 'success'
                  })
                  this.$router.push('/home')
                } else {
                  this.$message.error(data.data.message)
                }
              })
            })
            .catch(err => {
              this.$message({
                message: '用户不存在或密码错误',
                type: 'error'
              })
            })
        }
      })
    }, 1000)
  },
  created() {
    //登录添加键盘事件,注意,不能直接在焦点事件上添加回车
    let that = this
    document.onkeydown = function (e) {
      e = window.event || e
      if (that.$route.path == '/login' && (e.code == 'Enter' || e.code == 'Num Enter')) {
        //验证在登录界面和按得键是回车键enter
        that.submit() //登录函数 （-登录按钮的点击事件）
      }
    }
  }
}
</script>
<style lang="less" scoped>
.login-index {
  border: 1px solid white;
  padding-left: 850px;
  background-image: url(../assets/images/login_bac.png);
  background-size: contain;
  background-repeat: no-repeat;
}
a {
  text-decoration: none;
  color: black;
}
.login-container {
  width: 350px;
  border: 1px solid #eaeaea;
  margin: 180px auto;
  padding: 35px 35px 35px 35px;
  background-color: #fff;
  border-radius: 15px;
  box-shadow: 0 0 50px #cac6c6;
  box-sizing: border-box;
  .login_title {
    text-align: center;
    margin-bottom: 40px;
    color: #505458;
  }
  text {
    font-size: 10px;
    text-align: center;
    margin-bottom: 40px;
    color: #505458;
  }
  .el-input {
    width: 198px;
  }
}
.login-container::before,
.login-container::after {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  z-index: 0;
  width: 350px;
  height: 350px;
  background: linear-gradient(0deg, transparent, transparent, #03e9f4, #03e9f4, 03e9f4);
  transform-origin: bottom right;
  animation: login 5s linear infinite;
}
.login-container::after {
  background: linear-gradient(0deg, transparent, transparent, #ff2771, #ff2771, #ff2771);
  animation-delay: -3s;
}
@keyframes login {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
