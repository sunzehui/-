import "./css/reset.css"
import "./css/style.css"
import EventEmitter from "events"

// 传入Tabs构造器：Option类型
interface Option {
    nav: string,
    panel: string,
    activeIndex?: number
}

// 自己手写了个选择题，勉强用
const $ = (selector: string) => Array.prototype.slice.call(document.querySelectorAll(selector)) as Array<HTMLElement>;


class Tabs {
    private readonly options: Option;
    private panels: Array<HTMLElement>;
    private navs: Array<HTMLElement>;
    private fromTab: number;
    event: EventEmitter;

    static defaultOptions = {
        activeIndex: 0
    }

    constructor(opt: Option) {
        this.options = Object.assign(Tabs.defaultOptions, opt);
        this.fromTab = this.options.activeIndex;
        // 向外开放切换事件
        this.event = new EventEmitter();

        this.init();
        this.bindEvent()
        this.switchTo(this.fromTab);
    }

    // 给节点加上标记，方便操作
    private init() {
        this.panels = $(this.options.panel)
        this.navs = $(this.options.nav)
        this.navs.forEach((elem, index) => {
            elem.dataset.index = String(index);
        })
        this.panels.forEach((elem, index) => {
            elem.dataset.index = String(index);
        })
    }

    // 给nav绑定点击事件
    private bindEvent() {
        this.navs.forEach(elem => {
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

const tab = new Tabs({
    nav: ".tab-bar .bar",
    panel: ".tab-content .content"
})
tab.event.on("change", (obj) => {
    console.log(obj)
})