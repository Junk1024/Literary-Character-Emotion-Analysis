let db = require('../db/index')

exports.all = (req, res) => {
  //获取info表全部数据
  var sql = 'select * from user_info'
  db.query(sql, (err, data) => {
    if (err) {
      return res.send('错误：' + err.message)
    }
    res.send(data)
  })
}
exports.get = (req, res) => {
  //通过id查询数据
  var sql = 'select * from user_info where name = ?' //？用于占位
  db.query(sql, [req.query.name], (err, data) => {
    if (err) {
      return res.send('错误：' + err.message)
    }
    res.send(data)
  })
}
exports.login = (req, res) => {
  //通过id查询数据
  var sql = 'select * from user_info where name = ? and phone = ?' //？用于占位
  db.query(sql, [req.query.name, req.query.phone], (err, data) => {
    if (err) {
      return res.send('错误：用户不存在或密码错误')
    }
    res.send({
      data: data,
      status: 200
    })
  })
}

exports.del = (req, res) => {
  //通过id删除数据
  var sql = 'delete from user_info where ID = ?'
  db.query(sql, [req.query.ID], (err, data) => {
    if (err) {
      return res.send('错误：' + err.message)
    }
    res.send({
      data: data,
      status: 200,
      message: '删除成功'
    })
  })
}

exports.add = (req, res) => {
  //向info表添加数据
  var sql = 'insert into user_info (ID,name,sex,age,adr,phone) values (?,?,?,?,?,?)'
  db.query(sql, [req.query.ID, req.query.name, req.query.sex, req.query.age, req.query.adr, req.query.phone], (err, data) => {
    if (err) {
      console.log('添加失败')
      return res.send('错误：' + err.message)
    }
    res.send({
      status: 200,
      message: '添加成功'
    })
  })
}

exports.update = (req, res) => {
  //通过id更新数据
  var sql = 'update user_info set name = ?, sex = ?, age = ?, adr = ?, phone = ? where ID = ?'
  db.query(sql, [req.query.name, req.query.sex, req.query.age, req.query.adr, req.query.phone, req.query.ID], (err, data) => {
    if (err) {
      console.log('error')
      return res.send('错误：' + err.message)
    }
    res.send({
      data: data,
      status: 200,
      message: '修改成功'
    })
  })
}
