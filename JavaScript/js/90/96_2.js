// ⋕js.Pm.Md.MA.2
'use strict';
let arr = [[1, 2], [3, 4], [5, 6]];
let sum = 0;
for (let i of arr) {
    for (let j of i) {
        sum += j;
    }
}
document.write(sum)