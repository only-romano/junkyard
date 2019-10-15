(function() {

  let edited = false;
  let table = document.getElementById('bagua-table');
    table.addEventListener('click', editTable);

  function editTable() {
    if (event.target.tagName = 'TD' && !edited) {
      editTd(event.target);
    }
  }

  function editTd(node) {
    let tdRect = node.getBoundingClientRect();
    let area = document.createElement('textarea');
      area.value = node.innerHTML;
    setAreaStyle(area, tdRect);
    createBottoms(area, node, tdRect);
    document.body.appendChild(area);
    edited = true;
  }

  function setAreaStyle(area, rect) {
    area.className = 'edit-td';
    area.style.top = (rect.top + pageYOffset) + 'px';
    area.style.left = (rect.left + pageXOffset) + 'px';
    area.style.width = rect.width - 8 + 'px';
    area.style.height = rect.height - 8 + 'px';
  }

  function createBottoms(area, node, rect) {
    createAcceptBottom(area, node, rect);
    createCancelBottom(area, node);
  }

  function createAcceptBottom(area, node, rect) {
    let bottom = document.createElement('bottom');
      bottom.innerHTML = 'Accept';
      bottom.className = 'td-edit-bottom';
      bottom.onclick = function () {
        node.innerHTML = area.value;
        document.body.removeChild(area);
        let bottoms = document.getElementsByClassName('td-edit-bottom');
          for (let i = bottoms.length - 1; i >= 0; i--) {
            document.body.removeChild(bottoms[i]);
          }
        edited = false;
      }
    document.body.appendChild(bottom);
  }

  function createCancelBottom(area, node) {
    let bottom = document.createElement('bottom');
      bottom.innerHTML = 'Cancel';
      bottom.className = 'td-edit-bottom';
      bottom.onclick = function () {
        document.body.removeChild(area);
        let bottoms = document.getElementsByClassName('td-edit-bottom');
          for (let i = bottoms.length - 1; i >= 0; i--) {
            document.body.removeChild(bottoms[i]);
          }
        edited = false;
      }
    document.body.appendChild(bottom);
  }

})();