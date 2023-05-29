const a = [
  ['wang', 5],
  ['zhang', 6]
]
let obj = { 0: '男', 1: '女' }

// 使用for...in...循环，拿到对象的键、值
// 将其组成新对象，使用数组的push方法追加到数组中
function objToArr(obj) {
  let arr = []
  for (let i = 0; i < 2; i++) {
    arr.push({
      name: obj[i][0],
      count: obj[i][1]
    })
  }
  return arr
}

const arr = objToArr(a)
console.log(arr)
