<template>
  <div>
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm">
      <el-form-item prop="name">
        <el-input placeholder="请输入用户名" v-model="ruleForm.name">
          <i slot="prefix" class="el-icon-user-solid"></i>
        </el-input>
      </el-form-item>
      <el-form-item label="性别：" prop="sex">
        <el-select v-model="ruleForm.sex" placeholder="请选择">
          <el-option label="男" value="1"></el-option>
          <el-option label="女" value="0"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item prop="age">
        <el-input placeholder="请输入年龄" v-model="ruleForm.age">
          <i slot="prefix" class="el-icon-postcard"></i>
        </el-input>
      </el-form-item>
      <el-form-item prop="adr">
        <el-input placeholder="请输入地址" v-model="ruleForm.adr">
          <i slot="prefix" class="el-icon-phone"></i>
        </el-input>
      </el-form-item>
      <el-form-item prop="phone">
        <el-input placeholder="请输入手机号" v-model="ruleForm.phone">
          <i slot="prefix" class="el-icon-phone"></i>
        </el-input>
      </el-form-item>
      <el-form-item prop="code">
        <el-row :gutter="18">
          <el-col :span="16">
            <el-input placeholder="请输入验证码" v-model="ruleForm.code">
              <i slot="prefix" class="el-icon-tickets"></i>
            </el-input>
          </el-col>
          <el-col :span="6">
            <el-button class="btn" @click="sendCode" :disabled="disabled">{{ btnText }}</el-button>
          </el-col>
        </el-row>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" style="width: 100%" @click="phoneLogin">点击注册</el-button>
      </el-form-item>
      <el-form-item>
        <el-button style="width: 100%" @click="cancelresiter">返回</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { throttle, debounce } from '../utils/utils'
import axios from 'axios'
export default {
  name: 'PhoneLogin',
  components: {},
  props: {
    ruleForm: {
      name: '',
      sex: '',
      age: '',
      phone: '',
      adr: ''
    },
    countDown: {
      type: Number,
      default: 60
    }
  },
  data() {
    let checkPhone = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('手机号不能为空'))
      } else {
        let reg = /^1[3|4|5|7|8][0-9]\d{8}$/
        if (reg.test(value)) {
          callback()
        } else {
          return callback(new Error('请输入正确的手机号'))
        }
      }
    }
    return {
      rules: {
        phone: [{ validator: checkPhone, trigger: 'change' }],
        code: [{ required: true, message: '验证码不能为空', trigger: 'blur' }],
        name: [{ required: true, message: '姓名不能为空', trigger: 'blur' }],
        age: [{ required: true, message: '年龄不能为空', trigger: 'blur' }],
        sex: [{ required: true, message: '性别不能为空', trigger: 'blur' }],
        adr: [{ required: true, message: '地址不能为空', trigger: 'blur' }]
      },
      disabled: false,
      btnText: '发送验证码'
    }
  },
  methods: {
    cancelresiter() {
      this.$router.push('login')
    },
    phoneLogin: throttle(function () {
      this.$refs.ruleForm.validate(valid => {
        if (valid) {
          this.$emit('submit')
          console.log(this.ruleForm)
          axios
            .get('http://127.0.0.1/list/add', {
              params: {
                name: this.ruleForm.name,
                sex: this.ruleForm.sex,
                age: this.ruleForm.age,
                adr: this.ruleForm.adr,
                phone: this.ruleForm.phone
              }
            })
            .then(res => {
              this.$refs.ruleForm = []
              console.log(this.ruleForm)
              console.log(this)
              if (res.data.status == 200) {
                this.$message({
                  message: '添加成功',
                  type: 'successful'
                })
                this.$router.push('login')
              } else {
                this.$message({
                  message: '添加失败',
                  type: 'error'
                })
              }
            })
        } else {
          this.$emit('errHandle')
        }
      })
    }, 1000),
    sendCode: debounce(function () {
      this.$refs.ruleForm.validateField('phone', errorMessage => {
        if (errorMessage) {
          this.$message.error(errorMessage)
        } else {
          // 1.时间开始倒数
          // 2.按钮进入禁用状态
          // 3.如果倒计时结束 按钮恢复可用状态 按钮文字变为重新发送, 时间重置
          // 4.倒计时的过程中 按钮文字为 多少s后重新发送
          let timer = setInterval(() => {
            this.time--
            this.btnText = `${this.time}s后重新发送`
            this.disabled = true
            if (this.time === 0) {
              this.disabled = false
              this.btnText = '重新发送'
              this.time = this.countDown
              clearInterval(timer)
            }
          }, 1000)
          this.$emit('send')
        }
      })
    }, 500)
  },
  mounted() {
    this.time = this.countDown
  }
}
</script>
<style lang="less" scoped>
.btn {
  margin-right: 0;
}
</style>
