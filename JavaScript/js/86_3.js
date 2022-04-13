// ⋕js.Pm.Lp.FChT.3

'use strict';

let arr1 = [1, 2, 3, 4, 5];
let arr2 = [6, 7, 8, 9, 10];
let obj = {};

for (let i = 0, j = 0; i < arr1.length, j < arr2.length; i++, j++) {
    obj[arr1[i]] = arr2[j];
}
console.log(obj)