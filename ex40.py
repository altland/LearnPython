class song(object):
	def __init__(self,lyrics):
		self.lyrics=lyrics
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = song(["danwkedj dede","dwekfdow fewf",
				   "dewdff fdswd"])
				   
bulls = song(["jklm",
              "opqr",
			  "dscedve"])
			  
happy_bday.sing_me_a_song()
bulls.sing_me_a_song()

print "-"*20	

class songagain(object):
	def __init__(self):
		self.lyrics=["another one jkhs khd","another two dwqdew dsads"]
	def sms(self):
		for line in self.lyrics:
			print line
temp=songagain()
temp.sms()

	