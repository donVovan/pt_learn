'use strict';
let obj = { 'a': 12, 'b': 21, 'c': 13, 'd': 23, 'e': 17 };
let result = {};
for (let key in obj) {
    if (obj[key] >= 10 && obj[key] <= 20) {
        result[key] = obj[key];
    }
}
console.log(result);