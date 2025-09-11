import py5

angle = 0.0

def setup():
    py5.size(400,400)
    py5.smooth()

def draw():
    global angle

    py5.background(0)
    py5.push_matrix()
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate(py5.radians(angle))

    x1 = -50.0
    y1 = 50.0
    x2 = 50.0
    y2 = 50.0
    x3 = 0.0
    y3 = -50.0

    py5.fill(250)
    py5.triangle(x1, y1, x2, y2, x3, y3)

    py5.pop_matrix()

    #angle += 1

def key_pressed():
    global angle

    match py5.key_code:
        case py5.UP:
           print(f"UP PRESSED!") 
           angle += 90
        case py5.DOWN:
           print(f"DOWN PRESSED!")
           angle += 180
        case py5.LEFT:
            print(f"LEFT PRESSED!")
            angle += 90
        case py5.RIGHT:
            print(f"RIGHT PRESSED!")
            angle -= 90

py5.run_sketch()


