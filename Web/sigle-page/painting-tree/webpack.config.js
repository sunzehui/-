const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin');
const {CleanWebpackPlugin} = require("clean-webpack-plugin")
const config = {
    // 模式 ： production 生产模式；development：开发模式
    'mode':'development',
    // 入口文件路径
    entry: './src/index.ts',
    // 出口文件（生成目录）
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'js/bundle.js'
    },
    // 插件
    plugins: [
        new HtmlWebpackPlugin({
            template: './src/index.html'
        }),
        new CleanWebpackPlugin()
    ],
    resolve: {
        extensions: ['.ts', '.tsx', '.json', '.js']
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use:[
                    'style-loader',
                    'css-loader'
                ]
            },
            {
                test: /\.(png|svg|jpg|gif)$/,
                loader: 'url-loader',
                options: {
                    // 大于8kb，不生成base64
                    limit:8*1024,
                    name:'[name]-[hash:3].[ext]',
                    esModule:false,
                    outputPath:'imgs'
                }
            },
            {
                test: /\.(woff|svg|eot|ttf)\??.*$/,
                loader: 'file-loader',
                options: {
                    name:'[name]-[hash:3].[ext]',
                    outputPath:'font'
                }
            },
            {
                test: /\.(html)$/,
                use: {
                    loader: 'html-loader',
                }
            },
            {
                test: /\.tsx?$/,
                loader: "ts-loader"
            }
        ]
    },
    devServer: {
        contentBase:path.resolve(__dirname,'dist'),
        // 压缩
        compress:true,
        // 端口
        port:3000,
        // 自动打开浏览器
        open:true

    }
}
module.exports = config;
