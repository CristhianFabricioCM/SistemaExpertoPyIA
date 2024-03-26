import tkinter as tk
from ventana_preguntas import VentanaPreguntas

# Definición de la clase VentanaProblemas
class VentanaProblemas:

  # Método de inicialización de la clase
  def __init__(self, ventana_padre, marca, modelo, anio):
      
      # Inicializa variables de la clase con la ventana padre, la marca, el modelo y el año del vehículo
      self.ventana_padre = ventana_padre
      self.marca = marca
      self.modelo = modelo
      self.anio = anio

  # Método para mostrar la ventana de problemas
  def mostrar_ventana(self):

    # Crea una nueva ventana secundaria
    self.ventana_problemas = tk.Toplevel(self.ventana_padre)
    self.ventana_problemas.geometry("470x470")
    self.ventana_problemas.title("Problema del vehículo")

    # Crea una etiqueta para el título del sistema experto
    label_titulo = tk.Label(self.ventana_problemas, text="SISTEMA EXPERTO PARA EL DIAGNÓSTICO DE PROBLEMAS MECÁNICOS", font=("Arial", 10))
    label_titulo.grid(row=0, column=0, pady=7)

    # Crea etiquetas para mostrar las características del auto
    label_auto = tk.Label(self.ventana_problemas, text="Características del auto:", font=("Arial", 10))
    label_auto.grid(row=1, column=0, pady=5, padx=(100, 0), sticky="w")


    label_marca = tk.Label(self.ventana_problemas, text="Marca: " + self.marca, font=("Arial", 10))
    label_marca.grid(row=2, column=0, pady=2, padx=(100, 0), sticky="w")

    label_modelo = tk.Label(self.ventana_problemas, text="Modelo: " + self.modelo, font=("Arial", 10))
    label_modelo.grid(row=3, column=0, pady=2, padx=(100, 0), sticky="w")

    label_anio = tk.Label(self.ventana_problemas, text="Año: " + self.anio, font=("Arial", 10))
    label_anio.grid(row=4, column=0, pady=2, padx=(100, 0), sticky="w")

    # Crea una etiqueta para preguntar sobre el problema del vehículo
    label_pregunta = tk.Label(self.ventana_problemas, text="¿Qué ocurre con su vehículo? (Seleccione una opción):", font=("Arial", 10))
    label_pregunta.grid(row=5, column=0, pady=5, sticky="w")

    # Crea radio botones para que el usuario seleccione el problema del vehículo
    variable_seleccionada = tk.StringVar(value="No enciende")
    opcion_1 = tk.Radiobutton(self.ventana_problemas, text="No enciende", value="No enciende", variable=variable_seleccionada)
    opcion_1.grid(row=6, column=0, pady=5, padx=(100, 0), sticky="w")
    
    opcion_2 = tk.Radiobutton(self.ventana_problemas, text="Hace ruidos extraños", value="Hace ruidos extraños", variable=variable_seleccionada)
    opcion_2.grid(row=7, column=0, pady=5, padx=(100, 0), sticky="w")

    opcion_3 = tk.Radiobutton(self.ventana_problemas, text="Pérdida de Potencia", value="Pérdida de Potencia", variable=variable_seleccionada)
    opcion_3.grid(row=8, column=0, pady=5, padx=(100, 0), sticky="w")

    # Botón para enviar la opción seleccionada y abrir la ventana de preguntas
    boton_enviar = tk.Button(self.ventana_problemas, text="Enviar", command=lambda: self.abrir_ventana_preguntas(variable_seleccionada.get()))
    boton_enviar.grid(row=9, column=0, pady=12)

    # Botón para salir de la ventana de problemas
    boton_salir = tk.Button(self.ventana_problemas, text="Salir", command=self.ventana_problemas.destroy)
    boton_salir.grid(row=10, column=0, pady=10)

  # Método para abrir la ventana de preguntas
  def abrir_ventana_preguntas(self, variable_seleccionada):
    ventana_preguntas = VentanaPreguntas(self.ventana_problemas, variable_seleccionada)
    ventana_preguntas.mostrar_ventana()
