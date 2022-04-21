// ⋕js.Pm.Md.MSI.5
'use strict';
let data = {
    1: [
        'data11',
        'data12',
        'data13',
    ],
    2: [
        'data21',
        'data22',
        'data23',
    ],
    3: [
        'data31',
        'data32',
        'data33',
        'data34',
        'data35',
    ],
    4: [
        'data41',
        'data42',
    ],
};
for (let number in data) {
    for (let dt of data[number]) {
        document.write(dt + '<br>');
    }
}