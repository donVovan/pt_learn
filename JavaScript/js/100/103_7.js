// ⋕js.Pm.Md.MSI.7
'use strict';
let data = [
    {
        1: [
            'data111',
            'data112',
            'data113',
        ],
        2: [
            'data121',
            'data122',
            'data123',
        ],
    },
    {
        1: [
            'data211',
            'data212',
            'data213',
        ],
        2: [
            'data221',
            'data222',
            'data223',
            'data224',
        ],
        3: [
            'data231',
            'data232',
            'data233',
            'data234',
            'data235',
        ],
    },
    {
        1: [
            'data411',
            'data412',
            'data413',
        ],
        2: [
            'data421',
        ],
    },
];
for (let obj of data) {
    for (let item in obj) {
        for (let dt of obj[item]) {
            document.write(dt + '<br>');
        }
    }
}