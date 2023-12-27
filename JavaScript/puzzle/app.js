'use strict';

const INWIDTH = 9;
const INHEIGHT = 6;
const SIZETILE = 50;

let pieces = document.getElementById("pieces");
let field = document.getElementById("field");
let container = document.getElementById("container");

(function create_pieces(){
    for (let i = 0; i < INHEIGHT; i++){
        for (let j = 0; j < INWIDTH; j++){
            let puzzle = document.createElement("div");
            puzzle.classList.add("puzzle")
            puzzle.style.backgroundPosition = `${-j * SIZETILE}px ${-i * SIZETILE}px`;
            puzzle.setAttribute('puzzleIndex', i * INWIDTH + j);
            puzzle.style.top = getRandomValue(50, 400) + "px";
            puzzle.style.left = getRandomValue(50, 400) + "px";
            pieces.appendChild(puzzle);
            puzzle.addEventListener('mousedown', DragnDrop);
            puzzle.addEventListener('ondragstart', onDragStart);
            puzzle.addEventListener('mouseup', putOnBlock);

            let blockField = document.createElement("div");
            blockField.classList.add("blockField")
            blockField.style.backgroundPosition = `${-j * SIZETILE}px ${-i * SIZETILE}px`;
            blockField.setAttribute('blockIndex', i * INWIDTH + j);
            field.appendChild(blockField);
        }
    }
})()


function DragnDrop(event){

    let limits = {
        top: container.offsetTop,
        right: container.offsetWidth + container.offsetLeft - event.target.offsetWidth,
        bottom: container.offsetHeight + container.offsetTop - event.target.offsetHeight,
        left: container.offsetLeft
    };


    let shiftX = event.clientX - event.target.getBoundingClientRect().left;
    let shiftY = event.clientY - event.target.getBoundingClientRect().top;
  
    event.target.style.position = 'absolute';
    event.target.style.zIndex = 1000;
    container.append(event.target);
  
    moveAt(event.pageX, event.pageY);
  
    function moveAt(pageX, pageY) {
        let newLocation = {
            x: limits.left,
            y: limits.top
        };

        if (pageX > limits.right){
            newLocation.x = limits.right;
        } else if (pageX > limits.left) {
            newLocation.x = pageX;
        }
        if (pageY > limits.bottom) {
          newLocation.y = limits.bottom;
        } else if (pageY > limits.top) {
          newLocation.y = pageY;
        }
        event.target.style.left = newLocation.x - shiftX + 'px';
        event.target.style.top = newLocation.y - shiftY + 'px';
    }
  
    function onMouseMove(event) {
      moveAt(event.pageX, event.pageY);
      
    }
  
    document.addEventListener('mousemove', onMouseMove);
  
    event.target.onmouseup = function() {
      document.removeEventListener('mousemove', onMouseMove);
      event.target.onmouseup = null;
    };
  
};

function onDragStart(event){
    return false;
}

function putOnBlock(event){
	let x = 0;
    let y = 0;
 
	if (event.pageX || event.pageY){
		x = event.pageX;
		y = event.pageY;
	} else if (event.clientX || event.clientY){
		x = event.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
		y = event.clientY + document.body.scrollTop + document.documentElement.scrollTop;
	}
    event.target.hidden = true;
    let elem = document.elementFromPoint(event.clientX, event.clientY);
    event.target.hidden = false;
    if (elem.classList.contains("blockField")){
        x = elem.getBoundingClientRect().left;
        y = elem.getBoundingClientRect().top;
        event.target.style.left = x + "px";
        event.target.style.top = y + "px";
    }
}

function getRandomValue(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
};

