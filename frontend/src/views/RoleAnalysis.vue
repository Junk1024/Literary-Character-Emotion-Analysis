<template>
  <div class="app-container">
    <el-card class="box-card">
      <div class="tip">请上传要进行分析的文学作品txt文件</div>
      <el-upload class="upload-demo" drag action="" :limit="1" :http-request="uploadFile" accept=".txt" style="text-align: center; padding-top: 10px; padding-bottom: 10px">
        <i class="el-icon-upload" />
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      </el-upload>
    </el-card>
    <el-row style="text-align: center; padding-top: 20px; padding-bottom: 20px">
      <el-button type="primary" round @click="batchEmotionAnalysis()">获取人物名单</el-button>
    </el-row>
    <el-card v-show="visible" class="box-card">
      <div v-show="visible" class="tip">人物结果：</div>
      <div class="common-tabel">
        <el-table stripe height="500px" :data="tableData" style="width: 100%">
          <el-table-column prop="name" label="姓名"> </el-table-column>
          <el-table-column prop="count" label="频数"> </el-table-column>

          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="mini" @click="handleEdit(scope.row)">提取</el-button>
              <el-button type="danger" size="mini" @click="handleDelete(scope.row)">分析</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div class="pager">
          <el-pagination layout="prev, pager, next" :total="total" @current-change="handlePage"> </el-pagination>
        </div>
      </div>
    </el-card>
    <el-dialog title="信息" :visible.sync="dialogVisible" width="50%">
      <p>人物标签为{{ label }}分析结果如下</p>
      <el-table stripe :data="analyData" style="width: 100%">
        <el-table-column prop="name" label="标签"> </el-table-column>
        <el-table-column prop="value" label="频数"> </el-table-column>
      </el-table>
    </el-dialog>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      dialogVisible: false,
      allData: [],
      tableData: [],
      total: 0,
      pagelist: [],
      currentPage: 1,
      pagesize: 10,
      visible: false,
      form: [],
      label: '',
      analyData: [],
      labelList: []
    }
  },

  methods: {
    // 上传文件，获取上传文件内容并弹窗提示
    uploadFile(file) {
      this.fileData = file.file
      console.log(file.file)
      this.$message({
        showClose: true,
        message: '文件上传成功！',
        type: 'success'
      })
    },
    handleEdit(row) {
      let loading = this.$loading({
        lock: true, //lock的修改符--默认是false
        text: '拼命加载中，请稍候...', //显示在加载图标下方的加载文案
        background: 'rgba(0,0,0,0.8)', //遮罩层颜色
        spinner: 'el-icon-loading' //自定义加载图标类名
      })

      axios
        .get('http://127.0.0.1:8000/getcontent/', {
          params: {
            text: row.name
          }
        })
        .then(re => {
          loading.close()
          console.log(re)
          console.log(re.data)
          this.$message({
            showClose: true,
            message: '提取角色相关文本成功！',
            type: 'success'
          })
        })
    },
    handleDelete(row) {
      let loading = this.$loading({
        lock: true, //lock的修改符--默认是false
        text: '拼命加载中，请稍候...', //显示在加载图标下方的加载文案
        background: 'rgba(0,0,0,0.8)', //遮罩层颜色
        spinner: 'el-icon-loading' //自定义加载图标类名
      })
      axios
        .get('http://127.0.0.1:8000/roleanalysis/', {
          params: {
            name: row.name
          }
        })
        .then(re => {
          loading.close()
          console.log(re)
          console.log(re.data)
          re.data.label
          this.label = re.data.label
          this.dialogVisible = true
          this.analyData = re.data.labellist
        })
        .catch(error => {
          console.log(error)
          loading.close()
          this.$message({
            showClose: true,
            message: '请先提取人物相关文本！',
            type: 'error'
          })
        })
    },
    // // 保存纠错结果
    // saveResult() {
    //   var tempData = this.analysisResults
    //   if (tempData === '') {
    //     this.$message({
    //       showClose: true,
    //       message: '情感分析结果内容为空！',
    //       type: 'warning'
    //     })
    //   } else {
    //     // 第一个参数是导出文件的名称，第二个参数是需要导出的表格标签的id
    //     this.Excels.exportExcel('批量情感分析结果.xlsx', '#excel')
    //     this.$message({
    //       showClose: true,
    //       message: '情感分析结果保存成功！',
    //       type: 'success'
    //     })
    //   }
    // },
    // 批量情感分析
    batchEmotionAnalysis() {
      var that = this
      // 判断用户是否已经选择要上传的文件
      if (that.fileData === '') {
        this.$message({
          showClose: true,
          message: '请先选择要进行批量情感分析的txt文件！',
          type: 'warning'
        })
        that.analysisResults = ''
        that.visible = false
        return
      }
      let loading = this.$loading({
        lock: true, //lock的修改符--默认是false
        text: '拼命加载中，请稍候...', //显示在加载图标下方的加载文案
        background: 'rgba(0,0,0,0.8)', //遮罩层颜色
        spinner: 'el-icon-loading' //自定义加载图标类名
      })

      // 请求后端批量情感分析接口，请求方法为POST，请求体格式为form-data，字段为file，类型也为file
      var config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      var form = new FormData()
      form.append('file', that.fileData)
      axios
        .post('http://127.0.0.1:8000/v1/batchEmotionAnalysis', form, config)
        .then(response => {
          loading.close()
          that.visible = true
          that.$message({
            showClose: true,
            message: '人物名单获取完成！',
            type: 'success'
          })
          // 获取接口返回的情感分析预测结果并更新界面数据
          console.log(response)
          console.log(response.data.data)
          // let obj = response.data[0].data
          let obj = response.data.data
          let arr = []
          for (let i = 0; i < 100; i++) {
            arr.push({
              name: obj[i][0],
              count: obj[i][1]
            })
          }
          console.log(arr)
          this.allData = arr
          this.tableData = arr.slice((this.currentPage - 1) * this.pagesize, this.currentPage * this.pagesize)
          // that.tableData = tableData(0, 10)
          this.total = arr.length || 0
        })
        .catch(error => {
          console.log(error)
          that.analysisResults = ''
          that.visible = false
          that.$message({
            showClose: true,
            message: '请求异常，请检查后端服务模块！',
            type: 'error'
          })
        })
    },
    handlePage(val) {
      console.log(val)

      this.tableData = this.allData.slice((val - 1) * this.pagesize, val * this.pagesize)
      console.log(this.tableData)
      this.total = this.allData.length || 0
      // this.pagelist = this.tableData.slice((val - 1) * this.pagesize, val * this.pagesize)
      // console.log(this.pagelist)
      // this.getList(this.pagelist)
    }
  }
}
</script>

<style scoped>
.tip {
  font-family: 宋体;
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 20px;
  margin-bottom: 10px;
  text-align: left;
}
</style>
