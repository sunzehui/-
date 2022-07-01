import "./css/reset.css"
import "./css/style.css"
import TabsController from "./tabs-controller"
import {panelObject} from "./interface/panel-object";


class Component_child extends HTMLElement {

    static get TAG_NAME() {
        return 'tab-panel';
    };

    constructor() {
        super();

    }
}

customElements.define(Component_child.TAG_NAME, Component_child);

class Component extends HTMLElement {
    private readonly shadow: ShadowRoot;

    static get TAG_NAME() {
        return 'tab-bar';
    };

    panels: Array<panelObject> = []

    constructor() {
        super();
        this.shadow = this.attachShadow({mode: 'open'})

        this.classList.add("tab")
        const style = document.createElement("style")
        style.innerHTML = `
        
.tab-bar {
    display: flex;
    height: var(--bar-height);
}
.tab-bar .bar {
    flex: 1;
    text-align: center;
    font-size: 1.5rem;
    padding: 1rem 0;
    cursor: pointer;
}

.bar.active {
    border-bottom: grey 2px solid;

}


.tab-content {
    height: calc(100% - var(--bar-height));
    width: 100%;
    position: relative;
}

.tab-content .content {
    height: 100%;
    width: 100%;
    opacity: 0;

    transition: none;

    /*visibility: hidden;*/
    position: absolute;
    font-size: 2rem;
    display: grid;
    place-items: center;
}

.tab-content .content.active {
    /*visibility: visible;*/
    opacity: 1;
    transition: opacity .3s ease-in-out;

}`
        this.shadow.appendChild(style)
        this.panels = this.collectPanels()
        const tab = new TabsController({
            panels: this.panels
        })
        this.layoutElement()

    }

    layoutElement() {
        const nodeFragment = document.createDocumentFragment();
        console.log(this.panels)

        const bars = document.createElement("div");
        bars.classList.add("tab-bar")

        const tabs = document.createElement("div");
        tabs.classList.add("tab-content")

        for (let obj of this.panels) {
            bars.appendChild(obj.nav)
            tabs.appendChild(obj.panel)
        }

        nodeFragment.appendChild(bars)
        nodeFragment.appendChild(tabs)
        this.shadow.appendChild(nodeFragment.cloneNode(true));
    }

    collectPanels() {
        const panels = []
        for (let child of this.children) {
            const t_nav = this.createNav(child.getAttribute("label"))
            const t_panel = this.createPanel(child.innerHTML);
            panels.push({
                nav: t_nav,
                panel: t_panel
            });
        }
        return panels;
    }

    createNav(content: string) {
        const nav = document.createElement("li");
        nav.setAttribute("class", "bar");
        nav.innerHTML = content
        return nav;
    }

    createPanel(content: string) {
        const panel = document.createElement("div");
        panel.setAttribute("class", "content");
        panel.innerHTML = content
        return panel;
    }
}

customElements.define(Component.TAG_NAME, Component);
