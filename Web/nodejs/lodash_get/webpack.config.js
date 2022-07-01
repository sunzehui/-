const path = require('path')

const config = {
    mode: 'development',
    // 入口文件路径
    entry:'./src/index.ts',
    // 出口文件（生成目录）
    output:{
        path:path.resolve(__dirname,'output'),
        filename:'main.js'
    },
    resolve: {
        extensions: ['.ts', '.tsx', '.json', '.js']
    },
    externals : {
        axios: 'axios'
    },
    module: {
        rules: [
            {
                test:/\.js$/,
                //排除node_modules下的js文件
                exclude:/node_modules/,

                //单个loader用loader
            },
            {
                test: /\.tsx?$/,
                loader: "ts-loader",
                exclude: /node_modules/
            }
        ]
    }
}
module.exports = config;
