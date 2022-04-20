// ⋕js.Pm.Md.MAF.24
'use strict';
let arr = [];

for (let i = 0, k = 1; i < 3; i++) {
    arr[i] = [];

    for (let j = 0; j < 3; j++, k++) {
        arr[i][j] = k;
    }
}

console.log(arr);