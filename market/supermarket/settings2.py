import pygame as pg
vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
CYAN = (0, 255, 255)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 280
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# Weapon settings
BULLET_IMG = 'bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {'bullet_speed': 500,
                     'bullet_lifetime': 1000,
                     'rate': 250,
                     'kickback': 200,
                     'spread': 5,
                     'damage': 10,
                     'bullet_size': 'lg',
                     'bullet_count': 1}
WEAPONS['shotgun'] = {'bullet_speed': 400,
                      'bullet_lifetime': 500,
                      'rate': 900,
                      'kickback': 300,
                      'spread': 20,
                      'damage': 5,
                      'bullet_size': 'sm',
                      'bullet_count': 12}

# Mob settings
MOB_IMG = 'zombie1_hold.png'
MOB_SPEEDS = [150, 100, 75, 125]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 400

# Effects
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png',
                  'whitePuff18.png']
SPLAT = 'splat green.png'
FLASH_DURATION = 50
DAMAGE_ALPHA = [i for i in range(0, 255, 55)]
NIGHT_COLOR = (20, 20, 20)
LIGHT_RADIUS = (500, 500)
LIGHT_MASK = "light_350_soft.png"

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# Items
ITEM_IMAGES = {'Cheese Block': 'bullet.png',
               'Banana': 'bullet.png',
               'Grapes': 'bullet.png',
               'Surf': 'bullet.png',
               'Wheat flour': 'bullet.png',
               'Sugar': 'bullet.png',
               'Maize': 'bullet.png',
               'Wai Wai noodles': 'bullet.png',
               'Chings noodles': 'bullet.png',
               'Maggi noodles': 'bullet.png',
               'Yippie noodles': 'bullet.png',
               'Canned beans': 'bullet.png',
               'Jalapenos': 'bullet.png',
               'Rasgulla 500g': 'bullet.png',
               'Tuna can': 'bullet.png',
               'Schezwan sauce': 'bullet.png',
               'Sardines': 'bullet.png',
               'Peanut butter': 'bullet.png',
               'Pickle': 'bullet.png',
               'Mayonnaise': 'bullet.png',
               'Honey': 'bullet.png',
               'Ketchup': 'bullet.png',
               'Pepsi can': 'bullet.png',
               'Coca Cola': 'bullet.png',
               'Diet cola': 'bullet.png',
               '7up': 'bullet.png',
               'Sprite': 'bullet.png',
               'Red Bull': 'bullet.png',
               'Orange Juice': 'bullet.png',
               'Saffola gold': 'bullet.png',
               'Chocos': 'bullet.png',
               'Red wine': 'bullet.png',
               'Gin': 'bullet.png',
               'Whiskey': 'bullet.png',
               'Olive oil': 'bullet.png',
               'Raw honey': 'bullet.png',
               'Hersheys': 'bullet.png',
               'Chocolate': 'bullet.png',
               'Strawberry candy': 'bullet.png',
               'Pinwheel candy': 'bullet.png',
               'Milk candy': 'bullet.png',
               'Butterscotch toffee': 'bullet.png',
               'Lollipop': 'bullet.png',
               'Pastry': 'bullet.png',
               'Muffin': 'bullet.png',
               'Rye': 'bullet.png',
               'Brown bread': 'bullet.png',
               'Blue cheese': 'bullet.png',
               'Chicken leg': 'bullet.png',
               'Mutton': 'bullet.png',
               'Fish cuts': 'bullet.png',
               'Chicken breast': 'bullet.png',
               'Ribs': 'bullet.png',
               'Ham': 'bullet.png',
               'Blue fish': 'bullet.png',
               'Rohu fish': 'bullet.png',
               'Pompfret': 'bullet.png',
               'eel fish': 'bullet.png',
               'Katla fish': 'bullet.png',
               'Prawn': 'bullet.png',
               'Mackerel': 'bullet.png',
               'Cabbage': 'bullet.png',
               'Aubergine': 'bullet.png',
               'Brocolli': 'bullet.png',
               'Lemon grass': 'bullet.png',
               'Lilac Turnip': 'bullet.png',
               'Carrots': 'bullet.png',
               'Garlic': 'bullet.png',
               'Chinese cabbage': 'bullet.png',
               'Pumpkin': 'bullet.png',
               'Shiitake mushroom': 'bullet.png',
               'Oyester mushroom': 'bullet.png',
               'Shrooms': 'bullet.png',
               'Button mushrooms': 'bullet.png',
               'Chilly': 'bullet.png',
               'Potatoes': 'bullet.png',
               'Nectarine': 'bullet.png',
               'Red apple': 'bullet.png',
               'Pineapple': 'bullet.png',
               'Mulberry': 'bullet.png',
               'Lemon': 'bullet.png',
               'Cherry': 'bullet.png',
               'Strawberry': 'bullet.png',
               'Papaya': 'bullet.png',
               'Grapefruit': 'bullet.png',
               'Lime': 'bullet.png',
               'Avocado': 'bullet.png',
               'Pomegranate': 'bullet.png',
               'Mr. muscle': 'bullet.png',
               'Colin': 'bullet.png',
               'Sparx': 'bullet.png',
               'Bleach': 'bullet.png',
               'Eazy softener': 'bullet.png',
               'Tide': 'bullet.png',
               'Vanish': 'bullet.png',
               'Lipstick': 'bullet.png',
               'Sunscreen': 'bullet.png',
               'Nivea cream': 'bullet.png',
               'Lakme compact': 'bullet.png',
               'Eu de cologne': 'bullet.png',
               'Perfume': 'bullet.png',
               'Shovel': 'bullet.png',
               'Gardening gloves': 'bullet.png',
               'Watering can': 'bullet.png',
               'Green bucket': 'bullet.png',
               'Vacuum cleaner': 'bullet.png',
               'Wire brush': 'bullet.png',
               'Wiper': 'bullet.png',
               'Dustpan': 'bullet.png',
               'Mop wiper': 'bullet.png',
               'Broom': 'bullet.png',
               'Lux soap': 'bullet.png',
               'Blue pillow': 'bullet.png',
               'Yellow pillow': 'bullet.png',
               'White pillow': 'bullet.png',
               'Cushions': 'bullet.png',
               'Yellow cushions': 'bullet.png',
               'Satchel bag': 'bullet.png',
               'Brown bag': 'bullet.png',
               'Toothpaste': 'bullet.png',
               'Steam iron': 'bullet.png',
               'Nikon camera': 'bullet.png',
               'Yellow hotwheels': 'bullet.png',
               'Blue hotwheels': 'bullet.png',
               'Denim shirt': 'bullet.png',
               'Blue sweater': 'bullet.png',
               'Peplum top': 'bullet.png',
               'Bodycon skirt': 'bullet.png',
               'Pink top': 'bullet.png',
               'Denim jeans': 'bullet.png',
               'Balloon skirt': 'bullet.png',
               'Denim jacket': 'bullet.png',
               'Milk cartons': 'bullet.png',
               'Eggs': 'bullet.png',
               'Lotus': 'bullet.png',
               'Daisy': 'bullet.png',
               'Lillies': 'bullet.png',
               'Ferns': 'bullet.png',
               'Lavender': 'bullet.png',
               'Accessories': 'bullet.png',
               'Cold cream': 'bullet.png',
               'Air conditioner': 'bullet.png',
               'Coffee maker': 'bullet.png',
               'DVD player': 'bullet.png',
               'Microwave': 'bullet.png',
               'Dishwasher': 'bullet.png',
               'Refrigerator': 'bullet.png',
               'Roller blades': 'bullet.png',
               'Sunglasses': 'bullet.png',
               'Clock': 'bullet.png',
               'TV': 'bullet.png',
               'Mobile': 'bullet.png',



               }
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 10
BOB_SPEED = 0.3

# Sounds0