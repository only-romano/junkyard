PImage coinh, coint;
PFont font;
int headc, tailc;

void setup() {
  size(800, 600);
  frameRate(6);
  headc = 0;
  tailc = 0;
  font = createFont("Ariel", 20);
  textFont(font);
  coinh = loadImage("head.png");
  coint = loadImage("tail.png");
  fill(0, 0, 240);
  text("Click on the Screen", 100, 100);
}

void draw() {}

void mouseReleased() {
  background(255);
  if (.5 <= random(1)) {
    image(coinh, mouseX, mouseY, 100, 100);
    headc = headc + 1;
  } else {
    image(coint, mouseX, mouseY, 100, 100);
    tailc = tailc + 1;
  }
  
  text("Heads", 10, 20);
  text(headc, 10, 50);
  text("Tails", 80, 20);
  text(tailc, 80, 50);
}
