var c = document.getElementById("canvas");
var currentColorDiv = document.getElementById("currentColor");
var colors = [];
colors.push(document.getElementById("white"));
colors.push(document.getElementById("gray"));
colors.push(document.getElementById("red"));
colors.push(document.getElementById("orange"));
colors.push(document.getElementById("yellow"));
colors.push(document.getElementById("green"));
colors.push(document.getElementById("lightblue"));
colors.push(document.getElementById("blue"));
colors.push(document.getElementById("purple"));
colors.push(document.getElementById("pink"));
colors.push(document.getElementById("brown"));
colors.push(document.getElementById("black"));
colors.push(document.getElementById("gray2"));
colors.push(document.getElementById("red2"));
colors.push(document.getElementById("orange2"));
colors.push(document.getElementById("yellow2"));
colors.push(document.getElementById("green2"));
colors.push(document.getElementById("lightblue2"));
colors.push(document.getElementById("blue2"));
colors.push(document.getElementById("purple2"));
colors.push(document.getElementById("pink2"));
colors.push(document.getElementById("brown2"));
for (var i = 0; i < colors.length; i++) {
  colors[i].addEventListener("click", function(){updateColor(this);});
}
var clear = document.getElementById("clear");
clear.addEventListener("click", function(){clean();});

var isDrawing = false;
var lastLine;
var currentColor = "black";


var updateColor = function(e) {
  currentColor = e.style.backgroundColor;
  currentColorDiv.style.backgroundColor = e.style.backgroundColor;
}

var draw = function(d) {
  isDrawing = d;
  if (isDrawing) {
      var line = document.createElementNS('http://www.w3.org/2000/svg','polyline');
      line.setAttribute('points', "");
      line.setAttribute('fill', "none");
      line.setAttribute('stroke', currentColor);
      line.setAttribute('stroke-width', "3");
      lastLine = line;
      c.appendChild(line);
      // var line = document.createElementNS('http://www.w3.org/2000/svg','line');
      // line.setAttribute('x1', event.offsetX);
      // line.setAttribute('y1', event.offsetX);
      // line.setAttribute('x2', event.offsetX+3);
      // line.setAttribute('y2', event.offsetX+3);
      // c.appendChild(line);
  }
  else {
    lastLine = null;
  }
};

var update = function(e) {
  // var n = new Date().getTime();
  if (lastLine) {
    var point = c.createSVGPoint();
    // var rect = e.currentTarget.getBoundingClientRect();
    // console.log(event.offsetX);
    // console.log(rect.top);
    point.x = event.offsetX;
    point.y = event.offsetY;
    lastLine.points.appendItem(point);
  }
};

var clean = function() {
  while (c.childElementCount > 0) {
    c.removeChild(c.children[0]);
  }
  lastLine = null;
};

c.addEventListener("mousedown", function(){draw(true);});
c.addEventListener("mousemove", function(e){if (isDrawing) update(e);});
window.addEventListener("mouseup", function(){draw(false); });
