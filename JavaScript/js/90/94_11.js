// ⋕js.Pm.Lp.Mst.11
'use strict';

let arr = ['1', '2', '3', '4', '5'];
let sum = 0;

for (let i = 0; i < arr.length; i++) {
    sum += +arr[i];
}

console.log(sum); // почему-то выводит не 15