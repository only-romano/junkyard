(function() {
  // Files support & read

  if (window.File && window.FileReader && window.FileList && window.Blob) {

    function handleFileSelect(evt) {
      var files = evt.target.files;
      var output = [];
        for (var i = 0, f; f = files[i]; i++) {
          output.push('<li><strong>', escape(f.name), '</strong> (',
            f.type || 'n/a', ') - ', f.size, ' bytes, last modified: ',
            f.lastModifiedDate.toLocaleDateString(), '</li>');

          if (!f.name.match('\.txt')) {
            continue;
          }

          var reader = new FileReader();
            reader.onload = (function(file) {
              return function(e) {
                var ul = document.createElement('ul');
                  ul.className = 'tree';
                var articles = e.target.result.split('\n');
                  for (var i = 0; i < articles.length; i++) {
                    var li = document.createElement('li');
                    var articleBlocks = articles[i].split(' ');
                      li.innerHTML = '<span>Article ' + (i+1) + ': ' + articleBlocks[0] +
                                     '</span><ul></ul>';
                      for (var j = 1; j < articleBlocks.length; j++) {
                        var inLi = document.createElement('li');
                          inLi.innerHTML = '<span>Block ' + (i+1) + '.' + j + ': ' +
                                           articleBlocks[j] + '</span>';
                        li.children[1].appendChild(inLi);
                      }
                      ul.appendChild(li);
                  }
                document.body.appendChild(ul);
              };
            })(f);

          reader.readAsText(f);
        }
      document.getElementById('flist').innerHTML = '<ul>' +
          output.join('') + '</ul>';
    }

    document.getElementById('files').addEventListener('change',
      handleFileSelect, false)

  } else {
    alert('The File API are not fully supported in this browser');
  }
})();

(function() {
  var reader;
  var progress = document.querySelector('.percent')
  document.getElementsByTagName('button')[0].addEventListener('click', abortRead);

  function abortRead() {
    if (!reader) return;
    reader.abort();
  }

  function errorHandler(evt) {
    switch(evt.target.error.code) {
      case evt.target.error.NOT_FOUND_ERR:
        alert('File not found!');
        break;
      case evt.target.error.NOT_READABLE_ERR:
        alert('File is not readable');
        break;
      case evt.target.error.ABORT_ERR:
        break;
      default:
        alert('An error occured reading this file');
    };
  }

  function updateProgress(evt) {
    if (evt.lengthComputable) {
      var percentLoaded = Math.round((evt.loaded / evt.total) * 100);
        if (percentLoaded < 100) {
          progress.style.width = percentLoaded + '%';
          progress.textContent = percentLoaded + '%';
        }
    }
  }

  function handleFileSelect(evt) {
    progress.style.width = '0%';
    progress.textContent = '0%';

    reader = new FileReader();
    reader.onerror = errorHandler;
    reader.onprogress = updateProgress;
    reader.onabort = function(e) {
      alert('File read cancelled');
    };
    reader.onloadstart = function(e) {
    document.getElementById('progress_bar').className = 'loading';
    };
    reader.onload = function(e) {
      progress.style.width = '100%';
      progress.textContent = '100%';

    setTimeout('document.getElementById("progress_bar").className="";', 2000);
    };

    reader.readAsBinaryString(evt.target.files[0]);
  }

  document.getElementById('files').addEventListener('change', handleFileSelect, false);
})();


