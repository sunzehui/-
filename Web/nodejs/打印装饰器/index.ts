function createWorker(f: Function) {
    var blob = new Blob(['(' + f.toString() + ')()']);
    var url = window.URL.createObjectURL(blob);
    var worker = new Worker(url);
    return worker;
}
const interval = createWorker(function () {
    self.onmessage = function (e) {
        console.log("recived:", e);

    }
    let i = 0;
    setInterval(function () {
        self.postMessage(i++);
    }, 1000);
})
interval.onmessage = function (e) {
    console.log(e.data);
}
interval.postMessage("aoligei")
