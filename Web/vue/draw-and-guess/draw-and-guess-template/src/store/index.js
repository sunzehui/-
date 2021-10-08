import Vue from 'vue'
import Vuex from 'vuex'
import socket from '@/socket/index'

Vue.use(Vuex)

const state = {
  connected:false,
  nickName: '',
  allPlayer: [],
  holder: '',
  lines: []
}

const mutations = {
  updateNickname(state, nickName) {
    state.nickName = nickName || ''
  }, 
  updateallPlayer(state, players) {
    state.allPlayer = players || []
  }, 
  updateHolder(state, holder) {
    state.holder = holder || ''
    console.log(holder)
  }, 
  updateLines(state, lines) {
    state.lines = lines || []
  },
  dealUserEnter(state,nickName){
    const allPlayer = state.allPlayer
    allPlayer.every(name=>name!==nickName) &&
      state.allPlayer.push(nickName)
    // allPlayer.includes(nickName)||state.allPlayer.push(nickName)
  },
  updateServerStatus(state,ServerStatus){
    state.connected = ServerStatus
  },
  drawNewLine(state,newline){
    state.lines.push(newline)
  },
  updateLastLine(state,lastline){
    let last_now = state.lines[state.lines.length - 1]
    console.log(state.lines)
    last_now.points = lastline.points
  }
}

const actions = {
  checkNameExist(context, nickName) {
    return new Promise((resolve, reject) => {
      socket.emit("check_user_exist", nickName, (isExist) => {
        resolve(Boolean(isExist))
      })
    })
  },
  sendUserEnter(context) {
    const nickName = localStorage.getItem("nickName")
    socket.emit("enter", nickName)
    context.commit("updateNickname", nickName)
  },
  sendGameStart(context,answer){
    socket.emit('start_game',answer)
  },
  sendGameStop(context,answer){
    socket.emit('stop_game')
  },
  sendDrawNewLine(context,newline){
    socket.emit('new_line',newline)
  },
  sendUpdateLastLine(context,lastline){
    socket.emit('update_line',lastline)
  }
}

const getters = {
  isGameStarted(){
    return !!state.holder
  },
  isGameHolder(){
    return state.holder === state.nickName
  },
}

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters
})
