import pygame
import math
import numpy as np

def draw_square(x, y, size, color):
    pygame.draw.rect(window, color, (x, y, size, size))
    
def draw_circle(x, y, size, color):
    pygame.draw.circle(window, color, (x, y), size)
    
# move robot
def move_robot(x, y):
    robot_position[0] += x
    robot_position[1] += y
    return robot_position

# Inicjalizacja pygame
pygame.init()

# Ustawienia okna
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Gra 2D")

# Kolory
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Okrągły robot
robot_radius = 20
robot_position = [window_width//2, window_height//2]
robot_color = green

# Przeszkody
obstacle_radius = 50
obstacle_color = red
obstacle_positions = [
    [100, 100],
    [200, 300],
    [400, 200],
]

#pozycja początkowa roota

MR = [0, 0]

# Funkcja mierząca odległość
def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance
    
# Główna pętla gry
running = True
while running:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rysowanie tła
    window.fill(white)

    # Rysowanie przeszkód
    for obstacle in obstacle_positions:
        pygame.draw.circle(window, obstacle_color, obstacle, obstacle_radius)

    # Rysowanie robota
    
    MR = move_robot(MR[0] + np.random.randint(-1,1), MR[1]+ np.random.randint(-1,1))

    pygame.draw.circle(window, robot_color,  MR[0],  MR[1]) )



    # Mierzenie odległości
    for obstacle in obstacle_positions:
        distance = calculate_distance(robot_position[0], robot_position[1], obstacle[0], obstacle[1])
        if distance <= robot_radius + obstacle_radius:
            robot_color = red
            break
        else:
            robot_color = green
    draw_square(30,30,40 ,blue)
    # Aktualizacja ekranu
    pygame.display.update()

# Wyjście z gry
pygame.quit()
