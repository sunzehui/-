<template>
  <div>
    <el-card
      class="login-card"
      :body-style="{ display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '60px'}"
    >
      <el-form ref="loginForm" inline :model="formData" :rules="rules">
        <el-form-item prop="nickname">
          <el-input v-model="formData.nickname" placeholder="请输入您的昵称" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="enterGame">进入游戏</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
// import socket from '@/socket/index'
import { MessageBox } from 'element-ui'

export default {
  data() {
    return {
      // 表单信息
      formData: {
        nickname: ''
      },

      // 校验规则
      rules: {
        nickname: [{ required: true, message: '请输入您的昵称' }]
      }
    }
  },

  methods: {
    enterGame() {
      // 测试 socket 模块, 发消息的能力
      // socket.emit('check_user_exist', this.formData.nickname, isExist => {
      //   console.log(isExist)
      // })

      this.$refs.loginForm.validate(async flag => {
        if (!flag) return
        const nickname = this.formData.nickname
        // 判断昵称是否已经被人使用 （发送消息问服务器）封装到vuex的action中
        const isExist = await this.$store.dispatch('checkUserExist', nickname)
        if (isExist) {
          MessageBox.alert('大哥，该昵称已经被人占用了！换个吧')
        } else {
          // 昵称可用
          localStorage.setItem('nickname', nickname)
          // 跳转到首页即可
          this.$router.push('/home')
        }
      })
    }
  }
}
</script>

<style scoped>
.login-card {
  width: 50%;
  margin: 0 auto;
  margin-top: 200px;
}
</style>
