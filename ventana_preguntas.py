import tkinter as tk
from data import obtener_preguntas, obtener_diagnosticos

# Definición de la clase VentanaPreguntas
class VentanaPreguntas:

   # Método de inicialización de la clase
  def __init__(self, ventana_padre, variable_seleccionada):

    # Inicializa variables de la clase con la ventana padre y la variable seleccionada
    self.ventana_padre = ventana_padre
    self.variable_seleccionada = variable_seleccionada

     # Obtiene preguntas y diagnósticos del módulo data
    self.preguntas_a_mostrar = obtener_preguntas(self.variable_seleccionada)
    self.diagnosticos = obtener_diagnosticos()

  # Método para mostrar la ventana de preguntas
  def mostrar_ventana(self):

    # Crea una nueva ventana secundaria
    self.ventana_preguntas = tk.Toplevel(self.ventana_padre)
    self.ventana_preguntas.geometry("700x800")
    self.ventana_preguntas.title("Preguntas")

    # Crea una etiqueta para el título del sistema experto
    label_titulo = tk.Label(self.ventana_preguntas, text="SISTEMA EXPERTO PARA EL DIAGNÓSTICO DE PROBLEMAS MECÁNICOS", font=("Arial",9))
    label_titulo.grid(row=0, column=0, pady=7)

    respuestas = {}

    # Itera sobre las preguntas y crea etiquetas y radio botones para cada una
    for indice, pregunta in enumerate(self.preguntas_a_mostrar):
      label_pregunta = tk.Label(self.ventana_preguntas, text=pregunta, font=("Arial",9))
      label_pregunta.grid(row=indice+1, column=0, pady=5, sticky="w")
      
      respuesta_seleccionada = tk.StringVar(self.ventana_preguntas, value="Si")
      respuestas[pregunta] = respuesta_seleccionada

      label_espacio = tk.Label(self.ventana_preguntas, text="-", font=("Arial",9))
      label_espacio.grid(row=indice+1, column=1)

      radiobtn_respuesta_si = tk.Radiobutton(self.ventana_preguntas, text="Si", value="Si", variable=respuesta_seleccionada)
      # radiobtn_respuesta_si.grid(row=indice+1, column=1, pady=5, padx=(100, 0), sticky="w")
      # radiobtn_respuesta_si.grid(row=indice+1, column=2, pady=5, sticky="w")
      radiobtn_respuesta_si.grid(row=indice+1, column=2, pady=5)

      radiobtn_respuesta_no = tk.Radiobutton(self.ventana_preguntas, text="No", value="No", variable=respuesta_seleccionada)
      # radiobtn_respuesta_no.grid(row=indice+1, column=2, pady=5, padx=(0, 100), sticky="e")
      # radiobtn_respuesta_no.grid(row=indice+1, column=3, pady=5, sticky="e")
      radiobtn_respuesta_no.grid(row=indice+1, column=3, pady=5)

    # Botón para enviar respuestas y mostrar diagnóstico
    boton_enviar_respuestas = tk.Button(self.ventana_preguntas, text="Enviar Respuestas", command=lambda: self.mostrar_diagnostico(respuestas))
    boton_enviar_respuestas.grid(row=len(self.preguntas_a_mostrar)+1, column=0, columnspan=2, pady=10)

    # Botón para limpiar el diagnóstico
    boton_limpiar = tk.Button(self.ventana_preguntas, text="Limpiar", command=self.limpiar_diagnostico)
    boton_limpiar.grid(row=len(self.preguntas_a_mostrar)+1, column=1, pady=10)

    # Label para mostrar el diagnóstico
    self.label_diagnostico = tk.Label(self.ventana_preguntas, text="", font=("Arial", 9))
    self.label_diagnostico.grid(row=len(self.preguntas_a_mostrar)+2, column=0, columnspan=2, pady=5, sticky="w")
    
    # Botón para salir de la ventana de preguntas
    boton_salir = tk.Button(self.ventana_preguntas, text="Salir", command=self.ventana_preguntas.destroy)
    boton_salir.grid(row=len(self.preguntas_a_mostrar)+1, column=3, pady=10)

  # Método para mostrar el diagnóstico basado en las respuestas ingresadas
  def mostrar_diagnostico(self, respuestas):
    diagnosticos_encontrados = []
    for diagnostico in self.diagnosticos:

      # Itera sobre los diagnósticos y verifica si todas las preguntas tienen respuesta y son "Si"
      todas_respuestas = all(pregunta in respuestas for pregunta in diagnostico["preguntas"])
      
      if todas_respuestas:
        todas_si = all(respuestas[pregunta].get() == "Si" for pregunta in diagnostico["preguntas"])
        if todas_si:
          diagnosticos_encontrados.append(diagnostico["causa"])

     # Actualiza el texto del label de diagnóstico con los resultados encontrados
    if diagnosticos_encontrados:
      texto = "Se encontraron las siguientes posibles causas del problema:\n"
      for idx, diagnostico in enumerate(diagnosticos_encontrados, start=1):
        texto += f"{idx}. {diagnostico}\n"
      self.label_diagnostico.config(text=texto)
    else:
      self.label_diagnostico.config(text="No se encontraron posibles causas del problema.")

  # Método para limpiar el diagnóstico
  def limpiar_diagnostico(self):
    self.label_diagnostico.config(text="")
