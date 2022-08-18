const http = require("http");
const express = require("express");
const app = express();
const server = http.createServer(app);
//设置跨域访问
app.all("*", function (req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "X-Requested-With");
  res.header("Access-Control-Allow-Methods", "PUT,POST,GET,DELETE,OPTIONS");
  res.header("X-Powered-By", " 3.2.1");
  res.header("Content-Type", "application/json;charset=utf-8");
  next();
});
require("./rest")(app);
require("./websocket")(server);

server.listen(3000, () => {
  console.log("listening on *:3000");
});