(function() {
  var dragManager = new function() {
    var dragZone, avatar, dropTarget;
    var downX, downY;

    var self = this;

    function onMouseDown(e) {
        if (e.which != 1) return false;
      dragZone = findDragZone(e);
        if (!dragZone) return;

      downX = e.pageX;
      downY = e.pageY;

      return false;
    }

    function onMouseMove(e) {
        if (!dragZone) return;
        if (!avatar) {
            if (Math.abs(e.pageX - downX) < 3 && Math.abs(e.pageY = downY) < 3) return;
          avatar = dragZone.onDragStart(downX, downY, e);
            if (!avatar) {
              cleanUp();
              return;
            }
        }
      avatar.onDragMove(e);
      var newDropTarget = findDropTarget(e);
        if (newDropTarget != dropTarget) {
          dropTarget && dropTarget.onDragLeave(newDropTarget, avatar, e);
          newDropTarget && newDropTarget.onDragEnter(dropTarget, avatar, e);
        }
      dropTarget = newDropTarget;
      dropTarget && dropTarget.onDragMove(avatar, e);

      return false;
    }

    function onMouseUp(e) {
        if (e.which != 1) return false;
        if (avatar) {
          if (dropTarget) {
            dropTarget.onDragEnd(avatar, e);
          } else {
            avatar.onDragCancel();
          }
        }
      cleanUp();
    }

    function cleanUp() {
      dragZone = avatar = dropTarget = null;
    }

    function findDragZone(event) {
      var elem = event.target;
        while (elem != document && !elem.dragZone) {
          elem = elem.parentNode;
        }
      return elem.dragZone;
    }

    function findDropTarget(event) {
      var elem = avatar.getTargetElem();
        while (elem != document && !elem.dropTarget) {
          elem = elem.parentNode;
        }
        if (!elem.dropTarget) return null;
      return elem.dropTarget;
    }

    document.ondragstart = function() {
      return false;
    }

    document.onmousemove = onMouseMove;
    document.onmouseup = onMouseUp;
    document.onmousedown = onMouseDown;
  }

  function DragZone(elem) {
    elem.dragZone = this;
    this._elem = elem;
  }

  DragZone.prototype._makeAvatar = function() {};
  DragZone.prototype.onDragStart = function(downX, downY, event) {
    var avatar = this._makeAvatar();
      if (!avatar.initFromEvent(downX, downY, event)) return false;
    return avatar;
  };

  function TreeDragZone(elem) {
    DragZone.apply(this, arguments);
  }

  extend(TreeDragZone, DragZone);

  TreeDragZone.prototype._makeAvatar = function() {
    return new TreeDragAvatar(this, this._elem);
  }

  function DragAvatar(dragZone, dragElem) {
    this._dragZone = dragZone;
    this._dragZoneElem = dragElem;
    this._elem = dragElem;
  }

  DragAvatar.prototype.getDragInfo = function(event) {
    return {
      elem: this._elem,
      dragZoneElem: this._dragZoneElem,
      dragZone: this._dragZone
    };
  };

  DragAvatar.prototype.getTargetElem = function() {
    return this._currentTargetElem;
  };

  DragAvatar.prototype.onDragMove = function(event) {
    this._elem.style.left = event.pageX - this._shiftX + 'px';
    this._elem.style.top = event.pageY - this._shiftY + 'px';

    this._currentTargetElem = getElementUnderClientXY(this._elem, event.clientX, event.clientY);
  };

  DragAvatar.prototype.onDragCancel = function() {};
  DragAvatar.prototype.onDragEnd = function() {};

  function TreeDragAvatar(dragZone, dragElem) {
    DragAvatar.apply(this, arguments);
  }

  extend(TreeDragAvatar, DragAvatar);

  TreeDragAvatar.prototype.initFromEvent = function(downX, downY, event) {
      if (event.target.tagName != 'SPAN') return false;
    this._dragZoneElem = event.target;
    var elem = this._elem = this._dragZoneElem.cloneNode(true);
      elem.className = 'avatar';

    var coords = getCoords(this._dragZoneElem);
      this._shiftX = downX - coords.left;
      this._shiftY = downY - coords.top;
    document.body.appendChild(elem);
      elem.style.zIndex = 9999;
      elem.style.position = 'absolute';

    return true;
  };

  TreeDragAvatar.prototype._destroy = function() {
    this._elem.parentNode.removeChild(this._elem);
  };

  TreeDragAvatar.prototype.onDragCancel = function() {
    this._destroy();
  };

  TreeDragAvatar.prototype.onDragEnd = function() {
    this._destroy();
  };


  function DropTarget(elem) {
    elem.dropTarget = this;
    this._elem = elem;
    this._targetElem = null;
  }

  DropTarget.prototype._getTargetElem = function(avatar, event) {
    return this._elem;
  };

  DropTarget.prototype._hideHoverIndication = function(avatar) {};
  DropTarget.prototype._showHoverIndication = function(avatar) {};

  DropTarget.prototype.onDragMove = function(avatar, event) {
    var newTargetElem = this._getTargetElem(avatar, event);
      if (this._targetElem != newTargetElem) {
        this._hideHoverIndication(avatar);
        this._targetElem = newTargetElem;
        this._showHoverIndication(avatar);
      }
  };

  DropTarget.prototype.onDragEnd = function(avatar, event) {
    this._hideHoverIndication(avatar);
    this._targetElem = null;
  };

  DropTarget.prototype.onDragEnter = function(fromDropTarget, avatar, event) {};
  DropTarget.prototype.onDragLeave = function(toDropTarget, avatar, event) {
    this._hideHoverIndication();
    this._targetElem = null;
  }

  function TreeDropTarget(elem) {
    TreeDropTarget.parent.constructor.apply(this, arguments);
  }

  extend(TreeDropTarget, DropTarget);

  TreeDropTarget.prototype._showHoverIndication = function() {
    this._targetElem && this._targetElem.classList.add('hover');
  };

  TreeDropTarget.prototype._hideHoverIndication = function() {
    this._targetElem && this._targetElem.classList.remove('hover');
  };

  TreeDropTarget.prototype._getTargetElem = function(avatar, event) {
    var target = avatar.getTargetElem();
      if (target.tagName != 'SPAN') return;
    var elemToMove = avatar.getDragInfo(event).dragZoneElem.parentNode;
    var elem = target;
      while (elem) {
          if (elem == elemToMove) return;
        elem = elem.parentNode;
      }
    return target;
  };

  TreeDropTarget.prototype.onDragEnd = function(avatar, event) {
      if (!this._targetElem) {
        avatar.onDragCancel();
        return;
      }
    this._hideHoverIndication();
    var avatarInfo = avatar.getDragInfo(event);
    avatar.onDragEnd();
    var elemToMove = avatarInfo.dragZoneElem.parentNode;
    var title = avatarInfo.dragZoneElem.innerHTML;
    var ul = this._targetElem.parentNode.getElementsByTagName('UL')[0];
      if (!ul) {
        ul = document.createElement('UL');
        this._targetElem.parentNode.appendChild(ul);
      }
    var li = null;
      for (var i = 0; i < ul.children.length; i++) {
        li = ul.children[i];
        var childTitle = li.children[0].innerHTML;
          if (childTitle > title) {
            break;
          }
        li = null;
      }

      ul.insertBefore(elemToMove, li);
      this._targetElem = null;
  }

  function getCoords(elem) {
    var box = elem.getBoundingClientRect();
    var body = document.body;
    var docElem = document.documentElement;

    var scrollTop = window.pageYOffset || docElem.scrollTop || body.scrollTop;
    var scrollLeft = window.pageXOffset || docElem.scrollLeft || body.scrollLeft;

    var clientTop = docElem.clientTop || body.clientTop || 0;
    var clientLeft = docElem.clientLeft || body.clientLeft || 0;
    var top = box.top + scrollTop - clientTop;
    var left = box.left + scrollLeft - clientLeft;

    return {
      top: Math.round(top),
      left: Math.round(left)
    };
  }

  function getElementUnderClientXY(elem, clientX, clientY) {
    var display = elem.style.display || '';
      elem.style.display = 'none';
    var target = document.elementFromPoint(clientX, clientY);
      elem.style.display = display;
      if (!target || target == document) target = document.body;

    return target;
  }

  function extend(Child, Parent) {
    function F() {};
    F.prototype = Parent.prototype;
    Child.prototype = new F();
    Child.prototype.constructor = Child;
    Child.parent = Parent.prototype;
  }

  var dndButton = document.getElementsByTagName('button')[1];
    dndButton.addEventListener('click', onTrees, false);

  function onTrees() {
    var trees = document.getElementsByClassName('tree');
      for (var i = 0; i < trees.length; i++) {
        new TreeDragZone(trees[i]);
        new TreeDropTarget(trees[i]);
      }
  }
})();