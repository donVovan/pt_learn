// ⋕js.Pm.Lp.Prm.10
'use strict';

let arr = [6, 55, 5, 38, 16, 153, 18, 3, -25, 100],
    sum = 0;

for (let elem of arr) {
    sum += elem;
}
document.write(sum / arr.length);