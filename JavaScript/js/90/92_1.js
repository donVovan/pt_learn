// ⋕js.Pm.Lp.Cdg.1
'use strict';

let arr = [10, 20, 30, 40, 21, 32, 51], sum = 0;
for (let elem of arr) {
    if (elem > 9 && elem < 30) {
        sum += elem;
    }
}
console.log(sum);