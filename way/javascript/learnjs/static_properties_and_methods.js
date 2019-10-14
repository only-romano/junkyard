/*
function Article() {
  Article.count++;  // static property

  console.log( 'Article #' + Article.count );
}

Article.count = 0;
Article.DEFAULT_FORMAT = 'html';

Article.showCount = function() {  // static method
  console.log( 'Count of articles: ' + this.count );
}

new Article();
new Article();
Article.showCount();
console.log();


function Journal(date) {
  this.date = date;
  // ...

  this.getTitle = function() {  // нельзя сделать статическим, ибо в нём требуется property конкретного объекта this.date
    return 'Published in ' + Journal.formatDate(this.date);
  };

}

Journal.compare = function(journalA, journalB) {
  return (journalA.date > journalB.date) ? 1 : (journalA.date === journalB) ? 0 : -1;
};

Journal.formatDate = function(date) {
  return  date.getDate() + '.' + (date.getMonth() + 1) + '.' + date.getFullYear();
};


var journals = [
  new Journal(new Date(2012, 1, 1)),
  new Journal(new Date(2012, 0, 1)),
  new Journal(new Date(2011, 11, 1))
];


function findMin(journals) {
  var min = 0;

  for (var i = 0; i < journals.length; i++) {
    if (Journal.compare(journals[min], journals[i]) > 0) {
      min = i;
    }
  }

  return journals[min];
}

console.log( findMin(journals).getTitle() );
console.log( Journal.formatDate(new Date) );

var now = new Date();  // объект с текущей датой
var milliseconds = new Date(0);  //создаёт объект даты по колличеству миллисекунд (milliseconds)
var components = new Date(1990, 5, 17, 6);  // сщздаёт объект по компонентам - год, месяц, день, час ...
var string = new Date('2012-8-13 1:17');

console.log( now );
console.log( milliseconds );
console.log( components );
console.log( string );


var str = String.fromCharCode(65);  // создать строку из символа
console.log( str );
console.log();


function User(userData) {

  if (userData) {
    this.name = userData.name;
    this.age = userData.age;
  } else {
    this.name = 'Anonimous';
  }

  this.sayHi = function() {
    console.log( this.name + ', hi!' );
  };

}

var guest = new User();
guest.sayHi();

var someUser = new User({
  name: 'Vasily',
  age: 25
});

someUser.sayHi();
console.log();


function  FabricUser() {
  this.sayHi = function() {
    console.log( this.name + ', fabric hello.' );
  };
}

FabricUser.createAnonymous = function() {
  var user = new FabricUser;
  user.name = 'Anonimous';
  return user;
}

FabricUser.createFromData = function(userData) {
  var user = new FabricUser;
  user.name = userData.name;
  user.age = userData.age;
  return user;
}


var fabricGuest = FabricUser.createAnonymous();
fabricGuest.sayHi();

var fabricSomeUser = FabricUser.createFromData({
  name: 'Kato',
  age: 19
});
fabricSomeUser.sayHi();

*/

function Article() {
  this.created = new Date();

  if (!Article.counter) {
    Article.counter = 0;
  }
  Article.counter++;

  Article.lastDate = this.created;

  Article.showStats = function() {
    console.log( 'At all: ' + Article.counter + ',  Last date: ' + Article.lastDate.toString().slice(0, 24) );
  };
  // ...
}

new Article();
new Article();

Article.showStats();

new Article();
new Article();

Article.showStats();