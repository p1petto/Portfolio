'use strict';

let form = document.forms.card;
let add = document.getElementById('add');
let save = document.getElementById('save');
let cancel = document.getElementById('cancel');
let counter = 1;

add.addEventListener('click', function() {
    let card = document.getElementById('card')
    card.style.opacity = 1;
});

save.addEventListener('click', function() {
    let tasks = document.getElementById("list-of-task");

    let line = document.createElement('div');
    line.setAttribute('class', 'line');
    tasks.appendChild(line);

    let basic = document.createElement('div');
    basic.setAttribute('class', 'base');
    line.appendChild(basic);

    let checkbox = document.createElement('input');
    checkbox.setAttribute('type', 'checkbox');
    checkbox.setAttribute('name', 'complete');
    basic.appendChild(checkbox);

    if (form.priority.checked){
        let prioritySymbol = document.createElement('i');
        prioritySymbol.setAttribute('class', 'fa fa-bomb');
        basic.appendChild(prioritySymbol);
    }

    let titleTask = document.createElement('div');
    titleTask.setAttribute('class', 'numCheckbox');
    let description = form.elements.taskLabel
    if (description.value){
        titleTask.textContent = description.value;
    }
    else{
        titleTask.textContent = "Задача " + counter;
    }
    basic.appendChild(titleTask);

    let removal = document.createElement('button');
    removal.setAttribute('type', 'button');
    removal.setAttribute('class', 'button green');
    removal.onclick = function() { 
        line.remove();
    };
    line.appendChild(removal);

    let icon = document.createElement('i');
    icon.setAttribute('class', 'fa fa-trash');
    removal.appendChild(icon);

    counter += 1;
    clearForm();
});

cancel.addEventListener('click', function() {
    clearForm();
});

function clearForm(){
    form.reset();
    let card = document.getElementById('card')
    card.style.opacity = 0;
};

