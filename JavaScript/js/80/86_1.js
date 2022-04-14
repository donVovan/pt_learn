// ⋕js.Pm.Lp.FChT.1

'use strict';
let obj = {
	employee1: 100,
	employee2: 200,
	employee3: 300,
	employee4: 400,
	employee5: 500,
	employee6: 600,
	employee7: 700,
};
let wage = {};
for (let key in obj) {
    wage[key] = obj[key] + obj[key] * 0.1;
}
console.log(wage)