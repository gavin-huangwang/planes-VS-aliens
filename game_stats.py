class Gamestats():
	def __init__(self,ai_Settings):
		self.ai_Settings=ai_Settings
		self.reset_stats()
		self.game_active=True
		
	def reset_stats(self):
		self.ships_left=self.ai_Settings.ship_limit
