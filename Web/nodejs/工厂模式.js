// 鼠标抽象类
class AbstructMouse{
    use(){}
}
// 键盘抽象类
class AbstructKeyboard{
    use(){}
}

class Mouse {
    use(){
        console.log('鼠标，真好用！')
    }
}
class Keyboard {
    use(){
        console.log('键盘，真好用！')
    }
}

// 华硕家的产品
class AsusMouse extends Mouse{
    constructor(name = '未知'){
        super()
        this.name = name
        console.log("Asus鼠标被造出来了,型号：",this.name)
    }
    use(){
        console.log("Asus产的鼠标，真好用！")
    }
}
class AsusKeyboard extends Keyboard{
    constructor(name = '未知'){
        super()
        this.name = name
        console.log("Asus键盘被造出来了,型号：",this.name)
    }
    use(){
        console.log("Asus产的键盘，真好用！")
    }
}

// 联想家的产品
class LenovoMouse extends Mouse{
    constructor(name = '未知'){
        super()
        this.name = name
        console.log("Lenovo鼠标被造出来了,型号：",this.name)
    }
    use(){
        console.log("Lenovo产的鼠标，真好用！")
    }
}
class LenovoKeyboard extends Keyboard{
    constructor(name = '未知'){
        super()
        this.name = name
        console.log("Lenovo键盘被造出来了,型号：",this.name)
    }
    use(){
        console.log("Lenovo产的键盘，真好用！")
    }
}

// 工厂抽象类
class AbstructPcFactor{
    constructor(){
    }
    createMouse(name){
        throw new Error("必须实现老子")
    }
    createKeyboard(name){
        throw new Error("未实现createKeyboard")
    }
}
class AsusFactor extends AbstructPcFactor{
    constructor(){
        super()
    }
    createMouse(name){
        return new AsusMouse(name)
    }
    createKeyboard(name){
        return new AsusKeyboard(name)
    }
}
class LenovoFactor extends AbstructPcFactor{
    constructor(){
        super()
    }
    createMouse(name){
        return new LenovoMouse(name)
    }
    createKeyboard(){
        return new LenovoKeyboard(name)
    }
}

// 用于创建工厂的类
class FactoryProducer{
    getFactor(type){
        switch(type.toLowerCase()){
            case 'asus':
                return new AsusFactor()
            case 'lenovo':
                return new LenovoFactor()
            default:
                return ''
        }
    }
}

const 华硕 = new FactoryProducer().getFactor('asus')
const 华硕家的鼠标 = 华硕.createMouse("华硕1号")
const 华硕家的鼠标 = 华硕.createKeyboard("华硕2号")
华硕家的鼠标.use()
const 联想 = new FactoryProducer().getFactor('lenovo')
const 联想家的鼠标 = 联想.createMouse("联想小新")
const 联想家的鼠标 = 联想.createKeyboard("联想小旧")
联想家的鼠标.use()