// ⋕js.Pm.Md.MAF.16
'use strict';
let arr = [];

for (let i = 0, k = 2; i < 4; i++) {
    arr[i] = [];

    for (let j = 0; j < 3; j++) {
        arr[i][j] = k;
        k += 2;
    }
}

console.log(arr);