import py5

angle = 0.0

triangleVertices = [[100, 100], [200, 100], [150, 200]] # (x1,y1),(x2,y2),(x3,y3)
triangleVertices2 = [[-100, -100], [-200, -100], [-150, -200]] # (x1,y1),(x2,y2),(x3,y3)


def setup():
    py5.size(400, 400)
    py5.smooth()

def draw():
    global angle
    global triangleVertices
    global triangleVertices2
    
    # Para um segmento entre os pontos \((x_{1},y_{1})\) e \((x_{2},y_{2})\), o ponto médio M é \(((x_{1}+x_{2})/2,(y_{1}+y_{2})/2)\)
    midX = (triangleVertices[0][0] + triangleVertices[1][0]) / 2.0
    midY = (triangleVertices[0][1] + triangleVertices[1][1]) / 2.0

    midX2 = (triangleVertices2[0][0] + triangleVertices2[1][0]) / 2.0
    midY2 = (triangleVertices2[0][1] + triangleVertices2[1][1]) / 2.0

    py5.background(0)
    py5.push_matrix()
    py5.translate(py5.width / 2, py5.height / 2)
    #py5.translate(midX, midY);
    py5.rotate(py5.radians(angle))

    py5.fill(255, 0, 0)

    py5.no_stroke()

    py5.fill(255, 0, 0)

    py5.triangle(triangleVertices[0][0] - midX, triangleVertices[0][1] - midY,
                 triangleVertices[1][0] - midX, triangleVertices[1][1] - midY,
                 triangleVertices[2][0] - midX, triangleVertices[2][1] - midY)
    
    py5.text_size(30);
    py5.fill(0);
    py5.text("N", -9, 40, 101);
    
    py5.fill(0, 76, 153)
    
    py5.triangle(triangleVertices2[0][0] - midX2, triangleVertices2[0][1] - midY2,
                 triangleVertices2[1][0] - midX2, triangleVertices2[1][1] - midY2,
                 triangleVertices2[2][0] - midX2, triangleVertices2[2][1] - midY2)
    
    py5.text_size(30);
    py5.fill(0);
    py5.text("S", -9, -25, -101);

    py5.pop_matrix()

    deg = 360.0-angle;

    py5.fill(250)

    py5.text_size(20);

    py5.text("Press (↑) and (↓) to change angle:",30,20);

    py5.text("Heading: " + str(360-deg) + "º",30,50);

def key_pressed():
    global angle

    match py5.key_code:
        case py5.UP:
           print(f"UP PRESSED!") 
           angle += 1
        case py5.DOWN:
           print(f"DOWN PRESSED!")
           angle -= 1

py5.run_sketch()




