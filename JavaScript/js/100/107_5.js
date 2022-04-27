// ⋕js.Pm.SM.Prm.5
'use strict';

let str = 'var_test_text';

let words = str.split('_');
console.log(words);

for (let i = 0; i < words.length; i++) {
    words[i] = words[i].slice(0, 1).toUpperCase() + words[i].slice(1);
}

let result = words.join('');
document.write(result);
