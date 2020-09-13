Piece[] pieces;
PImage original;
PImage originalA;
int phase = 0;
Button[] buttons;
int NHor = 4;
int NVer = 3;
int NoP = NHor * NVer;
float oriWidth;
float oriHeight;
float oriRatio;
int adjustedWidth;
int adjustedHeight;
int wedgeW;
int wedgeH;
int pieceMoving = -1;
int offsetx;
int offsety;
int tolerance = 20;
int travelBackFrames;
int[] deltaxs = new int[NoP];
int[] deltays = new int[NoP];

void setup() {
  frameRate(30);
  travelBackFrames = 30 * 2;
  original = loadImage("pic.jpg");
  size(displayWidth, displayHeight);
  oriWidth = original.width;
  oriHeight = original.height;
  oriRatio = oriHeight / oriWidth;
  adjustedWidth = round(min(.75 * displayWidth, oriWidth));
  adjustedHeight = round(min(oriRatio * adjustedWidth,.75 * displayHeight));
  adjustedWidth = round(adjustedHeight / oriRatio);
  wedgeH = round(adjustedHeight / NVer);
  wedgeW = round(adjustedWidth / NHor);
  originalA = createImage(adjustedWidth, adjustedHeight, RGB);
  originalA.copy(original, 0, 0, round(oriWidth), round(oriHeight), 0, 0, adjustedWidth, adjustedHeight);
  makeButtons();
  makePieces();
}

void makeButtons() {
  buttons = new Button[2];
  buttons[0] = new Button(50, 30, 80, 40, color(200, 0, 0), "Mix up");
  buttons[1] = new Button(200, 30, 80, 40, color(0, 100, 0), "Restore");
}

void drawButtons() {
  for (int i = 0; i < buttons.length; i++) {
    buttons[i].display();
  }
}

void mouseClicked() {
  int mx, my;
  mx = mouseX;
  my = mouseY;
  if (buttons[0].isOver(mx, my)) {
    mixUpPieces();
    phase = 0;
  }
  if (buttons[1].isOver(mx, my)) {
    phase = 2;
    for (int i = 0; i < NoP; i++) {
      deltaxs[i] = floor(((100.0 + pieces[i].locx) - pieces[i].px) / travelBackFrames);
      deltays[i] = floor(((100.0 + pieces[i].locy) - pieces[i].py) / travelBackFrames);
    }
  }
}

void mousePressed() {
  int mx = mouseX;
  int my = mouseY;
  for (int i = 0; i < NoP; i++) {
    if (pieces[i].isOver(mx, my)) {
      pieceMoving = i;
      break;
    }
  }
}

void mouseDragged() {
  if (pieceMoving >= 0) {
    pieces[pieceMoving].px = mouseX - offsetx;
    pieces[pieceMoving].py = mouseY - offsety;
  }
}

void mouseReleased() {
  pieceMoving = -1;
  int firstx = pieces[0].px;
  int firsty = pieces[0].py;
  boolean oksofar = true;
  
  for (int i = 1; i < NoP; i++) {
    int pxi = pieces[i].px;
    int pyi = pieces[i].py;
    int perfectpx = firstx + pieces[i].locx;
    int perfectpy = firsty + pieces[i].locy;
    int errorx = abs(perfectpx - pxi);
    int errory = abs(perfectpy - pyi);
    if (errorx > tolerance || errory > tolerance) {
      oksofar = false;
      break;
    }
  }
  if (oksofar) {
    text("Close enough. You can click Restore or Mix up to try again.", 500, 20);
    phase = 1;
  }
}

void makePieces() {
  pieces = new Piece[NoP];
  int alli = 0;
  for (int i = 0; i < NHor; i++)
    for (int j = 0; j < NVer; j++) {
      int rx = round(random(.75 * displayWidth));
      int ry = round(random(.75 * displayHeight));
      pieces[alli] = new Piece(wedgeW * i, wedgeH * j, rx, ry, wedgeW, wedgeH);
      pieces[alli].display();
      alli++;
    }
}

void mixUpPieces() {
  for (int i = 0; i < NoP; i++) {
    int rx = round(random(.75 * displayWidth));
    int ry = round(random(.75 * displayHeight));
    pieces[i].px = rx;
    pieces[i].py = ry;
  }
}

void draw() {
  if (phase == 0) {
    background(255);
    drawPieces();
    drawButtons();
  }
  if (phase == 2) {
    for (int i = 0; i < NoP; i++) {
      pieces[i].px = pieces[i].px + deltaxs[i];
      pieces[i].py = pieces[i].py + deltays[i];
    }
    background(255);
    drawPieces();
    drawButtons();
    if (abs(pieces[0].px - 100) < 5 * tolerance) {
      for (int i = 0; i < NoP; i++) {
        pieces[i].px = 100 + pieces[i].locx;
        pieces[i].py = 100 + pieces[i].locy;
      }
      phase = 0;
    }
  }
}

void drawPieces() {
  for (int i = 0; i < NoP; i++) {
    pieces[i].display();
  }
}


class Button {
  int cx, cy;
  int bw, bh, bwsq, bhsq;
  color col;
  String label;
  
  Button (int x, int y, int bwid, int bht, color c, String lab) {
    cx = x;
    cy = y;
    bw = bwid;
    bh = bht;
    bwsq = bw * bw;
    bhsq = bh * bh;
    col = c;
    label = lab;
  }
  
  boolean isOver (int x, int y) {
    float disX = cx - x;
    float disXsq = disX * disX;
    float disY = cy - y;
    float disYsq = disY * disY;
    float v = (disXsq / bwsq) + (disYsq / bhsq);
    return v < 1;
  }
  
  void display() {
    fill(col);
    ellipse(cx, cy, bw, bh);
    fill(0);
    textAlign(CENTER, CENTER);
    text(label, cx, cy);
  }
}

class Piece {
  int locx;
  int locy;
  int px;
  int py;
  int pw;
  int ph;
  PImage content;

  Piece (int locxC, int locyC, int x, int y, int w, int h) {
    locx = locxC;
    locy = locyC;
    px = x;
    py = y;
    pw = w;
    ph = h;
    content = createImage(pw, ph, RGB);
    content.copy(originalA, locxC, locyC, pw, ph, 0, 0, pw, ph);
  }
  
  boolean isOver (int mx, int my) {
    if (mx >= px && mx <= (px + pw) && my >= py && my < (py + ph)) {
      offsetx = mx - px;
      offsety = my - py;
      return true;
    } else {
      return false;
    }
  }
  
  void display() {
    image(content, px, py, pw, ph);
  }
}
