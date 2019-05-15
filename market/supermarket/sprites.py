import pygame as pg
from random import uniform, choice, randint, random
from supermarket.settings2 import *
from supermarket.tilemap import collide_hit_rect
import pytweening as tween
from itertools import chain
vec = pg.math.Vector2
font_name = pg.font.match_font('hack')

tott_dist=0
tot_dist=0
vert_dist=0
hori_dist=0
total_dist=0
def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.rot = 0
        self.last_shot = 0
        self.health = PLAYER_HEALTH
        self.weapon = 'pistol'
        self.damaged = False
        self.screen = pg.display.set_mode((10+WIDTH, HEIGHT))




    def draw_text(self,text, size, color, x, y,align="bottomright"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(**{align: (x, y)})
        self.screen.blit(text_surface, text_rect)    

    def get_keys(self):
        global vert_dist
        global hori_dist
        global tot_dist
        # self.pos
        # global tot_dist
        # tot_dist=0
        global total_dist
        self.rot_speed = 0
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -PLAYER_ROT_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:

            old_vel=self.vel
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
            # self.update()
            new_vel=self.vel
            if old_vel!=new_vel:
                tot_dist+=3                                                             #for change of pos, add 3. This is to  prevent increase in steps while crashing against the wall
            # print(self.pos)
            # print("self.vel")
            # print(self.vel)
            # vert_dist+=1.5

            # # total_dist=vert_dist+hori_dist
            # print("self.game.dt")
            # print(self.game.dt)
            # print("self.pos")
            # print(self.pos)
            # print("self.pos multiply")
            # print(self.vel*self.game.dt)
            # vert_dist+=abs(self.vel[0])*self.game.dt
            # hori_dist+=self.vel[1]*self.game.dt
            # total_dist=vert_dist+hori_dist
            print(tot_dist)
            align1="bottomright"
        
            # temp=self.pos
        # if temp

            #multiply self.vel*self.game.dt
        # if keys[pg.K_DOWN] or keys[pg.K_s]:
        #     self.vel = vec(-PLAYER_SPEED, 0).rotate(-self.rot) #removed/2
        #     # dist+=self.pos[0]
        #     vert_dist=self.pos[0]
        #     total_dist=vert_dist+hori_dist
        # total_dist=vert_dist+hori_dist
        # print("total_dist")
        
    

    def update(self):
        global tott_dist
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        if self.damaged:
            try:
                self.image.fill((255, 255, 255, next(self.damage_alpha)), special_flags=pg.BLEND_RGBA_MULT)
            except:
                self.damaged = False
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        # old_pos=self.pos
        self.pos += self.vel * self.game.dt
        # new_pos=self.pos
        # if old_pos!=new_pos:
        #     tott_dist+=3
        # print(tott_dist)
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center
        self.draw_text('Path length:{}'.format(tott_dist), 30, GREEN, WIDTH - 10, HEIGHT - 45)
        pg.display.flip()


class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        
class Item(pg.sprite.Sprite):
    def __init__(self, game, pos, type):
        self._layer = ITEMS_LAYER
        self.groups = game.all_sprites, game.items
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.item_images[type]
        self.rect = self.image.get_rect()
        self.type = type
        self.pos = pos
        self.rect.center = pos
        self.tween = tween.easeInOutSine
        self.step = 0
        self.dir = 1

    def update(self):
        # bobbing motion
        offset = BOB_RANGE * (self.tween(self.step / BOB_RANGE) - 0.5)
        self.rect.centery = self.pos.y + offset * self.dir
        self.step += BOB_SPEED
        if self.step > BOB_RANGE:
            self.step = 0
            self.dir *= -1
