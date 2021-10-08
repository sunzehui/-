import Vue from 'vue'
import Vuex from 'vuex'
import socket from '../socket'

Vue.use(Vuex)

const state = {
  connected: false, // 连接状态
  nickname: '', // 当前用户昵称
  nicknames: [], // 房间用户列表
  holder: '', // 游戏主持
  lines: [] // 房间的绘图信息（记录画了多少根线，怎么画的）
}

const mutations = {
  updateNickname(state, nickname) {
    state.nickname = nickname || ''
  },
  updateNicknames(state, nicknames) {
    state.nicknames = nicknames || []
  },
  updateHolder(state, holder) {
    state.holder = holder || ''
  },
  updateLines(state, lines) {
    state.lines = lines || []
  },
  // 将新人，追加到昵称列表中去
  addToNicknames(state, nickname) {
    // 用户不存在，才追加
    if (!state.nicknames.includes(nickname)) {
      state.nicknames.push(nickname)
    }
  },
  // 更新connected状态
  updateConnected(state, flag) {
    state.connected = flag
  },

  // 画新线
  drawNewLine(state, newLine) {
    state.lines.push(newLine)
  },

  // 鼠标滑动，更新线
  updateNewLine(state, lastLine) {
    // 更新vuex中最后一项的points即可
    const line = state.lines[state.lines.length - 1]
    line.points = lastLine.points
  },

  delFromNicknames(state, nickname) {
    state.nicknames = state.nicknames.filter(item => item !== nickname)
  }
}

const actions = {
  // 确认昵称是否占用
  checkUserExist(context, nickname) {
    // 拿到异步操作的结果，需要promise封装了
    return new Promise((resolve, reject) => {
      socket.emit('check_user_exist', nickname, isExist => {
        resolve(isExist)
      })
    })
  },
  // 一进入房间，发消息告诉服务器，我来了
  sendUserEnter(context) {
    const nickname = localStorage.getItem('nickname')
    // 发送消息到服务器
    socket.emit('enter', nickname)
    // 进入房间了, 将nickname设置到vuex中
    context.commit('updateNickname', nickname)
  },

  // 告诉服务器，开始游戏啦，申请主持人
  sendStartGame(context, answer) {
    // 发消息， 通知到服务器
    socket.emit('start_game', answer)
  },

  // 终止游戏 - 发消息
  sendStopGame(context) {
    socket.emit('stop_game')
  },

  sendDrawNewLine(context, line) {
    socket.emit('new_line', line)
  },
  sendUpdateNewLine(context, line) {
    socket.emit('update_line', line)
  },
  sendAnswerGame(context, inputImageName) {
    socket.emit('answer_game', inputImageName)
  },

  sendUserLeave(context) {
    // 发送退出的消息
    socket.emit('leave')
    // 都退出了，本地的昵称等重置了
    context.commit('updateNickname', '')
    localStorage.removeItem('nickname')
  }
}

const getters = {
  // 标记游戏是否开始
  isGameStarted() {
    return !!state.holder
  },
  isGameHolder(state) {
    return state.nickname === state.holder
  }
}

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters
})
