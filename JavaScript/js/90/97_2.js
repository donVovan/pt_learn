// ⋕js.Pm.Md.MAI.2
'use strict';
let arr = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]];
let sum = 0;
for (let i of arr) {
    for (let j of i) {
        for (let k of j) {
            sum += k;
        }
    }
}
document.write(sum)