// Crazy letters random animation
class CrazyLetters{
  // Look for css-animations in css-useful things in animation.css file:
  // "Crazy letters" bundle from awesome blog
  _animationsArray = [
    ['balance', 'ease-out' 'transform-origin: 0 100% 0'],
    ['shrinkjump', 'ease-in-out' 'transform-origin: bottom center'],
    ['falling', 'ease-out' 'transform-origin: bottom center'],
    ['rotate', 'ease-out', ''],
    ['toplong', 'linear', ''],
  ];
  _colors = [  // length = 20
    'bisque', 'black', 'lavander', 'burlywood', 'darkgrey', 'red', 'magenta',
    'fuchsia', 'lightcoral', 'orangered', 'green', 'yellow', 'greenyellow',
    'darkolivegreen', 'springgreen', 'blue', 'blueviolet', 'cyan', 'dodgerblue',
    'lightsteelblue'
  ];
  constructor(element, word=false, options={}){
    this.element = element;  // where to send animated spans
    this.word = word || element.textContent;  // text to animate
    this.css = "";  // final css
    this.temp_css = [];  // temporal css array
  }

  animate(){
    this.css = "";
    this.temp_css = [];
  }


}

const crazyLetters = (word, options) => {

  css.push(create)

  css += createLettersForAnimation(name, num, styles, colors, h_name, css, opt);

    if (opt === false) {
      let header = document.getElementsByClassName('header')[0];
        h_name.addEventListener('click', function() {
          document.location.href = "/blog/page/1?author=" +
            name + checkColorScheme();
        });

        header.addEventListener('mouseleave', function() {
          let spans = document.querySelectorAll('.header__name span');
            for (let i = 0; i < spans.length; i++) {
              if (!spans[i].classList.contains('active')) {
                spans[i].classList.add('active');
              }
            }
        });

      css += '.header__name {width: calc(' + num + 'vw + ' + num + '0px)}';
    } else {
      if (opt === 1) {
        window.addEventListener('keydown', function () {
          let spans = document.getElementsByClassName('curious_span');
          setTimeout(function () {
          }, 1000);
          for (let i = 0; i < spans.length; i++) {
            for (let j = 0; j < spans[i].children.length; j++) {
              spans[i].children[j].innerHTML =
                regWordsRanomizer(spans[i].children[j].innerHTML);
            }
            spans[i].style.top = (15 + ~~(Math.random() * 75)) + 'vh';
            spans[i].style.left = (10 + ~~(Math.random() * 80)) + 'vw';
          }
        }, false);
        css += '.curious_span {width: calc(' + ~~(1.1*num) + 'vw + ' + ~~(1.1*num) + '0px)}';
      } else {
        h_name.addEventListener('mouseenter', function () {
          let spans = document.querySelectorAll('.curious_span span');
          for (let i = 0; i < spans.length; i++) {
            if (!spans[i].classList.contains('active')) {
              spans[i].classList.add('active');
              spans[i].style.opacity = 1;
            }
          }
        });
        css += '.curious_span {width: calc(' + ~~(num/2.5) + 'vw + ' + ~~(num/3) + '0px)}';
      }
    }

  if (opt === 1) {
    let res = [[50, 45], [85, 5], [85, 75], [35, 75], [35, 5]];
    let spans = document.getElementsByClassName('standart_let');
      for (let i = 0; i < spans.length; i++) {
        spans[i].style.top = res[i][0] + 'vh';
        spans[i].style.left = res[i][1] + 'vw';
      }
  }

  let style = document.createElement('style');
    if (style.styleSheet) style.styleSheet.cssText = css;
    else style.appendChild( document.createTextNode(css) );

  document.getElementsByTagName('head')[0].appendChild(style);
}


// Help function -  creates letters and sets styles for it
function createLettersForAnimation(name, num, styles, colors, h_name, css, opt) {
  for (let i = 0; i < num; i++) {
    let styleNow = styles[Math.floor(Math.random() * 4.99)];
    let letter = document.createElement('span');
      letter.textContent = name[i];
      if (opt !== 1 || Math.random() >.5) {
        letter.classList.add('letters_animation' + i);
        css += '.letters_animation' + i + '.active {animation: ' + styleNow[0] +
          (1 + Math.floor(Math.random() * 20) / 10) + styleNow[1] + '; color: ' +
          colors[Math.floor(Math.random() * 19.99)] + ';} ' + '.letters_animation' +
          i + ' {color: ' + colors[Math.floor(Math.random() * 19.99)] + ';}';

        if (opt === 1) {
          letter.addEventListener('animationend', () => {
            event.target.classList.remove('active');
            setTimeout(() => {
              letter.classList.add('active');
            }, Math.floor(Math.random() * 3000));
        });

        }
        letter.addEventListener('animationend', () => {
          event.target.classList.remove('active');
        });

        setTimeout(() => {
          letter.classList.add('active');
        }, Math.floor(Math.random() * 3000));
      } else {
        letter.classList.add('active')
      }
      if (name[i] === ' ') { letter.innerHTML = '<pre> </pre>' }

    h_name.appendChild(letter);
  }
  if (opt === 1) h_name.classList.add('standart_let');
  return css;
}


// Function to create random word from alphabet
function createWord(letters) {
  let word = '';
  let lang = letters[~~(Math.random() * 1.99)];
  let length = 4 + ~~(Math.random() * 10.99);
    for (i = 0; i < length; i++) {
      word += lang[~~(Math.random() * lang.length - 0.01)];
    }

  length = ~~(Math.random() * 4.99);
    if (word.length < 8) {
      for (i = 0; i < length; i++) {
        word += letters[2][~~(Math.random() * 9.99)];
      }
    }

  return word;
}


// Alphabets for randomizer, initial random animation
function regWordsRanomizer(flag=false) {
  let letters = [
    'aбвгдеёжзийклмнопрстуфхцчшщъыьэюя',
    'abcdefghijklmnopqrstuvwxuz',
    '1234567890'
  ];
  if (typeof flag === "string" && flag.length === 1) {
    for (let i = 0; i < letters.length; i++) {
      if (~letters[i].indexOf(flag)) {
        return letters[i][~~(Math.random() * letters[i].length - .01)]
      }
    }
  }

  if (flag === false) {
    for (let i = 0; i < ~~(1 + Math.random() * 6.99); i++) {
      animateName(createWord(letters), true);
    }
  } else if (flag === 1) {
    for (let i = 0; i < ~~(2 + Math.random() * 3.99); i++) {
      animateName(createWord(letters), flag)
    }
  }
}
