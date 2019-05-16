import pygame as pg
from os import path as ospath
import heapq
vec = pg.math.Vector2
from cart.forms import CartAddProductForm
from cart.cart import Cart
from supermarket.prototype import *
import time


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
ans=2
unique_list_prot=[]
boolean2=True
total_length=0

def dist():
    global total_length
    # print("total_length in prototype.py")
    # print(total_length)

def toggle():
    global boolean2
    boolean2=True


def start1(cart_prot,boolean5):
    global total_length
    total_length=0

    if boolean5==True:
        global cart_lst_prot
        cart_lst_prot=[]
        for item in cart_prot:
            items=item['product']
            # print("items="+str(items))
            cart_lst_prot.append(str(items)) 

        global unique_list_prot        
        for x in cart_lst_prot: 
        # check if exists in unique_list or not 
            if x not in unique_list_prot: 
                unique_list_prot.append(x) 
        global boolean2
        if boolean2==True:
            global p,o,path,goal1,cost,start,small,arrows
            p=len(unique_list_prot)
            o=len(unique_list_prot)
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
            home_img = pg.transform.scale(home_img, (20, 20))
            home_img.fill((0, 255, 0, 255), special_flags=pg.BLEND_RGBA_MULT)



            global sunglasses_img,eggs_img,rollerblades_img,mobile_img,dvd_img,tv_img,dishwasher_img,microwave_img,fridge_img,Ferns_img

            sunglasses_img = pg.image.load(ospath.join(icon_dir, 'specs.png')).convert_alpha()
            sunglasses_img = pg.transform.scale(sunglasses_img, (10, 10))

            eggs_img = pg.image.load(ospath.join(icon_dir, 'eggs.jpg')).convert_alpha()
            eggs_img = pg.transform.scale(eggs_img, (10, 10))

            Ferns_img = pg.image.load(ospath.join(icon_dir, 'Ferns.jpg')).convert_alpha()
            Ferns_img = pg.transform.scale(Ferns_img, (10, 10))


            rollerblades_img = pg.image.load(ospath.join(icon_dir, 'roller.png')).convert_alpha()
            rollerblades_img = pg.transform.scale(rollerblades_img, (10, 10))


            mobile_img = pg.image.load(ospath.join(icon_dir, 'cell.png')).convert_alpha()
            mobile_img = pg.transform.scale(mobile_img, (10, 10))

            dvd_img = pg.image.load(ospath.join(icon_dir, 'dvd.jpg')).convert_alpha()
            dvd_img = pg.transform.scale(dvd_img, (10, 10))


            tv_img = pg.image.load(ospath.join(icon_dir, 'TV.jpg')).convert_alpha()
            tv_img = pg.transform.scale(tv_img, (10, 10))


            dishwasher_img = pg.image.load(ospath.join(icon_dir, 'dishwasher.jpg')).convert_alpha()
            dishwasher_img = pg.transform.scale(dishwasher_img, (10, 10))


            microwave_img = pg.image.load(ospath.join(icon_dir, 'microwave.jpg')).convert_alpha()
            microwave_img = pg.transform.scale(microwave_img, (10, 10))


            fridge_img = pg.image.load(ospath.join(icon_dir, 'fridge.jpg')).convert_alpha()
            fridge_img = pg.transform.scale(fridge_img, (10, 10))

            global washingmachine_img,coffeemaker_img,ac_img,Cheese_Block_img,Lollipop_img, Saffola_gold_img,Chocos_img,up7_img,Red_Bull_img,Sprite_img,Orange_juice_img,Ketchup_img
            washingmachine_img = pg.image.load(ospath.join(icon_dir, 'wash.jpg')).convert_alpha()
            washingmachine_img = pg.transform.scale(washingmachine_img, (10, 10))


            coffeemaker_img = pg.image.load(ospath.join(icon_dir, 'coffee_make.jpg')).convert_alpha()
            coffeemaker_img = pg.transform.scale(coffeemaker_img, (10, 10))

            ac_img = pg.image.load(ospath.join(icon_dir, 'air_cond.jpg')).convert_alpha()
            ac_img = pg.transform.scale(ac_img, (10, 10))


            Cheese_Block_img = pg.image.load(ospath.join(icon_dir, 'Cheese_block.jpg')).convert_alpha()
            Cheese_Block_img = pg.transform.scale(Cheese_Block_img, (10, 10))

            Lollipop_img = pg.image.load(ospath.join(icon_dir, 'Lollipop.jpg')).convert_alpha()
            Lollipop_img = pg.transform.scale(Lollipop_img, (10, 10))

            Saffola_gold_img = pg.image.load(ospath.join(icon_dir, 'Saffola_gold.jpg')).convert_alpha()
            Saffola_gold_img = pg.transform.scale(Saffola_gold_img, (10, 10))

            Chocos_img = pg.image.load(ospath.join(icon_dir, 'Chocos.jpg')).convert_alpha()
            Chocos_img = pg.transform.scale(Chocos_img, (10, 10))

            up7_img = pg.image.load(ospath.join(icon_dir, '7up.jpg')).convert_alpha()
            up7_img = pg.transform.scale(up7_img, (10, 10))

            Red_Bull_img = pg.image.load(ospath.join(icon_dir, 'Red_Bull.jpg')).convert_alpha()
            Red_Bull_img = pg.transform.scale(Red_Bull_img, (10, 10))

            Sprite_img = pg.image.load(ospath.join(icon_dir, 'Sprite.jpg')).convert_alpha()
            Sprite_img = pg.transform.scale(Sprite_img, (10, 10))

            Orange_juice_img = pg.image.load(ospath.join(icon_dir, 'Orange_juice.jpg')).convert_alpha()
            Orange_juice_img = pg.transform.scale(Orange_juice_img, (10, 10))

            Ketchup_img = pg.image.load(ospath.join(icon_dir, 'Ketchup.jpg')).convert_alpha()
            Ketchup_img = pg.transform.scale(Ketchup_img, (10, 10))

            global Coca_cola_img,Pepsi_can_img,Diet_cola_img,Peanut_butter_img,Pickle_img,Mayonnaise_img,Honey_img,Rasgulla_500g_img,Tuna_can_img,Schezwan_sauce_img,Sardines_img

            Coca_cola_img = pg.image.load(ospath.join(icon_dir, 'Coca_cola.jpg')).convert_alpha()
            Coca_cola_img = pg.transform.scale(Coca_cola_img, (10, 10))

            Pepsi_can_img = pg.image.load(ospath.join(icon_dir, 'Pepsi_can.jpg')).convert_alpha()
            Pepsi_can_img = pg.transform.scale(Pepsi_can_img, (10, 10))

            Diet_cola_img = pg.image.load(ospath.join(icon_dir, 'Diet_cola.jpg')).convert_alpha()
            Diet_cola_img = pg.transform.scale(Diet_cola_img, (10, 10))

            Peanut_butter_img = pg.image.load(ospath.join(icon_dir, 'Peanut_butter.jpg')).convert_alpha()
            Peanut_butter_img = pg.transform.scale(Peanut_butter_img, (10, 10))

            Pickle_img = pg.image.load(ospath.join(icon_dir, 'Pickle.jpg')).convert_alpha()
            Pickle_img = pg.transform.scale(Pickle_img, (10, 10))

            Mayonnaise_img = pg.image.load(ospath.join(icon_dir, 'Mayonnaise.jpg')).convert_alpha()
            Mayonnaise_img = pg.transform.scale(Mayonnaise_img, (10, 10))

            Honey_img = pg.image.load(ospath.join(icon_dir, 'Honey.jpg')).convert_alpha()
            Honey_img = pg.transform.scale(Honey_img, (10, 10))

            Rasgulla_500g_img = pg.image.load(ospath.join(icon_dir, 'Rasgulla_500g.jpg')).convert_alpha()
            Rasgulla_500g_img = pg.transform.scale(Rasgulla_500g_img, (10, 10))

            Tuna_can_img = pg.image.load(ospath.join(icon_dir, 'Tuna_can.jpg')).convert_alpha()
            Tuna_can_img = pg.transform.scale(Tuna_can_img, (10, 10))

            Schezwan_sauce_img = pg.image.load(ospath.join(icon_dir, 'Schezwan_sauce.jpg')).convert_alpha()
            Schezwan_sauce_img = pg.transform.scale(Schezwan_sauce_img, (10, 10))

            Sardines_img = pg.image.load(ospath.join(icon_dir, 'Sardines.jpg')).convert_alpha()
            Sardines_img = pg.transform.scale(Sardines_img, (10, 10))

            global Maggi_noodles_img,Yippie_noodles_img,Canned_beans_img,Jalapenos_img,Sugar_img,Maize_img,Wai_wai_noodles_img,Chings_noodles_img,Eazy_softener_img,Tide_img,Surf_img 

            Maggi_noodles_img = pg.image.load(ospath.join(icon_dir, 'Maggi_noodles.jpg')).convert_alpha()
            Maggi_noodles_img = pg.transform.scale(Maggi_noodles_img, (10, 10))

            Yippie_noodles_img = pg.image.load(ospath.join(icon_dir, 'Yippie_noodles.jpg')).convert_alpha()
            Yippie_noodles_img = pg.transform.scale(Yippie_noodles_img, (10, 10))

            Canned_beans_img = pg.image.load(ospath.join(icon_dir, 'Canned_beans.jpg')).convert_alpha()
            Canned_beans_img = pg.transform.scale(Canned_beans_img, (10, 10))

            Jalapenos_img = pg.image.load(ospath.join(icon_dir, 'Jalapenos.jpg')).convert_alpha()
            Jalapenos_img = pg.transform.scale(Jalapenos_img, (10, 10))

            Sugar_img = pg.image.load(ospath.join(icon_dir, 'Sugar.jpg')).convert_alpha()
            Sugar_img = pg.transform.scale(Sugar_img, (10, 10))

            Maize_img = pg.image.load(ospath.join(icon_dir, 'Maize.jpg')).convert_alpha()
            Maize_img = pg.transform.scale(Maize_img, (10, 10))

            Wai_wai_noodles_img = pg.image.load(ospath.join(icon_dir, 'Wai_wai_noodles.jpg')).convert_alpha()
            Wai_wai_noodles_img = pg.transform.scale(Wai_wai_noodles_img, (10, 10))

            Chings_noodles_img = pg.image.load(ospath.join(icon_dir, 'Chings_noodles.jpg')).convert_alpha()
            Chings_noodles_img = pg.transform.scale(Chings_noodles_img, (10, 10))

            Eazy_softener_img = pg.image.load(ospath.join(icon_dir, 'Eazy_softener.jpg')).convert_alpha()
            Eazy_softener_img = pg.transform.scale(Eazy_softener_img, (10, 10))

            Tide_img = pg.image.load(ospath.join(icon_dir, 'Tide.jpg')).convert_alpha()
            Tide_img = pg.transform.scale(Tide_img, (10, 10))

            Surf_img = pg.image.load(ospath.join(icon_dir, 'Surf.jpg')).convert_alpha()
            Surf_img = pg.transform.scale(Surf_img, (10, 10))


            global Mr_muscle_img,Colin_img,Sparx_img,Bleach_img,Grapefruit_img,Lime_img,Avocado_img,Pomegranate_img,Lemon_img,litchi_img,Strawberry_img,Papaya_img,Banana_img,Pineapple_img


            Mr_muscle_img = pg.image.load(ospath.join(icon_dir, 'Mr_muscle.jpg')).convert_alpha()
            Mr_muscle_img = pg.transform.scale(Mr_muscle_img, (10, 10))

            Colin_img = pg.image.load(ospath.join(icon_dir, 'Colin.jpg')).convert_alpha()
            Colin_img = pg.transform.scale(Colin_img, (10, 10))

            Sparx_img = pg.image.load(ospath.join(icon_dir, 'Sparx.jpg')).convert_alpha()
            Sparx_img = pg.transform.scale(Sparx_img, (10, 10))

            Bleach_img = pg.image.load(ospath.join(icon_dir, 'Bleach.jpg')).convert_alpha()
            Bleach_img = pg.transform.scale(Bleach_img, (10, 10))

            Grapefruit_img = pg.image.load(ospath.join(icon_dir, 'Grapefruit.jpg')).convert_alpha()
            Grapefruit_img = pg.transform.scale(Grapefruit_img, (10, 10))

            Lime_img = pg.image.load(ospath.join(icon_dir, 'Lime.jpg')).convert_alpha()
            Lime_img = pg.transform.scale(Lime_img, (10, 10))

            Avocado_img = pg.image.load(ospath.join(icon_dir, 'Avocado.jpg')).convert_alpha()
            Avocado_img = pg.transform.scale(Avocado_img, (10, 10))

            Pomegranate_img = pg.image.load(ospath.join(icon_dir, 'Pomegranate.jpg')).convert_alpha()
            Pomegranate_img = pg.transform.scale(Pomegranate_img, (10, 10))

            Lemon_img = pg.image.load(ospath.join(icon_dir, 'Lemon.jpg')).convert_alpha()
            Lemon_img = pg.transform.scale(Lemon_img, (10, 10))

            litchi_img = pg.image.load(ospath.join(icon_dir, 'litchi.jpg')).convert_alpha()
            litchi_img = pg.transform.scale(litchi_img, (10, 10))

            Strawberry_img = pg.image.load(ospath.join(icon_dir, 'Strawberry.jpg')).convert_alpha()
            Strawberry_img = pg.transform.scale(Strawberry_img, (10, 10))

            Papaya_img = pg.image.load(ospath.join(icon_dir, 'Papaya.jpg')).convert_alpha()
            Papaya_img = pg.transform.scale(Papaya_img, (10, 10))

            Banana_img = pg.image.load(ospath.join(icon_dir, 'Banana.jpg')).convert_alpha()
            Banana_img = pg.transform.scale(Banana_img, (10, 10))

            Pineapple_img = pg.image.load(ospath.join(icon_dir, 'Pineapple.jpg')).convert_alpha()
            Pineapple_img = pg.transform.scale(Pineapple_img, (10, 10))

            global Mulberry_img,Grapes_img,Shrooms_img,Button_mushrooms_img,Chilly_img,Potatoes_img,Nectarine_img,Red_Apple_img,Shiitake_mushroom_img,Oyester_mushroom_img,Shrooms_img
            Mulberry_img = pg.image.load(ospath.join(icon_dir, 'Mulberry.jpg')).convert_alpha()
            Mulberry_img = pg.transform.scale(Mulberry_img, (10, 10))

            Grapes_img = pg.image.load(ospath.join(icon_dir, 'Grapes.jpg')).convert_alpha()
            Grapes_img = pg.transform.scale(Grapes_img, (10, 10))

            Shrooms_img = pg.image.load(ospath.join(icon_dir, 'Shrooms.jpg')).convert_alpha()
            Shrooms_img = pg.transform.scale(Shrooms_img, (10, 10))

            Button_mushrooms_img = pg.image.load(ospath.join(icon_dir, 'Button_mushrooms.jpg')).convert_alpha()
            Button_mushrooms_img = pg.transform.scale(Button_mushrooms_img, (10, 10))

            Chilly_img = pg.image.load(ospath.join(icon_dir, 'Chilly.jpg')).convert_alpha()
            Chilly_img = pg.transform.scale(Chilly_img, (10, 10))

            Potatoes_img = pg.image.load(ospath.join(icon_dir, 'Potatoes.jpg')).convert_alpha()
            Potatoes_img = pg.transform.scale(Potatoes_img, (10, 10))

            Nectarine_img = pg.image.load(ospath.join(icon_dir, 'Nectarine.jpg')).convert_alpha()
            Nectarine_img = pg.transform.scale(Nectarine_img, (10, 10))

            Red_Apple_img = pg.image.load(ospath.join(icon_dir, 'Red_Apple.jpg')).convert_alpha()
            Red_Apple_img = pg.transform.scale(Red_Apple_img, (10, 10))

            Shiitake_mushroom_img = pg.image.load(ospath.join(icon_dir, 'Shiitake_mushroom.jpg')).convert_alpha()
            Shiitake_mushroom_img = pg.transform.scale(Shiitake_mushroom_img, (10, 10))

            Oyester_mushroom_img = pg.image.load(ospath.join(icon_dir, 'Oyester_mushroom.jpg')).convert_alpha()
            Oyester_mushroom_img = pg.transform.scale(Oyester_mushroom_img, (10, 10))

            Shrooms_img = pg.image.load(ospath.join(icon_dir, 'Shrooms.jpg')).convert_alpha()
            Shrooms_img = pg.transform.scale(Shrooms_img, (10, 10))

            global Lilac_Turnip_img,Pumpkin_img,Carrots_img,Garlic_img,Chinese_Cabbage_img,Cabbage_img,Aubergine_img,Brocolli_img,Lemon_grass_img,Mackerel_img,Pompfret_img,Eel_fish_img
            Lilac_Turnip_img = pg.image.load(ospath.join(icon_dir, 'Lilac_Turnip.jpg')).convert_alpha()
            Lilac_Turnip_img = pg.transform.scale(Lilac_Turnip_img, (10, 10))

            Pumpkin_img = pg.image.load(ospath.join(icon_dir, 'Pumpkin.jpg')).convert_alpha()
            Pumpkin_img = pg.transform.scale(Pumpkin_img, (10, 10))

            Carrots_img = pg.image.load(ospath.join(icon_dir, 'Carrots.jpg')).convert_alpha()
            Carrots_img = pg.transform.scale(Carrots_img, (10, 10))

            Garlic_img = pg.image.load(ospath.join(icon_dir, 'Garlic.jpg')).convert_alpha()
            Garlic_img = pg.transform.scale(Garlic_img, (10, 10))

            Chinese_Cabbage_img = pg.image.load(ospath.join(icon_dir, 'Chinese_Cabbage.jpg')).convert_alpha()
            Chinese_Cabbage_img = pg.transform.scale(Chinese_Cabbage_img, (10, 10))

            Cabbage_img = pg.image.load(ospath.join(icon_dir, 'Cabbage.jpg')).convert_alpha()
            Cabbage_img = pg.transform.scale(Cabbage_img, (10, 10))

            Aubergine_img = pg.image.load(ospath.join(icon_dir, 'Aubergine.jpg')).convert_alpha()
            Aubergine_img = pg.transform.scale(Aubergine_img, (10, 10))

            Brocolli_img = pg.image.load(ospath.join(icon_dir, 'Brocolli.jpg')).convert_alpha()
            Brocolli_img = pg.transform.scale(Brocolli_img, (10, 10))

            Lemon_grass_img = pg.image.load(ospath.join(icon_dir, 'Lemon_grass.jpg')).convert_alpha()
            Lemon_grass_img = pg.transform.scale(Lemon_grass_img, (10, 10))

            Mackerel_img = pg.image.load(ospath.join(icon_dir, 'Mackerel.jpg')).convert_alpha()
            Mackerel_img = pg.transform.scale(Mackerel_img, (10, 10))

            Pompfret_img = pg.image.load(ospath.join(icon_dir, 'Pompfret.jpg')).convert_alpha()
            Pompfret_img = pg.transform.scale(Pompfret_img, (10, 10))

            Eel_fish_img = pg.image.load(ospath.join(icon_dir, 'Eel_fish.jpg')).convert_alpha()
            Eel_fish_img = pg.transform.scale(Eel_fish_img, (10, 10))

            global Katla_fish_img,Prawns_img,Ribs_img,Ham_img,Blue_fish_img,Chicken_leg_img,Rohu_fish_img,Mutton_img,Fish_cuts_img,Chicken_breast_img

            Katla_fish_img = pg.image.load(ospath.join(icon_dir, 'Katla_fish.jpg')).convert_alpha()
            Katla_fish_img = pg.transform.scale(Katla_fish_img, (10, 10))

            Prawns_img = pg.image.load(ospath.join(icon_dir, 'Prawns.jpg')).convert_alpha()
            Prawns_img = pg.transform.scale(Prawns_img, (10, 10))

            Ribs_img = pg.image.load(ospath.join(icon_dir, 'Ribs.jpg')).convert_alpha()
            Ribs_img = pg.transform.scale(Ribs_img, (10, 10))

            Ham_img = pg.image.load(ospath.join(icon_dir, 'Ham.jpg')).convert_alpha()
            Ham_img = pg.transform.scale(Ham_img, (10, 10))

            Blue_fish_img = pg.image.load(ospath.join(icon_dir, 'Blue_fish.jpg')).convert_alpha()
            Blue_fish_img = pg.transform.scale(Blue_fish_img, (10, 10))

            Rohu_fish_img = pg.image.load(ospath.join(icon_dir, 'Rohu_fish.jpg')).convert_alpha()
            Rohu_fish_img = pg.transform.scale(Rohu_fish_img, (10, 10))

            Chicken_leg_img = pg.image.load(ospath.join(icon_dir, 'Chicken_leg.jpg')).convert_alpha()
            Chicken_leg_img = pg.transform.scale(Chicken_leg_img, (10, 10))

            Mutton_img = pg.image.load(ospath.join(icon_dir, 'Mutton.jpg')).convert_alpha()
            Mutton_img = pg.transform.scale(Mutton_img, (10, 10))

            Fish_cuts_img = pg.image.load(ospath.join(icon_dir, 'Fish_cuts.jpg')).convert_alpha()
            Fish_cuts_img = pg.transform.scale(Fish_cuts_img, (10, 10))

            Chicken_breast_img = pg.image.load(ospath.join(icon_dir, 'Chicken_breast.jpg')).convert_alpha()
            Chicken_breast_img = pg.transform.scale(Chicken_breast_img, (10, 10))

            global Blue_cheese_img,Brown_Bread_img,Rye_img,Muffin_img,Pastry_img,vanish_img,lillies_img,lotus_img,daisy_img,milkcartons_img,toothpaste_img,whitepillow_img

            Blue_cheese_img = pg.image.load(ospath.join(icon_dir, 'Blue_cheese.jpg')).convert_alpha()
            Blue_cheese_img = pg.transform.scale(Blue_cheese_img, (10, 10))

            Brown_Bread_img = pg.image.load(ospath.join(icon_dir, 'Brown_Bread.jpg')).convert_alpha()
            Brown_Bread_img = pg.transform.scale(Brown_Bread_img, (10, 10))

            Rye_img = pg.image.load(ospath.join(icon_dir, 'Rye.jpg')).convert_alpha()
            Rye_img = pg.transform.scale(Rye_img, (10, 10))

            Muffin_img = pg.image.load(ospath.join(icon_dir, 'Muffin.jpg')).convert_alpha()
            Muffin_img = pg.transform.scale(Muffin_img, (10, 10))

            Pastry_img = pg.image.load(ospath.join(icon_dir, 'Pastry.jpg')).convert_alpha()
            Pastry_img = pg.transform.scale(Pastry_img, (10, 10))

            vanish_img = pg.image.load(ospath.join(icon_dir, '1_soap.jpg')).convert_alpha()
            vanish_img = pg.transform.scale(vanish_img, (10, 10))

            lillies_img = pg.image.load(ospath.join(icon_dir, 'b_lily.jpg')).convert_alpha()
            lillies_img = pg.transform.scale(lillies_img, (10, 10))

            lotus_img = pg.image.load(ospath.join(icon_dir, 'b_lotus.jpg')).convert_alpha()
            lotus_img = pg.transform.scale(lotus_img, (10, 10))

            daisy_img = pg.image.load(ospath.join(icon_dir, 'b_sunflower.jpg')).convert_alpha()
            daisy_img = pg.transform.scale(daisy_img, (10, 10))

            milkcartons_img = pg.image.load(ospath.join(icon_dir, 'only_milm.jpg')).convert_alpha()
            milkcartons_img = pg.transform.scale(milkcartons_img, (10, 10))

            toothpaste_img = pg.image.load(ospath.join(icon_dir, 'toothpaste.jpg')).convert_alpha()
            toothpaste_img = pg.transform.scale(toothpaste_img, (10, 10))

            whitepillow_img = pg.image.load(ospath.join(icon_dir, 'pillows.jpg')).convert_alpha()
            whitepillow_img = pg.transform.scale(whitepillow_img, (10, 10))

            global oliveoil_img,whiskey_img,gin_img,realwine_img,rawhoney_img,chocolatebar_img,hershey_img,cologne_img,compact_img,bodyconskirt_img,peplumtop_img,steamiron_img,nikoncamera_img
            oliveoil_img = pg.image.load(ospath.join(icon_dir, 'olive.jpg')).convert_alpha()
            oliveoil_img = pg.transform.scale(oliveoil_img, (10, 10))

            whiskey_img = pg.image.load(ospath.join(icon_dir, 'whiskey.jpg')).convert_alpha()
            whiskey_img = pg.transform.scale(whiskey_img, (10, 10))

            gin_img = pg.image.load(ospath.join(icon_dir, 'real_gin.jpg')).convert_alpha()
            gin_img = pg.transform.scale(gin_img, (10, 10))

            realwine_img = pg.image.load(ospath.join(icon_dir, 'real_wine.jpg')).convert_alpha()
            realwine_img = pg.transform.scale(realwine_img, (10, 10))

            rawhoney_img = pg.image.load(ospath.join(icon_dir, 'honeybee.jpg')).convert_alpha()
            rawhoney_img = pg.transform.scale(rawhoney_img, (10, 10))

            chocolatebar_img = pg.image.load(ospath.join(icon_dir, 'hershys.jpg')).convert_alpha()
            chocolatebar_img = pg.transform.scale(chocolatebar_img, (10, 10))

            hershey_img = pg.image.load(ospath.join(icon_dir, 'milmch.jpg')).convert_alpha()
            hershey_img = pg.transform.scale(hershey_img, (10, 10))

            cologne_img = pg.image.load(ospath.join(icon_dir, '3_fume.jpg')).convert_alpha()
            cologne_img = pg.transform.scale(cologne_img, (10, 10))

            compact_img = pg.image.load(ospath.join(icon_dir, '4_comp.jpg')).convert_alpha()
            compact_img = pg.transform.scale(compact_img, (10, 10))

            bodyconskirt_img = pg.image.load(ospath.join(icon_dir, 'a_skirt.jpg')).convert_alpha()
            bodyconskirt_img = pg.transform.scale(bodyconskirt_img, (10, 10))

            peplumtop_img = pg.image.load(ospath.join(icon_dir, 'a_top.jpg')).convert_alpha()
            peplumtop_img = pg.transform.scale(peplumtop_img, (10, 10))

            steamiron_img = pg.image.load(ospath.join(icon_dir, 'iron.jpg')).convert_alpha()
            steamiron_img = pg.transform.scale(steamiron_img, (10, 10))

            nikoncamera_img = pg.image.load(ospath.join(icon_dir, 'camera.jpg')).convert_alpha()
            nikoncamera_img = pg.transform.scale(nikoncamera_img, (10, 10))

            global yellowhotwheels_img,bluehotwheels_img,balloonskirt_img,pinktop_img,bluesweater_img,broom_img,wheat_img
            yellowhotwheels_img = pg.image.load(ospath.join(icon_dir, 'hotwheels.jpg')).convert_alpha()
            yellowhotwheels_img = pg.transform.scale(yellowhotwheels_img, (10, 10))

            bluehotwheels_img = pg.image.load(ospath.join(icon_dir, 'b_hotwheels.jpg')).convert_alpha()
            bluehotwheels_img = pg.transform.scale(bluehotwheels_img, (10, 10))

            balloonskirt_img = pg.image.load(ospath.join(icon_dir, 'a_oskirt.jpg')).convert_alpha()
            balloonskirt_img = pg.transform.scale(balloonskirt_img, (10, 10))

            pinktop_img = pg.image.load(ospath.join(icon_dir, 'a_dress.jpg')).convert_alpha()
            pinktop_img = pg.transform.scale(pinktop_img, (10, 10))

            bluesweater_img = pg.image.load(ospath.join(icon_dir, 'a_sweater.jpg')).convert_alpha()
            bluesweater_img = pg.transform.scale(bluesweater_img, (10, 10))

            broom_img = pg.image.load(ospath.join(icon_dir, '1_broom.jpg')).convert_alpha()
            broom_img = pg.transform.scale(broom_img, (10, 10))
            #broom_img.fill((0, 255, 0, 255), special_flags=pg.BLEND_RGBA_MULT)

            wheat_img = pg.image.load(ospath.join(icon_dir, 'only_wheat.jpg')).convert_alpha()
            wheat_img = pg.transform.scale(wheat_img, (10, 10))

            global coldcream_img,gloves_img,vacuum_img,watercan_img,greenbucket_img,wirebrush_img,wiper_img,dustpan_img,shovel_img,perfume_img,luxsoap_img,pinwheelcandy_img,strawberrycandy_img,milkcandy_img
            coldcream_img = pg.image.load(ospath.join(icon_dir, '3_cream.jpg')).convert_alpha()
            coldcream_img = pg.transform.scale(coldcream_img, (10, 10))

            gloves_img = pg.image.load(ospath.join(icon_dir, '1_gloves.jpg')).convert_alpha()
            gloves_img = pg.transform.scale(gloves_img, (10, 10))

            vacuum_img = pg.image.load(ospath.join(icon_dir, '1_vacuum.jpg')).convert_alpha()
            vacuum_img = pg.transform.scale(vacuum_img, (10, 10))

            watercan_img = pg.image.load(ospath.join(icon_dir, '1_can.jpg')).convert_alpha()
            watercan_img = pg.transform.scale(watercan_img, (10, 10))

            greenbucket_img = pg.image.load(ospath.join(icon_dir, '1_bucket.jpg')).convert_alpha()
            greenbucket_img = pg.transform.scale(greenbucket_img, (10, 10))

            wirebrush_img = pg.image.load(ospath.join(icon_dir, '4_brush.jpg')).convert_alpha()
            wirebrush_img = pg.transform.scale(wirebrush_img, (10, 10))

            wiper_img = pg.image.load(ospath.join(icon_dir, '3_broom.jpg')).convert_alpha()
            wiper_img = pg.transform.scale(wiper_img, (10, 10))

            dustpan_img = pg.image.load(ospath.join(icon_dir, '1_wiper.jpg')).convert_alpha()
            dustpan_img = pg.transform.scale(dustpan_img, (10, 10))

            shovel_img = pg.image.load(ospath.join(icon_dir, '1_shovel.jpg')).convert_alpha()
            shovel_img = pg.transform.scale(shovel_img, (10, 10))

            perfume_img = pg.image.load(ospath.join(icon_dir, '3_bot.jpg')).convert_alpha()
            perfume_img = pg.transform.scale(perfume_img, (10, 10))

            luxsoap_img = pg.image.load(ospath.join(icon_dir, 'soaps.jpg')).convert_alpha()
            luxsoap_img = pg.transform.scale(luxsoap_img, (10, 10))

            pinwheelcandy_img = pg.image.load(ospath.join(icon_dir, '6_candy.jpg')).convert_alpha()
            pinwheelcandy_img = pg.transform.scale(pinwheelcandy_img, (10, 10))

            strawberrycandy_img = pg.image.load(ospath.join(icon_dir, '7_candy.jpg')).convert_alpha()
            strawberrycandy_img = pg.transform.scale(strawberrycandy_img, (10, 10))

            milkcandy_img = pg.image.load(ospath.join(icon_dir, '5_candy.jpg')).convert_alpha()
            milkcandy_img = pg.transform.scale(milkcandy_img, (10, 10))

            global butterscotchtoffee_img,lavender_img,brownbag_img,satchelbag_img,yellowcushion_img,cushion_img,yellowpillow_img,bluepillow_img,brushes_img,sunscreen_img,lipstick_img
            butterscotchtoffee_img = pg.image.load(ospath.join(icon_dir, '1_candy.jpg')).convert_alpha()
            butterscotchtoffee_img = pg.transform.scale(butterscotchtoffee_img, (10, 10))

            lavender_img = pg.image.load(ospath.join(icon_dir, 'b_lavender.jpg')).convert_alpha()
            lavender_img = pg.transform.scale(lavender_img, (10, 10))

            brownbag_img = pg.image.load(ospath.join(icon_dir, 'bag_2.png')).convert_alpha()
            brownbag_img = pg.transform.scale(brownbag_img, (10, 10))

            satchelbag_img = pg.image.load(ospath.join(icon_dir, 'bag_1.png')).convert_alpha()
            satchelbag_img = pg.transform.scale(satchelbag_img, (10, 10))

            yellowcushion_img = pg.image.load(ospath.join(icon_dir, 'cushion.jpg')).convert_alpha()
            yellowcushion_img = pg.transform.scale(yellowcushion_img, (10, 10))

            cushion_img = pg.image.load(ospath.join(icon_dir, 'mpillows.jpg')).convert_alpha()
            cushion_img = pg.transform.scale(cushion_img, (10, 10))

            yellowpillow_img = pg.image.load(ospath.join(icon_dir, 'bypillow.jpg')).convert_alpha()
            yellowpillow_img = pg.transform.scale(yellowpillow_img, (10, 10))

            bluepillow_img = pg.image.load(ospath.join(icon_dir, 'bluepillow.jpg')).convert_alpha()
            bluepillow_img = pg.transform.scale(bluepillow_img, (10, 10))

            brushes_img = pg.image.load(ospath.join(icon_dir, '5_brushes.jpg')).convert_alpha()
            brushes_img = pg.transform.scale(brushes_img, (10, 10))

            sunscreen_img = pg.image.load(ospath.join(icon_dir, '4_tube.jpg')).convert_alpha()
            sunscreen_img = pg.transform.scale(sunscreen_img, (10, 10))

            lipstick_img = pg.image.load(ospath.join(icon_dir, '4_lips.jpg')).convert_alpha()
            lipstick_img = pg.transform.scale(lipstick_img, (10, 10))
            global niveacream_img,mopwiper_img,denimjacket_img,denimjaens_img,denimshirt_img
            niveacream_img = pg.image.load(ospath.join(icon_dir, '4_cream.jpg')).convert_alpha()
            niveacream_img = pg.transform.scale(niveacream_img, (10, 10))

            mopwiper_img = pg.image.load(ospath.join(icon_dir, '2_broom.jpg')).convert_alpha()
            mopwiper_img = pg.transform.scale(mopwiper_img, (10, 10))

            denimjacket_img = pg.image.load(ospath.join(icon_dir, 'a_denim.jpg')).convert_alpha()
            denimjacket_img = pg.transform.scale(denimjacket_img, (10, 10))

            denimjaens_img = pg.image.load(ospath.join(icon_dir, 'a_jean.jpg')).convert_alpha()
            denimjaens_img = pg.transform.scale(denimjaens_img, (10, 10))

            denimshirt_img = pg.image.load(ospath.join(icon_dir, 'a_shirt.jpg')).convert_alpha()
            denimshirt_img = pg.transform.scale(denimshirt_img, (10, 10))



            



            cross_img = pg.image.load(ospath.join(icon_dir, 'cross.png')).convert_alpha()
            cross_img = pg.transform.scale(cross_img, (20, 20))
            cross_img.fill((255, 0, 0, 255), special_flags=pg.BLEND_RGBA_MULT)
            # global arrows
            arrows = {}
            arrow_img = pg.image.load(ospath.join(icon_dir, 'arrowRight.png')).convert_alpha()
            arrow_img = pg.transform.scale(arrow_img, (5, 5))
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

            c={}

            for vector in unique_list_prot:
                if vector=="Nikon camera":
                    goal1.append(vec(16,18))
                if vector=="Bleach":
                    goal1.append(vec(37,28))
                if vector=="Brown bag":
                    goal1.append(vec(9,27))
                if vector=="7up":
                    goal1.append(vec(3,59))
                if vector=="Accessories":
                    goal1.append(vec(27,20))
                if vector=="Aubergine":
                    goal1.append(vec(24,77))
                if vector=="Avocado":
                    goal1.append(vec(37,39))
                if vector=="Balloon skirt":
                    goal1.append(vec(7,8))
                if vector=="Banana":
                    goal1.append(vec(37,59))
                if vector=="Blue cheese":
                    goal1.append(vec(6,73))
                if vector=="Blue fish":
                    goal1.append(vec(10,77))
                if vector=="Blue hotwheels":
                    goal1.append(vec(8,18))
                if vector=="Blue pillow":
                    goal1.append(vec(7,62))
                if vector=="Blue sweater":
                    goal1.append(vec(20,8))
                if vector=="Bodycon skirt":
                    goal1.append(vec(15,8))
                if vector=="Brocolli":
                    goal1.append(vec(26,77))
                if vector=="Broom":
                    goal1.append(vec(33,20))
                if vector=="Brown bread":
                    goal1.append(vec(13,74))
                if vector=="Butterscotch toffee":
                    goal1.append(vec(19,47))
                if vector=="Button mushrooms":
                    goal1.append(vec(37,69))
                if vector=="Cabbage":
                    goal1.append(vec(23,76))
                if vector=="Canned beans":
                    goal1.append(vec(3,20))
                if vector=="Carrots":
                    goal1.append(vec(32,77))
                if vector=="Cheese Block":
                    goal1.append(vec(3,74))
                if vector=="Cherry":
                    goal1.append(vec(37,49))
                if vector=="Chicken breast":
                    goal1.append(vec(4,77))
                if vector=="Chicken leg":
                    goal1.append(vec(2,75))
                if vector=="Chilly":
                    goal1.append(vec(37,67))
                if vector=="Chinese cabbage":
                    goal1.append(vec(36,77))
                if vector=="Chings noodles":
                    goal1.append(vec(3,14))
                if vector=="Chocolate":
                    goal1.append(vec(15,48))
                if vector=="Chocos":
                    goal1.append(vec(3,69))
                if vector=="Coca cola":
                    goal1.append(vec(3,53))
                if vector=="Cold cream":
                    goal1.append(vec(29,19))
                if vector=="Colin":
                    goal1.append(vec(37,32))
                if vector=="Cushions":
                    goal1.append(vec(7,43))
                if vector=="Daisy":
                    goal1.append(vec(33,67))
                if vector=="Denim jacket":
                    goal1.append(vec(9,6))
                if vector=="Denim jeans":
                    goal1.append(vec(9,11))
                if vector=="Denim shirt":
                    goal1.append(vec(17,6))
                if vector=="Diet cola":
                    goal1.append(vec(3,57))
                if vector=="Dustpan":
                    goal1.append(vec(33,33))
                if vector=="Eazy softener":
                    goal1.append(vec(37,26))
                if vector=="Eggs":
                    goal1.append(vec(26,67))
                if vector=="Eu de cologne":
                    goal1.append(vec(29,42))
                if vector=="Ferns":
                    goal1.append(vec(33,60))
                if vector=="Fish cuts":
                    goal1.append(vec(2,77))
                if vector=="Gardening gloves":
                    goal1.append(vec(22,54))
                if vector=="Garlic":
                    goal1.append(vec(34,77))
                if vector=="Gin":
                    goal1.append(vec(10,69))
                if vector=="Grapefruit":
                    goal1.append(vec(37,43))
                if vector=="Grapes":
                    goal1.append(vec(37,53))
                if vector=="Green bucket":
                    goal1.append(vec(27,51))
                if vector=="Ham":
                    goal1.append(vec(8,77))
                if vector=="Hersheys":
                    goal1.append(vec(15,54))
                if vector=="Honey":
                    goal1.append(vec(3,48))
                if vector=="Jalapenos":
                    goal1.append(vec(3,24))
                if vector=="Katla fish":
                    goal1.append(vec(18,77))
                if vector=="Ketchup":
                    goal1.append(vec(3,51))
                if vector=="Lakme compact":
                    goal1.append(vec(29,37))
                if vector=="Lavender":
                    goal1.append(vec(29,60))
                if vector=="Lemon":
                    goal1.append(vec(37,51))
                if vector=="Lemon grass":
                    goal1.append(vec(28,77))
                if vector=="Lilac turnip":
                    goal1.append(vec(30,77))
                if vector=="Lillies":
                    goal1.append(vec(29,66))
                if vector=="Lime":
                    goal1.append(vec(37,41))
                if vector=="Lipstick":
                    goal1.append(vec(27,24))
                if vector=="Lollipop":
                    goal1.append(vec(19,53))
                if vector=="Lotus":
                    goal1.append(vec(29,70))
                if vector=="Lux soap":
                    goal1.append(vec(26,38))
                if vector=="Mackerel":
                    goal1.append(vec(19,76))
                if vector=="Maggi noodles":
                    goal1.append(vec(3,16))
                if vector=="Maize":
                    goal1.append(vec(3,10))
                if vector=="Mayonnaise":
                    goal1.append(vec(3,45))
                if vector=="Milk candy":
                    goal1.append(vec(19,41))
                if vector=="Milk cartons":
                    goal1.append(vec(22,67))
                if vector=="Mop wiper":
                    goal1.append(vec(33,26))
                if vector=="Mr. muscle":
                    goal1.append(vec(37,34))
                if vector=="Muffin":
                    goal1.append(vec(19,65))
                if vector=="Mulberry":
                    goal1.append(vec(37,55))
                if vector=="Mutton":
                    goal1.append(vec(2,76))
                if vector=="Nectarine":
                    goal1.append(vec(37,63))
                if vector=="Nivea cream":
                    goal1.append(vec(29,31))
                if vector=="Olive oil":
                    goal1.append(vec(15,66))
                if vector=="Orange juice":
                    goal1.append(vec(3,65))
                if vector=="Oyester mushroom":
                    goal1.append(vec(37,73))
                if vector=="Papaya":
                    goal1.append(vec(37,45))
                if vector=="Pastry":
                    goal1.append(vec(19,59))
                if vector=="Peanut butter":
                    goal1.append(vec(3,39))
                if vector=="Peplum top":
                    goal1.append(vec(17,11))
                if vector=="Pepsi can":
                    goal1.append(vec(3,55))
                if vector=="Perfume":
                    goal1.append(vec(28,47))
                if vector=="Pickle":
                    goal1.append(vec(3,42))
                if vector=="Pineapple":
                    goal1.append(vec(37,57))
                if vector=="Pink top":
                    goal1.append(vec(12,8))
                if vector=="Pinwheel candy":
                    goal1.append(vec(15,37))
                if vector=="Pomegranate":
                    goal1.append(vec(37,37))
                if vector=="Pompfret":
                    goal1.append(vec(14,77))
                if vector=="Potatoes":
                    goal1.append(vec(37,65))
                if vector=="Prawn":
                    goal1.append(vec(19,79))
                if vector=="Pumpkin":
                    goal1.append(vec(37,77))
                if vector=="Rasgulla 500g":
                    goal1.append(vec(3,27))
                if vector=="Raw honey":
                    goal1.append(vec(15,60))
                if vector=="Red Bull":
                    goal1.append(vec(3,61))
                if vector=="Red apple":
                    goal1.append(vec(37,61))
                if vector=="Red wine":
                    goal1.append(vec(5,69))
                if vector=="Ribs":
                    goal1.append(vec(6,77))
                if vector=="Rohu fish":
                    goal1.append(vec(12,77))
                if vector=="Rye":
                    goal1.append(vec(19,71))
                if vector=="Saffola gold":
                    goal1.append(vec(3,67))
                if vector=="Sardines":
                    goal1.append(vec(3,36))
                if vector=="Satchel bag":
                    goal1.append(vec(7,31))
                if vector=="Schezwan sauce":
                    goal1.append(vec(3,33))
                if vector=="Shiitake mushroom":
                    goal1.append(vec(37,75))
                if vector=="Shovel":
                    goal1.append(vec(24,47))
                if vector=="Shrooms":
                    goal1.append(vec(37,71))
                if vector=="Sparx":
                    goal1.append(vec(37,30))
                if vector=="Sprite":
                    goal1.append(vec(3,63))
                if vector=="Steam iron":
                    goal1.append(vec(19,15))
                if vector=="Strawberry":
                    goal1.append(vec(37,47))
                if vector=="Strawberry candy":
                    goal1.append(vec(15,42))
                if vector=="Sugar":
                    goal1.append(vec(3,7))
                if vector=="Sunscreen":
                    goal1.append(vec(29,25))
                if vector=="Surf":
                    goal1.append(vec(37,22))
                if vector=="Tide":
                    goal1.append(vec(37,24))
                if vector=="Toothpaste":
                    goal1.append(vec(16,27))
                if vector=="Tuna can":
                    goal1.append(vec(3,30))
                if vector=="Vacuum cleaner":
                    goal1.append(vec(31,51))
                if vector=="Vanish":
                    goal1.append(vec(37,20))
                if vector=="Wai Wai noodles":
                    goal1.append(vec(3,12))
                if vector=="Watering can":
                    goal1.append(vec(26,54))
                if vector=="Wheat flour":
                    goal1.append(vec(3,4))
                if vector=="Whiskey":
                    goal1.append(vec(14,69))
                if vector=="White pillow":
                    goal1.append(vec(7,49))
                if vector=="Wiper":
                    goal1.append(vec(33,39))
                if vector=="Wire brush":
                    goal1.append(vec(33,45))
                if vector=="Yellow cushions":
                    goal1.append(vec(7,38))
                if vector=="Yellow pillow":
                    goal1.append(vec(7,56))
                if vector=="Yellow hotwheels":
                    goal1.append(vec(11,15))
                if vector=="Yippie noodles":
                    goal1.append(vec(3,18))
                if vector=="eel fish":
                    goal1.append(vec(16,77))
                if vector=="Air conditioner":
                    goal1.append(vec(23,27))
                if vector=="Coffee maker":
                    goal1.append(vec(26,32))
                if vector=="Washing machine":
                    goal1.append(vec(22,38))
                if vector=="Rerigerator":
                    goal1.append(vec(22,32))
                if vector=="Dishwasher":
                    goal1.append(vec(19,31))
                if vector=="Microwave":
                    goal1.append(vec(13,31))
                if vector=="TV":
                    goal1.append(vec(11,33))
                if vector=="DVD player":
                    goal1.append(vec(11,39))
                if vector=="Mobile":
                    goal1.append(vec(11,45))
                if vector=="Roller blades":
                    goal1.append(vec(11,51))
                if vector=="Sunglasses":
                    goal1.append(vec(11,56))
                if vector=="Clock":
                    goal1.append(vec(11,62))
               
            
            start = vec(8, 0)
            search_type = a_star_search

            for k in range(p):

                path[k] ,c[k] = search_type(g,goal1[k],start)


            # global small    
            small=100000



            goal_final=vec(0,0) 

            # global o
            for j in range(o):
                demo()
                if j==o-1:
                    time.sleep(5)


            # print("is it ending here?") 
            pg.quit()
            boolean2=False
            return total_length



