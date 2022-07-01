export default {
    updateConnected(state, connected) {
        state.connected = connected
    },

    updateQuestion(state, question) {
        state.question = question;
    },
    updateNickname(state, nickname) {
        state.nickname = nickname || ''
    },
    updateNicknames(state, nicknames) {
        state.nicknames = nicknames || []
    },
    updateHolder(state, holder) {
        state.holder = holder || ''
    },
    updatePenColor(state, newColor) {
        state.penColor = newColor
    },
    updateLines(state, lines) {
        state.lines = lines || []
    },
    updateLockState(state, newState) {
        state.locked = newState
    },
    addToNicknames(state, nickname) {
        if (!state.nicknames.includes(nickname)) {
            state.nicknames.push(nickname)
        }
    },
    drawNewLine(state, newLine) {
        state.lines.push(newLine)
    },
    updateNewLine(state, lastLine) {
        const line = state.lines[state.lines.length - 1]
        line.points = lastLine.points
    },
    delFromNicknames(state, nickname) {
        state.nicknames = state.nicknames.filter(item => item !== nickname)
    },
    transformElement(state, newPos) {
        const id = newPos.id;
        const toUpdated = state.question.content
            .find((elem) => {
                return elem.config.name === id;
            })
        const _config = {}
        for (const [key] of Object.entries(newPos.config)) {
            if (key === "id") continue
            _config[key] = newPos.config[key]
        }
        toUpdated.config = Object.assign({}, toUpdated.config, _config)
        console.log("mutations:", toUpdated.config)

    }
}
