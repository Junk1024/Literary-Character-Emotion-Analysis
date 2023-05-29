<template>
  <div>
    <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="200px" class="demo-ruleForm">
      <el-form-item label="请输入您要分析的内容" prop="pass">
        <el-input type="textarea" validate-event autosize v-model="ruleForm.pass" autocomplete="off" placeholder="请输入您要分析的内容"></el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm2('ruleForm')">百度结果</el-button>
        <el-button type="primary" @click="submitForm('ruleForm')">我的结果</el-button>
        <el-button @click="resetForm('ruleForm')">重置</el-button>
      </el-form-item>
      <el-form-item v-for="item in result2">
        <p>经过百度分析，情感信息如下</p>
        <p>置信度：{{ item.confidence }}</p>
        <!-- <p>消极概率：{{ item.negative_prob }}</p>
        <p>积极概率：{{ item.positive_prob }}</p> -->
        <p>分类标签：{{ item.sentiment == 0 ? '消极' : '积极' }}</p>
      </el-form-item>
      <el-form-item v-for="item in result">
        <p>经过系统分析，情感信息如下</p>
        <!-- <p>输入文本：{{ item.inputText }}</p> -->
        <p>分类标签：{{ item.singleAnalysisResult }}</p>
      </el-form-item>
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
      result2: [],
      ruleForm: {
        pass: ''
      },
      rules: {
        pass: [{ validator: validatePass, trigger: 'blur' }]
      }
    }
  },
  methods: {
    submitForm2(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          console.log(this.ruleForm.pass)
          this.$axios
            .post('https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token=24.8a36c1ba78ef21a82d484ece21b5e7f0.2592000.1687094838.282335-28398765', {
              text: this.ruleForm.pass
            })
            .then(re => {
              this.result2 = re.data.items
              console.log(this.result2)
            })

          // alert('提交成功!')
          // this.$refs[formName].resetFields()
        } else {
          console.log('提交失败!!')
          return false
        }
      })
    },
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          console.log(this.ruleForm.pass)
          this.$axios
            .get('http://localhost:8000/singleSentimentAnalysis/', {
              params: {
                text: this.ruleForm.pass
              }
            })
            .then(re => {
              console.log(re.data)
              this.result.push(re.data)
              console.log(this.result)
            })

          // alert('提交成功!')
          // this.$refs[formName].resetFields()
        } else {
          console.log('提交失败!!')
          return false
        }
      })
    },

    resetForm(formName) {
      this.result = []
      this.result2 = []
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style lang="less" scoped></style>
