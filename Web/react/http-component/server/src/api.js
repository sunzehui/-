const express = require("express");
const router = express.Router();
const axios = require("axios");
const corsOptions = {
  origin: "http://localhost:3000", //只有localhost:3000可以访问
  optionsSuccessStatus: 200,
};
const cors = require("cors");
router.get("/zhihu", cors(corsOptions), async (req, res) => {
  const sentence = await axios.get(
    "https://www.zhihu.com/api/v4/clubs/1174735957173088256/checkin",
    {
      headers: {
        cookie: `不给看，自己去抓`,
      },
    }
  );

  res.send(sentence.data);
  res.end();
});

module.exports = router;
