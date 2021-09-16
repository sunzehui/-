msysgit是 windows版的Git,如下：
![图片描述](https://img.mukewang.com/59c1cfa400019aee02460029.jpg)
需要从网上下载一个，然后进行默认安装即可。安装完成后，在开始菜单里面找到 "Git --> Git Bash",如下：
![图片描述](https://img.mukewang.com/59c1cfd20001c2d602530073.jpg)
会弹出一个类似的命令窗口的东西，就说明Git安装成功。如下：
![图片描述](https://img.mukewang.com/59c1cfe70001462e06680380.jpg)

安装完成后，还需要最后一步设置，在命令行输入如下：

![图片描述](https://img.mukewang.com/59c1d041000110d906460213.jpg)
因为Git是分布式版本控制系统，所以需要填写用户名和邮箱作为一个标识。

注意：git config --global 参数，有了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置，当然你也可以对某个仓库指定的不同的用户名和邮箱。

```shell
git init	#通过命令 git init 把这个目录变成git可以管理的仓库
git add readme.txt	# 使用命令 git add readme.txt添加到暂存区里面去
git commit -m '我是注释'	# 用命令 git commit告诉Git，把文件提交到仓库。
git status	#git status来查看是否还有文件未提交
git diff readme.txt	# 我想看下readme.txt文件到底改了什么内容
git log	# git log命令显示从最近到最远的显示日志
git log --pretty=oneline #	每条日志显示一行
git reset --hard HEAD^	# 回退到上一个版本 ^^回退到上上个版本
git reset --hard HEAD~100	# 回退到前100个版本
git reset --hard 版本号	# 通过版本号回退
git reflog	# 获取到版本号
```

