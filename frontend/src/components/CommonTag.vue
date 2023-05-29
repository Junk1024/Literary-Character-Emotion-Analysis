<template>
  <div class="tabs">
    <draggable v-bind="dragOptions" @start="drag = true" @end="drag = false">
      <el-tag v-for="(item, index) in tags" :key="item.path" :closable="item.name !== 'home'" :effect="$route.name === item.name ? 'dark' : 'plain'" @click="changeMenu(item, index)" @close="handleClose(item, index)" size="small">
        {{ item.label }}
      </el-tag>
    </draggable>
  </div>
</template>
<script>
import { mapState, mapMutations } from 'vuex'
import draggable from 'vuedraggable'

export default {
  display: 'Transitions',
  order: 8,
  components: {
    draggable
  },
  name: 'CommonTag',
  data() {
    return {
      list: tags.map((name, index) => {
        return { name, order: index + 1 }
      }),
      drag: false
    }
  },
  computed: {
    dragOptions() {
      return {
        animation: 200,
        group: 'description',
        disabled: false,
        ghostClass: 'ghost'
      }
    },
    ...mapState({
      tags: state => state.tab.tabList
    })
  },
  methods: {
    // 恢复原始排序
    sort() {
      this.list = this.list.sort((a, b) => a.order - b.order)
    },
    ...mapMutations(['closeTag']),
    // 点击tag跳转的功能
    changeMenu(item) {
      this.$router.push({ name: item.name })
    },
    // tag的删除功能
    handleClose(item, index) {
      this.closeTag(item)
      const length = this.tags.length
      // 删除之后的跳转逻辑
      if (item.name !== this.$route.name) {
        return
      }
      // 表示删除的是最后一项
      if (index === length) {
        this.$router.push({
          name: this.tags[index - 1].name
        })
      } else {
        this.$router.push({
          name: this.tags[index].name
        })
      }
    }
  }
}
</script>
<style lang="less" scoped>
.tabs {
  padding: 20px;
  .el-tag {
    margin-right: 15px;
    cursor: pointer;
  }
}
</style>
