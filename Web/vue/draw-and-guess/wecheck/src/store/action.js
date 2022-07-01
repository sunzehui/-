import socket from '@/socket'

export default {
    // 确认用户名是否存在
    checkUserExist(context, nickname) {
        return new Promise((resolve, reject) => {
            socket.emit('check_user_exist', nickname, isExist => {
                resolve(isExist)
            })
        })
    },
    // 进入房间
    sendUserEnter(context) {
        const nickname = localStorage.getItem('nickname')
        socket.emit('enter', nickname)
        context.commit('updateNickname', nickname)
    },
    // 开始游戏申请
    sendStartGame(context, question) {
        socket.emit('start_game', question)
    },
    // 结束游戏申请
    sendStopGame(context) {
        socket.emit('stop_game')
    },
    // 画新线
    sendDrawNewLine(context, newLine) {
        socket.emit('new_line', newLine)
    },
    // 更新线条
    sendUpdateNewLine(context, lastLine) {
        socket.emit('update_line', lastLine)
    },

    // 更新控件位置
    sendUpdateNewPos(context, newPos) {
        socket.emit('update_box_pos', newPos)
    },

    sendUserLeave(context) {
        socket.emit('leave')
        context.commit('updateNickname', '')
        localStorage.removeItem('nickname')
    }
}
