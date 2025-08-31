import math

RES = WIDTH, HEIGHT = 1920, 1080
EWIDTH = 1620
FPS = 30

player_angle = 0
player_rotation_speed = 0.004
player_base_speed = 0.002
player_fov = math.pi / 3
half_fov = player_fov / 2
num_rays = EWIDTH // 4
half_num_rays = num_rays // 2
delta_angle = player_fov / num_rays
max_depth = 20
half_HEIGHT = HEIGHT // 2
screen_dist = half_HEIGHT / math.tan(half_fov)
scale = EWIDTH / num_rays

goldcolour = [
    (184, 134, 11),
    (133, 96, 9),
    (107, 75, 0)]
goldinter = goldcolour + [(70, 70, 70)]
TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2

with open("maze.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    mazedimensions = len(lines)
    availibledimensions = mazedimensions // 2
file.close()
tile_size = min(RES) / mazedimensions
