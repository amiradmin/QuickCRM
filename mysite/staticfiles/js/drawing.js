var ctx = cnv.getContext('2d');
var cnvDispSizeW = 300;
var cnvDispSizeH = 300;
ctx.fillStyle = "white";
ctx.fillRect(0, 0, cnvDispSizeW, cnvDispSizeH);
var mDown = false;
var lastX = 0, lastY = 0;
var posConv = function(x, y) {
  return {
    x: cnv.width * x / cnvDispSizeW, 
    y: cnv.height * y / cnvDispSizeH
  }
};
cnv.onmousedown =  function(evt) {
  mDown = true;
  var mPos = posConv(evt.offsetX, evt.offsetY);
  draw(mPos.x, mPos.y);
}
cnv.onmouseup =  function(evt) {
  mDown = false;
  lastX = lastY = 0;
}
cnv.onmousemove = function(evt) {
  if(!mDown) return;
  var mPos = posConv(evt.offsetX, evt.offsetY);
  draw(mPos.x, mPos.y);
}

function draw(x, y) {
  if (mDown && lastX) {
    ctx.beginPath();
    ctx.strokeStyle = 'black';
    ctx.lineWidth = 1;
    ctx.lineJoin = 'round';
    ctx.moveTo(lastX, lastY);
    ctx.lineTo(x, y);
    ctx.closePath();
    ctx.stroke();
  }
  lastX = x; lastY = y;
}

btnImageLoad.onclick = function() {
  var img = new Image();
  img.onload = function() {
    var size = Math.max(img.naturalWidth, img.naturalHeight);
    cnv.width = size;
    cnv.height = size;
    ctx.drawImage(
      img, 
      (size - img.naturalWidth) / 2, 
      (size - img.naturalHeight) / 2, 
      img.naturalWidth, 
      img.naturalHeight
    );
    ctx.restore();
  }
  loadImage(img);
}
btnDownload.onclick = function(){
  if(cnv.toBlob) {
    cnv.toBlob(function(blob) {
      var url = URL.createObjectURL(blob);
      execDownload(url);
    }, 'image/jpeg', 1.0);
  } else {
    var url = cnv.toDataURL();
    execDownload(url);
  }
}

function execDownload(url) {
  var a = document.createElement('a');
  a.href = url;
  if(cnv.msToBlob) {
    var blob = cnv.msToBlob();
    window.navigator.msSaveBlob(blob, 'save.jpg');
  } else if(a.download === '') {
    a.download = 'sign.jpg';
    var evt = new MouseEvent('click', {view: window, bubbles: false});
    a.dispatchEvent(evt);
  } else if(navigator.userAgent.indexOf('Safari') > -1) {
    window.open(url, '_blank');
  }
}


function loadImage(img) {
  img.src = 'data:image/jpeg;base64,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'
}