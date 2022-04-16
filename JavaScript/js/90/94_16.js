// ⋕js.Pm.Lp.Mst.16
'use strict';

let obj = { a: 1, b: 2, c: 3 };
let sum = 0;

for (let key in obj) {
    sum += obj[key];
}

console.log(sum);