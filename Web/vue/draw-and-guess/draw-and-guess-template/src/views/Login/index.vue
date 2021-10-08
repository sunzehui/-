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
import {MessageBox} from "element-ui"

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
      this.$refs.loginForm.validate(async (flag)=>{
        if(!flag) return false;
        const {nickname} = this.formData;
        const isExist = await this.$store.dispatch("checkNameExist",nickname)
        console.log(isExist)
        
        isExist && MessageBox.alert("已经有小伙伴叫这个了，换一个吧！")
        localStorage.setItem('nickName',nickname);
        isExist || this.$router.push("/home")
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
