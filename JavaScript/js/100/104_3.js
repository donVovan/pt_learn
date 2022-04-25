// ⋕js.Pm.SM.Mth.3
'use strict';
let arr = [4, 2, 5, 19, 13, 0, 10];
let sum = 0;
for (let elem of arr) {
    sum += Math.pow(elem, 3);
}
document.write(Math.sqrt(sum));