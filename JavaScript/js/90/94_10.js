// ⋕js.Pm.Lp.Mst.10
'use strict';

let arr = ['1', '2', '3', '4', '5'];
let sum = 0;

for (let i = 0; i <= arr.length; i++) {
    sum += +i;
}

console.log(sum); // почему-то выводит NaN