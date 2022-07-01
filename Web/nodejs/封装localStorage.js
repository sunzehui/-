class Storage {
    constructor(namespace) {
        // 命名空间：防止污染全局
        this.namespace = namespace
    }
    set(key, value) {
        // 这一步是将当前的命名空间里的数据都存到localStorage里
        let storage = wx.getStorageSync({key: this.namespace})
        // let stoarge = localStorage.getItem(this.namespace)
        if (!storage){
            // 没有数据默认空对象
            storage = {}
        }else{
            // 有数据就把原来的值转出来，修改参数指定的key的value
            storage = JSON.parse(stoarge)
        }
        storage[key] =  value
        // 将数据更新到localStorage
        wx.setStorageSync(this.namespace, storage)
        // localStorage.setItem(this.namespace,JSON.stringify(stoarge))
    }
    get(key,def) {
        // let storage = localStorage.getItem(this.namespace)
        let storage = wx.getStorageSync({key: this.namespace})
        // 获取不到数据就返回默认值
        if(!storage) return def
        // localStorage里存的是String
        storage = JSON.parse(storage)
        return storage[key]
    }
}