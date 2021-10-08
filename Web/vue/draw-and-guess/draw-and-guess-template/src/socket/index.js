import store from '@/store'
import { Notification } from 'element-ui'
import io from "socket.io-client"
const socket = io()

socket.on("connect", () => {
    store.commit("updateServerStatus",true)
})
socket.on("disconnect", () => {
    store.commit("updateServerStatus",false)
})
socket.on("room_info", ({nicknames,holder,lines}) => {
    store.commit("updateallPlayer",nicknames)
    store.commit("updateLines",lines)
    store.commit("updateHolder",holder)
})

socket.on("user_enter", (nickName) => {
    store.commit("dealUserEnter",nickName)
})

socket.on("game_started", (holder) => {
    store.commit("updateHolder",holder)
    Notification.success(`${holder}作为主持人，大家开始猜吧！`)
})
socket.on("already_started", (holder) => {
    store.commit("updateHolder",holder)
    Notification.success(`已经有人先于您了，${holder}作为主持人！`)
})


socket.on("user_enter", (nickName) => {
    store.commit("dealUserEnter",nickName)
})

socket.on("game_stoped", () => {
    store.commit("updateHolder",'')
    store.commit("updateLines",[])
    Notification.warning("主持人结束了游戏")
})


socket.on("starting_line", (line) => {
    store.commit("drawNewLine",line)
})
socket.on("updating_line", (line) => {
    store.commit("updateLastLine",line)
})


export default socket