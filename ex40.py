class Song(object):
	def __init__(self,lyrics):
		self.lyrics=lyrics #why do I need __init__ and what attribute is self? why cant I just start with a sing_me_a_song function?
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",			
					"so I'll stop right here"])

bulls_on_parade= Song(["They rally around the family",
						"with pockets fullo of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

				
