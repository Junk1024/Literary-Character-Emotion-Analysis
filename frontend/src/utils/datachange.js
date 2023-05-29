function objToArr(obj) {
  let arr = []
  for (let i = 0; i < 100; i++) {
    arr.push({
      name: obj[i][0],
      count: obj[i][1]
    })
  }
  return arr
}
export default objToArr
