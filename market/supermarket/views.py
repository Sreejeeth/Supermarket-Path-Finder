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

# from supermarket.examples.pathfinding.prototype import *



unique_list=[]
boolean=True
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

# def about(request):
#     return render(request, 'about.html')  
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
    print("haaaaalo")
    gg.runpgm(request)
    print("home3")
    pg.quit()

    # sys.exit()
    return render(request,'home2.html')


def home3(request):
    
    cart_2=Cart(request)
                                                       

    start1(cart_2)
    

    return render(request,'about.html')

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
    # print("caaaaart")
    # print(cart)
    # for item in cart:
    #     print(item['product'])
    return render(request,'about.html',about_dict)



def Tempcart(request):
    global cart
    cart=Cart(request)





def about1(request):
   
    return render(request,'about1.html')

# global TempCart
# cart_lst=[]
# global cart
# def TempCart(request):
#     # initialize all variables and do all the setup for a new game
#         # global cart
#     # global cart    
#     cart = Cart(request)
    # global cart_lst
    # cart_lst=[]

# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Productdb.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request, 'list.html', {'category': category,
#                                                       'categories': categories,
#                                                       'products': products})
def product_detail(request, id, slug):
    product = get_object_or_404(Productdb, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

class Game:
    # global Tempcart
    # def Tempcart(request):

    #     global cart
    #     cart= Cart(request)
    #     return cart

    # def cartsystem():
    #     global request
    #     real_cart=Tempcart(request)

    # real_real_cart=cartsystem()
    # global Tempcart
    # global cart_lst
    # cart={}
    # def Tempcart(request):

    #     global cart
    #     cart= Cart(request)
        # return (request,cart)


    def __init__(self):
        global boolean
        pg.mixer.pre_init(44100, -16, 4, 2048)
        pg.init()
        self.screen = pg.display.set_mode((10+WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        # booleaZn=True



    def load_data(self):
        game_folder = ispath.dirname(__file__)
        img_folder = ispath.join(game_folder, 'img')
        
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
                print("items="+str(items))
                cart_lst.append(str(items)) 
        global unique_list        
        # unique_list = [] 
      
         # traverse for all elements 
        for x in cart_lst: 
        # check if exists in unique_list or not 
            if x not in unique_list: 
                unique_list.append(x) 
        # p=Player(self, 16,48)

        # p.draw_text('Path length:{}'.format(total_dist/2), 30, GREEN, WIDTH - 10, HEIGHT - 45)
        
        # pg.display.flip()      
        for tile_object in self.map.tmxdata.objects:
            
            obj_center = vec(tile_object.x + tile_object.width / 2,
                             tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)
            # global cart 
            # for item in cart:
            #     items=item['product']
            #     print("items="+str(items))
            #     cart_lst.append(str(items))
            # def unique(list1): 
      
            #  # intilize a null list 
            # unique_list = [] 
          
            #  # traverse for all elements 
            # for x in cart_lst: 
            # # check if exists in unique_list or not 
            #     if x not in unique_list: 
            #         unique_list.append(x)    
                    

                   
            item_lst=['Cheese','Banana', 'Grapes']  
            if tile_object.name in unique_list:    # use item in cart .. find out the value of product(eg cheese)... if that value is present, add to dictionary as {product:vec}
                Item(self, obj_center, tile_object.name)  # change to all characters to small case.. it will work
        # print(cart_lst)

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
            # print("is it going?")
            # print("False")

        while self.playing:
            # print("yes")
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
        self.all_sprites.update()
        self.camera.update(self.player)
        hits = pg.sprite.spritecollide(self.player, self.items, False)
        global unique_list
        for hit in hits:
            for thing in unique_list:

                # print(thing)
                if hit.type == thing:
                    
                    # print("hits")
                    
                    window=Tk()
                    
                    window.withdraw()

                    
                    messagebox.showinfo("Cart", "Adding item to cart")
                   
                    window.deiconify()
                    window.destroy()
                    window.quit()

                    # if answer=='yes':
                    hit.kill()





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

        # p.draw_text('Path length:{}'.format(total_dist), 30, GREEN, WIDTH - 10, HEIGHT - 45)
        
        # pg.display.flip()

    def events(self,request):
        # catch all events here
        global boolean
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # self.quit()
                # boolean=False
                # print("Flag")
                # boolean=False
                print("event")
                self.playing=False
                boolean=False
                # print("boolean")
                # print(boolean)
                # pg.quit()
                # sys.exit()
                # return render(request, 'about.html')

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    # self.quit()
                   # boolean=False
                   print("event")
                   self.playing=False
                   boolean=False
                   # print("False")
                   # return render(request, 'about.html')
                if event.key == pg.K_h:
                    self.draw_debug = not self.draw_debug
                if event.key == pg.K_p:
                    self.paused = not self.paused
                if event.key == pg.K_n:
                    self.night = not self.night

    def show_start_screen(self):
        pass

    def draw_text(self, text, font_name, size, color, x, y, align="topleft"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(**{align: (x, y)})
        self.screen.blit(text_surface, text_rect)    

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

        
                    
    def runpgm(self,request):
        g = Game()
        g.show_start_screen()
        # self.playing=True
        global boolean
        # boolean=True

        print("Boooooolean in runpgm")
        print(boolean)
        while boolean:
            g.new(request)
            print("asdasdadasdsadasdadasd")
            g.run(request)
            # self.quit()
            print("111111111111111111111111111111111111111asdasdadasdsadasdadasd")
            print(boolean)
            # if boolean==False:
            # pg.display.flip()
            # g.show_go_screen()

        # if boolean==False:
        #     print("asdasdasd")
            # pg.quit()
            # self.quit()

        # return render(request, 'about.html') 
