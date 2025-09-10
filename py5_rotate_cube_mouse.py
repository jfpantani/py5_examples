import py5

xAngle = 0.0
yAngle = 0.0
xMousePos = 0.0
yMousePos = 0.0
rotate = False


def drawCube():
    global xAngle
    global yAngle

    # Set de center of de cube
    py5.translate(py5.width / 2, py5.height / 2)

    # Applay rotations based on mouse input
    py5.rotate_x(py5.radians(xAngle))
    py5.rotate_y(py5.radians(yAngle))

    py5.fill(0, 76, 153)

    # Draw the cube's faces
    py5.box(100)


def setup():
    global xMousePos
    global yMousePos

    py5.size(600, 600, py5.P3D)
    #py5.background(200)
    xMousePos = py5.width / 2
    yMousePos = py5.height / 2

def draw():
    py5.background(000)
    py5.push_matrix()
    drawCube()
    py5.pop_matrix()

def mouse_pressed():
    global rotate
    global xMousePos
    global yMousePos

    rotate = True
    xMousePos = py5.mouse_x
    yMousePos = py5.mouse_y

def mouse_dragged():
    global rotate
    global xAngle
    global yAngle
    global xMousePos
    global yMousePos

    if (rotate):
       # Calculate the difference in mouse position
       dx = py5.mouse_x - xMousePos
       dy = py5.mouse_y - yMousePos
        
       # Update the angles for rotation (adjust sensitivity as needed)
       xAngle += dy * 1.5
       yAngle += dx * 1.5

       # Update the mouse position
       xMousePos = py5.mouse_x
       yMousePos = py5.mouse_y

py5.run_sketch()


