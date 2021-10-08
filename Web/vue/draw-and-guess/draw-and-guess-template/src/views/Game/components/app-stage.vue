<template>
  <el-card ref="wrapper" :body-style="{ padding: 0 }">
    <v-stage
      :config="stageConfig"
      @mousedown="mousedownHandler"
      @mouseup="mouseupHandler"
      @mousemove="mousemoveHandler"
    >
    <v-layer>
      <v-line
        v-for="(line, index) in lines"
        :key="index"
        :config="line"
      />
  </v-layer>
    </v-stage>
  </el-card>
</template>

<script>
import {mapState,mapGetters} from 'vuex'
export default {
  computed:{
    ...mapState(['lines']),
    ...mapGetters(['isGameStarted','isGameHolder'])
  },
  data() {
    return {
      // 画布配置
      
      // { stroke: '#df4b26', strokeWidth: 5, points: [100, 100, 100, 400] },
      // { stroke: '#ff00ff', strokeWidth: 5, points: [100, 100, 300, 300] }
      stageConfig: {
        width: 800,
        height: 700
      },
      // 绘画状态
      painting: false,

      // 画笔
      stroke:'#000000',
      strokeWidth:5
    }
  },

  mounted() {
    // 将画布宽度设置与容器同宽
    this.stageConfig.width = this.$refs.wrapper.$el.offsetWidth
  },

  methods: {
    // 鼠标按下
    mousedownHandler({evt:{layerX,layerY}}) {
      console.log(this.isGameStarted,this.isGameHolder)
      if(!(this.isGameStarted&&this.isGameHolder)){
        return
      }
        console.log('鼠标按下了');
      this.painting = true;
      
      const newLine = {
        stroke:this.stroke,
        strokeWidth:this.strokeWidth,
        points:[
          layerX,layerY
        ]
      }
      this.$store.commit('drawNewLine',newLine)
      this.$store.dispatch('sendDrawNewLine',newLine)
    },

    // 鼠标拖动
    mousemoveHandler({evt:{layerX,layerY}}) {
      if (this.painting) {
        console.log('鼠标拖动了, 绘画状态')
        const L = this.lines;
        const lastLine = L[L.length - 1]
        lastLine.points = lastLine.points.concat([layerX,layerY])
        this.$store.commit('updateLastLine',lastLine)
        
        this.$store.dispatch('sendUpdateLastLine',lastLine)
      }
    },

    // 鼠标释放
    mouseupHandler() {
      console.log('鼠标释放了')
      this.painting = false
    }
  }
}
</script>
