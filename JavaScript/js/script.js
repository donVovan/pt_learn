// ⋕js.Pm.Lp.OLF.6

'use strict';
let obj = { 1: "пн", 2: "вт", 3: "ср", 4: "чт", 5: "пт", 6: "сб", 7: "вс" };
let result = {};
for (let key in obj) {
    result[obj[key]] = key;
}
console.log(result);