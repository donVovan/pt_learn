// ⋕js.Pm.Md.MAF.3
'use strict';
let arr = [];
for (let i = 0; i < 3; i++) {
    arr[i] = [];
    for (let j = 0; j < 2; j++) {
        arr[i][j] = []
        arr[i].push(arr[j])
        for (let k = 0; k < 5; k++) {
            arr[i][j].push(k + 1)
        }
    }
}
console.log(arr);