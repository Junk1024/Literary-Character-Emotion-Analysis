<template>
  <div>
    <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="200px" class="demo-ruleForm">
      <el-form-item label="请输入您要分析的内容" prop="pass">
        <el-input type="textarea" validate-event autosize v-model="ruleForm.pass" autocomplete="off" placeholder="请输入您要分析的内容"></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
        <el-button @click="resetForm('ruleForm')">重置</el-button>
      </el-form-item>
      <el-dialog title="结果" :visible.sync="dialogVisible" width="50%">
        <el-form-item model="result">
          <p>经过系统分析，您输入的句子“{{ ruleForm.pass }}”的纠错结果如下</p>
          <p>正确的文本：{{ result.correct_query }}</p>
        </el-form-item>
      </el-dialog>
    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入您要分析的内容'))
      } else {
        if (this.ruleForm.checkPass !== '') {
          this.$refs.ruleForm.validateField('checkPass')
        }
        callback()
      }
    }

    return {
      result: [],
      dialogVisible: false,
      ruleForm: {
        pass: ''
      },
      rules: {
        pass: [{ validator: validatePass, trigger: 'blur' }]
      }
    }
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          console.log(this.ruleForm.pass)
          this.$axios
            .post('https://aip.baidubce.com/rpc/2.0/nlp/v1/ecnet?access_token=24.7bb92faf314fa61cfc22e6cea0ddc906.2592000.1683541429.282335-28398765&charset=UTF-8', {
              text: this.ruleForm.pass
            })
            .then(re => {
              console.log(re.data)
              this.result = re.data.item
              console.log(this.result)
              console.log(this.result.score)
              console.log(this.result.correct_query)
              console.log(this.result.vec_fragment)
            })

          // alert('提交成功!')
          // this.$refs[formName].resetFields()
        } else {
          console.log('提交失败!!')
          return false
        }
      })
      this.dialogVisible = true
    },
    resetForm(formName) {
      this.result = ''
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style lang="less" scoped></style>
