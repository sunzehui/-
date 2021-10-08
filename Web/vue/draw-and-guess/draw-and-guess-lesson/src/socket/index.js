import io from 'socket.io-client'
import store from '@/store'
import { Notification, MessageBox } from 'element-ui'

// 模块的作用： 收发消息
// 创建连接 io(地址)
const socket = io()

// 进行连接建立的监听
socket.on('connect', () => {
  console.log('和服务器已建立连接...')
})

// 监听room_info收消息
socket.on('room_info', ({ nicknames, holder, lines }) => {
  // console.log(nicknames, holder, lines)
  store.commit('updateNicknames', nicknames)
  store.commit('updateHolder', holder)
  store.commit('updateLines', lines)
})

// 监听user_enter, 通知：有新人进房间了
socket.on('user_enter', nickname => {
  // nickname，就是进入房间玩家的名字 (小王)
  store.commit('addToNicknames', nickname)
})

// 监听socket的连接，为了控制按钮
socket.on('connect', () => {
  store.commit('updateConnected', true)
})

// 监听socket的断开，为了控制按钮
socket.on('disconnect', () => {
  store.commit('updateConnected', false)
})

// 处理游戏成功开始
socket.on('game_started', holder => {
  store.commit('updateHolder', holder)
  Notification.success(`${holder} 作为主持人，已经成功开始了游戏，大家可以开始猜答案啦！`)
})

// 你去抢麦，没抢过，告诉你谁抢到了，谁组织了这个游戏
// 处理游戏已经开始， 但是不能重复开始的
socket.on('already_started', holder => {
  store.commit('updateHolder', holder)
  Notification.alert(`当前游戏已经进行中辣，主持人是 ${holder}`)
})

// 监听游戏的终止, 重置信息
socket.on('game_stoped', () => {
  // 1. 清除相关的数据 nickname nicknames holder lines
  store.commit('updateHolder', '')
  store.commit('updateLines', [])

  // 2. 弹出提示消息
  Notification.warning('主持人终止了当前的游戏')
})

// 监听线的开始绘制
socket.on('starting_line', line => {
  store.commit('drawNewLine', line)
})
// 监视线的持续绘制
socket.on('updating_line', line => {
  store.commit('updateNewLine', line)
})

// 监听猜答案的结果
socket.on('game_answered', ({ alreadyDone, success, nickname, answer }) => {
  // 处理已经答对的情况
  if (alreadyDone) {
    MessageBox.alert('当前答案已经被人猜中啦，您不能再猜了')
    return
  }

  // 处理没答对
  if (!success) {
    Notification.error(`玩家 ${nickname} 猜的答案不对！ ${answer}`)
    return
  }

  // 现在没有其他人答对，就他答对了
  MessageBox.alert(`玩家 ${nickname} 猜中了正确的答案: ${answer}`)
})

socket.on('user_leave', nickname => {
  // 将离开的人，从vuex nicknames中移除该项
  store.commit('delFromNicknames', nickname)

  // 其他人退出，没有任何问题，主持人如果退出了，做提示，主持人离开了，并清空信息
  if (nickname === store.state.holder) {
    store.commit('updateHolder', '')
    store.commit('updateLines', [])
    Notification.error('主持人离开了游戏！')
  }
})

// 将来便于其他模块使用socket对象，去发消息
export default socket
