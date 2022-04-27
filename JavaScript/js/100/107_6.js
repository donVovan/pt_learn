// ⋕js.Pm.SM.Prm.6
'use strict';

let str = 'var_test_text';

let words = str.split('_');
console.log(words);

for (let i = 1; i < words.length; i++) {
    words[i] = words[i].slice(0, 1).toUpperCase() + words[i].slice(1);
}

let result = words.join('');
document.write(result);
