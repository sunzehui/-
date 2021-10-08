const express = require("express");
const router = express.Router();
const axios = require("axios");
// const corsOptions = {
//   origin: "http://localhost:3000", //只有localhost:3000可以访问
//   optionsSuccessStatus: 200,
// };
// const cors = require("cors");
router.get("/zhihu", async (req, res) => {
  const sentence = await axios.get(
    "https://www.zhihu.com/api/v4/clubs/1174735957173088256/checkin",
    {
      headers: {
        cookie: `_zap=b5c16f9e-4b63-4a4a-bea3-562a20c2f39e; d_c0="AICeTnM6ZhOPTtBORO3VcDD0NjMogwFhx3w=|1626057941"; __snaker__id=E0Fy3QcpvqwGO9yw; _9755xjdesxxd_=32; gdxidpyhxdE=4jU2jt7A0zl4JrDG%5CSZnZIRXf0%2BdjUsh2%2BV4dB7285sRuBPY0u6GCR7KLusPHTA53UySluVna%2FmlJxW5R%5CpoQ%5CUmoPpOr44LX83w0xz9dHW500yBpA3Z4gcZ%2BRSmlTtxmoOokXRv%2FO%2F34jVdgSHGxGyNx91MXu96RtsaRcRf9HoqDKIL%3A1626592994204; YD00517437729195%3AWM_NI=D%2F%2BTvje2khkAgzcDg8f%2BWXM36wK5S3mNhZPbqx8agEjnUYwwLbDGH9Ssf8aluLK8LWiRVY6JSt8XaOqvGLYZOd5WGY%2Bc9zlFUdTikxjpOoI8nT917wmhMHbveCv5bb17eDQ%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeabec7996b499d7c65df29e8bb2c15a838f9baaaa728eae8b87f66e9bec858df52af0fea7c3b92a88f1e5b5f562a7eea589ea4ba5a6ada5e634a6f599b9d039f6a985d6d239af92a8bbd36ab3a8f882e64faab29bbaf67d90be8ca8cb3391adaad9e468b79485d9cf5dab8e9abab54291acf8b9e445b3aa89addc528dbcfbb8c653e9bdf79bef4e97bc9c8aea74aab08190cc34ae8cf7d2b67dafb883a9e17ea79dbad6e16af3e9aba5d437e2a3; YD00517437729195%3AWM_TID=bva4Dsra3AFBAVAQFAMr2IvQK0aI8fxr; z_c0=Mi4xOVBDckNBQUFBQUFBZ0o1T2N6cG1FeGNBQUFCaEFsVk5aU0hoWVFDSVlNOEJnLTBKQTNmMzVMWjMycXpLNm10WExn|1626592101|43d4a13f948dbafabe7ac62fecb57387773ff046; _xsrf=ACLoR96ZStMu819ZIDQl7HHktJ5Zb0pf; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1631963670,1631964179,1632049538,1632050713; KLBRSID=ed2ad9934af8a1f80db52dcb08d13344|1632099232|1632099232`,
      },
    }
  );

  res.send(sentence.data);
  res.end();
});

module.exports = router;
