import Mock from 'mockjs'
export default {
  getMenu: config => {
    const { sex } = JSON.parse(config.body)
    console.log(sex)
    // 先判断用户是否存在
    // 判断账号和密码是否对应
    if (sex == 1) {
      return {
        code: 20000,
        data: {
          menu: [
            {
              path: '/home',
              name: 'home',
              label: '首页',
              icon: 's-home',
              url: 'Home.vue'
            },
            {
              path: '/table',
              name: 'table',
              label: 'Echarts',
              icon: 'film',
              url: 'PersonCenter.vue'
            },
            {
              label: 'NLP',
              icon: 'video-play',

              children: [
                {
                  code: 1,
                  path: '/mall',
                  name: 'mall',
                  label: '情感分析',
                  icon: 'video-play',
                  url: 'Mall.vue'
                },
                {
                  code: 1,
                  path: '/sentenceimilar',
                  name: 'sentencesimilar',
                  label: '文本相似度',
                  icon: 'video-play',
                  url: 'SentenceSimilar.vue'
                },
                {
                  code: 1,
                  path: '/modifyerror',
                  name: 'modifyerror',
                  label: '文本纠错',
                  icon: 'video-play',
                  url: 'ModifyError.vue'
                },
                {
                  code: 1,
                  path: '/roleanalysis',
                  name: 'roleanalysis',
                  label: '人物分析',
                  icon: 'video-play',
                  url: 'RoleAnalysis.vue'
                }
              ]
            },
            {
              path: '/user',
              name: 'user',
              label: '用户管理',
              icon: 'user',
              url: 'User.vue'
            },
            {
              path: '/userR',
              name: 'userR',
              label: '用户数据',
              icon: 'user',
              url: 'UserR.vue'
            },
            {
              label: '常用组件',
              icon: 'goods',
              children: [
                {
                  code: 2,
                  path: '/guide',
                  name: 'guide',
                  label: '引导页',
                  icon: 'help',
                  url: 'guide.vue'
                },
                {
                  code: 2,
                  path: '/picupload',
                  name: 'picupload',
                  label: '图片上传',
                  icon: 'upload',
                  url: 'picupload.vue'
                },
                {
                  code: 2,
                  path: '/pullup',
                  name: 'pullup',
                  label: '拖拽组件',
                  icon: 'rank',
                  url: 'pullup.vue'
                }
              ]
            },
            {
              label: '其他',
              icon: 'link',
              children: [
                {
                  code: 3,
                  path: '/page1',
                  name: 'page1',
                  label: '项目介绍',
                  icon: 'coin',
                  url: 'PageOne.vue'
                },
                {
                  code: 3,
                  path: '/page2',
                  name: 'page2',
                  label: '我的Blog',
                  icon: 'apple',
                  url: 'PageTwo.vue'
                }
              ]
            }
          ],
          token: Mock.Random.guid(),
          message: '获取成功'
        }
      }
    } else if (sex == 0) {
      return {
        code: 20000,

        data: {
          menu: [
            {
              path: '/home',
              name: 'home',
              label: '首页',
              icon: 's-home',
              url: 'Home.vue'
            },
            {
              path: '/table',
              name: 'table',
              label: 'Echarts',
              icon: 'film',
              url: 'PersonCenter.vue'
            },
            {
              label: 'NLP',
              icon: 'video-play',

              children: [
                {
                  code: 1,
                  path: '/mall',
                  name: 'mall',
                  label: '情感分析',
                  icon: 'video-play',
                  url: 'Mall.vue'
                },
                {
                  code: 1,
                  path: '/sentenceimilar',
                  name: 'sentencesimilar',
                  label: '文本相似度',
                  icon: 'video-play',
                  url: 'SentenceSimilar.vue'
                },
                {
                  code: 1,
                  path: '/modifyerror',
                  name: 'modifyerror',
                  label: '文本纠错',
                  icon: 'video-play',
                  url: 'ModifyError.vue'
                },
                {
                  code: 1,
                  path: '/roleanalysis',
                  name: 'roleanalysis',
                  label: '人物分析',
                  icon: 'video-play',
                  url: 'RoleAnalysis.vue'
                }
              ]
            },

            {
              label: '常用组件',
              icon: 'goods',
              children: [
                {
                  code: 2,
                  path: '/guide',
                  name: 'guide',
                  label: '引导页',
                  icon: 'help',
                  url: 'guide.vue'
                },
                {
                  code: 2,
                  path: '/picupload',
                  name: 'picupload',
                  label: '图片上传',
                  icon: 'upload',
                  url: 'picupload.vue'
                },
                {
                  code: 2,
                  path: '/pullup',
                  name: 'pullup',
                  label: '拖拽组件',
                  icon: 'rank',
                  url: 'pullup.vue'
                }
              ]
            },
            {
              label: '其他',
              icon: 'link',
              children: [
                {
                  code: 3,
                  path: '/page1',
                  name: 'page1',
                  label: '项目介绍',
                  icon: 'coin',
                  url: 'PageOne.vue'
                },
                {
                  code: 3,
                  path: '/page2',
                  name: 'page2',
                  label: '我的Blog',
                  icon: 'apple',
                  url: 'PageTwo.vue'
                }
              ]
            }
          ],
          token: Mock.Random.guid(),
          message: '获取成功'
        }
      }
    } else {
      return {
        code: -999,
        data: {
          message: '密码错误'
        }
      }
    }
  }
}
