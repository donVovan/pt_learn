// ⋕js.Pm.Lp.OLF.6

'use strict';

let obj = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 };
for (let key in obj) {
    obj[key] **= 2;
}
console.log(obj);