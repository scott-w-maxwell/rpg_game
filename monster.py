weapons = {"Sword": 4, "Knife": 2, "LongSword": 5}

class Monster:
	def __init__(self, health = 100, attack_lvl = 20, weapon = None):
		self.health = health
		self.weapon = weapon

		# Increase attack if monster has weapon
		if weapon:
			self.attack_lvl = attack_lvl + weapons[weapon]
		else:
			self.attack_lvl = attack_lvl

	def attack(self, other_monster):
		other_monster.health -= self.attack_lvl

	def __str__(self):
		return f'Health {self.health}\nAttack Lvl: {self.attack_lvl}\nWeapon: {self.weapon}'


class Player(Monster):
	pass







