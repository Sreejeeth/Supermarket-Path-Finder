
import pygame as pg
from os import path as ospath
import heapq
vec = pg.math.Vector2

# screen =pg.display.set_mode((0, 0))
DARKGRAY = (40, 40, 40)

TILESIZE = 10
GRIDWIDTH = 40
GRIDHEIGHT = 80
WIDTH = TILESIZE * GRIDWIDTH
HEIGHT = TILESIZE * GRIDHEIGHT
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FOREST = (34, 57, 10)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
DARKGRAY = (40, 40, 40)
MEDGRAY = (75, 75, 75)
LIGHTGRAY = (140, 140, 140)
# home_img=

# p=6
# o=6
# path={}
# goal1=[]
# cost={}
# start=vec(20,0)
# small=100000
# global g
# g=WeightedGrid(40,80)


# home_img= 
# arrow={}
boolean=True
def start1():

    global boolean
    if boolean==True:
        print("start1")
        global p,o,path,goal1,cost,start,small,arrows
        p=6
        o=6
        path={}
        goal1=[]
        cost={}
        start=vec(8,0)
        small=100000



        pg.init()
        global screen
        global WIDTH
        global HEIGHT
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        clock = pg.time.Clock()

        global font_name
        font_name = pg.font.match_font('hack')

        # global path
        icon_dir = ospath.join(ospath.dirname(__file__), '../icons')
        global home_img,cross_img,broom_img,bucket_img
        home_img = pg.image.load(ospath.join(icon_dir, 'home.png')).convert_alpha()
        home_img = pg.transform.scale(home_img, (50, 50))
        home_img.fill((0, 255, 0, 255), special_flags=pg.BLEND_RGBA_MULT)
        broom_img = pg.image.load(ospath.join(icon_dir, '1_broom.jpg')).convert_alpha()
        broom_img = pg.transform.scale(broom_img, (50, 50))
        broom_img.fill((0, 255, 0, 255), special_flags=pg.BLEND_RGBA_MULT)

        bucket_img = pg.image.load(ospath.join(icon_dir, '1_bucket.jpg')).convert_alpha()
        bucket_img = pg.transform.scale(bucket_img, (50, 50))
        bucket_img.fill((0, 255, 0, 255), special_flags=pg.BLEND_RGBA_MULT)
        cross_img = pg.image.load(ospath.join(icon_dir, 'cross.png')).convert_alpha()
        cross_img = pg.transform.scale(cross_img, (50, 50))
        cross_img.fill((255, 0, 0, 255), special_flags=pg.BLEND_RGBA_MULT)
        # global arrows
        arrows = {}
        arrow_img = pg.image.load(ospath.join(icon_dir, 'arrowRight.png')).convert_alpha()
        arrow_img = pg.transform.scale(arrow_img, (50, 50))
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            arrows[dir] = pg.transform.rotate(arrow_img, vec(dir).angle_to(vec(1, 0)))

        global g
        g = WeightedGrid(GRIDWIDTH, GRIDHEIGHT)


        walls = [(0,3),(1,3),(2,3),(0,4),(1,4),(2,4),(0,5),(1,5),(2,5),(0,6),(1,6),(2,6),(0,7),(1,7),(2,7),(0,8),(1,8),(2,8),(0,9),(1,9),(2,9),(0,10),(1,10),(2,10),(0,11),(1,11),(2,11),(0,12),(1,12),(2,12),(0,13),(1,13),(2,13),(0,14),(1,14),(2,14),(0,15),(1,15),(2,15),(0,16),(1,16),(2,16),(0,17),(1,17),(2,17),(0,18),(1,18),(2,18),(0,19),(1,19),(2,19),(0,20),(1,20),(2,20),(0,21),(1,21),(2,21),(0,22),(1,22),(2,22),(0,23),(1,23),(2,23),(0,24),(1,24),(2,24),(0,25),(1,25),(2,25),(0,26),(1,26),(2,26),(0,27),(1,27),(2,27),(0,28),(1,28),(2,28),(0,29),(1,29),(2,29),(0,30),(1,30),(2,30),(0,31),(1,31),(2,31),(0,32),(1,32),(2,32),(0,33),(1,33),(2,33),(0,34),(1,34),(2,34),(0,35),(1,35),(2,35),(0,36),(1,36),(2,36),(0,37),(1,37),(2,37),(0,38),(1,38),(2,38),(0,39),(1,39),(2,39),(0,40),(1,40),(2,40),(0,41),(1,41),(2,41),(0,42),(1,42),(2,42),(0,43),(1,43),(2,43),(0,44),(1,44),(2,44),(0,45),(1,45),(2,45),(0,46),(1,46),(2,46),(0,47),(1,47),(2,47),(0,48),(1,48),(2,48),(0,49),(1,49),(2,49),(0,50),(1,50),(2,50),(0,51),(1,51),(2,51),(0,52),(1,52),(2,52),(0,53),(1,53),(2,53),(0,54),(1,54),(2,54),(0,55),(1,55),(2,55),(0,56),(1,56),(2,56),(0,57),(1,57),(2,57),(0,58),(1,58),(2,58),(0,59),(1,59),(2,59),(0,60),(1,60),(2,60),(0,61),(1,61),(2,61),(0,62),(1,62),(2,62),(0,63),(1,63),(2,63),(0,64),(1,64),(2,64),(0,65),(1,65),(2,65),(0,66),(1,66),(2,66),(0,67),(1,67),(2,67),(0,68),(1,68),(2,68),(0,69),(1,69),(2,69),(0,70),(1,70),(2,70),(0,71),(1,71),(2,71),(0,72),(1,72),(2,72),(0,73),(1,73),(2,73),(0,74),(1,74),(0,75),(1,75),(0,76),(1,76),(0,77),(1,77),(0,78),(1,78),(2,78),(0,79),(1,79),(2,79),
        (3,79),(4,79),(5,79),(6,79),(7,79),(8,79),(9,79),(10,79),(11,79),(12,79),(13,79),(14,79),(15,79),(16,79),(17,79),(18,79),(19,79),(20,79),(21,79),(22,79),(23,79),(24,79),(25,79),(26,79),(27,79),(28,79),(29,79),(30,79),(31,79),(32,79),(33,79),(34,79),(35,79),(36,79),(37,79),(38,79),(39,79),(20,77),(21,77),(22,77),(20,78),(21,78),(22,78),
        (16,36),(17,36),(18,36),
        (16,37),(17,37),(18,37),
        (16,38),(17,38),(18,38),
        (16,39),(17,39),(18,39),
        (16,40),(17,40),(18,40),
        (16,41),    (17,41),    (18,41),
        (16,42),    (17,42),    (18,42),
        (16,43),    (17,43),    (18,43),
        (16,44),    (17,44),    (18,44),
        (16,45),    (17,45),    (18,45),
        (16,46),    (17,46),    (18,46),
        (16,47),    (17,47),    (18,47),
        (16,48),    (17,48),    (18,48),
        (16,49),    (17,49),    (18,49),
        (16,50),    (17,50),    (18,50),
        (16,51),    (17,51),    (18,51),
        (16,52),    (17,52),    (18,52),
        (16,53),    (17,53),    (18,53),
        (16,54),    (17,54),    (18,54),
        (16,55),    (17,55),    (18,55),
        (16,56),    (17,56),    (18,56),
        (16,57),    (17,57),    (18,57),
        (16,58),    (17,58),    (18,58),
        (16,59),    (17,59),    (18,59),
        (16,60),    (17,60),    (18,60),
        (16,61),    (17,61),    (18,61),
        (16,62),    (17,62),    (18,62),
        (16,63),    (17,63),    (18,63),
        (16,64),    (17,64),    (18,64),
        (16,65),    (17,65),    (18,65),
        (16,66),    (17,66),    (18,66),
        (16,67),    (17,67),    (18,67),
        (16,68),    (17,68),    (18,68),
        (16,69),    (17,69),    (18,69),
        (16,70),    (17,70),    (18,70),
        (16,71),    (17,71),    (18,71),
        (16,72),    (17,72),    (18,72),
        (16,73),    (17,73),    (18,73),
        (3,71), (4,71), (5,71), (6,71), (7,71), (8,71), (9,71), (10,71),(11,71),(12,71),(13,71),(14,71),(15,71),
        (3,72), (4,72), (5,72), (6,72), (7,72), (8,72), (9,72), (10,72),(11,72),(12,72),(13,72),(14,72),(15,72),
        (3,73), (4,73), (5,73), (6,73), (7,73), (8,73), (9,73), (10,73),(11,73),(12,73),(13,73),(14,73),(15,73),
        (8,28), (9,28),
        (8,29), (9,29),
        (8,30), (9,30),
        (8,31), (9,31),
        (8,32), (9,32),
        (8,33), (9,33),
        (8,34), (9,34),
        (8,35), (9,35),
        (8,36), (9,36),
        (8,37), (9,37),
        (8,38), (9,38),
        (8,39), (9,39),
        (8,40), (9,40),
        (8,41), (9,41),
        (8,42), (9,42),
        (8,43), (9,43),
        (8,44), (9,44),
        (8,45), (9,45),
        (8,46), (9,46),
        (8,47), (9,47),
        (8,48), (9,48),
        (8,49), (9,49),
        (8,50), (9,50),
        (8,51), (9,51),
        (8,52), (9,52),
        (8,53), (9,53),
        (8,54), (9,54),
        (8,55), (9,55),
        (8,56), (9,56),
        (8,57), (9,57),
        (8,58), (9,58),
        (8,59), (9,59),
        (8,60), (9,60),
        (8,61), (9,61),
        (8,62), (9,62),
        (8,63), (9,63),
        (8,64), (9,64),
        (10,28),(11,28),(12,28),(13,28),(14,28),(15,28),(16,28),(17,28),(18,28),(19,28),(20,28),(21,28),(22,28),(23,28),(24,28),(25,28),
        (10,29),(11,29),(12,29),(13,29),(14,29),(15,29),(16,29),(17,29),(18,29),(19,29),(20,29),(21,29),(22,29),(23,29),(24,29),(25,29),
        (24,30),    (25,30),
        (24,31),    (25,31),
        (24,32),    (25,32),
        (24,33),    (25,33),
        (24,34),    (25,34),
        (24,35),    (25,35),
        (24,36),    (25,36),
        (24,37),    (25,37),
        (24,38),    (25,38),
        (24,39),    (25,39),
        (24,40),    (25,40),
        (24,41),    (25,41),
        (23,48),    (24,48),    (25,48),
        (23,49),    (24,49),    (25,49),
        (23,50),    (24,50),    (25,50),
        (23,51),    (24,51),    (25,51),
        (23,52),    (24,52),    (25,52),
        (23,53),    (24,53),    (25,53),
        (23,54),    (24,54),    (25,54),
        (23,55),    (24,55),    (25,55),
        (23,56),    (24,56),    (25,56),
        (23,57),    (24,57),    (25,57),
        (26,48),    (27,48),    (28,48),    (29,48),    (30,48),    (31,48),    (32,48),
        (26,49),    (27,49),    (28,49),    (29,49),    (30,49),    (31,49),    (32,49),
        (26,50),    (27,50),    (28,50),    (29,50),    (30,50),    (31,50),    (32,50),
        (30,18),    (31,18),    (32,18),
        (30,19),    (31,19),    (32,19),
        (30,20),    (31,20),    (32,20),
        (30,21),    (31,21),    (32,21),
        (30,22),    (31,22),    (32,22),
        (30,23),    (31,23),    (32,23),
        (30,24),    (31,24),    (32,24),
        (30,25),    (31,25),    (32,25),
        (30,26),    (31,26),    (32,26),
        (30,27),    (31,27),    (32,27),
        (30,28),    (31,28),    (32,28),
        (30,29),    (31,29),    (32,29),
        (30,30),    (31,30),    (32,30),
        (30,31),    (31,31),    (32,31),
        (30,32),    (31,32),    (32,32),
        (30,33),    (31,33),    (32,33),
        (30,34),    (31,34),    (32,34),
        (30,35),    (31,35),    (32,35),
        (30,36),    (31,36),    (32,36),
        (30,37),    (31,37),    (32,37),
        (30,38),    (31,38),    (32,38),
        (30,39),    (31,39),    (32,39),
        (30,40),    (31,40),    (32,40),
        (30,41),    (31,41),    (32,41),
        (30,42),    (31,42),    (32,42),
        (30,43),    (31,43),    (32,43),
        (30,44),    (31,44),    (32,44),
        (30,45),    (31,45),    (32,45),
        (30,46),    (31,46),    (32,46),
        (30,47),    (31,47),    (32,47),
        (25,21),    (26,21),    (27,21),    (28,21),    (29,21),
        (25,22),    (26,22),    (27,22),    (28,22),    (29,22),
        (25,23),    (26,23),    (27,23),    (28,23),    (29,23),
        (38,22),    (39,22),
        (38,23),    (39,23),
        (38,24),    (39,24),
        (38,25),    (39,25),
        (38,26),    (39,26),
        (38,27),    (39,27),
        (38,28),    (39,28),
        (38,29),    (39,29),
        (38,30),    (39,30),
        (38,31),    (39,31),
        (38,32),    (39,32),
        (38,33),    (39,33),
        (38,34),    (39,34),
        (38,35),    (39,35),
        (38,36),    (39,36),
        (38,37),    (39,37),
        (38,38),    (39,38),
        (38,39),    (39,39),
        (38,40),    (39,40),
        (38,41),    (39,41),
        (38,42),    (39,42),
        (38,43),    (39,43),
        (38,44),    (39,44),
        (38,45),    (39,45),
        (38,46),    (39,46),
        (38,47),    (39,47),
        (38,48),    (39,48),
        (38,49),    (39,49),
        (38,50),    (39,50),
        (38,51),    (39,51),
        (38,52),    (39,52),
        (38,53),    (39,53),
        (38,54),    (39,54),
        (38,55),    (39,55),
        (38,56),    (39,56),
        (38,57),    (39,57),
        (38,58),    (39,58),
        (38,59),    (39,59),
        (38,60),    (39,60),
        (38,61),    (39,61),
        (38,62),    (39,62),
        (38,63),    (39,63),
        (38,64),    (39,64),
        (38,65),    (39,65),
        (38,66),    (39,66),
        (38,67),    (39,67),
        (38,68),    (39,68),
        (38,69),    (39,69),
        (38,70),    (39,70),
        (38,71),    (39,71),
        (38,72),    (39,72),
        (38,73),    (39,73),
        (38,74),    (39,74),
        (38,75),    (39,75),
        (38,76),    (39,76),
        (38,77),    (39,77),
        (38,78),    (39,78),
        (39,0),
        (39,1),
        (39,2),
        (39,3),
        (39,4),
        (35,0),
        (35,1),
        (35,2),
        (35,3),
        (35,4),
        (31,0),
        (31,1),
        (31,2),
        (31,3),
        (31,4),
        (27,0),
        (27,1),
        (27,2),
        (27,3),
        (27,4),
        (23,0),
        (23,1),
        (23,2),
        (23,3),
        (23,4),
        (30,58),    (31,58),    (32,58),
        (30,59),    (31,59),    (32,59),
        (30,60),    (31,60),    (32,60),
        (30,61),    (31,61),    (32,61),
        (30,62),    (31,62),    (32,62),
        (30,63),    (31,63),    (32,63),
        (30,64),    (31,64),    (32,64),
        (30,65),    (31,65),    (32,65),
        (30,66),    (31,66),    (32,66),
        (30,67),    (31,67),    (32,67),
        (30,68),    (31,68),    (32,68),
        (30,69),    (31,69),    (32,69),
        (30,70),    (31,70),    (32,70),
        (30,71),    (31,71),    (32,71),
        (23,65),    (24,65),    (25,65),
        (23,66),    (24,66),    (25,66),
        (23,67),    (24,67),    (25,67),
        (23,68),    (24,68),    (25,68),
        (23,69),    (24,69),    (25,69),
        (23,70),    (24,70),    (25,70),
        (17,7), (18,7),
        (17,8), (18,8),
        (17,9), (18,9),
        (17,10),    (18,10),
        (16,8),
        (16,9),
        (19,8),
        (19,9),
        (9,7),  (10,7),
        (9,8),  (10,8),
        (9,9),  (10,9),
        (9,10), (10,10),
        (8,8),
        (8,9),
        (11,8),
        (11,9),
        (9,15), (10,15),
        (9,16), (10,16),
        (9,17), (10,17),
        (9,18), (10,18),
        (8,16),
        (8,17),
        (11,16),
        (11,17),
        (17,15),    (18,15),
        (17,16),    (18,16),
        (17,17),    (18,17),
        (17,18),    (18,18),
        (16,16),
        (16,17),
        (19,16),
        (19,17),
        (3,78),(4,78),(5,78),(6,78),(7,78),(8,78),(9,78),(10,78),(11,78), (12,78), (13,78), (14,78) ,(15,78) ,(16,78) ,(17,78) ,(18,78), (19,78),(20,76),(21,76),(22,76),
        (23,78), (24,78) ,(25,78) ,(26,78), (27,78) ,(28,78) ,(29,78), (30,78), (31,78) ,(32,78) ,(33,78), (34,78) ,(35,78) ,(36,78) ,(37,78),


        ]        

        # walls = []
        for wall in walls:
            g.walls.append(vec(wall))


        # path={}

        c={}
        # p=6
        # o=6
        # global p
        # global o
        # global goal1
        goal1=[vec(40,9),vec(14,8),vec(8,4),vec(20,8),vec(25,3),vec(9,6)]
        # global start
        start = vec(8, 0)
        search_type = a_star_search

        for k in range(p):

            path[k] ,c[k] = search_type(g,goal1[k],start)



        # global small    
        small=100000



        goal_final=vec(0,0) 

        # global o
        for j in range(o):
            print(o)
            print(p)
            demo()

        print("is it ending here?") 
        pg.quit()
        boolean=False



