import _debounce from 'lodash/debounce'
let fn = null
const debounce = {
  inserted: function (el, binding) {
    fn = _debounce(binding.value, 1000, {
      leading: true,
      trailing: false
    })
    el.addEventListener('click', fn)
  },
  unbind: function (el) {
    fn && el.removeEventListener('click', fn)
  }
}

const install = function (Vue) {
  Vue.directive('debounce', debounce)
}

if (window.Vue) {
  window['debounce'] = debounce
  Vue.use(install) // eslint-disable-line
}

debounce.install = install

export default debounce
