# 🎨 Interfaz Visual - Guía Rápida

## ✨ ¿Qué es esto?

Una aplicación web elegante y moderna que te permite:
- 👁️ Ver tu tarea de investigación en formato HTML con diseño profesional
- 📄 **Generar y descargar un PDF** con un solo clic
- 📝 Descargar el documento en Markdown

## 🚀 Inicio Rápido

### Opción 1: Usando el script automático (Recomendado)

**En Windows:**
```bash
# Simplemente haz doble clic en:
start.bat
```

**En Linux/Mac:**
```bash
chmod +x start.sh
./start.sh
```

### Opción 2: Manual

```bash
# 1. Instalar dependencias
pip install flask markdown pdfkit

# 2. Iniciar servidor
python app.py

# 3. Abrir navegador en:
http://localhost:5000
```

## ⚠️ Importante para generar PDFs

Para que funcione la generación de PDFs, necesitas instalar **wkhtmltopdf**:

### Windows:
1. Descarga desde: https://wkhtmltopdf.org/downloads.html
2. Instala en `C:\Program Files\wkhtmltopdf`
3. ¡Listo!

### Linux (Ubuntu/Debian):
```bash
sudo apt-get install wkhtmltopdf
```

### macOS:
```bash
brew install wkhtmltopdf
```

## 📸 Capturas

### Página Principal
La interfaz principal muestra:
- 📊 Estadísticas del documento (7 preguntas, 5 algoritmos, 6 métricas)
- 🎴 Tarjetas interactivas con los temas cubiertos
- 🔘 Botones de acción con iconos

### Botones Disponibles:
- **Ver Documento** → Abre en nueva pestaña con formato HTML
- **Descargar PDF** → Genera y descarga automáticamente
- **Descargar Markdown** → Descarga el archivo .md original

## 🎯 Características Destacadas

✅ **Diseño Moderno**
- Gradientes elegantes
- Animaciones suaves
- Responsive (se adapta a móviles)

✅ **Fácil de Usar**
- Un solo clic para generar PDF
- Interfaz intuitiva
- Sin configuración complicada

✅ **Profesional**
- Documento bien formateado
- Tablas y código estilizados
- Listo para entregar

## 🐛 Solución Rápida de Problemas

### "No module named flask"
```bash
pip install flask markdown
```

### "wkhtmltopdf not found"
Instala wkhtmltopdf siguiendo las instrucciones arriba

### "Puerto 5000 en uso"
Edita `app.py` y cambia el puerto:
```python
app.run(debug=True, port=5001)  # Cambiar a otro puerto
```

## 📝 Notas

- La primera vez que generes el PDF puede tardar unos segundos
- El archivo PDF se guardará automáticamente en tu carpeta de Descargas
- Puedes acceder desde cualquier dispositivo en tu red local usando tu IP

## 🎓 Créditos

**Autora:** Paloma Gómez Salazar  
**Proyecto:** Tarea de Investigación - ML Clasificación  
**Institución:** Factoría F5 Madrid

---

**¡Disfruta de tu interfaz visual!** 🚀
