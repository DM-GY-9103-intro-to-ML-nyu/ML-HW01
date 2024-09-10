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
    
