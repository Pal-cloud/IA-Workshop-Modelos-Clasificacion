/**
 * Funciones JavaScript para la interfaz de visualización
 * Maneja la descarga de PDF con SweetAlert2
 */

async function downloadPDF() {
    const btn = document.getElementById('pdfBtn');
    const loading = document.getElementById('loading');
    
    // Deshabilitar botón y mostrar loading
    btn.disabled = true;
    btn.style.opacity = '0.6';
    loading.style.display = 'block';
    
    try {
        // Realizar la petición
        const response = await fetch('/download-pdf');
        
        if (!response.ok) {
            // Intentar obtener el error en JSON
            const errorData = await response.json();
            
            // Si es error de wkhtmltopdf no instalado
            if (errorData.error === 'wkhtmltopdf_not_found') {
                Swal.fire({
                    title: '⚠️ wkhtmltopdf No Instalado',
                    html: `
                        <div style="text-align: left; padding: 20px;">
                            <p style="margin-bottom: 20px; font-size: 16px;">
                                Para generar PDFs necesitas instalar <strong>wkhtmltopdf</strong>. 
                                Sigue estos pasos:
                            </p>
                            
                            <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                                <h4 style="color: #667eea; margin-bottom: 10px;">🪟 Windows:</h4>
                                <ol style="margin-left: 20px;">
                                    <li style="margin: 8px 0;">Descarga desde: 
                                        <a href="https://wkhtmltopdf.org/downloads.html" 
                                           target="_blank" 
                                           style="color: #667eea; text-decoration: underline;">
                                           wkhtmltopdf.org/downloads.html
                                        </a>
                                    </li>
                                    <li style="margin: 8px 0;">Instala el archivo .exe</li>
                                    <li style="margin: 8px 0;">Reinicia la aplicación Flask</li>
                                </ol>
                            </div>
                            
                            <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                                <h4 style="color: #667eea; margin-bottom: 10px;">🐧 Linux (Ubuntu/Debian):</h4>
                                <pre style="background: #2d3748; color: #fff; padding: 10px; border-radius: 5px; overflow-x: auto;">
sudo apt-get update
sudo apt-get install wkhtmltopdf</pre>
                            </div>
                            
                            <div style="background: #f8f9fa; padding: 15px; border-radius: 8px;">
                                <h4 style="color: #667eea; margin-bottom: 10px;">🍎 macOS:</h4>
                                <pre style="background: #2d3748; color: #fff; padding: 10px; border-radius: 5px; overflow-x: auto;">
brew install wkhtmltopdf</pre>
                            </div>
                            
                            <p style="margin-top: 20px; padding: 15px; background: #e3f2fd; border-radius: 8px; font-size: 14px;">
                                💡 <strong>Alternativa:</strong> Puedes descargar el documento en formato 
                                Markdown y convertirlo online en sitios como 
                                <a href="https://www.markdowntopdf.com/" target="_blank" style="color: #667eea;">
                                    markdowntopdf.com
                                </a>
                            </p>
                        </div>
                    `,
                    icon: 'info',
                    confirmButtonText: 'Entendido',
                    confirmButtonColor: '#667eea',
                    width: '700px',
                    customClass: {
                        popup: 'swal-wide'
                    }
                });
            } else {
                // Otros errores
                Swal.fire({
                    title: '❌ Error',
                    text: errorData.message || 'Error al generar el PDF',
                    icon: 'error',
                    confirmButtonText: 'Cerrar',
                    confirmButtonColor: '#667eea'
                });
            }
            
            throw new Error(errorData.message);
        }
        
        // Obtener el blob del PDF
        const blob = await response.blob();
        
        // Crear URL temporal y descargar
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'TAREA_INVESTIGACION_CLASIFICACION.pdf';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
        
        // Mostrar mensaje de éxito
        Swal.fire({
            title: '✅ ¡Éxito!',
            text: 'PDF descargado exitosamente',
            icon: 'success',
            timer: 2000,
            showConfirmButton: false,
            toast: true,
            position: 'top-end'
        });
        
    } catch (error) {
        console.error('Error:', error);
    } finally {
        // Rehabilitar botón y ocultar loading
        btn.disabled = false;
        btn.style.opacity = '1';
        loading.style.display = 'none';
    }
}
