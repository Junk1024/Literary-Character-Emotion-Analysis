/**
 * @description: 防抖函数
 * @param {type}:callback 回调函数
 * @param {type}:wait 节流时间(默认1000ms)
 * @return: 函数
 */
export function debounce(callback, wait = 1000) {
  var timeId = null
  // 闭包的应用
  return function () {
    var self = this
    var args = arguments
    // 清除可能存在的timeId
    if (timeId !== null) {
      clearTimeout(timeId)
    }
    timeId = setTimeout(() => {
      // TODO: 必须使用apply或者call,将回调函数的this指向Vue
      callback.apply(self, args)
    }, wait)
  }
}

/**
 * @description: 节流函数
 * @param {type}:callback 回调函数
 * @param {type}:wait 节流时间(默认1000ms)
 * @return: callback 函数
 */
export function throttle(callback, wait = 1000) {
  var timeId = null
  var startTime = new Date()
  return function () {
    var self = this
    var args = arguments
    if (timeId !== null) {
      clearTimeout(timeId)
    }
    var currentTime = new Date()
    // 当前的时间差
    var spaceTime = currentTime - startTime
    if (spaceTime >= wait) {
      // TODO:调用apply或者call将this指向Vue
      callback.apply(self, args)
      // 执行完之后需要重置开始的时间
      startTime = new Date()
    } else {
      timeId = setTimeout(() => {
        // TODO:调用apply或者call将this指向Vue
        callback.apply(self, args)
      }, wait)
    }
  }
}
