export default {
    isGameStarted(state) {
        // 根据主持人是否存在, 判断游戏是否开始
        return !!state.holder
    },
    isGameHolder(state) {
        return state.nickname === state.holder
    },
    isLocked(state) {
        return state.locked
    }
}
