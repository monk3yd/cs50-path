/**
 * Todo List Version 2
 * 
 * DOM
 */

let textField = document.getElementById('textField');
let button = document.getElementById('taskButton');
let taskList = document.querySelector('#taskList');

button.onclick = function () {
    // create tag element <li>
    let newTask = document.createElement('LI');
    // stores field input in a variable called taskText
    let taskText = textField.value;
    // creates a node of text from taskText
    let taskTextNode = document.createTextNode(taskText);

    // creates a checkbox
    let checkbox = document.createElement('input');
    checkbox.type = 'checkbox';

    // closure : function that has access to the scope above it (variables).
    checkbox.onclick = function () {
        // access CSS
        newTask.setAttribute('style', 'text-decoration: line-through; opacity: 0;');

        // specify something happens (delete from <ul>) after 1 second.
        window.setTimeout(function () {
            // pass in <li> for deletionkk
            taskList.removeChild(newTask);
        }, 2000);
    }

    // adds for display
    newTask.appendChild(checkbox);
    newTask.appendChild(taskTextNode);
    taskList.appendChild(newTask);

    textField.value = '';
}