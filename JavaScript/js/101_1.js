// ⋕js.Pm.Md.VK.1
'use strict';
let months = {
    'ru': [
        'январь',
        'февраль',
        'март',
        'апрель',
        'май',
        'июнь',
        'июль',
        'август',
        'сентябрь',
        'октябрь',
        'ноябрь',
        'декабрь',
    ],
    'en': [
        'january',
        'february',
        'march',
        'april',
        'may',
        'june',
        'july',
        'august',
        'september',
        'october',
        'november',
        'december',
    ],
};
let lang = 'ru'; // может быть или 'ru' или 'en'
let month = 5;   // число от 0 до 11

document.write(months['ru'][5]);