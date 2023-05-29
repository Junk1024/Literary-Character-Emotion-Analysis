<template>
  <div>
    <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="200px" class="demo-ruleForm">
      <el-form-item label="请输入您要分析的内容" prop="pass">
        <el-input type="textarea" validate-event autosize v-model="ruleForm.pass1" autocomplete="off" placeholder="请输入您要分析的文本1"></el-input>
        <el-input type="textarea" validate-event autosize v-model="ruleForm.pass2" autocomplete="off" placeholder="请输入您要分析的文本2"></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
        <el-button @click="resetForm()">重置</el-button>
      </el-form-item>
      <el-dialog title="结果" :visible.sync="dialogVisible" width="50%">
        <el-form-item model="result">
          <p>经过系统分析，您输入的句子“{{ ruleForm.pass1 }}”和“{{ ruleForm.pass2 }}”的结果如下</p>
          <p>相似度：{{ result.score }}</p>
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
        pass1: '',
        pass2: ''
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
          this.$axios
            .post('https://aip.baidubce.com/rpc/2.0/nlp/v2/simnet?access_token=24.7bb92faf314fa61cfc22e6cea0ddc906.2592000.1683541429.282335-28398765&charset=UTF-8', {
              text_1: this.ruleForm.pass1,
              text_2: this.ruleForm.pass2
            })
            .then(re => {
              this.result = JSON.parse(JSON.stringify(re.data))

              console.log(this.result)
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
    resetForm() {
      this.result = ''
      this.ruleForm = {}
    }
  }
}
</script>

<style lang="less" scoped></style>
