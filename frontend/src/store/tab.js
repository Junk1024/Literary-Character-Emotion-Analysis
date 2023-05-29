import Cookie from 'js-cookie'
export default {
  state: {
    // 控制菜单的展开与否
    isCollapse: false,
    tabList: [
      {
        path: '/',
        name: 'home',
        label: '首页',
        icon: 's-home',
        url: 'Home/Home'
      }
    ],
    menu: []
  },
  mutations: {
    // 修改菜单展开或收起的方法
    collapseMenu(state) {
      state.isCollapse = !state.isCollapse
    },
    selectMenu(state, val) {
      // console.log(val, 'val')
      // 判断添加的数据是否为首页
      if (val.name !== 'home') {
        const index = state.tabList.findIndex(item => item.name === val.name)
        if (index === -1) {
          state.tabList.push(val)
        }
      }
    },
    // 删除tag的功能
    closeTag(state, item) {
      console.log(item, 'item')
      const index = state.tabList.findIndex(val => val.name === item.name)
      state.tabList.splice(index, 1)
    },
    // 设置menu数据
    setMenu(state, val) {
      state.menu = val
      Cookie.set('menu', JSON.stringify(val))
    },
    addMenu(state, router) {
      // 判断缓存中是否有数据
      if (!Cookie.get('menu')) return
      const menu = JSON.parse(Cookie.get('menu'))
      state.menu = menu
      // 组装动态路由的数据
      const menuArray = []
      menu.forEach(item => {
        if (item.children) {
          item.children = item.children.map(item => {
            // console.log(item.url)
            item.component = () => import(`../views/${item.url}`)
            return item
          })
          menuArray.push(...item.children)
        } else {
          // console.log(item.url)
          item.component = () => import(`../views/${item.url}`)
          menuArray.push(item)
        }
      })
      // console.log(menuArray, 'menuArray')
      // 路由的动态添加
      menuArray.forEach(item => {
        router.addRoute('Main', item)
      })
    }
  }
}
