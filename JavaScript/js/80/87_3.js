// ⋕js.Pm.Lp.AEC.3
'use strict';
let str = 'Далеко-далеко за словесными горами в стране гласных и согласных живут рыбные тексты'
let count = {};
for (let elem of str) {
    if (count[elem] === undefined) {
        count[elem] = 1;
    } else {
        count[elem]++;
    }
}
console.log(count);