def draw_text(text, size, color, x, y, align="topleft"):
    global font_name
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

    def cost(self, from_node, to_node):
        if (vec(to_node) - vec(from_node)).length_squared() == 1:

            num= self.weights.get(to_node, 0) + 10
            return num
        else:

            num= self.weights.get(to_node, 0) + 14
            return num
    def draw(self):

        for wall in self.walls:
            rect = pg.Rect(wall * TILESIZE, (TILESIZE, TILESIZE))
            pg.draw.rect(screen, LIGHTGRAY, rect)

            
        for tile in self.weights:
            x, y = tile
            rect = pg.Rect(x * TILESIZE + 3, y * TILESIZE + 3, TILESIZE - 3, TILESIZE - 3)
            pg.draw.rect(screen, FOREST, rect)

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

    broom_center1 = (vec(32,18).x * TILESIZE + TILESIZE / 2, vec(32,18).y * TILESIZE + TILESIZE / 2)
    screen.blit(broom_img, broom_img.get_rect(center=broom_center1))
    broom_center2 = (vec(32,19).x * TILESIZE + TILESIZE / 2, vec(32,19).y * TILESIZE + TILESIZE / 2)
    screen.blit(broom_img, broom_img.get_rect(center=broom_center2))
    broom_center3 = (vec(32,20).x * TILESIZE + TILESIZE / 2, vec(32,20).y * TILESIZE + TILESIZE / 2)
    screen.blit(broom_img, broom_img.get_rect(center=broom_center3))
    broom_center4 = (vec(32,21).x * TILESIZE + TILESIZE / 2, vec(32,21).y * TILESIZE + TILESIZE / 2)
    screen.blit(broom_img, broom_img.get_rect(center=broom_center4))
    broom_center5 = (vec(32,22).x * TILESIZE + TILESIZE / 2, vec(32,22).y * TILESIZE + TILESIZE / 2)
    screen.blit(broom_img, broom_img.get_rect(center=broom_center5))
    broom_center6 = (vec(32,23).x * TILESIZE + TILESIZE / 2, vec(32,23).y * TILESIZE + TILESIZE / 2)
    screen.blit(broom_img, broom_img.get_rect(center=broom_center6))

    coldcream_center1 = (vec(30,18).x * TILESIZE + TILESIZE / 2, vec(30,18).y * TILESIZE + TILESIZE / 2)
    screen.blit(coldcream_img, coldcream_img.get_rect(center=coldcream_center1))
    coldcream_center2 = (vec(30,19).x * TILESIZE + TILESIZE / 2, vec(30,19).y * TILESIZE + TILESIZE / 2)
    screen.blit(coldcream_img, coldcream_img.get_rect(center=coldcream_center2))
    coldcream_center3 = (vec(30,20).x * TILESIZE + TILESIZE / 2, vec(30,20).y * TILESIZE + TILESIZE / 2)
    screen.blit(coldcream_img, coldcream_img.get_rect(center=coldcream_center3))
    coldcream_center4 = (vec(30,21).x * TILESIZE + TILESIZE / 2, vec(30,21).y * TILESIZE + TILESIZE / 2)
    screen.blit(coldcream_img, coldcream_img.get_rect(center=coldcream_center4))


    wheat_center1 = (vec(0,3).x * TILESIZE + TILESIZE / 2, vec(0,3).y * TILESIZE + TILESIZE / 2)
    screen.blit(wheat_img, wheat_img.get_rect(center=wheat_center1))
    wheat_center2 = (vec(1,3).x * TILESIZE + TILESIZE / 2, vec(1,3).y * TILESIZE + TILESIZE / 2)
    screen.blit(wheat_img, wheat_img.get_rect(center=wheat_center2))
    wheat_center3 = (vec(2,3).x * TILESIZE + TILESIZE / 2, vec(2,3).y * TILESIZE + TILESIZE / 2)
    screen.blit(wheat_img, wheat_img.get_rect(center=wheat_center3))
    wheat_center4 = (vec(0,4).x * TILESIZE + TILESIZE / 2, vec(0,4).y * TILESIZE + TILESIZE / 2)
    screen.blit(wheat_img, wheat_img.get_rect(center=wheat_center4))
    wheat_center5 = (vec(1,4).x * TILESIZE + TILESIZE / 2, vec(1,4).y * TILESIZE + TILESIZE / 2)
    screen.blit(wheat_img, wheat_img.get_rect(center=wheat_center5))
    wheat_center6 = (vec(2,4).x * TILESIZE + TILESIZE / 2, vec(2,4).y * TILESIZE + TILESIZE / 2)
    screen.blit(wheat_img, wheat_img.get_rect(center=wheat_center6))
    wheat_center7 = (vec(0,5).x * TILESIZE + TILESIZE / 2, vec(0,5).y * TILESIZE + TILESIZE / 2)
    screen.blit(wheat_img, wheat_img.get_rect(center=wheat_center7))
    wheat_center8 = (vec(1,5).x * TILESIZE + TILESIZE / 2, vec(1,5).y * TILESIZE + TILESIZE / 2)
    screen.blit(wheat_img, wheat_img.get_rect(center=wheat_center8))
    wheat_center9 = (vec(2,5).x * TILESIZE + TILESIZE / 2, vec(2,5).y * TILESIZE + TILESIZE / 2)
    screen.blit(wheat_img, wheat_img.get_rect(center=wheat_center9))


    gloves_center1 = (vec(23,52).x * TILESIZE + TILESIZE / 2, vec(23,52).y * TILESIZE + TILESIZE / 2)
    screen.blit(gloves_img, gloves_img.get_rect(center=gloves_center1))
    gloves_center2 = (vec(23,53).x * TILESIZE + TILESIZE / 2, vec(23,53).y * TILESIZE + TILESIZE / 2)
    screen.blit(gloves_img, gloves_img.get_rect(center=gloves_center2))
    gloves_center3 = (vec(23,54).x * TILESIZE + TILESIZE / 2, vec(23,54).y * TILESIZE + TILESIZE / 2)
    screen.blit(gloves_img, gloves_img.get_rect(center=gloves_center3))
    gloves_center4 = (vec(23,55).x * TILESIZE + TILESIZE / 2, vec(23,55).y * TILESIZE + TILESIZE / 2)
    screen.blit(gloves_img, gloves_img.get_rect(center=gloves_center4))
    gloves_center5 = (vec(23,56).x * TILESIZE + TILESIZE / 2, vec(23,56).y * TILESIZE + TILESIZE / 2)
    screen.blit(gloves_img, gloves_img.get_rect(center=gloves_center5))
    gloves_center6 = (vec(23,57).x * TILESIZE + TILESIZE / 2, vec(23,57).y * TILESIZE + TILESIZE / 2)
    screen.blit(gloves_img, gloves_img.get_rect(center=gloves_center6))

    vacuum_center1 = (vec(30,50).x * TILESIZE + TILESIZE / 2, vec(30,50).y * TILESIZE + TILESIZE / 2)
    screen.blit(vacuum_img, vacuum_img.get_rect(center=vacuum_center1))
    vacuum_center2 = (vec(31,50).x * TILESIZE + TILESIZE / 2, vec(31,50).y * TILESIZE + TILESIZE / 2)
    screen.blit(vacuum_img, vacuum_img.get_rect(center=vacuum_center2))
    vacuum_center3 = (vec(32,50).x * TILESIZE + TILESIZE / 2, vec(32,50).y * TILESIZE + TILESIZE / 2)
    screen.blit(vacuum_img, vacuum_img.get_rect(center=vacuum_center3))
    vacuum_center4 = (vec(32,47).x * TILESIZE + TILESIZE / 2, vec(32,47).y * TILESIZE + TILESIZE / 2)
    screen.blit(vacuum_img, vacuum_img.get_rect(center=vacuum_center4))
    vacuum_center5 = (vec(32,48).x * TILESIZE + TILESIZE / 2, vec(32,48).y * TILESIZE + TILESIZE / 2)
    screen.blit(vacuum_img, vacuum_img.get_rect(center=vacuum_center5))
    vacuum_center6 = (vec(32,49).x * TILESIZE + TILESIZE / 2, vec(32,49).y * TILESIZE + TILESIZE / 2)
    screen.blit(vacuum_img, vacuum_img.get_rect(center=vacuum_center6))

    watercan_center1 = (vec(25,52).x * TILESIZE + TILESIZE / 2, vec(25,52).y * TILESIZE + TILESIZE / 2)
    screen.blit(watercan_img, watercan_img.get_rect(center=watercan_center1))
    watercan_center2 = (vec(25,53).x * TILESIZE + TILESIZE / 2, vec(25,53).y * TILESIZE + TILESIZE / 2)
    screen.blit(watercan_img, watercan_img.get_rect(center=watercan_center2))
    watercan_center3 = (vec(25,54).x * TILESIZE + TILESIZE / 2, vec(25,54).y * TILESIZE + TILESIZE / 2)
    screen.blit(watercan_img, watercan_img.get_rect(center=watercan_center3))
    watercan_center4 = (vec(25,55).x * TILESIZE + TILESIZE / 2, vec(25,55).y * TILESIZE + TILESIZE / 2)
    screen.blit(watercan_img, watercan_img.get_rect(center=watercan_center4))
    watercan_center5 = (vec(25,56).x * TILESIZE + TILESIZE / 2, vec(25,56).y * TILESIZE + TILESIZE / 2)
    screen.blit(watercan_img, watercan_img.get_rect(center=watercan_center5))
    watercan_center6 = (vec(25,57).x * TILESIZE + TILESIZE / 2, vec(25,57).y * TILESIZE + TILESIZE / 2)
    screen.blit(watercan_img, watercan_img.get_rect(center=watercan_center6))

    greenbucket_center1 = (vec(25,50).x * TILESIZE + TILESIZE / 2, vec(25,50).y * TILESIZE + TILESIZE / 2)
    screen.blit(greenbucket_img, greenbucket_img.get_rect(center=greenbucket_center1))
    greenbucket_center2 = (vec(25,51).x * TILESIZE + TILESIZE / 2, vec(25,51).y * TILESIZE + TILESIZE / 2)
    screen.blit(greenbucket_img, greenbucket_img.get_rect(center=greenbucket_center2))
    greenbucket_center3 = (vec(26,50).x * TILESIZE + TILESIZE / 2, vec(26,50).y * TILESIZE + TILESIZE / 2)
    screen.blit(greenbucket_img, greenbucket_img.get_rect(center=greenbucket_center3))
    greenbucket_center4 = (vec(27,50).x * TILESIZE + TILESIZE / 2, vec(27,50).y * TILESIZE + TILESIZE / 2)
    screen.blit(greenbucket_img, greenbucket_img.get_rect(center=greenbucket_center4))
    greenbucket_center5 = (vec(28,50).x * TILESIZE + TILESIZE / 2, vec(28,50).y * TILESIZE + TILESIZE / 2)
    screen.blit(greenbucket_img, greenbucket_img.get_rect(center=greenbucket_center5))
    greenbucket_center6 = (vec(29,50).x * TILESIZE + TILESIZE / 2, vec(29,50).y * TILESIZE + TILESIZE / 2)
    screen.blit(greenbucket_img, greenbucket_img.get_rect(center=greenbucket_center6))

    wirebrush_center1 = (vec(32,46).x * TILESIZE + TILESIZE / 2, vec(32,46).y * TILESIZE + TILESIZE / 2)
    screen.blit(wirebrush_img, wirebrush_img.get_rect(center=wirebrush_center1))
    wirebrush_center2 = (vec(32,45).x * TILESIZE + TILESIZE / 2, vec(32,45).y * TILESIZE + TILESIZE / 2)
    screen.blit(wirebrush_img, wirebrush_img.get_rect(center=wirebrush_center2))
    wirebrush_center3 = (vec(32,44).x * TILESIZE + TILESIZE / 2, vec(32,44).y * TILESIZE + TILESIZE / 2)
    screen.blit(wirebrush_img, wirebrush_img.get_rect(center=wirebrush_center3))
    wirebrush_center4 = (vec(32,43).x * TILESIZE + TILESIZE / 2, vec(32,43).y * TILESIZE + TILESIZE / 2)
    screen.blit(wirebrush_img, wirebrush_img.get_rect(center=wirebrush_center4))
    wirebrush_center5 = (vec(32,42).x * TILESIZE + TILESIZE / 2, vec(32,42).y * TILESIZE + TILESIZE / 2)
    screen.blit(wirebrush_img, wirebrush_img.get_rect(center=wirebrush_center5))
    wirebrush_center6 = (vec(32,41).x * TILESIZE + TILESIZE / 2, vec(32,41).y * TILESIZE + TILESIZE / 2)
    screen.blit(wirebrush_img, wirebrush_img.get_rect(center=wirebrush_center6))

    wiper_center1 = (vec(32,40).x * TILESIZE + TILESIZE / 2, vec(32,40).y * TILESIZE + TILESIZE / 2)
    screen.blit(wiper_img, wiper_img.get_rect(center=wiper_center1))
    wiper_center2 = (vec(32,39).x * TILESIZE + TILESIZE / 2, vec(32,39).y * TILESIZE + TILESIZE / 2)
    screen.blit(wiper_img, wiper_img.get_rect(center=wiper_center2))
    wiper_center3 = (vec(32,38).x * TILESIZE + TILESIZE / 2, vec(32,38).y * TILESIZE + TILESIZE / 2)
    screen.blit(wiper_img, wiper_img.get_rect(center=wiper_center3))
    wiper_center4 = (vec(32,37).x * TILESIZE + TILESIZE / 2, vec(32,37).y * TILESIZE + TILESIZE / 2)
    screen.blit(wiper_img, wiper_img.get_rect(center=wiper_center4))
    wiper_center5 = (vec(32,36).x * TILESIZE + TILESIZE / 2, vec(32,36).y * TILESIZE + TILESIZE / 2)
    screen.blit(wiper_img, wiper_img.get_rect(center=wiper_center5))

    dustpan_center1 = (vec(32,35).x * TILESIZE + TILESIZE / 2, vec(32,35).y * TILESIZE + TILESIZE / 2)
    screen.blit(dustpan_img, dustpan_img.get_rect(center=dustpan_center1))
    dustpan_center2 = (vec(32,34).x * TILESIZE + TILESIZE / 2, vec(32,34).y * TILESIZE + TILESIZE / 2)
    screen.blit(dustpan_img, dustpan_img.get_rect(center=dustpan_center2))
    dustpan_center3 = (vec(32,33).x * TILESIZE + TILESIZE / 2, vec(32,33).y * TILESIZE + TILESIZE / 2)
    screen.blit(dustpan_img, dustpan_img.get_rect(center=dustpan_center3))
    dustpan_center4 = (vec(32,32).x * TILESIZE + TILESIZE / 2, vec(32,32).y * TILESIZE + TILESIZE / 2)
    screen.blit(dustpan_img, dustpan_img.get_rect(center=dustpan_center4))
    dustpan_center5 = (vec(32,31).x * TILESIZE + TILESIZE / 2, vec(32,31).y * TILESIZE + TILESIZE / 2)
    screen.blit(dustpan_img, dustpan_img.get_rect(center=dustpan_center5))
    dustpan_center6 = (vec(32,30).x * TILESIZE + TILESIZE / 2, vec(32,30).y * TILESIZE + TILESIZE / 2)
    screen.blit(dustpan_img, dustpan_img.get_rect(center=dustpan_center6))

    shovel_center1 = (vec(23,48).x * TILESIZE + TILESIZE / 2, vec(23,48).y * TILESIZE + TILESIZE / 2)
    screen.blit(shovel_img, shovel_img.get_rect(center=shovel_center1))
    shovel_center2 = (vec(23,49).x * TILESIZE + TILESIZE / 2, vec(23,49).y * TILESIZE + TILESIZE / 2)
    screen.blit(shovel_img, shovel_img.get_rect(center=shovel_center2))
    shovel_center3 = (vec(23,50).x * TILESIZE + TILESIZE / 2, vec(23,50).y * TILESIZE + TILESIZE / 2)
    screen.blit(shovel_img, shovel_img.get_rect(center=shovel_center3))
    shovel_center4 = (vec(23,51).x * TILESIZE + TILESIZE / 2, vec(23,51).y * TILESIZE + TILESIZE / 2)
    screen.blit(shovel_img, shovel_img.get_rect(center=shovel_center4))    
    shovel_center5 = (vec(24,48).x * TILESIZE + TILESIZE / 2, vec(24,48).y * TILESIZE + TILESIZE / 2)
    screen.blit(shovel_img, shovel_img.get_rect(center=shovel_center5))
    shovel_center6 = (vec(25,48).x * TILESIZE + TILESIZE / 2, vec(25,48).y * TILESIZE + TILESIZE / 2)
    screen.blit(shovel_img, shovel_img.get_rect(center=shovel_center6))

    perfume_center1 = (vec(26,48).x * TILESIZE + TILESIZE / 2, vec(26,48).y * TILESIZE + TILESIZE / 2)
    screen.blit(perfume_img, perfume_img.get_rect(center=perfume_center1))
    perfume_center2 = (vec(27,48).x * TILESIZE + TILESIZE / 2, vec(27,48).y * TILESIZE + TILESIZE / 2)
    screen.blit(perfume_img, perfume_img.get_rect(center=perfume_center2))
    perfume_center3 = (vec(28,48).x * TILESIZE + TILESIZE / 2, vec(28,48).y * TILESIZE + TILESIZE / 2)
    screen.blit(perfume_img, perfume_img.get_rect(center=perfume_center3))
    perfume_center4 = (vec(29,48).x * TILESIZE + TILESIZE / 2, vec(29,48).y * TILESIZE + TILESIZE / 2)
    screen.blit(perfume_img, perfume_img.get_rect(center=perfume_center4))
    perfume_center5 = (vec(30,48).x * TILESIZE + TILESIZE / 2, vec(30,48).y * TILESIZE + TILESIZE / 2)
    screen.blit(perfume_img, perfume_img.get_rect(center=perfume_center5))
    perfume_center6 = (vec(30,47).x * TILESIZE + TILESIZE / 2, vec(30,47).y * TILESIZE + TILESIZE / 2)
    screen.blit(perfume_img, perfume_img.get_rect(center=perfume_center6))

    for coordinate in [(25,36),(25,37),(25,38),(25,39),(25,40),(25,41)]:
        luxsoap_center1 = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(luxsoap_img, luxsoap_img.get_rect(center=luxsoap_center1))

    for coordinate in [(16,36),(16,37),(16,38),(18,36),(18,37),(18,38)]:
        pinwheelcandy_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(pinwheelcandy_img, pinwheelcandy_img.get_rect(center=pinwheelcandy_center))

    for coordinate in [(16,39),(16,40),(16,41),(16,42),(16,43),(16,44)]:
        strawberrycandy_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(strawberrycandy_img, strawberrycandy_img.get_rect(center=strawberrycandy_center))

    for coordinate in [(18,39),(18,40),(18,41),(18,42),(18,43),(18,44)]:
        milkcandy_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(milkcandy_img, milkcandy_img.get_rect(center=milkcandy_center))

    for coordinate in [(18,45),(18,46),(18,47),(18,48),(18,49),(18,50)]:
        butterscotchtoffee_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(butterscotchtoffee_img, butterscotchtoffee_img.get_rect(center=butterscotchtoffee_center))

    for coordinate in [(30,58),(30,59),(30,60),(30,61),(30,62)]:
        lavender_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(lavender_img, lavender_img.get_rect(center=lavender_center))

    for coordinate in [(8,28),(9,28),(10,28),(11,28),(12,28),(13,28)]:
        brownbag_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(brownbag_img, brownbag_img.get_rect(center=brownbag_center))

    for coordinate in [(8,29),(8,30),(8,31),(8,32),(8,33),(8,34)]:
        satchelbag_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(satchelbag_img, satchelbag_img.get_rect(center=satchelbag_center))

    for coordinate in [(8,35),(8,36),(8,37),(8,38),(8,39),(8,40)]:
        yellowcushion_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(yellowcushion_img, yellowcushion_img.get_rect(center=yellowcushion_center))

    for coordinate in [(8,41),(8,42),(8,43),(8,44),(8,45),(8,46)]:
        cushion_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(cushion_img, cushion_img.get_rect(center=cushion_center))

    for coordinate in [(8,53),(8,54),(8,55),(8,56),(8,57),(8,58)]:
        yellowpillow_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(yellowpillow_img, yellowpillow_img.get_rect(center=yellowpillow_center))

    for coordinate in [(8,59),(8,60),(8,61),(8,62),(8,63),(8,64)]:
        bluepillow_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(bluepillow_img, bluepillow_img.get_rect(center=bluepillow_center))

    for coordinate in [(25,21),(26,21),(27,21),(28,21),(29,21)]:
        brushes_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(brushes_img, brushes_img.get_rect(center=brushes_center))

    for coordinate in [(30,23),(30,24),(30,25),(30,26),(30,27),(30,28)]:
        sunscreen_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(sunscreen_img, sunscreen_img.get_rect(center=sunscreen_center))

    for coordinate in [(25,23),(26,23),(27,23),(28,23),(29,23)]:
        lipstick_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(lipstick_img, lipstick_img.get_rect(center=lipstick_center))

    for coordinate in [(30,29),(30,30),(30,31),(30,32),(30,33),(30,34)]:
        niveacream_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(niveacream_img, niveacream_img.get_rect(center=niveacream_center))

    for coordinate in [(32,24),(32,25),(32,26),(32,27),(32,28),(32,29)]:
        mopwiper_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(mopwiper_img, mopwiper_img.get_rect(center=mopwiper_center))

    for coordinate in [(9,7),(10,7)]:
        denimjacket_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(denimjacket_img, denimjacket_img.get_rect(center=denimjacket_center))

    for coordinate in [(9,10),(10,10)]:
        denimjaens_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(denimjaens_img, denimjaens_img.get_rect(center=denimjaens_center))

    for coordinate in [(17,7),(18,7)]:
        denimshirt_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(denimshirt_img, denimshirt_img.get_rect(center=denimshirt_center))

    for coordinate in [(8,8),(8,9)]:
        balloonskirt_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(balloonskirt_img, balloonskirt_img.get_rect(center=balloonskirt_center))

    for coordinate in [(11,8),(11,9)]:
        pinktop_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(pinktop_img, pinktop_img.get_rect(center=pinktop_center))

    for coordinate in [(19,8),(19,9)]:
        bluesweater_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(bluesweater_img, bluesweater_img.get_rect(center=bluesweater_center))

    for coordinate in [(9,15),(10,15),(11,16),(11,17)]:
        yellowhotwheels_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(yellowhotwheels_img, yellowhotwheels_img.get_rect(center=yellowhotwheels_center))

    for coordinate in [(8,16),(8,17),(9,18),(10,18)]:
        bluehotwheels_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(bluehotwheels_img, bluehotwheels_img.get_rect(center=bluehotwheels_center))

    for coordinate in [(17,15),(18,15),(19,16),(19,17)]:
        steamiron_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(steamiron_img, steamiron_img.get_rect(center=steamiron_center))

    for coordinate in [(16,16),(16,17),(17,18),(18,18)]:
        nikoncamera_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(nikoncamera_img, nikoncamera_img.get_rect(center=nikoncamera_center))

    for coordinate in [(16,8),(16,9)]:
        bodyconskirt_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(bodyconskirt_img, bodyconskirt_img.get_rect(center=bodyconskirt_center))

    for coordinate in [(17,10),(18,10)]:
        peplumtop_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(peplumtop_img, peplumtop_img.get_rect(center=peplumtop_center))

    for coordinate in [(30,41),(30,42),(30,43),(30,44),(30,45),(30,46)]:
        cologne_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(cologne_img, cologne_img.get_rect(center=cologne_center))

    for coordinate in [(30,35),(30,36),(30,37),(30,38),(30,39),(30,40)]:
        compact_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(compact_img, compact_img.get_rect(center=compact_center))

    for coordinate in [(16,45),(16,46),(16,47),(16,48),(16,49),(16,50)]:
        chocolatebar_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(chocolatebar_img, chocolatebar_img.get_rect(center=chocolatebar_center))

    for coordinate in [(16,51),(16,52),(16,53),(16,54),(16,55),(16,56)]:
        hershey_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(hershey_img, hershey_img.get_rect(center=hershey_center))

    for coordinate in [(16,63),(16,64),(16,65),(16,66),(16,67),(16,68),(16,69)]:
        oliveoil_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(oliveoil_img, oliveoil_img.get_rect(center=oliveoil_center))

    for coordinate in [(16,70),(13,71),(14,71),(15,71),(16,71)]:
        whiskey_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(whiskey_img, whiskey_img.get_rect(center=whiskey_center))

    for coordinate in [(8,71),(9,71),(10,71),(11,71),(12,71)]:
        gin_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(gin_img, gin_img.get_rect(center=gin_center))

    for coordinate in [(3,71),(4,71),(5,71),(6,71),(7,71)]:
        realwine_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(realwine_img, realwine_img.get_rect(center=realwine_center))

    for coordinate in [(16,57),(16,58),(16,59),(16,60),(16,61),(16,62)]:
        rawhoney_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(rawhoney_img, rawhoney_img.get_rect(center=rawhoney_center))

    for coordinate in [(14,28),(15,28),(16,28),(17,28),(18,28),(19,28)]:
        toothpaste_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(toothpaste_img, toothpaste_img.get_rect(center=toothpaste_center))

    for coordinate in [(8,47),(8,48),(8,49),(8,50),(8,51),(8,52)]:
        whitepillow_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(whitepillow_img, whitepillow_img.get_rect(center=whitepillow_center))

    for coordinate in [(30,63),(30,64),(30,65),(30,66),(30,67),(30,68)]:
        lillies_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(lillies_img, lillies_img.get_rect(center=lillies_center))

    for coordinate in [(30,69),(30,70),(30,71),(32,69),(32,70),(32,71)]:
        lotus_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(lotus_img, lotus_img.get_rect(center=lotus_center))

    for coordinate in [(32,63),(32,64),(32,65),(32,66),(32,67),(32,68)]:
        daisy_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(daisy_img, daisy_img.get_rect(center=daisy_center))

    for coordinate in [(23,65),(23,66),(23,67),(23,68),(23,69),(23,70),(24,70)]:
        milkcartons_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(milkcartons_img, milkcartons_img.get_rect(center=milkcartons_center))

    for coordinate in [(38,20),(39,20),(38,21),(39,21)]:
        vanish_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(vanish_img, vanish_img.get_rect(center=vanish_center))

    for coordinate in [(0,73),(1,73),(2,73),(3,73)]:
        Cheese_Block_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Cheese_Block_img, Cheese_Block_img.get_rect(center=Cheese_Block_center))

    for coordinate in [(4,73),(5,73),(6,73),(7,73),(8,73),(9,73)]:
        Blue_cheese_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Blue_cheese_img, Blue_cheese_img.get_rect(center=Blue_cheese_center))

    for coordinate in [(10,73),(11,73),(12,73),(13,73),(14,73),(15,73)]:
        Brown_Bread_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Brown_Bread_img, Brown_Bread_img.get_rect(center=Brown_Bread_center))

    for coordinate in [(16,73),(17,73),(18,73),(18,70),(18,71),(18,72)]:
        Rye_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Rye_img, Rye_img.get_rect(center=Rye_center))

    for coordinate in [(18,64),(18,65),(18,66),(18,67),(18,68),(18,69)]:
        Muffin_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Muffin_img, Muffin_img.get_rect(center=Muffin_center))

    for coordinate in [(18,58),(18,59),(18,60),(18,61),(18,62),(18,63)]:
        Pastry_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Pastry_img, Pastry_img.get_rect(center=Pastry_center))

    for coordinate in [(18,51),(18,52),(18,53),(18,54),(18,55),(18,56),(18,57)]:
        Lollipop_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Lollipop_img, Lollipop_img.get_rect(center=Lollipop_center))

    for coordinate in [(0,74),(1,74),(0,75),(1,75)]:
        Chicken_leg_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Chicken_leg_img, Chicken_leg_img.get_rect(center=Chicken_leg_center))

    for coordinate in [(0,76),(1,76),(0,77),(1,77)]:
        Mutton_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Mutton_img, Mutton_img.get_rect(center=Mutton_center))

    for coordinate in [(0,78),(1,78),(2,78),(0,79),(1,79),(2,79),(2,78)]:
        Fish_cuts_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Fish_cuts_img, Fish_cuts_img.get_rect(center=Fish_cuts_center))

    for coordinate in [(3,79),(4,79),(3,78),(4,78)]:
        Chicken_breast_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Chicken_breast_img, Chicken_breast_img.get_rect(center=Chicken_breast_center))

    for coordinate in [(5,78),(6,78),(5,79),(6,79)]:
        Ribs_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Ribs_img, Ribs_img.get_rect(center=Ribs_center))

    for coordinate in [(7,78),(8,78),(7,79),(8,79)]:
        Ham_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Ham_img, Ham_img.get_rect(center=Ham_center))

    for coordinate in [(9,78),(10,78),(9,79),(10,79)]:
        Blue_fish_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Blue_fish_img, Blue_fish_img.get_rect(center=Blue_fish_center))

    for coordinate in [(11,78),(12,78),(11,79),(12,79)]:
        Rohu_fish_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Rohu_fish_img, Rohu_fish_img.get_rect(center=Rohu_fish_center))

    for coordinate in [(13,78),(14,78),(13,79),(14,79)]:
        Pompfret_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Pompfret_img, Pompfret_img.get_rect(center=Pompfret_center))

    for coordinate in [(15,78),(16,78),(15,79),(16,79)]:
        Eel_fish_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Eel_fish_img, Eel_fish_img.get_rect(center=Eel_fish_center))

    for coordinate in [(17,78),(18,78),(17,79),(18,79)]:
        Katla_fish_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Katla_fish_img, Katla_fish_img.get_rect(center=Katla_fish_center))

    for coordinate in [(19,78),(20,78),(19,79),(20,79)]:
        Prawns_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Prawns_img, Prawns_img.get_rect(center=Prawns_center))

    for coordinate in [(20,76),(20,77)]:
        Mackerel_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Mackerel_img, Mackerel_img.get_rect(center=Mackerel_center))

    for coordinate in [(22,76),(22,77),(22,78),(22,79)]:
        Cabbage_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Cabbage_img, Cabbage_img.get_rect(center=Cabbage_center))

    for coordinate in [(23,78),(24,78),(23,79),(24,79)]:
        Aubergine_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Aubergine_img, Aubergine_img.get_rect(center=Aubergine_center))

    for coordinate in [(25,78),(26,78),(25,79),(26,79)]:
        Brocolli_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Brocolli_img, Brocolli_img.get_rect(center=Brocolli_center))

    for coordinate in [(27,78),(28,78),(27,79),(28,79)]:
        Lemon_grass_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Lemon_grass_img, Lemon_grass_img.get_rect(center=Lemon_grass_center))

    for coordinate in [(29,78),(30,78),(29,79),(30,79)]:
        Lilac_Turnip_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Lilac_Turnip_img, Lilac_Turnip_img.get_rect(center=Lilac_Turnip_center))

    for coordinate in [(31,78),(32,78),(31,79),(32,79)]:
        Carrots_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Carrots_img, Carrots_img.get_rect(center=Carrots_center))

    for coordinate in [(33,78),(34,78),(33,79),(34,79)]:
        Garlic_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Garlic_img, Garlic_img.get_rect(center=Garlic_center))

    for coordinate in [(35,78),(36,78),(35,79),(36,79),(37,78),(37,79)]:
        Chinese_Cabbage_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Chinese_Cabbage_img, Chinese_Cabbage_img.get_rect(center=Chinese_Cabbage_center))

    for coordinate in [(38,77),(39,77),(38,78),(39,78),(38,79),(39,79)]:
        Pumpkin_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Pumpkin_img, Pumpkin_img.get_rect(center=Pumpkin_center))

    for coordinate in [(38,75),(39,75),(38,76),(39,76)]:
        Shiitake_mushroom_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Shiitake_mushroom_img, Shiitake_mushroom_img.get_rect(center=Shiitake_mushroom_center))

    for coordinate in [(38,73),(39,73),(38,74),(39,74)]:
        Oyester_mushroom_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Oyester_mushroom_img, Oyester_mushroom_img.get_rect(center=Oyester_mushroom_center))

    for coordinate in [(38,69),(39,69),(38,70),(39,70)]:
        Button_mushrooms_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Button_mushrooms_img, Button_mushrooms_img.get_rect(center=Button_mushrooms_center))

    for coordinate in [(38,67),(39,67),(38,68),(39,68)]:
        Chilly_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Chilly_img, Chilly_img.get_rect(center=Chilly_center))

    for coordinate in [(38,65),(39,65),(38,66),(39,66)]:
        Potatoes_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Potatoes_img, Potatoes_img.get_rect(center=Potatoes_center))

    for coordinate in [(38,63),(39,63),(38,64),(39,64)]:
        Nectarine_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Nectarine_img, Nectarine_img.get_rect(center=Nectarine_center))

    for coordinate in [(38,61),(39,61),(38,62),(39,62),(38,36),(39,36)]:
        Red_Apple_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Red_Apple_img, Red_Apple_img.get_rect(center=Red_Apple_center))

    for coordinate in [(38,71),(39,71),(38,72),(39,72)]:
        Shrooms_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Shrooms_img, Shrooms_img.get_rect(center=Shrooms_center))

    for coordinate in [(38,59),(39,59),(38,60),(39,60)]:
        Banana_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Banana_img, Banana_img.get_rect(center=Banana_center))

    for coordinate in [(38,57),(39,57),(38,58),(39,58)]:
        Pineapple_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Pineapple_img, Pineapple_img.get_rect(center=Pineapple_center))

    for coordinate in [(38,55),(39,55),(38,56),(39,56)]:
        Mulberry_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Mulberry_img, Mulberry_img.get_rect(center=Mulberry_center))

    for coordinate in [(38,53),(39,53),(38,54),(39,54)]:
        Grapes_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Grapes_img, Grapes_img.get_rect(center=Grapes_center))

    for coordinate in [(38,51),(39,51),(38,52),(39,52)]:
        Lemon_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Lemon_img, Lemon_img.get_rect(center=Lemon_center))

    for coordinate in [(38,49),(39,49),(38,50),(39,50)]:
        litchi_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(litchi_img, litchi_img.get_rect(center=litchi_center))

    for coordinate in [(38,47),(39,47),(38,48),(39,48)]:
        Strawberry_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Strawberry_img, Strawberry_img.get_rect(center=Strawberry_center))

    for coordinate in [(38,45),(39,45),(38,46),(39,46)]:
        Papaya_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Papaya_img, Papaya_img.get_rect(center=Papaya_center))

    for coordinate in [(38,43),(39,43),(38,44),(39,44)]:
        Grapefruit_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Grapefruit_img, Grapefruit_img.get_rect(center=Grapefruit_center))

    for coordinate in [(38,41),(39,41),(38,42),(39,42)]:
        Lime_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Lime_img, Lime_img.get_rect(center=Lime_center))

    for coordinate in [(38,39),(39,39),(38,40),(39,40)]:
        Avocado_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Avocado_img, Avocado_img.get_rect(center=Avocado_center))

    for coordinate in [(38,37),(39,37),(38,38),(39,38)]:
        Pomegranate_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Pomegranate_img, Pomegranate_img.get_rect(center=Pomegranate_center))

    for coordinate in [(38,34),(39,34),(38,35),(39,35)]:
        Mr_muscle_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Mr_muscle_img, Mr_muscle_img.get_rect(center=Mr_muscle_center))

    for coordinate in [(38,32),(39,32),(38,33),(39,33)]:
        Colin_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Colin_img, Colin_img.get_rect(center=Colin_center))

    for coordinate in [(38,30),(39,30),(38,31),(39,31)]:
        Sparx_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Sparx_img, Sparx_img.get_rect(center=Sparx_center))

    for coordinate in [(38,28),(39,28),(38,29),(39,29)]:
        Bleach_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Bleach_img, Bleach_img.get_rect(center=Bleach_center))

    for coordinate in [(38,26),(39,26),(38,27),(39,27)]:
        Eazy_softener_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Eazy_softener_img, Eazy_softener_img.get_rect(center=Eazy_softener_center))

    for coordinate in [(38,24),(39,24),(38,25),(39,25)]:
        Tide_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Tide_img, Tide_img.get_rect(center=Tide_center))

    for coordinate in [(38,22),(39,22),(38,23),(39,23)]:
        Surf_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Surf_img, Surf_img.get_rect(center=Surf_center))

    for coordinate in [(0,6),(1,6),(2,6),(0,7),(1,7),(2,7),(0,8),(1,8),(2,8)]:
        Sugar_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Sugar_img, Sugar_img.get_rect(center=Sugar_center))

    for coordinate in [(0,9),(1,9),(2,9),(0,10),(1,10),(2,10),(0,11),(1,11),(2,11)]:
        Maize_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Maize_img, Maize_img.get_rect(center=Maize_center))

    for coordinate in [(0,12),(1,12),(2,12),(0,13),(1,13),(2,13)]:
        Wai_wai_noodles_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Wai_wai_noodles_img, Wai_wai_noodles_img.get_rect(center=Wai_wai_noodles_center))

    for coordinate in [(0,14),(1,14),(2,14),(0,15),(1,15),(2,15)]:
        Chings_noodles_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Chings_noodles_img, Chings_noodles_img.get_rect(center=Chings_noodles_center))

    for coordinate in [(0,16),(1,16),(2,16),(0,17),(1,17),(2,17)]:
        Maggi_noodles_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Maggi_noodles_img, Maggi_noodles_img.get_rect(center=Maggi_noodles_center))

    for coordinate in [(0,18),(1,18),(2,18),(0,19),(1,19),(2,19)]:
        Yippie_noodles_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Yippie_noodles_img, Yippie_noodles_img.get_rect(center=Yippie_noodles_center))

    for coordinate in [(0,20),(1,20),(2,20),(0,21),(1,21),(2,21),(0,22),(1,22),(2,22)]:
        Canned_beans_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Canned_beans_img, Canned_beans_img.get_rect(center=Canned_beans_center))

    for coordinate in [(0,23),(1,23),(2,23),(0,24),(1,24),(2,24),(0,25),(1,25),(2,25)]:
        Jalapenos_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Jalapenos_img, Jalapenos_img.get_rect(center=Jalapenos_center))

    for coordinate in [(0,26),(1,26),(2,26),(0,27),(1,27),(2,27),(0,28),(1,28),(2,28)]:
        Rasgulla_500g_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Rasgulla_500g_img, Rasgulla_500g_img.get_rect(center=Rasgulla_500g_center))

    for coordinate in [(0,29),(1,29),(2,29),(0,30),(1,30),(2,30),(0,31),(1,31),(2,31)]:
        Tuna_can_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Tuna_can_img, Tuna_can_img.get_rect(center=Tuna_can_center))

    for coordinate in [(0,32),(1,32),(2,32),(0,33),(1,33),(2,33),(0,34),(1,34),(2,34)]:
        Schezwan_sauce_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Schezwan_sauce_img, Schezwan_sauce_img.get_rect(center=Schezwan_sauce_center))

    for coordinate in [(0,35),(1,35),(2,35),(0,36),(1,36),(2,36),(0,37),(1,37),(2,37)]:
        Sardines_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Sardines_img, Sardines_img.get_rect(center=Sardines_center))

    for coordinate in [(0,38),(1,38),(2,38),(0,39),(1,39),(2,39),(0,40),(1,40),(2,40)]:
        Peanut_butter_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Peanut_butter_img, Peanut_butter_img.get_rect(center=Peanut_butter_center))

    for coordinate in [(0,41),(1,41),(2,41),(0,42),(1,42),(2,42),(0,43),(1,43),(2,43)]:
        Pickle_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Pickle_img, Pickle_img.get_rect(center=Pickle_center))

    for coordinate in [(0,44),(1,44),(2,44),(0,45),(1,45),(2,45),(0,46),(1,46),(2,46)]:
        Mayonnaise_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Mayonnaise_img, Mayonnaise_img.get_rect(center=Mayonnaise_center))

    for coordinate in [(0,47),(1,47),(2,47),(0,48),(1,48),(2,48),(0,49),(1,49),(2,49)]:
        Honey_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Honey_img, Honey_img.get_rect(center=Honey_center))

    for coordinate in [(0,50),(1,50),(2,50),(0,51),(1,51),(2,51),(0,52),(1,52),(2,52)]:
        Ketchup_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Ketchup_img, Ketchup_img.get_rect(center=Ketchup_center))

    for coordinate in [(0,53),(1,53),(2,53),(0,54),(1,54),(2,54)]:
        Coca_cola_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Coca_cola_img, Coca_cola_img.get_rect(center=Coca_cola_center))

    for coordinate in [(0,55),(1,55),(2,55),(0,56),(1,56),(2,56)]:
        Pepsi_can_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Pepsi_can_img, Pepsi_can_img.get_rect(center=Pepsi_can_center))

    for coordinate in [(0,57),(1,57),(2,57),(0,58),(1,58),(2,58)]:
        Diet_cola_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Diet_cola_img, Diet_cola_img.get_rect(center=Diet_cola_center))

    for coordinate in [(0,59),(1,59),(2,59),(0,60),(1,60),(2,60)]:
        up7_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(up7_img, up7_img.get_rect(center=up7_center))

    for coordinate in [(0,61),(1,61),(2,61),(0,62),(1,62),(2,62)]:
        Red_Bull_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Red_Bull_img, Red_Bull_img.get_rect(center=Red_Bull_center))

    for coordinate in [(0,63),(1,63),(2,63),(0,64),(1,64),(2,64)]:
        Sprite_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Sprite_img, Sprite_img.get_rect(center=Sprite_center))

    for coordinate in [(0,65),(1,65),(2,65),(0,66),(1,66),(2,66)]:
        Orange_juice_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Orange_juice_img, Orange_juice_img.get_rect(center=Orange_juice_center))

    for coordinate in [(0,67),(1,67),(2,67),(0,68),(1,68),(2,68)]:
        Saffola_gold_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Saffola_gold_img, Saffola_gold_img.get_rect(center=Saffola_gold_center))

    for coordinate in [(0,69),(1,69),(2,69),(0,70),(1,70),(2,70),(0,71),(1,71),(2,71)]:
        Chocos_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Chocos_img, Chocos_img.get_rect(center=Chocos_center))

    for coordinate in [(20,28),(21,28),(22,28),(23,28),(24,28),(25,28),(25,29)]:
        ac_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(ac_img, ac_img.get_rect(center=ac_center))

    for coordinate in [(25,30),(25,31),(25,32),(25,33),(25,34),(25,35)]:
        coffeemaker_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(coffeemaker_img, coffeemaker_img.get_rect(center=coffeemaker_center))

    for coordinate in [(23,36),(23,37),(23,38),(23,39),(23,40),(23,41)]:
        washingmachine_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(washingmachine_img, washingmachine_img.get_rect(center=washingmachine_center))

    for coordinate in [(23,30),(23,31),(23,32),(23,33),(23,34),(23,35)]:
        fridge_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(fridge_img, fridge_img.get_rect(center=fridge_center))

    for coordinate in [(11,30),(12,30),(13,30),(14,30),(15,30),(16,30)]:
        microwave_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(microwave_img, microwave_img.get_rect(center=microwave_center))

    for coordinate in [(17,30),(18,30),(19,30),(20,30),(21,30),(22,30)]:
        dishwasher_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(dishwasher_img, dishwasher_img.get_rect(center=dishwasher_center))

    for coordinate in [(10,30),(10,31),(10,32),(10,33),(10,34),(10,35)]:
        tv_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(tv_img, tv_img.get_rect(center=tv_center))

    for coordinate in [(10,36),(10,37),(10,38),(10,39),(10,40),(10,41)]:
        dvd_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(dvd_img, dvd_img.get_rect(center=dvd_center))

    for coordinate in [(10,42),(10,43),(10,44),(10,45),(10,46),(10,47)]:
        mobile_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(mobile_img, mobile_img.get_rect(center=mobile_center))

    for coordinate in [(10,48),(10,49),(10,50),(10,51),(10,52),(10,53)]:
        rollerblades_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(rollerblades_img, rollerblades_img.get_rect(center=rollerblades_center))

    for coordinate in [(10,54),(10,55),(10,56),(10,57),(10,58),(10,59)]:
        sunglasses_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(sunglasses_img, sunglasses_img.get_rect(center=sunglasses_center))

    for coordinate in [(24,65),(25,65),(25,66),(25,67),(25,68),(25,69),(25,70)]:
        eggs_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(eggs_img, eggs_img.get_rect(center=eggs_center))

    for coordinate in [(32,58),(32,59),(32,60),(32,61),(32,62)]:
        Ferns_center = (vec(coordinate).x * TILESIZE + TILESIZE / 2, vec(coordinate).y * TILESIZE + TILESIZE / 2)
        screen.blit(Ferns_img, Ferns_img.get_rect(center=Ferns_center))


    broom_center = (vec(16,8).x * TILESIZE + TILESIZE / 2, vec(16,8).y * TILESIZE + TILESIZE / 2)
    screen.blit(broom_img, broom_img.get_rect(center=goal_center))


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


    global goal_final 
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


    return small


def demo():
    search_type = a_star_search
    global total_length
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
        draw_text('Path length for the next item:{}'.format(l), 30, GREEN, WIDTH - 10, HEIGHT - 45, align="bottomright")

        pg.display.flip()


     
    total_length+=l  

    # print(total_length)  
    draw_text('Total Path length:{}'.format(total_length), 30, GREEN, WIDTH - 10, HEIGHT - 65, align="bottomright")
    pg.display.flip()
    # print(start)
    start=goal
    goal1.remove(goal)
        
    # print(goal)
    # print(goal1)

    if len(goal1)<0:
        # start=goal
        # goal=vec(0,38)
        
        pg.quit()
        running=False
        # exit(0)
    small=100000
    # global p
    p=p-1
    for k in range(p):
        path[k] ,c[k] = search_type(g,goal1[k],start) 
