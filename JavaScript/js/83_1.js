'use strict';
let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14];
for (let i = 0; i < arr.length; i++) {
    arr[i] = arr[i] ** 2;
}

document.write(arr);