# 简介

界面使用 Element UI，工程化框架使用 Vue, 全局状态管理 Vuex

后端使用 Node.js, 使用 WebSocket 实现长连接，使用 Socket.io 简化前后端交互操作

## 项目结构

文件夹 `wecheck`是客户端，使用 yarn 生成的工程化项目

文件夹`wecheck-server`是服务端，使用 node 搭建的 WebSocket 服务器

## 项目愿景

实现多人在线同时做题，由提问者发出问题截图，多位作答者进入房间做题，并且全员所看到的界面同步显示。

更进一步，可以开很多房间，不仅仅是交流学术问题，可以交流诸如

- 我新买的包好不好看？
- 这个 手机/电脑 怎么样？
- 有没有要跟我处对象的？

## 启动方法

前端：

```sh
cd wecheck
yarn
yarn serve
```

后端：

```sh
cd wecheck-server
yarn
yarn start
```



### 额外说明

如遇到安装依赖缓慢，请换淘宝镜像源

```bash
yarn config set registry https://registry.npm.taobao.org/
```

