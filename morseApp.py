#imports
from tkinter import *
import winsound 
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
#functions
tt = ''

def traducir_letra(l):
		letra_traducida = ""
		for i in range(1, 27):

			if l == alfabeto_morse[i]:
				letra_traducida = alfabeto[i]
			
			elif l == " ":
				letra_traducida = " "
			
			else:
				continue
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
	global tt
	tt = traducir(mainWindow.e.get())	
	entrytt = Entry(root, width=50, bg="#f1f1f1", borderwidth=0)
	entrytt.insert(0, "El texto en morse es: " + tt)
	entrytt.grid(row=2, column=0)


def button2():
	tm = traducir_morse(mainWindow.e1.get())
	entrytm = Entry(root, width=50, bg="#f1f1f1", borderwidth=0)
	entrytm.insert(0, "El morse en texto es: " + tm)
	entrytm.grid(row=5, column=0)


def play(mt):
	for x in mt:
		if x == '.':
			winsound.Beep(3799, 500)

		elif x == '-':
			winsound.Beep(3799, 1000)
	
		else:
			continue
#graphics
root = Tk()
root.title("MorseApp")
root.geometry("420x450")


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

		self.mybutton3 = Button(self.root, text='Escuchar', command= lambda: play(tt))
		self.mybutton3.grid(row=1, column=2)


if __name__ == '__main__':
	mainWindow = Window(root)


root.mainloop()
