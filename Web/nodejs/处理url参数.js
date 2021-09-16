const url = "https://xxx.com/user?id=523666&page=favlist"
const reg = /[?&][^?&]+=[^?&]+/g
const found = url.match(reg)
const result = found.reduce((previousValue, currentValue) => {
    const obj = currentValue.substring(1).split("=")
    const key = obj[0]
    previousValue[key] = obj[1]
    return previousValue
},{})