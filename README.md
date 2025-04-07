## Introducción

Este proyecto es un programa de línea de comandos (CLI) desarrollada en Python como parte del reto técnico de Interbank Academy 25.

El objetivo es procesar un archivo CSV que contiene transacciones bancarias y generar un reporte completo en la terminal.
El reporte incluye:

- El "balance final", resultado de la suma de transacciones tipo "Crédito" menos las de tipo "Débito".
- La "transacción con el monto más alto", mostrando su ID y valor.
- El "conteo total de transacciones" por tipo ("Crédito" y "Débito").

La aplicación fue desarrollada con un enfoque paso a paso, incorporando validaciones para asegurar la correcta lectura de datos. Este reto permitió aplicar buenas prácticas de programación, manteniendo la solución clara, sencilla y fácil de entender.

--

## Instrucciones de Ejecución

### Requisitos

- Tener Python 3 instalado en el sistema (se recomienda Python 3.8 o superior).
- No se requiere instalar paquetes adicionales, ya que se utilizan únicamente módulos estándar de Python (`csv`, `os`).

---

### Archivos necesarios

Asegúrate de tener los siguientes archivos en la misma carpeta:

- `main.py` → Archivo principal con el código fuente de la aplicación.
- `data.csv` → Archivo de entrada con las transacciones bancarias (formato CSV).

Ejemplo de contenido para `data.csv`:

```csv
id,tipo,monto
1,Crédito,100.00
2,Débito,50.00
3,Crédito,200.00
```
---

### Cómo ejecutar el programa

Abre una terminal y navega hasta la carpeta del proyecto.

Ejecuta el siguiente comando:

```python main.py```

Si todo está correcto, verás un reporte como el siguiente en la terminal:

```Reporte de Transacciones
---------------------------------------------
Balance Final: 325.00
Transacción de Mayor Monto: ID 3 - 200.00
Conteo de Transacciones: Crédito: 3 Débito: 2
```
---

### Notas adicionales

Si el archivo data.csv no existe, está vacío o contiene errores de formato (como montos no numéricos), el programa mostrará un mensaje de advertencia y finalizará de forma segura.
Se recomienda usar un editor como VSCode o ejecutarlo directamente desde terminal o consola de Python.

--

## Enfoque y Solución

La solución fue desarrollada paso a paso, con un enfoque modular y didáctico, ideal para entornos de nivel junior o de aprendizaje guiado. A continuación, se describe la lógica principal y las decisiones técnicas tomadas:

---

### 1. Lectura y validación del archivo CSV

- Se creó una función llamada `leer_transacciones()` que se encarga de:
  - Validar si el archivo `data.csv` existe.
  - Leer cada línea como un diccionario utilizando `csv.DictReader`.
  - Convertir el campo `monto` de texto a número (`float`).
  - Verificar que el tipo de transacción sea válido (`"Crédito"` o `"Débito"`).
  - Manejar errores de forma controlada con `try-except`.

Esta validación temprana permite evitar errores durante el procesamiento y garantiza que los datos sean confiables.

---

### 2. Cálculo del balance final

- Se recorren todas las transacciones.
- Se suma el monto si es de tipo `"Crédito"`.
- Se resta el monto si es de tipo `"Débito"`.
- El resultado acumulado representa el balance final.

Esta lógica fue implementada en la función `calcular_balance()`.

---

### 3. Identificación de la transacción de mayor monto

- Se recorre la lista de transacciones comparando los montos.
- Se guarda la transacción con el monto más alto y su respectivo ID.
- Esta lógica fue implementada en la función `encontrar_transaccion_mayor()`.

---

### 4. Conteo de transacciones por tipo

- Se cuenta cuántas veces aparece cada tipo de transacción.
- Se utilizó una estructura condicional simple (`if`) con dos contadores independientes.
- Esta lógica fue implementada en la función `contar_transacciones_por_tipo()`.

---

### Diseño general

- Todas las funciones fueron separadas por responsabilidad, manteniendo el código organizado y fácil de entender.
- Se utilizó un 'main' limpio que orquesta la ejecución del programa, llamando a las funciones según el flujo lógico.
- El enfoque fue mantener claridad por encima de optimización avanzada, siguiendo buenas prácticas de código limpio para principiantes.

--

## Estructura del Proyecto

La estructura del proyecto es simple y está organizada de manera que cualquier persona pueda entenderla fácilmente.
Todos los archivos se encuentran en la raíz del proyecto.
```cli-interbank/
 ├── main.py # Archivo principal del programa
 ├── data.csv # Archivo de entrada con transacciones bancarias
 └── README.md # Documentación del proyecto
```
---

### Descripción de archivos

- ***main.py***  
  Contiene toda la lógica del programa. Incluye:
  - Lectura y validación del archivo CSV
  - Cálculo del balance final
  - Identificación de la transacción de mayor monto
  - Conteo de transacciones por tipo
  - Impresión del reporte en consola

- ***data.csv***
  Archivo con los datos de entrada. Cada línea representa una transacción con formato:  
  ```id,tipo,monto```

- ***README.md***  
  Documentación que explica el propósito del proyecto, cómo ejecutarlo, decisiones de diseño y estructura general.

---

## Autor

Este proyecto fue desarrollado por:

**Luis Alberto Felix Rosas**
Ingeniero de Sistemas
Lima, Perú
luis.felix.rosas@gmail.com

Me apasiona la programación práctica, el aprendizaje continuo y los retos técnicos que impulsan el crecimiento real. Este proyecto fue desarrollado con un enfoque paso a paso, aplicando buenas prácticas y fortaleciendo habilidades esenciales como:

- Lectura y validación de datos
- Lógica condicional
- Estructuración de código limpio y modular
- Manejo de errores y control de flujo

Estoy en constante evolución como desarrollador y listo para seguir creciendo en el mundo de la tecnología.




