# 你画我猜 [ 乞丐版 ]

![image-20210527160841324](./你画我猜笔记/images/image-20210527160841324.png)

## 技术架构

- Vue + VueRouter +  **Vuex(核心)**

  作用: 便于多组件通信, 页面这里为了避免交叉操作, 页面组件只和 vuex 交互

- **Socket.IO (核心)**

  负责客户端 和 服务端交互, 将服务端拿到的数据存入 Vuex Store 中

- Konva （基于Canvas的绘图库）

  插件, 辅助开发



## 启动服务器

`draw-server` 服务器目录

```bash
- 安装依赖
  yarn
  
- 启动接口
  yarn start
```



## 启动项目

`draw-and-guess` 完整代码目录

```txt
- 安装依赖
  yarn
  
- 启动项目
  yarn serve
```



## 开发实战

`draw-and-guess-template` 静态结构代码目录