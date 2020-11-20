#imports
from tkinter import * 
#letters
alfabeto = {
	1: "a",
	2: "b",
	3: "c",
	4: "d",
	5: "e",
	6: "f",
	7: "g",
	8: "h",
	9: "i",
	10: "j",
	11: "k",
	12: "l",
	13: "m",
	14: "n",
	15: "o",
	16: "p",
	17: "q",
	18: "r",
	19: "s",
	20: "t",
	21: "u",
	22: "v",
	23: "w",
	24: "x",
	25: "y",
	26: "z"
}
#morse letters
alfabeto_morse = {
	1: ".-",
	2: "-...",
	3: "-.-.",
	4: "-..",
	5: ".",
	6: "..-.",
	7: "--.",
	8: "....",
	9: "..",
	10: ".---",
	11: "-.-",
	12: ".-..",
	13: "--",
	14: "-.",
	15: "---",
	16: ".--.",
	17: "--.-",
	18: ".-.",
	19: "...",
	20: "-",
	21: "..-",
	22: "...-",
	23: ".--",
	24: "-..-",
	25: "-.--",
	26: "--.."
}
#funciones
def traducir_letra(l):
		letra_traducida = ""
		if l == alfabeto_morse[1]:
		 	letra_traducida = alfabeto[1]
		elif l == alfabeto_morse[2]:
		 	letra_traducida = alfabeto[2] 
		elif l == alfabeto_morse[3]:
		 	letra_traducida = alfabeto[3]
		elif l == alfabeto_morse[4]:
		 	letra_traducida = alfabeto[4]
		elif l == alfabeto_morse[5]:
		 	letra_traducida = alfabeto[5]
		elif l == alfabeto_morse[6]:
		 	letra_traducida = alfabeto[6]
		elif l == alfabeto_morse[7]:
		 	letra_traducida = alfabeto[7]
		elif l == alfabeto_morse[8]:
			letra_traducida = alfabeto[8]
		elif l == alfabeto_morse[9]:
		 	letra_traducida = alfabeto[9]
		elif l == alfabeto_morse[10]:
		 	letra_traducida = alfabeto[10]
		elif l == alfabeto_morse[11]:
		 	letra_traducida = alfabeto[11]
		elif l == alfabeto_morse[12]:
		 	letra_traducida = alfabeto[12]
		elif l == alfabeto_morse[13]:
		 	letra_traducida = alfabeto[13]
		elif l == alfabeto_morse[14]:
		 	letra_traducida = alfabeto[14]
		elif l == alfabeto_morse[15]:
		 	letra_traducida = alfabeto[15]
		elif l == alfabeto_morse[16]:
		 	letra_traducida = alfabeto[16]
		elif l == alfabeto_morse[17]:
		 	letra_traducida = alfabeto[17]
		elif l == alfabeto_morse[18]:
		 	letra_traducida = alfabeto[18]
		elif l == alfabeto_morse[19]:
		 	letra_traducida = alfabeto[19]
		elif l == alfabeto_morse[20]:
		 	letra_traducida = alfabeto[20]
		elif l == alfabeto_morse[21]:
		 	letra_traducida = alfabeto[21]
		elif l == alfabeto_morse[22]:
		 	letra_traducida = alfabeto[22]
		elif l == alfabeto_morse[23]:
		 	letra_traducida = alfabeto[23]
		elif l == alfabeto_morse[24]:
		 	letra_traducida = alfabeto[24]
		elif l == alfabeto_morse[25]:
		 	letra_traducida = alfabeto[25]
		elif l == alfabeto_morse[26]:
		 	letra_traducida = alfabeto[26]
		elif l == " ":
			letra_traducida = " "
		return letra_traducida

 		
def traducir_morse(f):
	letra = ""
	traduccion_final = ""
	for x in f:
	 	if x != "/":
	 	 	letra = letra + x

	 	elif x == "/":
	 		traduccion_final = traduccion_final + traducir_letra(letra)
	 		letra = ""
	return traduccion_final


