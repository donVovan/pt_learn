// ⋕js.Pm.Md.MAF.17
'use strict';
let arr = [];
let m = 1;
for (let i = 0; i < 3; i++) {
    arr[i] = [];
    for (let j = 0; j < 3; j++) {
        arr[i][j] = []
        arr[i].push(arr[j])
        for (let k = 0; k < 5; k++) {
            arr[i][j].push(m)
            m++;
        }
    }
}
console.log(arr);