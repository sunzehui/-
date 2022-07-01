const express = require("express");
// const { readFileSync } = require("fs");
// const { resolve } = require("path");
const bodyParser = require("body-parser");

const app = express();
app.unsubscribe(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

const api_router = require("./src/api");
app.use("/api", api_router);
app.get("/", (req, res) => {
  res.end("index");
});

app.listen(8_080, () => {
  console.log("running at http://localhost:8080");
});
