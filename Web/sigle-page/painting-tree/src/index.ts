const canvas = document.getElementById("myCanvas") as HTMLCanvasElement;
const ctx = canvas.getContext("2d");
const
    //  计算画布的宽度
    width = canvas.offsetWidth * 2,
    //  计算画布的高度
    height = canvas.offsetHeight * 2;


//  设置宽高
canvas.width = width;
canvas.height = height;

// Point类型
interface Point {
    x: number,
    y: number
}

function tree_plot(ctx: CanvasRenderingContext2D, p: Point, a: number, w: number, h: number, L: number) {
    // 出口
    if (L > 10) {
        return;
    }

    // 绘制一棵树
    const {x, y} = p;
    ctx.translate(x, y)
    ctx.rotate(a * Math.PI / 180)
    ctx.moveTo(-w / 2, 0)
    ctx.lineTo(-w * 0.65 / 2, -h)
    ctx.lineTo(w * 0.65 / 2, -h)
    ctx.moveTo(w / 2, 0)
    ctx.strokeStyle = "black";
    ctx.setTransform(1, 0, 0, 1, 0, 0)
    ctx.fill()

    // 递归下一个树枝
    const nextX = x + h * Math.sin(a * Math.PI / 180)
    const nextY = y - h * Math.cos(a * Math.PI / 180)
    tree_plot(ctx, {x: nextX, y: nextY}, a + 15, w * 0.65, h * 0.9, L + 1)
    tree_plot(ctx, {x: nextX, y: nextY}, a - 15, w * 0.65, h * 0.9, L + 1)
}


tree_plot(ctx, {x: width / 2, y: height}, 0, 30, 180, 0)