import tkinter as tk
from data import obtener_preguntas, obtener_diagnosticos

class VentanaPreguntas:
  def __init__(self, ventana_padre, variable_seleccionada):
    self.ventana_padre = ventana_padre
    self.variable_seleccionada = variable_seleccionada
    self.preguntas_a_mostrar = obtener_preguntas(self.variable_seleccionada)
    self.diagnosticos = obtener_diagnosticos()

  def mostrar_ventana(self):
    self.ventana_preguntas = tk.Toplevel(self.ventana_padre)
    self.ventana_preguntas.geometry("900x900")
    self.ventana_preguntas.title("Preguntas")

    label_titulo = tk.Label(self.ventana_preguntas, text="SISTEMA EXPERTO PARA EL DIAGNÓSTICO DE PROBLEMAS MECÁNICOS", font=("Arial",9))
    label_titulo.grid(row=0, column=0, pady=7)

    respuestas = {}

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

    boton_enviar_respuestas = tk.Button(self.ventana_preguntas, text="Enviar Respuestas", command=lambda: self.mostrar_diagnostico(respuestas))
    boton_enviar_respuestas.grid(row=len(self.preguntas_a_mostrar)+1, column=0, columnspan=2, pady=10)

    # Botón para limpiar el diagnóstico
    boton_limpiar = tk.Button(self.ventana_preguntas, text="Limpiar", command=self.limpiar_diagnostico)
    boton_limpiar.grid(row=len(self.preguntas_a_mostrar)+1, column=1, pady=10)

    # Label para mostrar el diagnóstico
    self.label_diagnostico = tk.Label(self.ventana_preguntas, text="", font=("Arial", 9))
    self.label_diagnostico.grid(row=len(self.preguntas_a_mostrar)+2, column=0, columnspan=2, pady=5, sticky="w")
    
    boton_salir = tk.Button(self.ventana_preguntas, text="Salir", command=self.ventana_preguntas.destroy)
    boton_salir.grid(row=len(self.preguntas_a_mostrar)+1, column=3, pady=10)

  def mostrar_diagnostico(self, respuestas):
    diagnosticos_encontrados = []
    for diagnostico in self.diagnosticos:
      # Verificar si todas las preguntas del diagnóstico tienen una respuesta
      todas_respuestas = all(pregunta in respuestas for pregunta in diagnostico["preguntas"])
      if todas_respuestas:
        # Verificar si todas las respuestas son "Si"
        todas_si = all(respuestas[pregunta].get() == "Si" for pregunta in diagnostico["preguntas"])
        if todas_si:
          diagnosticos_encontrados.append(diagnostico["causa"])

    if diagnosticos_encontrados:
      texto = "Se encontraron las siguientes posibles causas del problema:\n"
      for idx, diagnostico in enumerate(diagnosticos_encontrados, start=1):
        texto += f"{idx}. {diagnostico}\n"
      self.label_diagnostico.config(text=texto)
    else:
      self.label_diagnostico.config(text="No se encontraron posibles causas del problema.")

  def limpiar_diagnostico(self):
    self.label_diagnostico.config(text="")
