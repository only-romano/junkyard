'use strict';
let kittyInterval = null;  // интервал выпадения котят
let counter = 1;	   // количество уже выпавших котят


// Добавляет котёнка в дождик из котят
function addKitty() {
	let vapp = document.getElementById("vApp");
	if (vapp && counter < 200) {
		vapp.appendChild(createKitten());
		counter++;
	}
}


// Создаёт и возвращает готового div-котёнка с фразой и изображением
function createKitten() {	
	let kitten = document.createElement("div");
		kitten.classList.add("kitty-img");

		if (counter % 50 === 0) {// каждый 50-й - Путин
			kitten.style.left = "333px";
			kitten.appendChild(createKittyFrase(true));
			kitten.appendChild(createKittyImage(true));
		} else {
			kitten.style.left = getLeft() + "px";
			kitten.appendChild(createKittyFrase());
			kitten.appendChild(createKittyImage());
		}

	return kitten;
}


// Создаёт и возвращает случайное изображение котёнка
function createKittyImage(putin=false) {
	let kittyImage = document.createElement("img");

	if (putin) {
		kittyImage.src = "img/kitty100.png";
	} else {
		let num = ~~(Math.random() * 100/*колличество картинок*/);
		kittyImage.src = "img/kitty" + num.toString() + ".png";
	}

	return kittyImage;
}


// Создаёт и возвращает h3-фразу из глобального массива frases
function createKittyFrase(putin=false) {
	let kittyFrase = document.createElement("h3");
		kittyFrase.classList.add("kitty-frase");

		if (putin) {
			kittyFrase.textContent = putinFrase;
			kittyFrase.style.color = "black";
			kittyFrase.classList.add("putin");
		} else {
			kittyFrase.textContent = frases[~~(/*frases.length*/100 * Math.random())];
			kittyFrase.style.color = "rgb(" + (~~(255 * Math.random())) + "," +
				(~~(255 * Math.random())) + "," + (~~(255 * Math.random())) + ")";
		}

	return kittyFrase;
}


// Уничтожение kitty-элементов
function deleteKittens() {
	let vapp = document.getElementById("vApp");
	let kittens = document.getElementsByClassName("kitty-img");
	let len = kittens.length;
	if (vapp) {
		for (let i = len-1; i >= 0; i--) {
			vapp.removeChild(kittens[i]);
		}
		counter = 1;
	}
}


// Возвращает левый край активного окна
function getLeft() {
	let w = window,
    	d = document,
    	e = d.documentElement,
    	g = d.getElementsByTagName('body')[0],
    	x = w.innerWidth || e.clientWidth || g.clientWidth;
    return ~~((x - 256) * Math.random());
}


// Если kittyInterval существует - уничтожает его и всех созданных kitty; иначе -
// создаёт интервал на создание котят. kittyInterval - глобальная переменная
function kittyRain() {
	if (kittyInterval) {
		clearInterval(kittyInterval);
		kittyInterval = null;
		deleteKittens();
		return;
	}

	kittyInterval = setInterval(addKitty, 1000);
}


// Хэндлер нажатия кнопки-сердечка, переключает класс active, запускает kittyRain
function loveYou() {
	let button = document.getElementById("love-you");
	if (button) {
		button.classList.toggle("active");
	}

	kittyRain();
}

