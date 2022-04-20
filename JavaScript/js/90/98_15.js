// ⋕js.Pm.Md.MAF.15
'use strict';
let arr = [];

for (let i = 0, k = 1; i < 4; i++) {
    arr[i] = [];

    for (let j = 0; j < 2; j++, k++) {
        arr[i][j] = k;
    }
}

console.log(arr);