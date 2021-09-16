const obj = {
    foo: false,
    bar: true,
    foobar: 1,
    star: undefined,
    arr: [
        1, 0, false, '', true, null
    ]
}

function compactObject(obj) {
    // 检查传来的对象是不是数组，是数组就直接filter，不是就继续
    const data = Array.isArray(obj) ? obj.filter(Boolean) : obj
    // 将对象的key列成数组使用reduce
    return Object.keys(data).reduce((acc, cur) => {
        if (data[cur]) {
            // 当前值为真，判断当前的值是不是对象，是就继续递归
            acc[cur] = typeof data[cur] === 'object' ? compactObject(data[cur]) : data[cur]
        }
        return acc
        // 判断初始值类型
    }, data instanceof Array ? [] : {})
}

console.log(JSON.stringify(compactObject(obj),null,2));