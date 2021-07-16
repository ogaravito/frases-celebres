import tkinter
import random
import time

ventana = tkinter.Tk()
ventana.title("Mensajes")
ventana.geometry("225x75")

texto = tkinter.Label(ventana, wraplength=200)
texto.pack()

mensajes = [
    "Perder es ganar un poco. - Francisco Maturana",
    "Trabajar no es malo, lo malo es tener que trabajar - Don Ramón",
    "Si la culpa es mia entonces se la puedo echar a quien yo quiera - Homer Simpson",
    "Así lo ví, así lo conocí, así lo querí - Ivan Duque",
    "A veces cierro los ojos y no veo - Nicolás Maduro"
]

def nuevo_mensaje():
    mensaje = random.choice(mensajes)
    texto["text"] = mensaje
    texto["fg"] = 'darkblue'
    ventana.after(10000, nuevo_mensaje)

nuevo_mensaje()

ventana.mainloop()