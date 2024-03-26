# Diccionario de preguntas categorizadas por problemas del vehículo

preguntas = {
  "No enciende": [
    "1. ¿El vehículo ha pasado por mantenimiento en los últimos 6 meses?",
    "2. ¿Se le ha presentado este problema en los últimos 6 meses?",
    "3. ¿El vehículo presentaba ruidos extraños?",
    "4. ¿El auto presentaba dificultades para encender?",
    "5. ¿Se encienden las luces del tablero cuando giras la llave?",
    "6. ¿Escuchas algún clic al intentar encender el motor?",
    "7. ¿Hay suficiente combustible en el tanque?",
    "8. ¿Has notado algún olor a quemado o algún humo inusual?",
    "9. ¿El vehículo ha estado estacionado durante mucho tiempo sin uso?",
    "10. ¿El auto hace algún sonido cuando intentas encenderlo?",
    "11. ¿La luz interior del vehículo se enciende correctamente?",
    "12. ¿Has revisado los fusibles relacionados con el sistema de encendido?",
    "13. ¿El vehículo ha estado expuesto a condiciones climáticas extremas recientemente?",
    "14. ¿Has intentado encender el automóvil después de un largo período de inactividad?",
    "15. ¿La llave de encendido gira con normalidad?"
  ],
  "Hace ruidos extraños": [
    "1. ¿El ruido ocurre al conducir a una velocidad específica o en cualquier momento?",
    "2. ¿El ruido es más pronunciado al girar en una dirección particular?",
    "3. ¿El ruido cambia con la velocidad del motor?",
    "4. ¿El ruido parece provenir del motor, las ruedas o la transmisión?",
    "5. ¿El ruido se produce solo cuando el automóvil está en movimiento?",
    "6. ¿El ruido se intensifica al frenar o acelerar?",
    "7. ¿Ha habido algún incidente o impacto reciente con el vehículo?",
    "8. ¿Has notado alguna vibración acompañando al ruido?",
    "9. ¿El vehículo ha recibido mantenimiento regularmente?",
    "10. ¿El ruido es constante o intermitente?",
    "11. ¿El ruido apareció repentinamente o ha estado presente gradualmente?",
    "12. ¿El ruido cambia cuando se enciende o apaga el aire acondicionado?",
    "13. ¿Ha habido algún trabajo de reparación reciente en el automóvil?",
    "14. ¿El ruido varía al cambiar de marcha o al realizar maniobras específicas?"
  ],
  "Pérdida de Potencia": [
    "1. ¿El vehículo ha estado estacionado durante mucho tiempo sin uso?",
    "2. ¿Has revisado el nivel de aceite y otros fluidos del automóvil recientemente?",
    "3. ¿El vehículo ha sido modificado o tuneado de alguna manera?",
    "4. ¿Hay suficiente combustible en el tanque?",
    "5. ¿El filtro de aire ha sido reemplazado dentro del intervalo recomendado?",
    "6. ¿El vehículo ha sido sometido a mantenimiento regularmente?",
    "7. ¿Se han realizado inspecciones recientes en el sistema de escape?",
    "8. ¿Has notado fugas de líquidos debajo del automóvil?",
    "9. ¿La pérdida de potencia se acompaña de algún otro síntoma, como vibraciones?",
    "10. ¿La pérdida de potencia ocurre solo bajo ciertas condiciones?",
    "11. ¿El rendimiento del motor ha disminuido en general o solo en ciertas situaciones?",
    "12. ¿Has realizado alguna inspección visual del motor en busca de componentes dañados o sueltos?",
    "13. ¿Has notado alguna luz de advertencia en el tablero relacionada con la potencia del motor?",
    "14. ¿La pérdida de potencia es más notable al subir pendientes o al llevar cargas pesadas?"
  ]
}

# Función para obtener las preguntas asociadas a un problema específico
def obtener_preguntas(variable_seleccionada):
  return preguntas.get(variable_seleccionada, [])

