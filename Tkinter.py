import tkinter as tk

def saludar():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    etiqueta_resultado.config(text=f"Hola {nombre}, tienes {edad} años.")

ventana = tk.Tk()
ventana.title("Mi primera app gráfica")
ventana.geometry("400x220")
ventana.configure(bg="lightblue")  # Fondo azul claro

etiqueta_nombre = tk.Label(ventana, text="Ingresa tu nombre:", bg="lightblue")
etiqueta_nombre.pack(pady=4)

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=4)

etiqueta_edad = tk.Label(ventana, text="Ingresa tu edad:", bg="lightblue")
etiqueta_edad.pack(pady=4)

entrada_edad = tk.Entry(ventana)
entrada_edad.pack(pady=4)

boton = tk.Button(ventana, text="Mostrar saludo", command=saludar)
boton.pack(pady=6)

etiqueta_resultado = tk.Label(ventana, text="", bg="lightblue")
etiqueta_resultado.pack(pady=6)


ventana.mainloop()
