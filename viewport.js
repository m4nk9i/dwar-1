
function hexagrid()
{
var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
let cellsize=80
let wallsize=10;
let cmw=cellsize-wallsize;
for (let i=0;i<20;i++)
{
    for (let j=0;j<20;j++)
    {
        let x=i*cellsize*1.5;
        let y=j*cellsize*0.86;
        ctx.beginPath();
        ctx.moveTo(x+0.5*cmw,y);
        ctx.lineTo(x+0.25*cmw,y+0.43*cmw);
        ctx.lineTo(x-0.25*cmw,y+0.43*cmw);
        ctx.lineTo(x-0.5*cmw,y);
        ctx.lineTo(x-0.25*cmw,y-0.43*cmw);
        ctx.lineTo(x+0.25*cmw,y-0.43*cmw);
        ctx.lineTo(x+0.5*cmw,y);
        ctx.stroke();

        x=(0.5+i)*(cellsize)*1.5;
        y=(0.5+j)*(cellsize)*0.86;
        ctx.beginPath();
        ctx.moveTo(x+0.5*cmw,y);
        ctx.lineTo(x+0.25*cmw,y+0.43*cmw);
        ctx.lineTo(x-0.25*cmw,y+0.43*cmw);
        ctx.lineTo(x-0.5*cmw,y);
        ctx.lineTo(x-0.25*cmw,y-0.43*cmw);
        ctx.lineTo(x+0.25*cmw,y-0.43*cmw);
        ctx.lineTo(x+0.5*cmw,y);
        ctx.stroke();

    }
}
}