# Lista de diagnósticos con preguntas y posibles causas
diagnosticos = [
  {"preguntas": ["1. ¿El vehículo ha pasado por mantenimiento en los últimos 6 meses?",
                  "2. ¿Se le ha presentado este problema en los últimos 6 meses?",
                  "3. ¿El vehículo presentaba ruidos extraños?"],
    "causa": "Problemas con el sistema de encendido y fallo en la bomba de combustible."},
  {"preguntas": ["4. ¿El auto presentaba dificultades para encender?" ,
                  "5. ¿Se encienden las luces del tablero cuando giras la llave?",
                  "6. ¿Escuchas algún clic al intentar encender el motor?"],
    "causa": "Posible batería descargada y fallo en el sistema de encendido."},
  {"preguntas": ["7. ¿Hay suficiente combustible en el tanque?",
                  "8. ¿Has notado algún olor a quemado o algún humo inusual?",
                  "9. ¿El vehículo ha estado estacionado durante mucho tiempo sin uso?"],
    "causa": "Problemas con la mezcla de aire y combustible y obstrucción en el sistema de escape."},
  {"preguntas": ["10. ¿El auto hace algún sonido cuando intentas encenderlo?",
                  "11. ¿La luz interior del vehículo se enciende correctamente?",
                  "12. ¿Has revisado los fusibles relacionados con el sistema de encendido?"],
    "causa": "Problemas eléctricos y posibles fusibles fundidos."},
  {"preguntas": ["13. ¿El vehículo ha estado expuesto a condiciones climáticas extremas recientemente?",
                  "14. ¿Has intentado encender el automóvil después de un largo período de inactividad?",
                  "15. ¿La llave de encendido gira con normalidad?"],
    "causa": "Daños causados por la temperatura y problemas con el sistema de bloqueo."},
  
  {"preguntas": ["1. ¿El ruido ocurre al conducir a una velocidad específica o en cualquier momento?",
                  "2. ¿El ruido es más pronunciado al girar en una dirección particular?"],
    "causa": "Problemas con la transmisión y desgaste de los neumáticos."},
  {"preguntas": ["3. ¿El ruido cambia con la velocidad del motor?",
                  "4. ¿El ruido parece provenir del motor, las ruedas o la transmisión?",
                  "5. ¿El ruido se produce solo cuando el automóvil está en movimiento?"],
    "causa": "Problemas con la distribución y con el sistema de refrigeración."},
  {"preguntas": ["6. ¿El ruido se intensifica al frenar o acelerar?",
                  "7. ¿Ha habido algún incidente o impacto reciente con el vehículo?",
                  "8. ¿Has notado alguna vibración acompañando al ruido?"],
    "causa": "Problemas con los frenos y daños en el sistema de escape."},
  {"preguntas": ["9. ¿El vehículo ha recibido mantenimiento regularmente?",
                  "10. ¿El ruido es constante o intermitente?",
                  "11. ¿El ruido apareció repentinamente o ha estado presente gradualmente?"],
    "causa": "Falta de lubricación y desgaste entre los componentes."},
  {"preguntas": ["12. ¿El ruido cambia cuando se enciende o apaga el aire acondicionado?"],
    "causa": "Problemas con el compresor del aire acondicionado."},
  {"preguntas": ["13. ¿Ha habido algún trabajo de reparación reciente en el automóvil?"],
    "causa": "Posibles daños causados por trabajos de reparación anteriores."},
  {"preguntas": ["9. ¿El vehículo ha recibido mantenimiento regularmente?",
                  "14. ¿El ruido varía al cambiar de marcha o al realizar maniobras específicas?"],
    "causa": "Problemas en el sistema de embrague por falta de lubricación en la transmisión."},

  {"preguntas": ["1. ¿El vehículo ha estado estacionado durante mucho tiempo sin uso?",
                  "2. ¿Has revisado el nivel de aceite y otros fluidos del automóvil recientemente?",
                  "3. ¿El vehículo ha sido modificado de alguna manera?"],
    "causa": "Falta de mantenimiento y posibles problemas con la presión de los neumáticos."},
  {"preguntas": ["4. ¿Hay suficiente combustible en el tanque?"],
    "causa": "Posible falta de combustible."},
  {"preguntas": ["5. ¿El filtro de aire ha sido reemplazado dentro del intervalo recomendado?",
                  "6. ¿El vehículo ha sido sometido a mantenimiento regularmente?"],
    "causa": "Problemas con el filtro de aire y el sensor de flujo de aire."},
  {"preguntas": ["7. ¿Se han realizado inspecciones recientes en el sistema de escape?",
                  "8. ¿Has notado fugas de líquidos debajo del automóvil?",
                  "9. ¿La pérdida de potencia se acompaña de algún otro síntoma, como vibraciones?"],
    "causa": "Problemas con el sistema de escape (posible obstrucción) y fugas en el sistema."},
  {"preguntas": ["10. ¿La pérdida de potencia ocurre solo bajo ciertas condiciones?",
                  "11. ¿El rendimiento del motor ha disminuido en general o solo en ciertas situaciones?",
                  "12. ¿Has realizado alguna inspección visual del motor en busca de componentes dañados o sueltos?"],
    "causa": "Problemas con el sistema de transmisión y fallo en el sensor de posición del acelerador."},
  {"preguntas": ["13. ¿Has notado alguna luz de advertencia en el tablero relacionada con la potencia del motor?"],
    "causa": "Problemas con el sistema de combustible."},
  {"preguntas": ["2. ¿Has revisado el nivel de aceite y otros fluidos del automóvil recientemente?",
                  "7. ¿Se han realizado inspecciones recientes en el sistema de escape?",
                  "14. ¿La pérdida de potencia es más notable al subir pendientes o al llevar cargas pesadas?"],
    "causa": "Problemas con la inyección de combustible."}
]

# Función para obtener la lista de diagnósticos
def obtener_diagnosticos():
  return diagnosticos
