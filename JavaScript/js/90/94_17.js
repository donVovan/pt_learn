// ⋕js.Pm.Lp.Mst.17
'use strict';

let arr = [1, 2, 3, 4, 5];
let res = '';

for (let elem of arr) {

    if (elem === 3) {
        res = '+++';
        break;
    } else {
        res = '---';

    }
}

console.log(res);