<template>
  <el-card>
    <div class="pen-select">
      <span>更换字迹颜色:</span>
      <el-color-picker
          v-model="color"
          :predefine="predefineColors"
          @change="active_change">
      </el-color-picker>
      <div class="lock" @click="changeLockState">
        <div v-show="this.isLocked" data-is="lock">
          <span>解锁:</span>
          <i class="el-icon-lock"></i>
        </div>
        <div v-show="this.isLocked === false" data-is="unlock">
          <span>锁定:</span>
          <i class="el-icon-unlock"></i>
        </div>
      </div>
    </div>
  </el-card>
</template>

<script>
import {mapGetters, mapMutations} from "vuex"

export default {
  name: "app-side-pen",
  computed: {
    ...mapMutations(['updatePenColor', 'updateLockState']),
    ...mapGetters(['isLocked'])
  },
  data() {
    return {
      color: 'rgb(255, 69, 0)',
      predefineColors: [
        '#ff4500',
        '#ff8c00',
        '#ffd700',
        '#90ee90',
        '#00ced1',
        '#1e90ff',
        '#c71585',
        'hsv(51, 100, 98)',
        'hsl(181, 100%, 37%)',
      ]
    }
  },
  methods: {
    active_change(e) {
      this.$store.commit("updatePenColor", e);
    },
    changeLockState() {
      this.$store.commit("updateLockState", !this.isLocked)
    }

  },
  mounted() {
    console.log(this.isLocked)
  }
}
</script>

<style scoped>
.pen-select {
  display: flex;
  align-items: center;
  justify-content: space-around;
  min-width: 200px;
}
</style>
