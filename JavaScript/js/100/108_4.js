// ⋕js.Pm.SM.Mst.4
'use strict';

let num = 12345;
let arr = String(num).split('');

let sum = 0;
for (let digit of arr) {
    sum += Number(digit);
}

console.log(sum);
