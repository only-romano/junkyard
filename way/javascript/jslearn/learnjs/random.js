var peopleOn = [
{
    name:"Александра Хлебушкина",
    value: 1
},
{
    name: "Коля Пахомов",
    value: 2
},
{
    name: "Мария Пономарёва",
    value: 3
},
{
    name: "Ксения Депутат",
    value: 4
},
{
    name: "Серж Павук",
    value: 5
},
{
    name: "Реваз Ильющенко",
    value: 6
},
{
    name: "Михаил Шнюк",
    value: 7
},
{
    name: "Катерина Туманова",
    value: 8
},
{
    name: "Սամուել Ջոնսոն",
    value: 9
},
{
    name: "Dizzy Mekaar",
    value: 10
},
{
    name: "Мирослава Овсянникова",
    value: 11
},
{
    name: "Ксения Лермонтова",
    value: 12
},
{
    name: "Артём Триер",
    value: 13
},
{
    name: "Катерина Трубина",
    value: 14
},
{
    name: "Деймон Сальваторе",
    value: 15
},
{
    name: "Влада Аккермен",
    value: 16
},
{
    name: "Аня Смирнова",
    value: 17
},
{
    name: "Антон Коробейников",
    value: 18
},
{
    name: "Костя Беспрозванных",
    value: 19
},
{
    name: "Ульяна Лютая",
    value: 20
},
{
    name: "Cherry Blossom",
    value: 21
},
{
    name: "Катёнка Феликсова",
    value: 22
}
];

var peopleOff = [
{
    name:"Александра Хлебушкина",
    value: 1
},
{
    name: "Коля Пахомов",
    value: 2
},
{
    name: "Мария Пономарёва",
    value: 3
},
{
    name: "Ксения Депутат",
    value: 4
},
{
    name: "Серж Павук",
    value: 5
},
{
    name: "Реваз Ильющенко",
    value: 6
},
{
    name: "Михаил Шнюк",
    value: 7
},
{
    name: "Катерина Туманова",
    value: 8
},
{
    name: "Սամուել Ջոնսոն",
    value: 9
},
{
    name: "Dizzy Mekaar",
    value: 10
},
{
    name: "Мирослава Овсянникова",
    value: 11
},
{
    name: "Ксения Лермонтова",
    value: 12
},
{
    name: "Артём Триер",
    value: 13
},
{
    name: "Катерина Трубина",
    value: 14
},
{
    name: "Деймон Сальваторе",
    value: 15
},
{
    name: "Влада Аккермен",
    value: 16
},
{
    name: "Аня Смирнова",
    value: 17
},
{
    name: "Антон Коробейников",
    value: 18
},
{
    name: "Костя Беспрозванных",
    value: 19
},
{
    name: "Ульяна Лютая",
    value: 20
},
{
    name: "Cherry Blossom",
    value: 21
},
{
    name: "Катёнка Феликсова",
    value: 22
}
];

while (peopleOn.length) {
    var rand = ~~(peopleOn.length * Math.random());
    var first = peopleOn.splice(rand, 1)[0];
    rand = ~~(peopleOn.length * Math.random());
    var second = peopleOn.splice(rand, 1)[0];
    console.log(first.value + " : " + second.value);
}