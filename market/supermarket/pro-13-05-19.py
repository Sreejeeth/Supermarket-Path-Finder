
import pygame as pg
from os import path as ospath
import heapq
vec = pg.math.Vector2

# screen =pg.display.set_mode((0, 0))
DARKGRAY = (40, 40, 40)

TILESIZE = 32
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
        start=vec(20,0)
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
        walls = [(1,1),(10, 7), (11, 7), (12, 7), (13, 7), (14, 7), (15, 7), (16, 7), (7, 7), (6, 7), (5, 7), (5, 5), (5, 6), (1, 6), (2, 6), (3, 6), (5, 10), (5, 11), (5, 12), (5, 9), (5, 8), (12, 8), (12, 9), (12, 10), (12, 11), (15, 14), (15, 13), (15, 12), (15, 11), (15, 10), (17, 7), (18, 7), (21, 7), (21, 6), (21, 5), (21, 4), (21, 3), (22, 5), (23, 5), (24, 5), (25, 5), (18, 10), (20, 10), (19, 10), (21, 10), (22, 10), (23, 10), (14, 4), (14, 5), (14, 6), (14, 0), (14, 1), (9, 2), (9, 1), (7, 3), (8, 3), (10, 3), (9, 3), (11, 3), (2, 5), (2, 4), (2, 3), (2, 2), (2, 0), (2, 1), (0, 11), (1, 11), (2, 11), (21, 2), (20, 11), (20, 12), (23, 13), (23, 14), (24, 10), (25, 10), (6, 12), (7, 12), (10, 12), (11, 12), (12, 12), (5, 3), (6, 3), (5, 4)]
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
        goal1=[vec(0,9),vec(14,8),vec(8,4),vec(10,8),vec(25,3),vec(9,6)]
        # global start
        start = vec(20, 0)
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


