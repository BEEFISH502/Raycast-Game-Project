from animate_sprites import *


class Weapon(AnimatedSprite):
	def __init__(self, game, path='C:/Users/Brandon/RaycastingGame/_resources/_weapon/weapon_1.png', scale=0.4, animation_time=90, pos=(0, 0), shift = 0):
		super().__init__(game=game, path=path, scale=scale, animation_time=animation_time, pos=pos, shift=shift)
		self.images = deque(
			[pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
			 for img in self.images])
		self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())


	def draw(self):
		self.game.screen.blit(self.images[0], self.weapon_pos)

	def update(self):
		pass