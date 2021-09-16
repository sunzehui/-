---
title: webpack笔记
date: 2020-12-06 12:26:26
tags:
---
## webpack初探

```js
const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin');
const config = {
    // 入口文件路径
    entry:'./src/index.js',
    // 出口文件（生成目录）
    output:{
        path:path.resolve(__dirname,'dist'),
        filename:'main.js'
    },
    // 插件
    plugins:[
        new HtmlWebpackPlugin({
            template:'./src/index.html'
        })
    ]
}
module.exports = config;
```

- 文件路径不能有特殊符号
- 使用除js以外的文件格式需要装loader

## 引入css-loader && style-loader

```shell
npm install --save-dev style-loader css-loader
```

```js
// webpack.config.js
const config = {
    module:{
        rules:[
            {
                test: /\.css$/,
                use:[
                    'style-loader',
                    'css-loader'
                ]
            }
        ]
    }
}
// index.js
import './style.css'
```

- Can't resolve 'style.css'
  - 原：import 'style.css'
  - 应该为：import './style.css'
- 路径要加“ ./ ”


## 使用file-loader

```shell
npm install --save-dev file-loader
```

- 引入图片文件

```js
// webpack.config.js
const config = {
    module:{
        rules:[
            {
                test:/\.(png|svg|jpg|gif)$/,
                use:'file-loader'
            }
        ]
    }
}
```

- 引入字体文件

```js
// webpack.config.js
const config = {
    module:{
        rules:[
            {
                test: /\.(woff|woff2|eot|ttf|otf)$/,
                use:'file-loader'
            }
        ]
    }
}

// style.css
@font-face {
    font-family: 'myfont';
    src: url("./font.ttf");
    font-weight: 600;
    font-style: normal;
}
h1{
    font-family: myfont;
}
```





## 解析html中的img

```js
// webpack.config.js
const config = {
    module: {
        rules: [
            {
                test: /\.(png|svg|jpg|gif)$/,
                loader: 'url-loader',
                options: {
                    limit:8*1024,
                    name:'[name]-[hash:3].[ext]',
                    esModule:false,
                    outputPath:'imgs'
                }
            },
            {
                test: /\.(html)$/,
                use: {
                    loader: 'html-loader',
                }
            },
        ]
    }
}
```







## 配置webpack-dev-server

webpack5版本不兼容

解决方法：退到webpack4



```js
{
    "webpack": "^4.17.1",
    "webpack-cli": "^3.3.9",
    "webpack-dev-server": "^3.8.2",
    "webpack-hot-middleware": "^2.22.0",
    "webpack-merge": "^4.1.1"
}
```

package.json添加以上属性，执行

```shell
npm install
```



```js
// webpack.config.js
const config = {
    devServer: {
        contentBase:path.resolve(__dirname,'dist'),
        // 压缩
        compress:true,
        // 端口
        port:80,
        // 自动打开浏览器
        open:true

    }
}
```

