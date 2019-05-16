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
from django.shortcuts import render, get_object_or_404

from supermarket.models import Productdb,Category,About
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import pygame as pg
import sys
from random import choice, random
from os import path as ispath
from supermarket.settings2 import *
from supermarket.sprites import *
from supermarket.tilemap import *
from tkinter import *
from tkinter import messagebox
from cart.forms import CartAddProductForm
from cart.cart import Cart
from supermarket.prototype import *
import time
# from supermarket.examples.pathfinding.prototype import *
global font_name
font_name = pg.font.match_font('hack')
no_of_items=0
i=0
dist_of_manual=0
def ini():
    global no_of_items
    no_of_items=0
possible_ans=0
unique_list=[]
boolean=True
boolean1=False
@login_required
def home(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Productdb.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'home.html', {'category': category,
                                                          'categories': categories,
                                                          'products': products})
    # return render(request,'home.html')

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



def virtual(request):
    return render(request, 'virtual.html')  

def front2(request):
    return render(request, 'front2.html')  

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        # item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   # 'update': True})
        print(item)                                                           

def logout(request):
  auth.logout(request)
  # Redirect to a success page.
  return HttpResponseRedirect("/account/loggedout/")

def help(request):
    gg=Game()
    gg.runpgm(request)
    pg.quit()
    global boolean5
    boolean5=True

    return render(request,'home2.html')


def home3(request):
    
    #   global dist_of_manual
    # global possible_ans
    global boolean,boolean5,dist_of_manual
    boolean=True
    global i
    boolean5=True
    cart_2=Cart(request)
    global possible_ans
    global i
    i=i+1
    if i==1:                               
        possible_ans=start1(cart_2,boolean5)
        
    boolean5=False
    dist_of_manual=number()
    pg.quit()


  
    VarA=dist_of_manual
    VarB=possible_ans
    dict_compare={
    'dist_of_manual1': VarA,
    'possible_ans1': VarB,
    }
    return render(request,'compare.html',dict_compare)

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Productdb.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})

def about(request):
    about_list = About.objects.all()
    about_dict = {"about_records":about_list}
    # cart = Cart(request)
    global boolean,boolean5
    global dist_of_manual
    global i
    boolean5=True
    boolean=True
    toggle()
    dist_of_manual=number()
    i=0
    global tot_dist
    tot_dist=0
    return render(request,'about.html',about_dict)



def Tempcart(request):
    global cart
    cart=Cart(request)



def compare(request):
    # global tot_dist
    global dist_of_manual
    global possible_ans
    VarA=dist_of_manual
    VarB=possible_ans
    dict_compare={
    'dist_of_manual1': VarA,
    'possible_ans1': VarB,
    }
  
    return render(request,'compare.html',dict_compare)

def thanks(request):
   
    return render(request,'thanks.html')

def product_detail(request, id, slug):
    product = get_object_or_404(Productdb, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

class Game:

    def __init__(self):
        global boolean
        pg.mixer.pre_init(44100, -16, 4, 2048)
        pg.init()
        self.screen = pg.display.set_mode((10+WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()



    def load_data(self):
        game_folder = ispath.dirname(__file__)
        img_folder = ispath.join(game_folder, 'img')
        self.title_font = ispath.join(img_folder, 'ZOMBIE.TTF')
        
        self.map_folder = ispath.join(game_folder, 'maps')
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0, 0, 0, 180))
        self.player_img = pg.image.load(ispath.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.item_images = {}
        for item in ITEM_IMAGES:
            self.item_images[item] = pg.image.load(ispath.join(img_folder, ITEM_IMAGES[item])).convert_alpha()     

    def new(self,request):

        
        # global request
        global cart_lst
        cart_lst=[]
        cart=Cart(request)
        global tot_dist
        tot_dist=0
        # req,usable_cart=Tempcart(request)
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.items = pg.sprite.Group()
        # self.map = TiledMap(path.join(self.map_folder, 'level1.tmx'))
        self.map = TiledMap(ispath.join(self.map_folder, 'file_map_final.tmx'))

        self.map_img = self.map.make_map()
        self.map.rect = self.map_img.get_rect()
        for item in cart:
                items=item['product']
                cart_lst.append(str(items)) 
        global unique_list        
 
        for x in cart_lst: 
        # check if exists in unique_list or not 
            if x not in unique_list: 
                unique_list.append(x) 

        for tile_object in self.map.tmxdata.objects:
            
            obj_center = vec(tile_object.x + tile_object.width / 2,
                             tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)

            item_lst=['Cheese','Banana', 'Grapes']  
            if tile_object.name in unique_list:    # use item in cart .. find out the value of product(eg cheese)... if that value is present, add to dictionary as {product:vec}
                Item(self, obj_center, tile_object.name)  # change to all characters to small case.. it will work
        

        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False
        self.paused = False
        self.night = False
        
    def run(self,request):
        # game loop - set self.playing = False to end the game
        self.playing = True
        global boolean
        if boolean==False:
            self.playing=False
        while self.playing:
 
            self.dt = self.clock.tick(FPS) / 1000.0  # fix for Python 2.x
            self.events(request)
            # print("Flag")
            if not self.paused:
                self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def donothing():
        filewin = Toplevel(root)
        button = Button(filewin, text="Do nothing button")
        button.pack()    

    def update(self):
        # update portion of the game loop
        global no_of_items
        global unique_list
        ini()
        global boolean
        u=len(unique_list)
        self.all_sprites.update()
        self.camera.update(self.player)
        hits = pg.sprite.spritecollide(self.player, self.items, False)
        # global unique_list
        for hit in hits:
            for thing in unique_list:

                if hit.type == thing:
                    window=Tk()                    
                    window.withdraw()      
                    no_of_items+=1
                    u=u-1                
                    messagebox.showinfo("Cart", "Adding item to card. {} item collected. {} items left to buy ".format(no_of_items,len(unique_list)-no_of_items))
                    # if no_of_items==len(unique_list):
                        # self.show_go_screen()
                        # pg.quit()
                        # boolean=False

                                     
                    window.deiconify()
                    window.destroy()
                    window.quit()
                    hit.kill()


    def draw_text1(self, text, size, color, x, y, align="topleft"):
        global font_name
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(**{align: (x, y)})
        self.screen.blit(text_surface, text_rect)  


    def draw(self):

        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.blit(self.map_img, self.camera.apply(self.map))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
        if self.draw_debug:
            for wall in self.walls:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(wall.rect), 1)
    def events(self,request):
        # catch all events here
        global boolean
        for event in pg.event.get():
            if event.type == pg.QUIT:
 
                self.playing=False
                boolean=False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
  
                   self.playing=False
                   boolean=False

                if event.key == pg.K_h:
                    self.draw_debug = not self.draw_debug
                if event.key == pg.K_p:
                    self.paused = not self.paused
                if event.key == pg.K_n:
                    self.night = not self.night

    def events1(self,request):
        # catch all events here
        global boolean
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

                # self.playing=False
                # boolean=False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pq.quit()
                   # self.playing=False
                   # boolean=False

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
        self.draw_text1("GAME OVER", 100, RED,
                       WIDTH / 2, HEIGHT / 2)
        self.draw_text1("Press a key to start",  75, WHITE,
                       WIDTH / 2, HEIGHT * 3 / 4)
        time.sleep(5)
        pg.display.flip()

        self.wait_for_key1()

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

    def wait_for_key1(self):
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

        
                    
    def runpgm(self,request):
        g = Game()
        g.show_start_screen()
        global boolean
        global tot_dist
        tot_dist=0
        while boolean:
            g.new(request)
            g.run(request)
        
            