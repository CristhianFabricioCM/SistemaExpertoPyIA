import tkinter as tk
from ventana_problemas import VentanaProblemas

class VentanaDatos:
  def __init__(self):
    self.ventana_datos = tk.Tk()
    self.ventana_datos.geometry("470x250")
    self.ventana_datos.title("Sistema Experto")

    self.label_titulo = tk.Label(self.ventana_datos, text="SISTEMA EXPERTO PARA EL DIAGNÓSTICO DE PROBLEMAS MECÁNICOS", font=("Arial", 10))
    self.label_titulo.grid(row=0, column=0, pady=7)

    self.label_marca = tk.Label(self.ventana_datos, text="Marca:", font=("Arial", 10))
    self.label_marca.grid(row=1, column=0, pady=5, padx=(100, 0), sticky="w")
    self.entrada_marca = tk.Entry(self.ventana_datos, font=("Arial", 10))
    self.entrada_marca.grid(row=1, column=0, pady=5, padx=(0, 100), sticky="e")

    self.label_modelo = tk.Label(self.ventana_datos, text="Modelo:", font=("Arial", 10))
    self.label_modelo.grid(row=2, column=0, pady=5, padx=(100, 0), sticky="w")
    self.entrada_modelo = tk.Entry(self.ventana_datos, font=("Arial", 10))
    self.entrada_modelo.grid(row=2, column=0, pady=5, padx=(0, 100), sticky="e")

    self.label_anio = tk.Label(self.ventana_datos, text="Año:", font=("Arial", 10))
    self.label_anio.grid(row=3, column=0, pady=5, padx=(100, 0), sticky="w")
    self.entrada_anio = tk.Entry(self.ventana_datos, font=("Arial", 10))
    self.entrada_anio.grid(row=3, column=0, pady=5, padx=(0, 100), sticky="e")

    self.boton_iniciar = tk.Button(self.ventana_datos, text="Iniciar", command=self.abrir_ventana_problemas)
    self.boton_iniciar.grid(row=5, column=0, pady=10)

    self.boton_salir = tk.Button(self.ventana_datos, text="Salir", command=self.ventana_datos.destroy)
    self.boton_salir.grid(row=6, column=0, pady=10)

  def abrir_ventana_problemas(self):
    marca = self.entrada_marca.get()
    modelo = self.entrada_modelo.get()
    anio = self.entrada_anio.get()
    ventana_problemas = VentanaProblemas(self.ventana_datos, marca, modelo, anio)
    ventana_problemas.mostrar_ventana()

  def iniciar(self):
    self.ventana_datos.mainloop()
