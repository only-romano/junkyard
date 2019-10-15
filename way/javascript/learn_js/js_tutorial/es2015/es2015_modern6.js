'use strict';
console.time();

let map = new Map();
  map.set('1', 'str1');
  map.set(1, 'num1').set(true, 'bool1');
console.log( map.get(1), map.get('1'), map.size,  map);

let handyMap = new Map([
  ['1', 'str1'],
  [1, 'num1'],
  [true, 'bool1']
]);
console.log( handyMap.get(1), handyMap.get('1'), handyMap.size,  handyMap);

let mapUser = { name: 'vasily' };
let visitsCountMap = new Map( [[mapUser, 123]] );
console.log( visitsCountMap.get(mapUser) );

  map.delete(1);
  map.delete('1');
  handyMap.clear();
console.log( map, handyMap, visitsCountMap.has(mapUser) );

let string = '';
let recipeMap = new Map([
  ['pickles', '500 gr'],
  ['tomatos', '350 gr'],
  ['creamy', '50 gr']
]);

  for (let fruit of recipeMap.keys()) string += fruit + ' ';
console.log( string, string = '' );
  for (let amount of recipeMap.values()) string += amount + ' ';
console.log( string, string = '' );
  for (let amount of recipeMap) string += amount + ' ';
console.log( string, string = '' );

  recipeMap.forEach( (value, key, map) => { console.log( `${key}: ${value}`); } );

let set = new Set();
let vasya = {name: 'Vasily'};
let petya = {name: 'Petro'};
let dasha = {name: 'Daria'};
  set.add(vasya).add(petya).add(dasha).add(vasya).add(petya);
console.log( set.size, set, set.delete(petya), set.has(dasha), set.size );
  set.forEach( user => console.log(user.name) );

let fruits = new Set(["oranges", 'apples', 'bannanas']);
  for (let value of fruits) string += value + ' ';
console.log( string, string = '' );

let activeUsers = [
  {name: 'Vasya'},
  {name: 'Petya'},
  {name: 'Maria'},
];
let weakMap = new WeakMap();
  weakMap.set(activeUsers[0], 1).set(activeUsers[1], 2).set(activeUsers[2], 3);
  // weakMap.set('Katya', 4)  - TypeError - 'Katya' is not non-null object;
console.log( weakMap.get(activeUsers[0]) );
activeUsers.splice(0, 1);
activeUsers.splice(0, 1);
console.log( weakMap.get(activeUsers[0]) );


console.timeEnd();