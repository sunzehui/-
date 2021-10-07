import EventEmitter from "events"
import {panelObject} from "./interface/panel-object";


// 传入Tabs构造器：Option类型
interface Option {
    panels: Array<panelObject>
    activeIndex?:
        number
}

// 自己手写了个选择题，勉强用
const $ = (selector: string) => Array.prototype.slice.call(document.querySelectorAll(selector)) as Array<HTMLElement>;


export default class TabsController {
    private readonly options: Option;
    private panels: Array<HTMLElement>;
    private navs: Array<HTMLElement>;
    private fromTab: number;
    event: EventEmitter;

    static defaultOptions = {
        activeIndex: 0
    }

    constructor(opt: Option) {
        this.options = Object.assign(TabsController.defaultOptions, opt);
        this.fromTab = this.options.activeIndex;
        // 向外开放切换事件
        this.event = new EventEmitter();

        this.init();
        this.bindEvent()
        this.switchTo(this.fromTab);
    }

    // 给节点加上标记，方便操作
    private init() {
        this.panels = this.options.panels.map(item => item.panel)
        this.navs = this.options.panels.map(item => item.nav)
        // debugger
        this.navs.forEach((elem, index) => {
            console.log(elem)
            elem.dataset.index = String(index);
        })
        this.panels.forEach((elem, index) => {
            elem.dataset.index = String(index);
        })
        console.log(this.panels, this.navs)
    }

    // 给nav绑定点击事件
    private bindEvent() {
        this.navs.forEach(elem => {
            console.log(elem)
            debugger
            elem.onclick = () => {
                this.switchTo(+elem.dataset.index);
            }
        })
    }

    // 切换nav操作
    private switchNav(index: number) {
        // 记录上一次点击的nav下标，将其移出active，下同
        this.navs[this.fromTab].classList.remove("active")
        this.navs[index].classList.add("active")
    }

    // 切换panel操作
    private switchPanel(index: number) {
        this.panels[this.fromTab].classList.remove("active");
        this.panels[index].classList.add("active");
    }

    // 切换tab
    private switchTo(toIndex: number) {
        this.switchNav(toIndex);
        this.switchPanel(toIndex);
        this.event.emit("change", {
            toIndex, fromIndex: this.fromTab
        })
        // 更新上一次点击的下标
        this.fromTab = toIndex;
    }
}




