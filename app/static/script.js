var c = document.getElementById("canvas");
var currentColorDiv = document.getElementById("currentColor");
var header = document.getElementById("header");
var minutes = 3;
var seconds = 0;
setTimeout('tick()',1000);
var roundNumber = 1;
var colors = [];
var strokeWidth = 4;
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
currentColorDiv.setAttribute("style", "background-color:white");
colorcircle = document.createElementNS('http://www.w3.org/2000/svg','circle');
colorcircle.setAttribute("cx", 25);
colorcircle.setAttribute("cy", 25);
colorcircle.setAttribute("r", strokeWidth);
colorcircle.setAttribute("fill", currentColor);
colorcircle.setAttribute("stroke", "black")
currentColorDiv.appendChild(colorcircle);

var updateColor = function(e) {
  currentColor = e.style.backgroundColor;
  currentColorDiv.innerHTML = "";
  currentColorDiv.setAttribute("style", "background-color:white");
  colorcircle = document.createElementNS('http://www.w3.org/2000/svg','circle');
  colorcircle.setAttribute("cx", 25);
  colorcircle.setAttribute("cy", 25);
  colorcircle.setAttribute("r", (strokeWidth/2));
  colorcircle.setAttribute("fill", currentColor);
  colorcircle.setAttribute("stroke", "black")
  currentColorDiv.appendChild(colorcircle);
}

var changeWidth = function(e) {
  if(strokeWidth == 4){
    strokeWidth = 8;
  }
  else if(strokeWidth == 8){
    strokeWidth = 16;
  }
  else if(strokeWidth == 16){
    strokeWidth = 32;
  }
  else if(strokeWidth == 32){
    strokeWidth = 4;
  }
  currentColorDiv.innerHTML = "";
  currentColorDiv.setAttribute("style", "background-color:white");
  colorcircle = document.createElementNS('http://www.w3.org/2000/svg','circle');
  colorcircle.setAttribute("cx", 25);
  colorcircle.setAttribute("cy", 25);
  colorcircle.setAttribute("r", (strokeWidth/2));
  colorcircle.setAttribute("fill", currentColor);
  colorcircle.setAttribute("stroke", "black")
  currentColorDiv.appendChild(colorcircle);
}

currentColorDiv.addEventListener("click", changeWidth);

var draw = function(d) {
  isDrawing = d;
  if (isDrawing) {
      var line = document.createElementNS('http://www.w3.org/2000/svg','polyline');
      line.setAttribute('points', "");
      line.setAttribute('fill', "none");
      line.setAttribute('stroke', currentColor);
      line.setAttribute('stroke-width', strokeWidth);
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
    var rect = e.currentTarget.getBoundingClientRect();
    var x = e.clientX - rect.left; //x position within the element.
    var y = e.clientY - rect.top;  //y position within the element
    point.x = x;
    point.y = y;
    // console.log(e.currentTarget);
    lastLine.points.appendItem(point);
  }
};

var clean = function() {
  while (c.childElementCount > 0) {
    c.removeChild(c.children[0]);
  }
  lastLine = null;
};

var updateHeader = function(){
  header.innerHTML = "";
  if(seconds < 10){
    var time = document.createTextNode("Time Left  " + minutes + ":" + "0" + seconds);
  }
  else{
    var time = document.createTextNode("Time Left  " + minutes + ":" + seconds);
  }
  var players = document.createTextNode("Players: ")
  var roundNum = document.createTextNode("Round Number: " + roundNumber + "/" + "20")
  header.appendChild(time);
  header.appendChild(players);
  header.appendChild(roundNum);
}

var tick = function(){
  if(seconds == 0){
    minutes-=1;
    seconds = 60;
  }
  if(minutes<0){
    //it's next player's turn
    //pick a new word from wordlist
    clean()
  }
  else{
    seconds-=1;
    setTimeout('tick()',1000);
  }
  updateHeader();
}

c.addEventListener("mousedown", function(){draw(true);});
c.addEventListener("mousemove", function(e){if (isDrawing) update(e);});
window.addEventListener("mouseup", function(){draw(false); });