def draw_text(text, size, color, x, y, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    screen.blit(text_surface, text_rect)




class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.connections = [vec(1, 0), vec(-1, 0), vec(0, 1), vec(0, -1)]
        # comment/uncomment this for diagonals:
        self.connections += [vec(1, 1), vec(-1, 1), vec(1, -1), vec(-1, -1)]

    def in_bounds(self, node):
        return 0 <= node.x < self.width and 0 <= node.y < self.height

    def passable(self, node):
        return node not in self.walls

    def find_neighbors(self, node):
        neighbors = [node + connection for connection in self.connections]
        neighbors = filter(self.in_bounds, neighbors)
        neighbors = filter(self.passable, neighbors)
        return neighbors

    def draw(self):
        for wall in self.walls:
            # print(wall)
            rect = pg.Rect(wall * TILESIZE, (TILESIZE, TILESIZE))
            pg.draw.rect(screen, LIGHTGRAY, rect)
            # if wall.x=='1':


class WeightedGrid(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    # def new(self):
    #     self.camera = Camera(self.width, self.height)

    # def update(self):
    #     # update portion of the game loop
    #     # self.all_sprites.update()
    #     global goal_center
    #     self.camera.update(goal_center)
        

    def cost(self, from_node, to_node):
        if (vec(to_node) - vec(from_node)).length_squared() == 1:
            # num= self.weights.get(to_node, 0) + 10
            # return num/32
            num= self.weights.get(to_node, 0) + 10
            return num
        else:
            # num= self.weights.get(to_node, 0) + 14
            # return num/32
            num= self.weights.get(to_node, 0) + 14
            return num
    def draw(self):
        # self.screen.blit(self.map_img, self.camera.apply(self.map))
        # g=Camera()
        # self.new()
        # self.update()
        for wall in self.walls:
            rect = pg.Rect(wall * TILESIZE, (TILESIZE, TILESIZE))
            pg.draw.rect(screen, LIGHTGRAY, rect)
            # if walls[1][1]==7:
            # broom_center = (vec(22,8).x * TILESIZE + TILESIZE / 2, vec(22,8).y * TILESIZE + TILESIZE / 2)
            # screen.blit(broom_img, broom_img.get_rect(center=broom_center))

            # bucket_center = (vec(21,7).x * TILESIZE + TILESIZE / 2, vec(21,7).y * TILESIZE + TILESIZE / 2)
            # screen.blit(bucket_img, bucket_img.get_rect(center=bucket_center))
            
        for tile in self.weights:
            x, y = tile
            rect = pg.Rect(x * TILESIZE + 3, y * TILESIZE + 3, TILESIZE - 3, TILESIZE - 3)
            pg.draw.rect(screen, FOREST, rect)

    # def new(self):
    #     self.camera = Camera(self.map.width, self.map.height)

    # def update(self):
    #     # update portion of the game loop
    #     # self.all_sprites.update()
    #     self.camera.update(self.player)
    #     # hits = pg.sprite.spritecollide(self.player, self.items, False)
    # def draw(self):
    #     # pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
    #     # self.screen.fill(BGCOLOR)
    #     self.screen.blit(self.map_img, self.camera.apply(self.map))
    #     # self.draw_grid()
    #     for sprite in self.all_sprites:
    #         # print(sprite.image)# i think this constantly changes the position of the player(sprite)
    #         self.screen.blit(sprite.image, self.camera.apply(sprite))
    #         if self.draw_debug:
    #             pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
    #     if self.draw_debug:
    #         for wall in self.walls:
    #             pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(wall.rect), 1)


class PriorityQueue:
    def __init__(self):
        self.nodes = []

    def put(self, node, cost):
        heapq.heappush(self.nodes, (cost, node))

    def get(self):
        return heapq.heappop(self.nodes)[1]

    def empty(self):
        return len(self.nodes) == 0

def draw_grid():
    for x in range(0, WIDTH, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))

def draw_icons():
    start_center = (goal.x * TILESIZE + TILESIZE / 2, goal.y * TILESIZE + TILESIZE / 2)
    screen.blit(home_img, home_img.get_rect(center=start_center))

    goal_center = (start.x * TILESIZE + TILESIZE / 2, start.y * TILESIZE + TILESIZE / 2)
    screen.blit(cross_img, cross_img.get_rect(center=goal_center))

    # broom_center = (vec(16,8).x * TILESIZE + TILESIZE / 2, vec(16,8).y * TILESIZE + TILESIZE / 2)
    # screen.blit(broom_img, broom_img.get_rect(center=goal_center))


def vec2int(v):
    return (int(v.x), int(v.y))

def heuristic(a, b):
    # return abs(a.x - b.x) ** 2 + abs(a.y - b.y) ** 2
    return (abs(a.x - b.x) + abs(a.y - b.y)) * 10

def a_star_search(graph, start, end):
    frontier = PriorityQueue()
    frontier.put(vec2int(start), 0)
    path = {}
    cost = {}
    total_cost=0
    path[vec2int(start)] = None
    cost[vec2int(start)] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == end:
            break
        for next in graph.find_neighbors(vec(current)):
            next = vec2int(next)
            next_cost = cost[current] + graph.cost(current, next)
            if next not in cost or next_cost < cost[next]:
                cost[next] = next_cost
                priority = next_cost + heuristic(end, vec(next))
                frontier.put(next, priority)
                path[next] = vec(current) - vec(next)
                total_cost+=cost[next]

    return path, cost 

def dijkstra_search(graph, start, end):
    frontier = PriorityQueue()
    frontier.put(vec2int(start), 0)
    path = {}
    cost = {}
    path[vec2int(start)] = None
    cost[vec2int(start)] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == end:
            break
        for next in graph.find_neighbors(vec(current)):
            next = vec2int(next)
            next_cost = cost[current] + graph.cost(current, next)
            # print("next cost=")
            # print(next_cost)
            if next not in cost or next_cost < cost[next]:
                cost[next] = next_cost
                priority = next_cost
                frontier.put(next, priority)
                path[next] = vec(current) - vec(next)
    return path, cost


def cal_cost(goal_para,path_para):


    global goal_final  #doubtful
    global small  

    global start
    # global small
    goal=goal_para
    path=path_para

    current11 = start # + path[vec2int(start)]
    l = 0
    while current11 != goal:
        v = path[(current11.x, current11.y)]
        if v.length_squared() == 1:
            l += 10
        else:
            l += 14

        current11 = current11 + path[vec2int(current11)]

    if small>l:
        small=l

        goal_final=goal_para
        # print("goal_final")
        # print(goal_final)

    return small


def demo():
    search_type = a_star_search
    # small=100000
    global arrows
    global small
    global p
    global goal
    global goal1
    global path
    global start  

    for a in range(p):
        gg=goal1[a]
        pp=path[a]
        small=cal_cost(gg,pp)

    goal=goal_final
    # print("goal")
    # print(goal)


    global start

    path, c = search_type(g, goal, start)

    running = True
    while running:
        # clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                if event.key == pg.K_SPACE:
                    if search_type == a_star_search:
                        search_type = dijkstra_search
                    else:
                        search_type = a_star_search
                    path, c = search_type(g, goal, start)
                if event.key == pg.K_m:
                    # dump the wall list for saving
                    print([(int(loc.x), int(loc.y)) for loc in g.walls])


        # pg.display.set_caption("{:.2f}".format(clock.get_fps()))
        screen.fill(DARKGRAY)
        # fill explored area
        for node in path:
            x, y = node
            rect = pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
            pg.draw.rect(screen, MEDGRAY, rect)
        draw_grid()
        g.draw()
        # draw path from start to goal
        current = start # + path[vec2int(start)]
        l = 0
        while current != goal:
            v = path[(current.x, current.y)]
            if v.length_squared() == 1:
                l += 10
            else:
                l += 14


            img = arrows[vec2int(v)]
            x = current.x * TILESIZE + TILESIZE / 2
            y = current.y * TILESIZE + TILESIZE / 2
            r = img.get_rect(center=(x, y))
            screen.blit(img, r)
            # find next in path
            current = current + path[vec2int(current)]
        draw_icons()
        draw_text(search_type.__name__, 30, GREEN, WIDTH - 10, HEIGHT - 10, align="bottomright")
        draw_text('Path length:{}'.format(l), 30, GREEN, WIDTH - 10, HEIGHT - 45, align="bottomright")
        # print(l)
        pg.display.flip()

    print(start)
    start=goal
    # if p !=-1:
    goal1.remove(goal)
        
    print(goal)
    print(goal1)

    if len(goal1)<0:
        pg.quit()
        running=False
        # exit(0)
    small=100000
    # global p
    p=p-1
    for k in range(p):
        path[k] ,c[k] = search_type(g,goal1[k],start) 



