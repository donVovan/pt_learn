// ⋕js.Pm.SM.Prm.4
'use strict';

let str = 'word1 word2 word3';

let words = str.split(' ');
console.log(words);

for (let i = 0; i < words.length; i++) {
	words[i] = words[i].slice(0, 1).toUpperCase() + words[i].slice(1);
}

let result = words.join(' ');
document.write(result);
