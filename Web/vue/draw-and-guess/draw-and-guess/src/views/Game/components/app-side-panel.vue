<template>
  <el-card>
    <!-- 玩家列表 -->
    <div class="panel-area">
      <ul class="participants">
        <li v-for="item in nicknames" :key="item">
          <span>{{ item }} {{ item === nickname ? '（我）' : '' }}</span>
          <el-tag v-if="item === holder" size="mini">主持</el-tag>
        </li>
      </ul>
    </div>

    <!-- 按钮工具栏 -->
    <div class="panel-area button-area">
      <el-button
          v-if="!isGameStarted"
          type="primary"
          size="small"
          icon="el-icon-edit"
          @click="startGameHandler"
      >主持游戏
      </el-button>

      <el-button
          v-if="isGameStarted && nickname === holder"
          type="warning"
          size="small"
          icon="el-icon-delete"
          @click="stopGameHandler"
      >终止游戏
      </el-button>


      <el-button
          type="danger"
          size="small"
          icon="el-icon-switch-button"
          @click="exitHandler"
      >退出游戏
      </el-button>
    </div>

    <!-- 弹出框：主持人设置答案 -->
    <el-dialog
        title="请设置答案"
        :visible.sync="resultDialogVisible"
        width="420px"
    >
      <el-tabs v-model="patten" type="card" :stretch="true">
        <el-tab-pane label="文本" name="text">
          <el-input v-model="questionText"></el-input>
        </el-tab-pane>
        <el-tab-pane label="图片" name="image">
          <el-upload
              drag
              multiple
              :auto-upload="false"
              action="#"
              :file-list="fileList"
              :on-change="uploadImg">
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
            <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
          </el-upload>
        </el-tab-pane>
      </el-tabs>
      <span slot="footer" class="dialog-footer">
        <el-button @click="resultDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="saveDialogHandler">确 定</el-button>
      </span>
    </el-dialog>

  </el-card>
</template>

<script>
import {mapGetters, mapState} from 'vuex'
import {v4 as uuidv4} from 'uuid';

export default {
  data() {
    return {
      resultDialogVisible: false,

      patten: 'text',
      questionText: '',
      fileList: []
    }
  },

  computed: {
    ...mapState(['nickname', 'nicknames', 'holder']),
    ...mapGetters(['isGameStarted'])
  },

  methods: {
    uploadImg(f, fl) {
      this.fileList = fl
    },

    startGameHandler() {
      // 开始游戏
      // 1. 显示弹框
      this.resultDialogVisible = true
      // 2. 清空输入框内容
      this.questionText = ''
    },

    stopGameHandler() {
      this.$confirm('确定要终止游戏吗?', '温馨提示').then(() => {
        // 发送游戏终止申请
        this.$store.dispatch('sendStopGame')
      }).catch(e => {
        console.log(e)
      })
    },

    saveDialogHandler() {

      const question = {
        patten: this.patten
      }
      // 1. 判断输入类型
      if (this.patten === "text") {
        question.content = this.questionText
      } else {
        question.content = this.fileList.map(elem => ({
          data: elem.raw,
          config: {
            x: 10,
            y: 10,
            scaleX: 1,
            scaleY: 1,
            rotation: 0,
            name: uuidv4()
          }
        }))
      }


      // 2. 发送开始游戏的申请
      this.$store.dispatch('sendStartGame', question)

      // 3. 关闭弹框
      this.resultDialogVisible = false
    },


    exitHandler() {
      this.$confirm('是否退出游戏', '温馨提示').then(() => {
        this.$store.dispatch('sendUserLeave')
        this.$router.replace('/login')
      }).catch(e => {
        console.log(e)
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.panel-area {
  margin: 10px 0;
}

</style>
