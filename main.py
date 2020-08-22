import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""

		       S P A M  S M S      
		---------------------------
		      Author : Andrian    

Jangan Disalah Gunakan !!!

1. SMS Gratis
2. OTP Matahari
3. OTP Hallodok
4. OTP Olx.co.id
5. OTP Sociolla.com
""")
		pilih=int(input('Silahkan Di Pilih No Nya /> '))
		if pilih == 1:
			import src.All-Operator
		elif pilih == 2:
			import src.Matahari
		elif pilih == 3:
			import src.Halodok
		elif pilih == 4:
			import src.olx
		elif pilih == 5:
			import src.socil
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))