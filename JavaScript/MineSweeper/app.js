'use strict';

let field = document.getElementById("field");
let button = document.getElementById('bt');
let size = 12;
let bombCount = document.getElementById('numOfBombs').value;
let matrix;
let isFirstStep = true;
let bombsxy=[];
let bombsBlocks=[];
let isPlay = true;



function getRandomFloat(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
};


button.addEventListener('click', function() {
    bombCount = document.getElementById("numOfBombs").value;
    isPlay = true;
    createField();
    bombsxy=[];
    bombsBlocks=[];
    focusX = 0;
    focusY = 0;
});


function createField(){
    let isFirstBlock = true;
    matrix = new Array(size).fill(0).map(() => new Array(size).fill(0));
    isFirstStep = true;
    while (field.firstChild) {
        field.removeChild(field.lastChild);
      }
    for (let i = 0; i < matrix.length; i++){
        let row = document.createElement('div');
        row.classList.add('field__row');
        field.appendChild(row);
        for (let j = 0; j < matrix.length; j++){
            let block =  document.createElement('div');
            block.addEventListener('click', step);
            block.addEventListener('contextmenu', setFlag);
            block.addEventListener('focus', test);
            block.setAttribute('dataIndex', i * size + j);
            // block.setAttribute('tabindex', i * size + j);
            block.classList.add('field__block');
            if (isFirstBlock){
                block.focus();
                isFirstBlock = false;
            }
            row.appendChild(block);
        }
    }
};

function test(event){
    return;
};

function setFlag(event){
    event.preventDefault();
    if (isPlay && !event.target.classList.contains("opened")){
        event.target.classList.toggle("marked");
        // console.log(event.target);
        return false;
    }
};

function setFlagByKey(x, y){
    let idx = getIndex(x, y);
    if (isPlay && !document.querySelector(`[dataIndex='${idx}']`).classList.contains("opened")){
        document.querySelector(`[dataIndex='${idx}']`).classList.toggle("marked");
        // console.log(event.target);
        return false;
    }
};

function step(event){
    if (isPlay){
        event.target.classList.add("opened");
        let idx = event.target.attributes[0].value;
        if (isFirstStep){
            isFirstStep = false;
            generateBombs();
        }
        let x = getPoints(idx)[0];
        let y = getPoints(idx)[1];
        openCells(x, y);
        if (isWin()) win();
    }
};

function stepByKey(x, y){
    if (isPlay){
        let idx = getIndex(x, y);
        document.querySelector(`[dataIndex='${idx}']`).classList.add("opened");
        if (isFirstStep){
            isFirstStep = false;
            generateBombs();
        }
        openCells(x, y);
        if (isWin()) win();
    }
};

function generateBombs(){
    let num = bombCount;
    while (num > 0){
        let x = getRandomFloat(0, size);
        let y = getRandomFloat(0, size);
        let idx = getIndex(x, y);
        if (document.querySelector(`[dataIndex='${idx}']`).classList.contains("opened") || matrix[x][y] == -2) {
            continue;
        }
        num--;
        matrix[x][y] = -2;
        bombsBlocks.push(getIndex(x,y));
        bombsxy.push([x,y]);
    }
    for (let i = 0; i < size; i++){
        for (let j = 0; j < size; j++){
            if (matrix[i][j] != -2) matrix[i][j] = getCountBombsAround(i, j);
        }
    }
};


function getCountBombsAround(x, y){
    let counter = 0;
    for (let i = -1; i <= 1; i++){
        for (let j = -1; j <= 1; j++)
            if (isInside(x + i) && isInside(y + j)){
                if (matrix[x + i][y + j] == -2){
                    counter++;
                }     
            }
            
    }
    return counter;
};


function isInside(a){
    return (a >= 0 && a < size);
};

function getPoints(idx){
    let x;
    let y;
    if (idx == 0){
        x = 0;
        y = 0;
    }
    else{
        x = Math.floor(idx / size);
        y = Math.floor(idx % size);
    }
    return [x, y];
};

function getIndex(x, y){
    return x * size + y;
};

function openCells(x, y){
    // return;

    if (x < 0 || x >= size || y < 0 || y >= size) return;

    if (matrix[x][y] == -2){
        gameOver();
        return;
    }

    if (matrix[x][y] == -1) return;

    let indx = getIndex(x, y);
    document.querySelector(`[dataIndex='${indx}']`).classList.remove("marked");

    if (matrix[x][y] >= 1 && matrix[x][y] <= 8){
        let idx = getIndex(x, y);
        document.querySelector(`[dataIndex='${idx}']`).classList.add("opened");
        document.querySelector(`[dataIndex='${idx}']`).textContent = matrix[x][y];
    }
    
    if (matrix[x][y] == 0){
        let idx = getIndex(x, y);
        document.querySelector(`[dataIndex='${idx}']`).classList.add("opened");
        
        matrix[x][y] = -1;


        openCells(x-1, y-1); openCells(x, y-1); openCells(x+1, y-1);
        openCells(x-1, y  );                    openCells(x+1, y  );
        openCells(x-1, y+1); openCells(x, y+1); openCells(x+1, y+1);
    }
    else return;
};

function gameOver(){
    for (let i = 0; i < bombsBlocks.length; i++){
        document.querySelector(`[dataIndex='${bombsBlocks[i]}']`).classList.add("bomb");
    }
    isPlay = false
    setTimeout(function(){
        alert("Вы проиграли")
    }, 300);
    
};

function isWin(){
    let countOpened = document.getElementsByClassName("opened").length;
    console.log(countOpened);
    if (countOpened == size*size - bombCount)
        return true;
    else return false;
};

function win(){
    isPlay = false
    setTimeout(function(){
        alert("Вы выиграли")
    }, 300);
}

let focusX = 0;
let focusY = 0;

document.addEventListener('keydown', e => {
    if (!matrix) return;
    let idx = getIndex(focusX, focusY);

    document.querySelector(`[dataIndex='${idx}']`).classList.remove("selected");

    
    if (e.code == 'Enter' && e.ctrlKey){
        setFlagByKey(focusX, focusY);
        return;
    }
    if (e.code == 'Enter'){
        stepByKey(focusX, focusY);
        return;
    }

    if (e.key == 'ArrowUp' && matrix[focusX-1])
        focusX--;
    else if (e.key == 'ArrowDown' && matrix[focusX+1])
        focusX++;
    else if (e.key == 'ArrowRight' && matrix[focusX][focusY+1] !== undefined)
        focusY++;
    else if (e.key == 'ArrowLeft' && matrix[focusX][focusY-1] !== undefined)
        focusY--;
    idx = getIndex(focusX, focusY);
    document.querySelector(`[dataIndex='${idx}']`).classList.add("selected");
  })