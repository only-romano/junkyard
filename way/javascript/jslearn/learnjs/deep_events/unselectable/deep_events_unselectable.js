function clearSelection() {
  if (window.getSelection) {
    window.getSelection().removeAllRanges();
  } else {
    document.selection.empty();
  }
}

function copyRight() {
  window.getSelection().removeAllRanges();
  var some = document.createElement('span');
    some.innerHTML = 'fuck you';
  document.body.appendChild(some);
  var range = document.createRange()
  range.selectNode(some);
  window.getSelection().addRange(range)
  document.execCommand('copy');
  document.body.removeChild(some);
  window.getSelection().removeAllRanges();
  return false;
}