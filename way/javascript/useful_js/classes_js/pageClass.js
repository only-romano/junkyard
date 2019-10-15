;'use strict';

/*
  PAGE helper
*/
const PAGE = {

  random(value){
    // returns random integer up to given value (not included)
    return Math.floor(Math.random * value);
  },

  undrag(el) {
    // makes element undragable
    el.ondrag = el.ondragdrop = el.ondragstart = ()=> {
      event.preventDefault();
      return false;
    };
  },

  hide(el){
    // hides element
    el.setAttribute('hidden', true);
  },

  show(el){
    // shows hidden element
    el.setAttribute('hidden', false);
  },

  rect(el, prop){
    // returns rect property
    return el.getBoundingClientRect()[prop];
  },

  intValue(el, prop){
    // returns int value of property
    return parseInt(getComputedStyle(el)[prop]);
  },

  pack(el){
    // packs element with bundle functions
    el.hide = () => el.setAttribute('hidden', true);
    el.show = () => el.setAttribute('hidden', false);
    el.rect = (prop) => el.getBoundingClientRect()[prop];
    el.value = (prop) => parseInt(getComputedStyle(el)[prop]);
    el.undrag = () => {
      el.ondrag = el.ondragdrop = el.ondragstart = (evt) => {
        evt.preventDefault();
        return false;
      };
    }
  },
}
