import io from 'socket.io-client'
import store from '@/store'
import {MessageBox, Notification} from 'element-ui'

const env = process.env.NODE_ENV
const url = env === 'development' ?'localhost:3000':"0.0.0.0:3000"
const socket = io(url,{
  'Access-Control-Allow-Credentials':true
});

socket.on('connect', () => {
    console.log('>>>>>>> 和服务器已建立连接')
})


// 自己进入房间, 监听room_info事件, 获取房间信息
socket.on('room_info', ({nicknames, holder, lines, question}) => {
    store.commit('updateNicknames', nicknames)
    store.commit('updateHolder', holder)
    store.commit('updateLines', lines)
    console.log(question)
    store.commit("updateQuestion", question)
})

// 别人进入房间, 监听user_enter事件, 获取进入房间的用户信息
socket.on('user_enter', nickname => {
    store.commit('addToNicknames', nickname)
})

// 处理服务连接
socket.on('connect', () => {
    store.commit('updateConnected', true)
})

// 处理服务失去连接
socket.on('disconnect', () => {
    store.commit('updateConnected', false)
})

// 处理游戏开始
socket.on('game_started', room_info => {
    store.commit('updateHolder', room_info.holder)
    store.commit('updateQuestion', room_info.question)

    Notification.success(`${room_info.holder} 作为主持人开始了新游戏，大家可以开始踊跃猜答案啦！`)
})

// 处理游戏已经开始, 不能重复开始
socket.on('already_started', holder => {
    store.commit('updateHolder', holder)
    MessageBox.alert('当前已有游戏在进行中，主持人是：' + holder)
})


// 处理终止游戏
socket.on('game_stoped', () => {
    // 1. 清理相关数据
    store.commit('updateHolder', '')
    store.commit('updateLines', [])
    store.commit('updateQuestion', {})

    // 2. 弹出提示消息
    Notification.warning('主持人终止了当前游戏')
})

// 监听新线的绘制
socket.on('starting_line', newLine => {
    store.commit('drawNewLine', newLine)
})

// 监听线的更新
socket.on('updating_line', lastLine => {
    store.commit('updateNewLine', lastLine)
})
socket.on("box_pos_updated", newPos => {
    store.commit("transformElement", newPos)
})

socket.on('user_leave', nickname => {
    store.commit('delFromNicknames', nickname)

    if (nickname === store.state.holder) {
        store.commit('updateHolder', '')
        store.commit('updateLines', [])
        store.commit('updateQuestion', {})
        Notification.error('主持人离开了游戏!')
    }
})

export default socket
