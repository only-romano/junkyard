
elem.onclick = function(event) {
  console.log( 'Type of event is "' + event.type + '" on target: ' + event.currentTarget );
  console.log( 'Cursour coordinates on click relative to window are: ' + event.clientX + ':' + event.clientY );
}

cbevent1.onclick = function(event)  {
  event = event || window.event;
  console.log (event);
}

cbevent2.onclick = function(e) {
  // only if 'event' is not used in own bindings
  e = e || event;
  console.log (e);
}