def traducir(frase):
		traduccion = ""
		for letra in frase:
			if letra in alfabeto[1]:
				traduccion = traduccion + alfabeto_morse[1] + "/"
			elif letra in alfabeto[2]:
				traduccion = traduccion + alfabeto_morse[2] + "/"
			elif letra in alfabeto[3]:
				traduccion = traduccion + alfabeto_morse[3] + "/"	
			elif letra in alfabeto[4]:
				traduccion = traduccion + alfabeto_morse[4] + "/"	
			elif letra in alfabeto[5]:
				traduccion = traduccion + alfabeto_morse[5] + "/"	
			elif letra in alfabeto[6]:
				traduccion = traduccion + alfabeto_morse[6] + "/"	
			elif letra in alfabeto[7]:
				traduccion = traduccion + alfabeto_morse[7] + "/"	
			elif letra in alfabeto[8]:
				traduccion = traduccion + alfabeto_morse[8] + "/"	
			elif letra in alfabeto[9]:
				traduccion = traduccion + alfabeto_morse[9] + "/"	
			elif letra in alfabeto[10]:
				traduccion = traduccion + alfabeto_morse[10] + "/"	
			elif letra in alfabeto[11]:
				traduccion = traduccion + alfabeto_morse[11] + "/"	
			elif letra in alfabeto[12]:
				traduccion = traduccion + alfabeto_morse[12] + "/"	
			elif letra in alfabeto[13]:
				traduccion = traduccion + alfabeto_morse[13] + "/"	
			elif letra in alfabeto[14]:
				traduccion = traduccion + alfabeto_morse[14] + "/"	
			elif letra in alfabeto[15]:
				traduccion = traduccion + alfabeto_morse[15] + "/"	
			elif letra in alfabeto[16]:
				traduccion = traduccion + alfabeto_morse[16] + "/"	
			elif letra in alfabeto[17]:
				traduccion = traduccion + alfabeto_morse[17] + "/"	
			elif letra in alfabeto[18]:
				traduccion = traduccion + alfabeto_morse[18] + "/"	
			elif letra in alfabeto[19]:
				traduccion = traduccion + alfabeto_morse[19] + "/"	
			elif letra in alfabeto[20]:
				traduccion = traduccion + alfabeto_morse[20] + "/"	
			elif letra in alfabeto[21]:
				traduccion = traduccion + alfabeto_morse[21] + "/"	
			elif letra in alfabeto[22]:
				traduccion = traduccion + alfabeto_morse[22] + "/"	
			elif letra in alfabeto[23]:
				traduccion = traduccion + alfabeto_morse[23] + "/"	
			elif letra in alfabeto[24]:
				traduccion = traduccion + alfabeto_morse[24] + "/"	
			elif letra in alfabeto[25]:
				traduccion = traduccion + alfabeto_morse[25] + "/"
			elif letra in alfabeto[26]:
				traduccion = traduccion + alfabeto_morse[26] + "/"	
			elif letra == " ":
				traduccion = traduccion + " " + "/"
			else:
				traduccion = traduccion + "*caracter invalido*/"
		return traduccion


def button1():
	tt = traducir(mainWindow.e.get())	
	entrytt = Entry(root, width=50, bg="#f1f1f1", borderwidth=0)
	entrytt.insert(0, "El texto en morse es: " + tt)
	entrytt.grid(row=2, column=0)


def button2():
	tm = traducir_morse(mainWindow.e1.get())
	entrytm = Entry(root, width=50, bg="#f1f1f1", borderwidth=0)
	entrytm.insert(0, "El morse en texto es: " + tm)
	entrytm.grid(row=5, column=0)

#graphics
root = Tk()
root.title("MorseApp")
root.geometry("400x450")


#Class window
class Window:

	def __init__(self, root):
		self.root = root

		self.mylabel1 = Label(self.root, text="Escribe el texto sin tildes, ni mayusculas ni comas", fg="blue")
		self.mylabel1.grid(row=0, column=0)
		self.e = Entry(self.root, width=50)
		self.e.grid(row=1, column=0)
		self.mybutton1 = Button(self.root, text="traducir", command=button1)
		self.mybutton1.grid(row=1, column=1)

		self.mylabel2 = Label(self.root, text='Escribe el texto en morse con "/" para separar las letras', fg="blue")
		self.mylabel2.grid(row=3, column=0)
		self.e1 = Entry(self.root, width=50)
		self.e1.grid(row=4, column=0)
		self.mybutton2 = Button(self.root, text="traducir", command=button2)
		self.mybutton2.grid(row=4, column=1)


if __name__ == '__main__':
	mainWindow = Window(root)

root.mainloop()
