int ctrx = 200;
int ctry = 320;
int faceWidth = 160;
int faceHeight = 200;
int skinnyFaceWidth = 120;
int skinnyFaceHeight = 260;
int eyeSize = 10;
color skinTone = color(155, 124, 109);

void setup() {
  size(1200, 800);
}

void draw() {
  daddy(ctrx, ctry, faceWidth, faceHeight);
  daddy(3*ctrx, 2*ctry, skinnyFaceWidth, skinnyFaceHeight);
  daddy(5*ctrx, ctry, faceWidth, skinnyFaceHeight);
  noLoop();
}

void daddy(int x, int y, int w, int h) {
  noStroke();
 
  fill(skinTone);
  
  int eyeXoffset = int((15.0/80.0) * w);
  int eyeYoffset = int(.35 * h);
  int mouthYoffset = int(.1 * h);
  int mouthWidth = int(.5 * w);
  int mouthHeight = int(.3 * h);
  int hairYoffset = eyeYoffset * 3;
  int hairRadius = 3 * eyeSize;
  
  ellipse(x, y, 1.2*w, h);
  ellipse(x, y-h/2, w, h);
  stroke(0);
  fill(0);
  ellipse(x-eyeXoffset, y-eyeYoffset, eyeSize, eyeSize);
  ellipse(x+eyeXoffset, y-eyeYoffset, eyeSize, eyeSize);
  noFill();
  
  arc(x, y-hairYoffset, hairRadius, hairRadius, -PI/2, PI/2);
  arc(x, y-hairYoffset-hairRadius, hairRadius, hairRadius, PI/2, PI*3/2);
  stroke(240, 0, 0);
  arc(x, y+mouthYoffset, mouthWidth*1.5, mouthHeight, QUARTER_PI, 3*QUARTER_PI);
}
