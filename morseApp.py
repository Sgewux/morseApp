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
				break
			
			elif l == " ":
				letra_traducida = " "
				break
			
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
			for i in range(1, 27):
				if letra == alfabeto[i]:
					traduccion += alfabeto_morse[i] + '/'
					break

				elif letra == ' ':
					traduccion += ' ' + '/'
					break

				else:
					continue
					
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
