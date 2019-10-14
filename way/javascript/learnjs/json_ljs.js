var numbers = [0, 1, 2, 3, 4, 5];
var object = {
    "name": "Vasily",
    "age": 35,
    "isAdmin": false,
    "friends": [0,1,2,3]
};

var jsonNum = JSON.stringify(numbers);
var jsonObj = JSON.stringify(object);

console.dir( jsonNum );
console.dir( JSON.parse(jsonNum) );
console.dir( jsonObj );
console.dir( JSON.parse(jsonObj) );

var incorrectObject = {
    name: "Vasily",       // incorrect - name ; to correct - "name"
    "surname": 'Petrov',  // incorrect - 'Petrov' ; to correct - "Petrov"
    "age": 35,
    "isAdmin": true,
    // comments are also incorrect
    "friends": [0, 1, 2, 3, 4]
}

var jsonIncorrectObj = JSON.stringify(incorrectObject);
console.dir( incorrectObject );
console.dir( jsonIncorrectObj );
console.dir( JSON.parse(jsonIncorrectObj) );

var str = '{"title":"Conference","date":"2014-11-30T12:00:00.000Z"}';
var event = JSON.parse(str, function(key, value) {
  return key == 'date' ? new Date(value) : value;
});

console.dir( event );
console.dir( event.date.toLocaleString() );


var schedule = '{ \
  "events": [ \
    {"title":"Conference", "date":"2014-11-30T12:00:00.000Z"}, \
    {"title":"Birthday Day", "date":"2015-04-18T12:00:00.000Z"} \
  ]\
}';

var jsonSchedule = JSON.parse(schedule, function(key, value) {
  return key == 'date' ? new Date(value) : value;
});

console.dir( jsonSchedule.events[1].date.getDate() );


var newEvent = {
  title: "Conference",
  date: "Today"
};

var newStr = JSON.stringify(newEvent);
console.dir( newStr );
console.dir( JSON.parse(newStr) );

function some() {}


var room = {
  number: 23,
  function: function() {
    console.log( this.number );
  },
  toJSON: function() {
    return this;
  }
};

var roomEvent = {
  title: "Conference",
  date: new Date(Date.UTC(2014, 0, 1)),
  room: room
};

console.dir( JSON.stringify(roomEvent) );


var userVasily = {
  name: 'Vasily',
  age: 25,
  window: 'some big & cycled propperty as window'
};

console.dir( JSON.stringify(userVasily, ["name", "age"]) );

var strUserVasily = JSON.stringify( userVasily, function(key, value) {
  return key == 'window' ? undefined : value;
})
console.log( strUserVasily );


var userBigVasily = {
  name: "Vasily",
  age: 25,
  roles: {
    isAdmin: false,
    isEditor: true
  }
};

console.log( JSON.stringify(userBigVasily, "", 2) );


var leader = {
  name: "Vasily Ivanovich",
  age: 35
};

var jsonLeader = JSON.stringify(leader, "", 2);
console.log(jsonLeader);

console.dir(JSON.parse(jsonLeader));


var newLeader = {
  name: 'Vasily Ivanovich',
  id: 12
};

var coLider = {
  name: 'Petka',
  id: 51
};


newLeader.coLiderId = 51;
coLider.newLeaderId = 12;

var team = {12: newLeader, 51: coLider};

console.dir( JSON.stringify(team) );