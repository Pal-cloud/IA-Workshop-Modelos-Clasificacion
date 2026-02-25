# 🎓 Interfaz Visual - Tarea de Investigación ML

Esta aplicación web proporciona una interfaz visual elegante para ver y descargar la tarea de investigación sobre algoritmos de clasificación en Machine Learning.

## 🚀 Características

- ✨ Interfaz moderna y responsive
- 📄 Visualización del documento en HTML
- 📥 Descarga en formato PDF
- 📝 Descarga en formato Markdown
- 🎨 Diseño atractivo con gradientes y animaciones

## 📋 Requisitos Previos

### 1. Python 3.8 o superior

### 2. wkhtmltopdf (para generar PDFs)

**Windows:**
```bash
# Descargar e instalar desde:
https://wkhtmltopdf.org/downloads.html
# Recomendado: instalar en C:\Program Files\wkhtmltopdf
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install wkhtmltopdf
```

**macOS:**
```bash
brew install wkhtmltopdf
```

## 🔧 Instalación

### Paso 1: Instalar dependencias de Python

```bash
pip install -r requirements.txt
```

### Paso 2: Configurar wkhtmltopdf (si no está en PATH)

Si wkhtmltopdf no está en tu PATH, edita `app.py` y añade la configuración:

```python
import pdfkit

# Windows
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

# En las llamadas a pdfkit.from_file, añade: configuration=config
```

## ▶️ Uso

### 1. Iniciar el servidor

```bash
python app.py
```

### 2. Abrir el navegador

Navega a: http://localhost:5000

### 3. Opciones disponibles

- **👁️ Ver Documento**: Abre el documento en formato HTML en una nueva pestaña
- **📄 Descargar PDF**: Genera y descarga el documento en formato PDF
- **📝 Descargar Markdown**: Descarga el archivo Markdown original

## 📁 Estructura del Proyecto

```
IA-Workshop-Modelos-Clasificacion/
├── app.py                              # Aplicación Flask
├── requirements.txt                     # Dependencias Python
├── TAREA_INVESTIGACION_CLASIFICACION.md # Documento Markdown
├── templates/
│   ├── index.html                      # Página principal
│   └── document.html                   # Vista del documento
└── README_APP.md                        # Este archivo
```

## 🎨 Características de la Interfaz

### Página Principal
- Información del autor y fecha
- Estadísticas del documento
- Grid de tarjetas con los temas cubiertos
- Botones de descarga con iconos
- Diseño responsive

### Vista del Documento
- Navegación fija superior
- Formato profesional para el contenido
- Tablas estilizadas
- Código con syntax highlighting
- Botón "volver arriba" flotante
- Scrollbar personalizada

## 🛠️ Tecnologías Utilizadas

- **Backend:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Conversión:** Markdown → HTML → PDF
- **Librerías:** 
  - Flask para el servidor web
  - Markdown para parsear el contenido
  - PDFKit para generar PDFs
  - wkhtmltopdf como motor de renderizado

## 🔍 Solución de Problemas

### Error: "No wkhtmltopdf executable found"

**Solución:**
1. Instala wkhtmltopdf desde https://wkhtmltopdf.org/downloads.html
2. Añade wkhtmltopdf a tu PATH, o
3. Configura la ruta manualmente en `app.py`

### Error al generar PDF

**Solución:**
```python
# En app.py, modifica las opciones de pdfkit:
options = {
    'enable-local-file-access': None,
    'no-outline': None,
    'quiet': ''
}
```

### Puerto 5000 ya en uso

**Solución:**
```python
# Cambia el puerto en app.py:
app.run(debug=True, host='0.0.0.0', port=5001)
```

## 📝 Personalización

### Cambiar colores del tema

Edita los gradientes en `templates/index.html` y `templates/document.html`:

```css
/* Gradiente principal */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Puedes cambiarlo por otros colores, por ejemplo: */
background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
```

### Modificar estilos del PDF

Edita la sección de estilos en `app.py` dentro de la función `download_pdf()`.

## 🚀 Despliegue

### Despliegue local

Ya está listo para uso local siguiendo las instrucciones de instalación.

### Despliegue en producción

Para desplegar en un servidor, considera usar:
- **Gunicorn** como servidor WSGI
- **Nginx** como proxy inverso
- **Docker** para containerización

Ejemplo con Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📄 Licencia

Este proyecto es parte de la tarea educativa del workshop de Machine Learning en Factoría F5 Madrid.

## 👥 Autor

**Paloma Gómez Salazar**  
Factoría F5 Madrid - 2026

---

**¿Preguntas o problemas?** Abre un issue en el repositorio o contacta al autor.
