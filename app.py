"""
Aplicación Flask para visualizar y exportar la tarea de investigación
Autor: Paloma Gómez
"""

from flask import Flask, render_template, send_file, jsonify
import markdown
import pdfkit
from pathlib import Path
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Página principal con la interfaz visual"""
    return render_template('index.html')

@app.route('/view')
def view_document():
    """Muestra el documento en formato HTML"""
    # Leer el archivo markdown desde docs/
    md_path = Path(__file__).parent / 'docs' / 'TAREA_INVESTIGACION_CLASIFICACION.md'
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convertir Markdown a HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'codehilite']
    )
    
    return render_template('document.html', content=html_content)

@app.route('/download-pdf')
def download_pdf():
    """Genera y descarga el PDF"""
    try:
        # Leer el archivo markdown desde docs/
        md_path = Path(__file__).parent / 'docs' / 'TAREA_INVESTIGACION_CLASIFICACION.md'
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convertir Markdown a HTML con estilos
        html_content = markdown.markdown(
            md_content,
            extensions=['tables', 'fenced_code', 'codehilite']
        )
        
        # HTML completo con estilos para PDF
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: 'Segoe UI', Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 900px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                h1 {{
                    color: #2c3e50;
                    border-bottom: 3px solid #3498db;
                    padding-bottom: 10px;
                }}
                h2 {{
                    color: #3498db;
                    margin-top: 30px;
                }}
                h3 {{
                    color: #16a085;
                }}
                h4, h5 {{
                    color: #27ae60;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 6px;
                    border-radius: 3px;
                    font-family: 'Courier New', monospace;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 15px;
                    border-radius: 5px;
                    border-left: 4px solid #3498db;
                    overflow-x: auto;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px 0;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: left;
                }}
                th {{
                    background-color: #3498db;
                    color: white;
                }}
                tr:nth-child(even) {{
                    background-color: #f9f9f9;
                }}
                blockquote {{
                    border-left: 4px solid #3498db;
                    padding-left: 15px;
                    color: #555;
                    font-style: italic;
                }}
                ul, ol {{
                    margin-left: 20px;
                }}
                li {{
                    margin: 5px 0;
                }}
            </style>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Guardar HTML temporal en carpeta temp/
        temp_html = Path(__file__).parent / 'temp' / 'temp_document.html'
        with open(temp_html, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        # Generar PDF en carpeta temp/
        pdf_path = Path(__file__).parent / 'temp' / 'TAREA_INVESTIGACION_CLASIFICACION.pdf'
        
        # Configuración para wkhtmltopdf
        options = {
            'page-size': 'A4',
            'margin-top': '20mm',
            'margin-right': '20mm',
            'margin-bottom': '20mm',
            'margin-left': '20mm',
            'encoding': "UTF-8",
            'enable-local-file-access': None
        }
        
        pdfkit.from_file(str(temp_html), str(pdf_path), options=options)
        
        # Limpiar archivo temporal
        if temp_html.exists():
            temp_html.unlink()
        
        return send_file(
            pdf_path,
            as_attachment=True,
            download_name='TAREA_INVESTIGACION_CLASIFICACION.pdf',
            mimetype='application/pdf'
        )
    
    except OSError as e:
        # Error específico cuando wkhtmltopdf no está instalado
        if 'wkhtmltopdf' in str(e).lower() or 'no wkhtmltopdf' in str(e).lower():
            return jsonify({
                'error': 'wkhtmltopdf_not_found',
                'message': 'wkhtmltopdf no está instalado en tu sistema'
            }), 404
        return jsonify({
            'error': 'os_error',
            'message': f'Error del sistema: {str(e)}'
        }), 500
    
    except Exception as e:
        return jsonify({
            'error': 'general_error',
            'message': f'Error al generar PDF: {str(e)}'
        }), 500

@app.route('/download-md')
def download_md():
    """Descarga el archivo Markdown original"""
    md_path = Path(__file__).parent / 'docs' / 'TAREA_INVESTIGACION_CLASIFICACION.md'
    return send_file(
        md_path,
        as_attachment=True,
        download_name='TAREA_INVESTIGACION_CLASIFICACION.md',
        mimetype='text/markdown'
    )

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Servidor iniciado!")
    print("📝 Abre tu navegador en: http://localhost:5001")
    print("="*60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5001)
