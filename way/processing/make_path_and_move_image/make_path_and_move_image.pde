Location[] path = {};

Boolean pathmade = false;
int pathI = 0;
String instructions = "Press mouse buttin down, drag and release to make a path";
float imageW;
float imageH;
float half_imageW;
float half_imageH;
PImage biker;

void setup() {
  size(1200, 900);
  background(255);
  biker = loadImage("eye.jpg");
  imageW = biker.width/3;
  imageH = biker.height/3;
  half_imageW = imageW / 2;
  half_imageH = imageH / 2;
  strokeWeight(3);
  fill(0);
  textSize(30);
  text(instructions, 10, 20);
  frameRate(30);
}

void draw() {
  if (pathmade) {
    background(255);
    text(instructions, 10, 20);
    Location p = path[pathI];
    pathI++;
    image(biker, p.xp-half_imageW, p.yp-half_imageH, imageW, imageH);
    if (pathI >= path.length) {
      pathI = 0;
    }
  }
}

void mousePressed() {
  path = new Location[0];
  pathI = 0;
  pathmade = false;
  path = (Location[]) append(path, new Location(mouseX, mouseY)); 
}

void mouseDragged() {
  path = (Location[]) append(path, new Location(mouseX, mouseY));
  line(pmouseX, pmouseY, mouseX, mouseY);
}

void mouseReleased() {
  pathmade = true;
}

class Location {
  float xp;
  float yp;
  Location (float x, float y) {
    xp = x;
    yp = y;
  }
}
