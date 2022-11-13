var ctx;
var drawing = [];
var mstate;


function loadState()
{
    //-- fetch("base.json").then(response => response.json()).then(json => console.log(json));
    fetch('./base.json')
    .then((response) => response.json())
    .then((json) => console.log(json));
}

function loadImages() {
    drawing[0] = new Image;
    drawing[0].src = "./pics/crrt1.png"
    console.log(drawing[0])
    console.log("hhgg")
}

function butt1click()
{
    drawImages();
    loadState();
}

function Init()
{
    var canvas = document.getElementById("myCanvas");
    ctx = canvas.getContext("2d");

}

function refreshViewport() {
    Init();
    loadImages();
    hexagrid();
    drawImages();
}

function drawImages() {
    ctx.drawImage(drawing[0], 10, 10, 64, 64);
}

function hexagrid() {
    let cellsize = 100;
    let wallsize = 10;
    let cmw = cellsize - wallsize;
    for (let i = 0; i < 20; i++) {
        for (let j = 0; j < 20; j++) {
            let x = i * cellsize * 1.5;
            let y = j * cellsize * 0.86;
            ctx.beginPath();
            ctx.moveTo(x + 0.5 * cmw, y);
            ctx.lineTo(x + 0.25 * cmw, y + 0.43 * cmw);
            ctx.lineTo(x - 0.25 * cmw, y + 0.43 * cmw);
            ctx.lineTo(x - 0.5 * cmw, y);
            ctx.lineTo(x - 0.25 * cmw, y - 0.43 * cmw);
            ctx.lineTo(x + 0.25 * cmw, y - 0.43 * cmw);
            ctx.lineTo(x + 0.5 * cmw, y);
            ctx.stroke();

            x = (0.5 + i) * (cellsize) * 1.5;
            y = (0.5 + j) * (cellsize) * 0.86;
            ctx.beginPath();
            ctx.moveTo(x + 0.5 * cmw, y);
            ctx.lineTo(x + 0.25 * cmw, y + 0.43 * cmw);
            ctx.lineTo(x - 0.25 * cmw, y + 0.43 * cmw);
            ctx.lineTo(x - 0.5 * cmw, y);
            ctx.lineTo(x - 0.25 * cmw, y - 0.43 * cmw);
            ctx.lineTo(x + 0.25 * cmw, y - 0.43 * cmw);
            ctx.lineTo(x + 0.5 * cmw, y);
            ctx.stroke();

        }
    }
}