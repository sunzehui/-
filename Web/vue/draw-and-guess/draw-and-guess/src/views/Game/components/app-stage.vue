<template>
  <el-card ref="wrapper" :body-style="{ padding: 0 }">
    <v-stage
        :config="stageConfig"
        @mousedown="mousedownHandler"
        @mouseup="mouseupHandler"
        @mousemove="mousemoveHandler"
    >
      <v-layer>
        <template v-if="this.question.patten === 'image'">
          <template v-for="conf in img_config">
            <v-image
                @transformend="handleTransformEnd"
                :config="conf" @dragstart="imgDragStart"
                @dragend="imgDragEnd"
            />
          </template>
        </template>

        <v-text
            v-else
            @dragstart="isDragging = true"
            @dragend="isDragging = false"
            :config="text_config"
        ></v-text>
        <v-line
            v-for="(line, index) in lines"
            :key="index"
            :config="line"
        />
        <v-transformer ref="transformer" v-if="!this.isLocked"/>

      </v-layer>
    </v-stage>
  </el-card>
</template>

<script>
import {mapGetters, mapState, mapActions} from 'vuex'
import {arrayBufferToBase64} from "../../../util";

export default {
  data() {
    return {
      // 画布配置
      stageConfig: {
        width: 800,
        height: 700,
      },
      // 绘画状态
      painting: false,
      strokeWidth: 2,

      isDragging: false,
      image: "",
    }


  },
  computed: {
    ...mapState(['lines', 'question', 'penColor']),
    ...mapGetters(['isGameStarted', 'isGameHolder', 'isLocked']),
    ...mapActions(['sendUpdateNewPos']),
    text_config() {
      return {
        text: this.question.content || "",
        x: 50,
        y: 50,
        name: 'text',
        fontSize: 64,
        draggable: !this.isLocked,
        fill: this.isDragging ? 'green' : 'black'
      }
    },
    img_config() {
      console.log("change")
      return this.question?.content?.map(img => {
        const image = new window.Image();
        if (img.data) {
          image.src = 'data:image/jpeg;base64,' + (arrayBufferToBase64(img.data));
        } else {
          image.src = "https://konvajs.org/assets/yoda.jpg";
        }
        return {
          image,
          draggable: !this.isLocked,
          ...img.config
        }
      })
    }
  },

  mounted() {
    // 将画布宽度设置与容器同宽
    this.stageConfig.width = this.$refs.wrapper.$el.offsetWidth;
  },

  methods: {
    // 鼠标按下
    mousedownHandler(e) {

      if (!this.isGameStarted)
        return
      if (!this.isLocked) {
        return;
      }

      this.painting = true
      // 创建一个新线条
      const newLine = {
        stroke: this.penColor,
        strokeWidth: this.strokeWidth,
        points: [e.evt.layerX, e.evt.layerY]
      }
      // 本地画线, 存到vuex中
      this.$store.commit('drawNewLine', newLine)
      // 请求服务器
      this.$store.dispatch('sendDrawNewLine', newLine)
    },

    // 鼠标拖动
    mousemoveHandler(e) {
      if (!this.painting) return
      const lastLine = this.lines[this.lines.length - 1]
      lastLine.points = lastLine.points.concat([e.evt.layerX, e.evt.layerY])
      this.$store.commit('updateNewLine', lastLine)
      // 请求服务器
      this.$store.dispatch('sendUpdateNewLine', lastLine)
    },

    // 鼠标释放
    mouseupHandler() {
      this.painting = false
    },
    imgDragStart(e) {
      this.selectedShapeName = e.target.name();
      this.updateTransformer();
      console.log(e.target._lastPos)
    },

    imgDragEnd(e) {
      this.beforeUpdatePos((base) => {
        const objPos = base;
        objPos.id = e.target.name();

        // update the state
        objPos.config.x = e.target._lastPos.x
        objPos.config.y = e.target._lastPos.y
        return objPos
      })
    },

    handleTransformEnd(e) {
      this.beforeUpdatePos((base) => {
        const objPos = base;
        objPos.id = e.target.name();

        // update the state
        objPos.config.x = e.target.x();
        objPos.config.y = e.target.y();
        objPos.config.rotation = e.target.rotation();
        objPos.config.scaleX = e.target.scaleX();
        objPos.config.scaleY = e.target.scaleY();
        return objPos
      })
    },

    // 更改图片，文字大小
    updateTransformer() {
      // here we need to manually attach or detach Transformer node
      const transformerNode = this.$refs.transformer.getNode();
      const stage = transformerNode.getStage();
      const {selectedShapeName} = this;

      const selectedNode = stage.findOne("." + selectedShapeName);
      // do nothing if selected node is already attached
      if (selectedNode === transformerNode.node()) {
        return;
      }

      if (selectedNode) {
        // attach to another node
        transformerNode.nodes([selectedNode]);
      } else {
        // remove transformer
        transformerNode.nodes([]);
      }
      console.log(transformerNode)
    },
    beforeUpdatePos(cb) {

      const objPos = cb({
        id: null,
        config: {}
      })

      this.$store.commit("transformElement", objPos)
      this.$store.dispatch("sendUpdateNewPos", objPos)
    }
  }
}
</script>
