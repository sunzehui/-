<template>
  <el-card>
    <!-- 玩家列表 -->
    <div class="panel-area">
      <ul class="participants">
        <li v-for="item in playerList" :key="item.name">
          <span>{{item.name}}</span>
          <el-tag size="mini" v-if="item.isMe">我</el-tag>
          <el-tag size="mini" v-if="item.isHolder">主持</el-tag>
        </li>
      </ul>
    </div>

    <!-- 按钮工具栏 -->
    <div class="panel-area button-area">
      <el-button
        @click="startGameHandler"
      v-if="!isGameStarted"
        type="primary"
        size="small"
        icon="el-icon-edit"
      >主持游戏</el-button>

      <el-button
        v-if="isGameStarted && this.nickName === this.holder"
        @click="stopGameHandler"
        type="warning"
        size="small"
        icon="el-icon-delete"
      >终止游戏</el-button>

      <el-button
      
        v-if="isGameStarted && this.nickName !== this.holder"
        type="success"
        size="small"
        icon="el-icon-magic-stick"
      >猜答案</el-button>

      <el-button
        type="danger"
        size="small"
        icon="el-icon-switch-button"
      >退出游戏</el-button>
    </div>

    <!-- 弹出框：主持人设置答案 -->
    <el-dialog
      title="请设置答案"
      :visible.sync="resultDialogVisible"
      width="30%"
    >
      <el-input v-model="expectImageName" placeholder="请输入您的答案" />

      <span slot="footer" class="dialog-footer">
        <el-button @click="resultDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="saveDialogHandler">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 弹出框：答题人设置答案 -->
    <el-dialog
      title="请填写答案"
      :visible.sync="answerDialogVisible"
      width="30%"
    >
      <el-input v-model="inputImageName" placeholder="请输入您的答案" />

      <span slot="footer" class="dialog-footer">
        <el-button @click="answerDialogVisible = false">取 消</el-button>
        <el-button
          type="primary"
          @click="saveAnswerDialogHandler"
        >确 定</el-button>
      </span>
    </el-dialog>
  </el-card>
</template>

<script>
import {mapGetters, mapState} from 'vuex'
export default {
  data() {
    return {
      resultDialogVisible: false,
      expectImageName: '',
      answerDialogVisible: false,
      inputImageName: ''
    }
  },
  computed:{
    ...mapState(['allPlayer','nickName','holder']),
    ...mapGetters(['isGameStarted']),
    playerList(){
      const holder = this.holder
      const me = this.nickName
      return this.allPlayer.map(elem=>{
        return {
          name:elem,
          isMe:elem===me,
          isHolder:elem===holder
        }
      })  
    }
  },
  methods: {
    saveDialogHandler() {
      this.expectImageName === '' ||
        this.$store.dispatch("sendGameStart",this.expectImageName)
      this.resultDialogVisible=false
    },

    saveAnswerDialogHandler() {
    },

    startGameHandler(){

      this.resultDialogVisible = true
      this.expectImageName = ""
      
    },
    stopGameHandler(){
      this.$confirm("真的不玩了吗？","请问").then(()=>{
        this.$store.dispatch('sendGameStop')
      }).catch(e=>console.log)
    }
  }
}
</script>

<style lang="scss" scoped>
.panel-area {
  margin: 10px 0;
}
</style>
