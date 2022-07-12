/**
 * Todo List Version 1
 * 
 * Web Console (Developer Tools)
 */

// array
let tasks = [];
// string variable
let taskInput = '';

do {
    //prompt for input
    taskInput = prompt('Enter Task:');
    if (taskInput !== 'quit') {
        // insert input into array
        tasks.push(taskInput);
    }
}
while (taskInput !== 'quit');

// passing a function to a function. the second one is anonymous (lambda)
// for each task in tasks run -inject- the function and pass in that task (call it e)
tasks.forEach(function (e) {
    console.log(e);
});


/**
 * Loops
 */

// Traditional way for loop
// let total = 0;
// let elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// for (let i = 0; i < elements.length; i++) {
//     total += elements[i];
// }

// console.log(total);


// Not traditional way .forEach
// let total = 0;

// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].forEach(function (e) {
//     total += e;
// });

// console.log(total);