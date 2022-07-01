module.exports = {
  publicPath: "./",

  devServer: {
    proxy: {
      "/socket.io": {
        target: "http://localhost:3000",
        changeOrigin: true,
        ws: true
      }
    }
  },
  lintOnSave: false
};
