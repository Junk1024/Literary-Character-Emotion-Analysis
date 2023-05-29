// mock数据模拟
import Mock from 'mockjs'

// 图表数据
let List = []
export default {
  getStatisticalData: () => {
    //Mock.Random.float 产生随机数100到8000之间 保留小数 最小0位 最大0位
    for (let i = 0; i < 7; i++) {
      List.push(
        Mock.mock({
          正向: Mock.Random.float(100, 8000, 0, 0),
          负向: Mock.Random.float(100, 8000, 0, 0),
          中立: Mock.Random.float(100, 8000, 0, 0),
          积极: Mock.Random.float(100, 8000, 0, 0),
          消极: Mock.Random.float(100, 8000, 0, 0),
          无感: Mock.Random.float(100, 8000, 0, 0)
        })
      )
    }
    return {
      code: 20000,
      data: {
        // 饼图
        videoData: [
          {
            name: 'happy',
            value: 2835
          },
          {
            name: 'angry',
            value: 4677
          },
          {
            name: 'netural',
            value: 9615
          },
          {
            name: 'sad',
            value: 1695
          },
          {
            name: 'surprise',
            value: 1288
          },
          {
            name: 'fear',
            value: 298
          }
        ],
        // 柱状图
        userData: [
          {
            date: 'angry',
            new: 3758,
            active: 503,
            test: 416
          },
          {
            date: 'sad',
            new: 1367,
            active: 181,
            test: 151
          },
          {
            date: 'fear',
            new: 247,
            active: 23,
            test: 28
          },
          {
            date: 'netural',
            new: 7825,
            active: 825,
            test: 965
          },
          {
            date: 'happy',
            new: 2218,
            active: 324,
            test: 293
          },
          {
            date: 'surprise',
            new: 993,
            active: 144,
            test: 147
          }
        ],
        // 折线图
        orderData: {
          date: ['20191001', '20191002', '20191003', '20191004', '20191005', '20191006', '20191007'],
          data: List
        },
        tableData: [
          {
            name: 'angry',
            todayBuy: 8343,
            monthBuy: 586,
            totalBuy: 1508
          },
          {
            name: 'sad',
            todayBuy: 4990,
            monthBuy: 346,
            totalBuy: 900
          },
          {
            name: 'fear',
            todayBuy: 1220,
            monthBuy: 87,
            totalBuy: 210
          },
          {
            name: 'netural',
            todayBuy: 5749,
            monthBuy: 420,
            totalBuy: 990
          },
          {
            name: 'happy',
            todayBuy: 5378,
            monthBuy: 391,
            totalBuy: 1018
          },
          {
            name: 'surprise',
            todayBuy: 2086,
            monthBuy: 170,
            totalBuy: 374
          }
        ]
      }
    }
  }
}
