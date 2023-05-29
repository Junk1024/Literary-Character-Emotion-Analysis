<template>
  <div class="manage">
    <el-dialog title="信息" :visible.sync="dialogVisible2" width="50%" :before-close="handleClose2">
      <!-- 用户的表单信息 -->
      <div>
        <el-table :data="finddata">
          <el-table-column prop="ID" label="ID"></el-table-column>
          <el-table-column prop="name" label="姓名"> </el-table-column>
          <el-table-column prop="sex" label="性别">
            <template slot-scope="scope">
              <span>{{ scope.row.sex == 1 ? '男' : '女' }}</span>
            </template>
          </el-table-column>
          <el-table-column prop="age" label="年龄"> </el-table-column>
          <el-table-column prop="phone" label="手机号"> </el-table-column>
          <el-table-column prop="adr" label="地址"> </el-table-column>
        </el-table>
      </div>

      <!-- <p>ID{{ finddata.ID }}</p>
      <p>姓名{{ finddata.name }}</p>
      <p>性别{{ finddata.sex == 1 ? '男' : '女' }}</p>
      <p>年龄{{ finddata.age }}</p>
      <p>地址{{ finddata.adr }}</p>
      <p>手机号{{ finddata.phone }}</p> -->
    </el-dialog>

    <el-dialog title="提示" :visible.sync="dialogVisible" width="50%" :before-close="handleClose">
      <!-- 用户的表单信息 -->
      <el-form ref="form" :rules="rules" :inline="true" :model="form" label-width="80px">
        <el-form-item label="ID" prop="id">
          <el-input placeholder="请输入ID" v-model="form.id"></el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="name">
          <el-input placeholder="请输入姓名" v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="年龄" prop="age">
          <el-input placeholder="请输入年龄" v-model="form.age"></el-input>
        </el-form-item>
        <el-form-item label="性别" prop="sex">
          <el-select v-model="form.sex" placeholder="请选择">
            <el-option label="男" value="1"></el-option>
            <el-option label="女" value="0"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="手机号" prop="phone">
          <el-input placeholder="请输入手机号" v-model="form.phone"></el-input>
        </el-form-item>
        <el-form-item label="地址" prop="adr">
          <el-input placeholder="请输入地址" v-model="form.adr"></el-input>
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button @click="cancel">取 消</el-button>
        <el-button type="primary" @click="submit()">确 定</el-button>
      </span>
    </el-dialog>
    <div class="manage-header">
      <el-button @click="handleAdd" type="primary"> + 新增 </el-button>
      <!-- form搜索区域 -->
      <el-form :inline="true" :model="userForm">
        <el-form-item>
          <el-input placeholder="请输入名称" v-model="userForm.name"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">查询</el-button>
        </el-form-item>
      </el-form>
    </div>
    <div class="common-tabel">
      <el-table stripe height="90%" :data="tableData" style="width: 100%">
        <el-table-column prop="ID" label="ID"> </el-table-column>
        <el-table-column prop="name" label="姓名"> </el-table-column>
        <el-table-column prop="sex" label="性别">
          <template slot-scope="scope">
            <span>{{ scope.row.sex == 1 ? '男' : '女' }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="age" label="年龄"> </el-table-column>
        <el-table-column prop="phone" label="手机号"> </el-table-column>
        <el-table-column prop="adr" label="地址"> </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" @click="handleEdit(scope.row)">编辑</el-button>
            <el-button type="danger" size="mini" @click="handleDelete(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="pager">
        <el-pagination layout="prev, pager, next" :total="total" @current-change="handlePage"> </el-pagination>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      dialogVisible: false,
      dialogVisible2: false,
      form: {
        name: '',
        sex: '',
        age: '',
        phone: '',
        adr: '',
        ID: ''
      },

      rules: {
        name: [{ required: true, message: '请输入姓名' }],
        sex: [{ required: true, message: '请选择性别' }],
        age: [{ required: true, message: '请输入年龄' }],
        phone: [{ required: true, message: '请输入手机号' }],
        adr: [{ required: true, message: '请输入地址' }]
      },
      tableData: [],
      finddata: [],
      modalType: 0, // 0表示新增的弹窗， 1表示编辑
      total: 0, //当前的总条数
      pagelist: [],
      currentPage: 1,
      pagesize: 10,
      userForm: {
        name: ''
      }
    }
  },
  methods: {
    // 提交用户表单
    submit() {
      this.$refs.form.validate(valid => {
        console.log(valid, 'valid')
        if (valid) {
          // 后续对表单数据的处理
          if (this.modalType === 0) {
            console.log(this.form.age)
            console.log(this.form)
            axios
              .get('http://127.0.0.1/list/add', {
                params: {
                  name: this.form.name,
                  sex: this.form.sex,
                  age: this.form.age,
                  adr: this.form.adr,
                  phone: this.form.phone
                }
              })
              .then(res => {
                // console.log(res.data)
                if (res.data.status == 200) {
                  this.$message({
                    message: '添加成功',
                    type: 'successful'
                  })
                  this.getList()
                } else {
                  this.$message({
                    message: '添加失败',
                    type: 'error'
                  })
                }
              })

            this.getList()
          } else {
            console.log(this.form)
            console.log(this.form.ID)
            axios
              .get('http://127.0.0.1/list/update', {
                params: {
                  ID: this.form.ID,
                  name: this.form.name,
                  sex: this.form.sex,
                  age: this.form.age,
                  adr: this.form.adr,
                  phone: this.form.phone
                }
              })
              .then(res => {
                this.getList()
                console.log(res.data)
                if (res.data.status == 200) {
                  this.$message({
                    message: '修改成功',
                    type: 'successful'
                  })
                } else {
                  this.$message({
                    message: '修改失败',
                    type: 'error'
                  })
                }
              })
          }

          // 清空表单的数据
          this.$refs.form.resetFields()
          // 关闭弹窗
          this.dialogVisible = false
        }
      })
    },
    // 弹窗关闭的时候
    handleClose() {
      this.$refs.form.resetFields()
      this.dialogVisible = false
    },
    handleClose2() {
      this.userForm = []
      this.dialogVisible2 = false
    },

    cancel() {
      this.handleClose()
    },
    handleEdit(row) {
      this.modalType = 1
      this.dialogVisible = true
      // 注意需要对当前行数据进行深拷贝，否则会出错

      // this.form = row
      this.form = JSON.parse(JSON.stringify(row))
      console.log(row)
    },
    handleDelete(row) {
      console.log(row)
      this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        axios
          .get('http://127.0.0.1/list/del', {
            params: {
              ID: row.ID
            }
          })
          .then(() => {
            this.$message({
              type: 'success',
              message: '删除成功!'
            })
            // 重新获取列表的接口
            this.getList()
          })

          .catch(() => {
            this.$message({
              type: 'info',
              message: '已取消删除'
            })
          })
      })
    },
    handleAdd() {
      this.modalType = 0
      this.dialogVisible = true
      this.form = []
    },
    // 获取列表的数据
    getList() {
      // 获取的列表的数据
      // console.log(this.userForm)
      axios.get('http://127.0.0.1/list/all').then(({ data }) => {
        console.log(data)
        this.tableData = data.slice((this.currentPage - 1) * this.pagesize, this.currentPage * this.pagesize)

        this.total = data.length || 0
      })
    },
    // 选择页码的回调函数
    handlePage(val) {
      console.log(val)
      axios.get('http://127.0.0.1/list/all').then(({ data }) => {
        console.log(data)
        this.tableData = data.slice((val - 1) * this.pagesize, val * this.pagesize)
        console.log(this.tableData)
        this.total = data.length || 0
        // this.pagelist = this.tableData.slice((val - 1) * this.pagesize, val * this.pagesize)
        // console.log(this.pagelist)
        // this.getList(this.pagelist)
      })
    },
    // 列表的查询
    onSubmit() {
      axios
        .get('http://127.0.0.1/list/get', {
          params: {
            name: this.userForm.name
          }
        })
        .then(res => {
          this.finddata = res.data
          console.log(this.finddata)
        })
        .then(() => {
          this.dialogVisible2 = true
          console.log(this.finddata)
        })
        .catch(err => {
          console.log('操作失败' + err)
        })
    }
  },
  mounted() {
    this.getList()
    // this.onSubmit()
  }
}
</script>
<style lang="less" scoped>
.manage {
  height: 90%;
  .manage-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .common-tabel {
    position: relative;
    height: calc(100% - 62px);
    .pager {
      position: absolute;
      bottom: 0;
      right: 20px;
    }
  }
}
</style>
