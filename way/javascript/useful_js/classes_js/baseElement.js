;'use strict';

/*
  Base new element creation class
 */
class BaseElement {
  constructor(tag, parent=null, classes=[], attrs={}, style={}) {
    this.element = document.createElement(tag);
    this.parent = parent;

    for (let i = 0; i < classes.length; i++)         // adds classes
      this.element.classList.add(classes[i]);
    for (let [key, value] of Object.entries(attrs))  // adds attributes
      this.element.setAttribute(key, value);
    for (let [key, value] of Object.entries(style))  // adds style attributes
      this.element.style[key] = value;

  }

  append(){
    // appends element to parent node
    if (this.parent)
      this.parent.appendChild(this.element);
  }

  getAppendable(){
    // returns element only with availability to append()
    this.element.append = this.append.bind(this);
    return this.element;
  }
}
