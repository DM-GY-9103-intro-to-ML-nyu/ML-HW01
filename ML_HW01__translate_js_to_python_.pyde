diamSmall = 10
diamLarge = 3 * diamSmall

def setup():
    size(360, 360)
    
def draw():
    background(255,215,0)
    stroke(0)
    fill(0)
    for x in range (0, 360, 5*diamSmall):
        for y in range (0, 360, 5*diamSmall):
            ellipse(x,y, diamSmall, diamSmall)
    for x in range (0, 360, 2*5*diamSmall):
        for y in range (0, 360, 2*5*diamSmall):
            ellipse(x,y, diamLarge, diamLarge)
            
    translate(5*diamSmall, 5*diamSmall)
    
    for x in range(0, 360, 2*5*diamSmall):
        for y in range (0, 360, 2*5*diamSmall):
            ellipse(x,y,diamLarge, diamLarge)
    


""" original JS file:

let diamSmall = 10;
let diamLarge = 3 * diamSmall;

function setup() {
  createCanvas(windowWidth, windowHeight);
}

function draw() {
  background("gold");
  stroke(0);

  fill(0);
  for (let x = 0; x < width; x += 5 * diamSmall) {
    for (let y = 0; y < height; y += 5 * diamSmall) {
      ellipse(x, y, diamSmall, diamSmall);
    }
  }

  for (let x = 0; x < width; x += 2 * 5 * diamSmall) {
    for (let y = 0; y < height; y += 2 * 5 * diamSmall) {
      ellipse(x, y, diamLarge, diamLarge);
    }
  }

  translate(5 * diamSmall, 5 * diamSmall);
  for (let x = 0; x < width; x += 2 * 5 * diamSmall) {
    for (let y = 0; y < height; y += 2 * 5 * diamSmall) {
      ellipse(x, y, diamLarge, diamLarge);
    }
  }
}
"""
