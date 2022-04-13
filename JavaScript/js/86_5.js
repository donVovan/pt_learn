// ⋕js.Pm.Lp.FChT.5

'use strict';

let obj = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }, keys = [], elements = [];

for (let key in obj) {
    keys.push(key);
    elements.push(obj[key]);
}
console.log(keys);
console.log(elements);