// ⋕js.Pm.Lp.FiNb.2
'use strict';

let nl = 0, one = 1, two = 2;

for (let i = 1; i <= 10; i++) {
    let current = nl + one + two;
    nl = one;
    one = two;
    two = current;
    console.log(current);
}



