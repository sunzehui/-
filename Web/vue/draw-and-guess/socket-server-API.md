# 你画我猜【乞丐版】Socket.IO API



## 客户端发送事件：

| 事件名           | 参数                           | 功能                                                         |
| ---------------- | ------------------------------ | ------------------------------------------------------------ |
| check_user_exist | 参数1：nickname<br>回调isExist | 检查用户昵称是否在房间中已存在                               |
| enter            | 字符串：nickname               | 进入游戏房间；服务端响应 room_info、广播 user_enter 事件     |
| leave            |                                | 离开游戏房间；服务端广播 user_leave 事件                     |
| start_game       | 字符串：imageName              | 作为主持人开始游戏，并设置游戏的答案；<br/>已有主持人时服务端广播 already_started，<br/>否则全局广播 game_started 事件 |
| stop_game        |                                | 终止游戏；服务端广播 game_stoped 事件                        |
| answer_game      | 字符串：answer                 | 作为游戏参与者，猜游戏的答案；服务端广播 game_answered 事件  |
| new_line         | 对象：line                     | 开始绘制一条新的线条；服务端广播 starting_line 事件          |
| update_line      | 对象：line                     | 持续的更新当前的线条；服务端广播 updating_line 事件          |



## 客户端接收事件：

| 事件名          | 参数                                             | 功能                                                         |
| --------------- | ------------------------------------------------ | ------------------------------------------------------------ |
| connect         |                                                  | 与服务器的连接已建立                                         |
| disconnect      |                                                  | 与服务器的连接已断开                                         |
| room_info       | 对象：{ nicknames, holder, lines }               | 获取游戏房间的当前信息                                       |
| user_enter      | 字符串：nickname                                 | 有玩家进入了房间                                             |
| user_leave      | 字符串：nickname                                 | 有玩家离开了房间                                             |
| already_started | 字符串：holder                                   | 当几个玩家同时抢主持人时，<br/>提示游戏已经开始，即房间中已经有游戏主持人了 |
| game_started    | 字符串：holder                                   | 游戏开始，即某玩家称为主持人                                 |
| game_stoped     |                                                  | 主持人终止了游戏                                             |
| game_answered   | 对象：{ alreadyDone, success, nickname, answer } | 玩家猜答案后的反馈信息                                       |
| starting_line   | 对象：line                                       | 主持人开始绘制一条新的线条                                   |
| updating_line   | 对象：line                                       | 主持人正在持续绘制当前线条                                   |

