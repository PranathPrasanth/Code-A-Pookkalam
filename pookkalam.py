import turtle
import math

def get_star_vertices(outer_radius, inner_radius, points, angle_offset=0):
    vertices = []
    angle_step = 360 / points
    
    for i in range(points):
        
        outer_angle = math.radians(i * angle_step + angle_offset)
        vertices.append((outer_radius * math.cos(outer_angle), outer_radius * math.sin(outer_angle)))
        
        
        inner_angle = math.radians((i * angle_step) + (angle_step / 2) + angle_offset)
        vertices.append((inner_radius * math.cos(inner_angle), inner_radius * math.sin(inner_angle)))
        
    return vertices

def draw_polygon(t, vertices, fill_color):
    t.penup()
    t.goto(vertices[-1]) 
    t.pendown()
    t.color(fill_color)
    t.begin_fill()
    for vertex in vertices:
        t.goto(vertex)
    t.end_fill()
    t.penup()

def draw_layered_flower(t):
    flower_layers = [
        {'radius': 90, 'color': '#FFD700'},  
        {'radius': 65, 'color': '#FF1493'}, 
        {'radius': 45, 'color': '#FFFFFF'}  
    ]
    
    start_heading = -22.5 
    petal_arc_angle = 60  

    for layer in flower_layers:
        t.goto(0, 0)
        t.color(layer['color'])
        
        for i in range(8): 
            t.setheading(start_heading + i * 45)
            t.begin_fill()
            t.circle(layer['radius'], petal_arc_angle)
            t.left(180 - petal_arc_angle)
            t.circle(layer['radius'], petal_arc_angle)
            t.end_fill()

def create_pookalam_design():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white") 
    screen.title("Code A Pookkalam")
    screen.tracer(0) 
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    star_layers = [
        {'radius': 350, 'color': "#000000"}, 
        {'radius': 335, 'color': '#DC143C'}, 
        {'radius': 320, 'color': '#DC143C'}, 
        {'radius': 305, 'color': '#FF8C00'}, 
        {'radius': 290, 'color': '#FF8C00'}, 
        {'radius': 275, 'color': "#FFFFFF"}, 
        {'radius': 260, 'color': "#000000"}, 
        {'radius': 245, 'color': "#FF0808"}, 
        {'radius': 230, 'color': '#FF69B4'}, 
        {'radius': 215, 'color': '#DB7093'}, 
        {'radius': 200, 'color': '#C71585'}, 
        {'radius': 185, 'color': '#DA70D6'}, 
        {'radius': 170, 'color': '#BA55D3'}, 
        {'radius': 155, 'color': '#9932CC'}, 
        {'radius': 140, 'color': '#8A2BE2'}, 
        {'radius': 125, 'color': 'black'},   
    ]

    INNER_RADIUS_RATIO = 0.85 
    STAR_POINTS = 8
    ANGLE_OFFSET = 360 / (STAR_POINTS * 2) 

    for layer in star_layers:
        outer_r = layer['radius']
        inner_r = outer_r * INNER_RADIUS_RATIO
        vertices = get_star_vertices(outer_r, inner_r, STAR_POINTS, ANGLE_OFFSET)
        draw_polygon(t, vertices, layer['color'])

    draw_layered_flower(t)

    t.goto(0, 0)
    t.dot(45, '#8B0000') 

    screen.update()
    print("Drawing complete! Click on the window to exit.")
    screen.exitonclick()

if __name__ == "__main__":
    create_pookalam_design()

