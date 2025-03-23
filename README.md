# Scanet 🔍  

Scanet es una herramienta de escaneo de redes, dispositivos, puertos y servicios, desarrollada completamente en Python. Permite detectar las redes a las que esta conectado el usuario, analizar un rango de puertos abiertos en una IP específica, escaneo de puertos comunes y generar reportes en formato `.txt`.  

## 🚀 **Características:**  
- Escaneo de redes disponibles.  
- Escaneo de puertos en un rango definido por el usuario.  
- Escaneo de puertos más comunes.  
- Generación de reportes `.txt` con los resultados.  
- Interfaz de línea de comandos con salida en colores para mejor visualización.  

## 🛠 **Requisitos previos:**  
Para ejecutar este proyecto, asegúrate de tener Python instalado. 

## 📥 **Clonar el repositorio:**  
Para comenzar a usar Scanet, primero clona el repositorio de GitHub en tu máquina local. Sigue estos pasos:  

1. Abre una terminal o línea de comandos.  
2. Ejecuta el siguiente comando para clonar el repositorio:  

```bash
git clone https://github.com/daniescamilla/scanet.git
```

3. Navega al directorio del proyecto.

```bash
cd scanet
```

4. Instala las dependencias.

```bash
pip install -r requirements.txt
```

## 🏃 **Uso:**  
Ejecuta el script con:  

```bash
python scanet.py
```

Luego, sigue las instrucciones en pantalla del menú interactuvo para seleccionar el tipo de escaneo que deseas realizar.  

## **Encontrarás 5 opciones:**
        1) Escanear las redes a las que está conectada tu máquina.
        2) Escanear una dirección IP que introduzcas en un rango de puertos que desees.
        3) Generar archivo .txt con escaneo de la dirección IP que introduzcas en el rango de puertos que desees.
        4) Generar archivo .txt con escaneo de puertos comunes de la dirección IP que introduzcas.
        5) Salir del programa.

### En la primera opción realizará directamente el escaneo de las redes.

### En la segunda opción deberás introducir una dirección IP como "192.168.1.1" y un primer y último puerto para determinar el rango dónde se realizará el escaneo (1-65535).

### La tercera opción pide los mismos parámetros que la segunda y también muestra el escaneo por la terminal solo que también te generará un .txt a modo de resumen.

### La cuarta opción solo deberás ingresar la dirección IP ya que los puertos comunes están previamente definidos en el código.

### La quinta es simplemente para salir del programa aunque tambien puedes hacerlo en cualquier momento con Ctrl + C.
