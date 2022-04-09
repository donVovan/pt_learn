'use strict';
//let arr = ['a', 'b', 'c', 'd', 'e'];
//let result = 0;
//let arr = [10, 20, 30, 50, 4, 235, 3000, 7]
let week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
let currentDay = new Date().getDay() - 1;
for (let i = 0; i < week.length; i++) {
    if (i < 5 && i != currentDay) {
        document.write(week[i] + '<br>');
    } else if (i == currentDay && i < 5) {
        document.write('<i>' + week[i] + '</i>' + '<br>');
    } else if (i >= 5 && i != currentDay) {
        document.write('<b>' + week[i] + '</b>' + '<br>');
    } else {
        document.write('<i><b>' + week[i] + '</b></i>' + '<br>');
    }
}

let monthes = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
let currentMonth = new Date().getMonth();
let arr = [1, 2, 3, 4, 5];
for (let i = 0; i < 12; i++) {
    if (i != currentMonth) {
        document.write(monthes[i] + '<br>');
    } else {
        document.write('<i>' + monthes[i] + '</i>' + '<br>');
    }
};


//document.write(day.getDay());
console.log();