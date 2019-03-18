from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
# #from sirmvit.models import Studentdbs,Category
# from django.shortcuts import render, get_object_or_404

# from django.db.models import Q
# from django.contrib import messages






# @login_required
# def home(request, category_slug=None):
#     # category = None
#     # categories = Category.objects.all()
#     # products = Studentdbs.objects.filter(available=True)
#     # if category_slug:
#     #     category = get_object_or_404(Category, slug=category_slug)
#     #     products = products.filter(category=category)
#     return render(request, 'home.html')


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})


from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import pygame as pg
import sys
from random import choice, random
from os import path
from supermarket.settings2 import *
from supermarket.sprites import *
from supermarket.tilemap import *

@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def front(request):
    return render(request, 'front.html')  

def logout(request):
  auth.logout(request)
  # Redirect to a success page.
  return HttpResponseRedirect("/account/loggedout/")

def help(request):
    gg=Game()
    gg.runpgm()
    return render(request,'home2.html')



class Game:
    def __init__(self):
        pg.mixer.pre_init(44100, -16, 4, 2048)
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    # 

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        
        self.map_folder = path.join(game_folder, 'maps')
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0, 0, 0, 180))
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.item_images = {}
        for item in ITEM_IMAGES:
            self.item_images[item] = pg.image.load(path.join(img_folder, ITEM_IMAGES[item])).convert_alpha()     

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.map = TiledMap(path.join(self.map_folder, 'level1.tmx'))
        self.map_img = self.map.make_map()
        self.map.rect = self.map_img.get_rect()
        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2,
                             tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)  
            if tile_object.name in ['item1', 'item2','item3', 'item4']:
                Item(self, obj_center, tile_object.name)  
        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False
        self.paused = False
        self.night = False
        
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0  # fix for Python 2.x
            self.events()
            if not self.paused:
                self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()



    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        hits = pg.sprite.spritecollide(self.player, self.items, False)
        
        for hit in hits:
            if hit.type == 'item1dup':
                hit.type='item1'
                hit.kill()         
            if hit.type == 'item2dup':
                hit.type='item2'
                hit.kill()

            if hit.type == 'item3dup':
                hit.type='item3'
                hit.kill()

            if hit.type == 'item4dup':
                hit.type='item4'
                hit.kill() 
            if hit.type=='item1':
                hit.kill()                                                                                         # removes items 
                                                                                                   # removes items 
                
    # def draw_grid(self):
    #     for x in range(0, WIDTH, TILESIZE):
    #         pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
    #     for y in range(0, HEIGHT, TILESIZE):
    #         pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))


    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply(self.map))
        # self.draw_grid()
        for sprite in self.all_sprites:
            # print(sprite.image)# i think this constantly changes the position of the player(sprite)
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
        if self.draw_debug:
            for wall in self.walls:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(wall.rect), 1)

        # pg.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        if self.night:
            self.render_fog()
        # HUD functions
        if self.paused:
            self.screen.blit(self.dim_screen, (0, 0))
            self.draw_text("Paused", self.title_font, 105, RED, WIDTH / 2, HEIGHT / 2, align="center")
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_h:
                    self.draw_debug = not self.draw_debug
                if event.key == pg.K_p:
                    self.paused = not self.paused
                if event.key == pg.K_n:
                    self.night = not self.night

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", self.title_font, 100, RED,
                       WIDTH / 2, HEIGHT / 2, align="center")
        self.draw_text("Press a key to start", self.title_font, 75, WHITE,
                       WIDTH / 2, HEIGHT * 3 / 4, align="center")
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        pg.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False

        
                    
    def runpgm(self):
        g = Game()
        g.show_start_screen()
        while True:
            g.new()
            g.run()
            g.show_go_screen()


        return render(request, 'home2.html') 
