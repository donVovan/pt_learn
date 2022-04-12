'use strict';
let arr = [6, 55, -38, 16, 153, 18, 3, -25, 100];
let result = [];
for (let elem of arr) {
    if (elem >= 0) {
        result.push(elem);
    }
}
document.write(result);

