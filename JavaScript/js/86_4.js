// ⋕js.Pm.Lp.FChT.4

'use strict';

let obj = { 1: 6, 2: 7, 3: 8, 4: 9, 5: 10 };
let keySum = 0, elemSum = 0;

for (let key in obj) {
    keySum = Number(key) + keySum;
    elemSum = obj[key] + elemSum;
}
console.log(keySum / elemSum);