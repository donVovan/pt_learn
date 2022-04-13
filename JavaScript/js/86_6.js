// ⋕js.Pm.Lp.FChT.6
'use strict';
let obj = {
    1: 125,
    2: 225,
    3: 128,
    4: 356,
    5: 145,
    6: 281,
    7: 452,
};
let arr = [];

for (let key in obj) {
    if (obj[key] > 99 && obj[key] < 300) {
        arr.push(obj[key]);
    }
}
console.log(arr);