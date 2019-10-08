"use strict";

const create_element = (parent, name, text) => {
    let element = document.createElement(name);
    element.innerText = text;
    parent.appendChild(element);
}

let blocks = document.getElementsByTagName('div');
for (let i = 0; i < blocks.length; i++) {
    let div = blocks[i];
    create_element(div, "h2", "English header");
    create_element(div, "h3", "Кирилический заголовок");
    create_element(div, "p", "Маленький текст, small text. This is - " + div.classList[0])
}
