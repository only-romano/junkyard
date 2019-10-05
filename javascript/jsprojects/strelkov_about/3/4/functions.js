
function addDisclaimerListeners() {
  let disclamers = document.getElementsByClassName('content__disclaimer_control');
    for (let i = 0; i < disclamers.length; i++) {
      disclamers[i].onclick = toggleDisclaimer;
    }
}


function addListenersCycle(nodelist) {
  for (let i = 0; i < nodelist.length; i++) {
    let node = nodelist[i];
    node.ondrag = node.ondragdrop = node.ondragstart = preventDrag;
  }
}


function addNoDragListeners() { 
  let nodelist = document.getElementsByTagName('img');
  addListenersCycle(nodelist);

  nodelist = document.getElementsByTagName('a');
  addListenersCycle(nodelist);
};


function listenerBody() {
    if ( !(event.target.id == 'menu-icon') &&
              document.querySelector('.header__menu.open') ) toggleMenu();
};


function preventDrag() { 
  event.preventDefault();
  return false;
};


function toggleDisclaimer() {
  document.querySelector('.content__disclaimer').classList.toggle('open');
  document.querySelector('.d__opener').classList.toggle('open');
}


function toggleMenu() {
  let menu = document.getElementsByClassName('header__menu')[0];
    menu.classList.toggle('open');
}
