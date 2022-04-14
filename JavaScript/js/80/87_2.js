// ⋕js.Pm.Lp.AEC.2
'use strict';
let arr = [1, 2, 3, 2, 4, 3, 5, 6, 3, 2, 3];
let two = 0, three = 0, counter = 0;
// немного не понял условие задачи, но:

for (let elem of arr) {
    // считаем отдельно каждую цифру отдельно
    if (elem == 2) {
        two++;
    };
    if (elem == 3) {
        three++;
    };

    // или все вместе
    if (elem == 2 || elem == 3) {
        counter++;
    }

}
console.log(two, three);
console.log(counter);