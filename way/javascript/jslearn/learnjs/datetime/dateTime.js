/*
var now = new Date();
console.log( now, now.getFullYear(), now.getYear(), now.getMonth(), now.getDate() );

var jan02_1970 = new Date(3600 * 24 * 1000);
console.log( jan02_1970, jan02_1970.getHours(), jan02_1970.getMinutes() );

var date = new Date(2011, 0, 1, 2, 3, 4, 567);
console.log( date, date.getSeconds(), date.getMilliseconds(), date.getDay() );
console.log( now.getUTCHours(), now.getUTCSeconds(), now.getTime() );
console.log( now.getTimezoneOffset() );

date.setFullYear(2018); date.setMonth(2); date.setDate(16); date.setHours(13);
date.setMinutes(38); date.setSeconds(13); date.setMilliseconds(457);
console.log( date );

var newDate = new Date();
newDate.setTime(1521186004565);
console.log(newDate);

var d = new Date(2018, 1, 45);
console.log( d );
d.setDate(d.getDate() + 2);
console.log( d );
d = new Date();
d.setSeconds(d.getSeconds() + 70);
console.log( d );
d.setDate(1);
console.log( d );
d.setDate(0);
console.log( d );
d.setDate( -1 );
console.log( d, +d );

console.log( now - d );

var start = new Date;

var doSomething = 1
for (var i = 0; i < 100000; i++) {
    doSomething *= i;
}

var end = new Date;
console.log( (end - start) + "ms" );
var arr = [];
for (var i = 0; i < 1000; i++) arr[i] = i;

function walkIn(arr) {
    for (var key in arr) arr[key]++;
}

function walkLength(arr)  {
    for (var i = 0; i < arr.length; i++) arr[i]++;
}

function bench(f) {
    var date = new Date();
    for (var i = 0; i < 10000; i++) f(arr);
    return new Date() - date;
}

var timeIn = 0;
var timeLength = 0;

for (var i = 0; i < 100; i++) {
    timeIn += bench(walkIn);
    timeLength += bench(walkLength);
}

console.log( 'WalkIn time: ' + timeIn + 'ms' );
console.log( 'WalkLength time: ' + timeLength + 'ms' );

var arr = [];
for (var i = 0; i < 1000; i++) arr[i] = 0;

function walkIn(arr) {
    for (var key in arr) arr[key]++;
}

function walkLength(arr) {
    for (var i = 0; i < arr.length; i++) arr[i]++;
}

function bench(f) {
    for (var i = 0; i < 10000; i++) f(arr);
}

console.time("All Benchmarks");

console.time("walkIn");
bench(walkIn);
console.timeEnd("walkIn");

console.time("walkLength");
bench(walkLength);
console.timeEnd("walkLength");

console.timeEnd("All Benchmarks");


var date = new Date(2018, 2, 16, 15, 8, 0);

var options = {
    era: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    weekday: 'long',
    timezone: 'UTC+6',
    hour: 'numeric',
    minute: 'numeric',
    second: 'numeric'
};

console.log( date.toLocaleString("ru", options) );
console.log( date.toLocaleString("en-US", options) );


var d = new Date();
console.log( d.toString() );
console.log( d.toDateString() );
console.log( d.toUTCString() );
console.log( d.toISOString() );

var msUTC = Date.parse('2018-02-16T15:22:50.417Z');
var ms = Date.parse('2018-02-16T15:22:50.417-07:00');

console.log( msUTC, ms );

var msOld = Date.parse("March 16, 2018 15:24:50");
console.log( msOld );


console.time('slow date');
var msSlow = new Date();
console.timeEnd('slow date')


console.time('fast date');
var msFast = Date.now();
console.timeEnd ('fast date');

console.log( msSlow );
console.log( msFast );


var myDate = new Date(2012, 1, 20, 2, 12);
console.log( myDate.toUTCString() );


function getWeekDay(date) {
    return date.toString().slice(0, 2);
}

var date = new Date();
var testDate = new Date(2012, 0, 3);

console.log( getWeekDay(myDate), getWeekDay(date), getWeekDay(testDate) );


function getLocalDay(date) {
    var day = date.getDay();
    return day ? day : 7;
}

var sun = new Date(2012, 0, 1);

console.log( getLocalDay(myDate), getLocalDay(date), getLocalDay(testDate), getLocalDay(sun) );


function getDateAgo(date, days) {
    var newDate = new Date()
    newDate.setTime(0)
    newDate.setDate(1 + days);
    newDate = +newDate;

    var tempDate = +date;
    tempDate = tempDate - newDate;

    finalDate = new Date(0);
    finalDate.setTime(tempDate);
    return finalDate.getDate();
}

var date = new Date(2015, 0, 2);
console.log( getDateAgo(date, 1), getDateAgo(date, 2), getDateAgo(date, 365) );

function getLastDayOfMonth(year, month) {
    var date = (month + 1) < 12 ? new Date(year, month+1) : new Date(year+1, 0);
    date.setDate(0);
    return date.getDate();
}

console.log( getLastDayOfMonth(2012, 1), getLastDayOfMonth(2018, 2), getLastDayOfMonth(2017, 1) );


function getSecondsToday() {
    var date = arguments[0] || new Date();
    return date.getHours() * 60 * 60 + date.getMinutes() * 60 + date.getSeconds();
}

var date = new Date(2011, 0, 1, 2, 3, 4, 567);
console.log( getSecondsToday(), getSecondsToday(date) );


function getSecondsToTomorrow() {
    var date = arguments[0] || new Date();
    return 86400 - (date.getHours() * 60 * 60 + date.getMinutes() * 60 + date.getSeconds());
}

console.log( getSecondsToTomorrow(), getSecondsToTomorrow(date) );


function formatDate(date) {
    var formattedDate = '';
    formattedDate += date.getDate().toString().length > 1 ? date.getDate() + '.' : '0' + date.getDate() + '.';
    formattedDate += (date.getMonth() + 1).toString().length > 1 ? (date.getMonth() + 1) + '.' : '0' + (date.getMonth() + 1) + '.'
    formattedDate += date.getFullYear().toString().slice(2);
    return formattedDate;
}

var d = new Date(2014, 0, 30);
console.log( formatDate(d), formatDate(date) );


function relativeFormatDate(date) {
    var diff = +(new Date()) - +date;
    if ( diff < 1000 ) return 'it was right now';
    if ( diff < 60000 ) return 'it was ' + Math.floor(diff/1000) + ' seconds ago';
    if ( diff < 3600000 ) return 'it was ' + Math.floor(diff/60000) + ' minutes ago';
    var hours = date.getHours().toString();
    var minutes = date.getMinutes().toString();
    var format = formatDate(date) + '  ';
    format += hours.length > 1 ? hours + ':' : '0' + hours + ':';
    format += minutes.length > 1 ? minutes : '0' + minutes;
    return format;
}

console.log( relativeFormatDate(new Date(new Date - 1)) );
console.log( relativeFormatDate(new Date(new Date - 30 * 1000)) );
console.log( relativeFormatDate(new Date(new Date - 5 * 60 * 1000)) );
console.log( relativeFormatDate(new Date(new Date - 86400000)) );

*/

function formatDateSome(date) {
    var diff = (new Date() - date) / 1000;
    return diff < 1 ? 'it was right now' :
      diff < 60 ? 'it was ' + Math.floor(diff) + ' seconds ago' :
      diff < 3600 ? 'it was ' + Math.floor(diff / 60) + ' minutes ago' :
      date.toLocaleString(undefined, { day: '2-digit' }) + '.' +
      date.toLocaleString(undefined, { month: '2-digit' }) + '.' +
      date.toLocaleString(undefined, { year: '2-digit' }) + '  ' +
      date.toLocaleString(undefined, {
        hour: '2-digit',
        minute: '2-digit'
      });
}

console.log( formatDateSome(new Date(new Date - 1)) );
console.log( formatDateSome(new Date(new Date - 30 * 1000)) );
console.log( formatDateSome(new Date(new Date - 5 * 60 * 1000)) );
console.log( formatDateSome(new Date(new Date - 86400000)) );