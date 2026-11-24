import os
from core.network import fetch_html
from core.parser import extract_properties
from core.pipeline import save_data

# HTML Simulado de un portal de bienes raíces para pruebas unitarias de arquitectura
def load_mock_html(filepath="mocks/sample_properties.html"):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    return None

def run_pipeline():
    print("=" * 60)
    print("[*] INICIANDO ORQUESTADOR CENTRAL - REAL ESTATE SCRAPER")
    print("=" * 60)
    
    # PASO 1: Simulación del Network Module
    # En producción usaríamos: html = fetch_html("https://portal-realestate.com/ventas")
    print("[1] Ejecutando módulo de red simulado...")
    html_content = load_mock_html()
    
    if not html_content:
        print("[-] Error: No se obtuvo contenido HTML válido. Abortando.")
        return
        
    # PASO 2: Ejecución del Parser Module
    print("[2] Analizando DOM HTML con BeautifulSoup4 y Regex...")
    properties_extracted = extract_properties(html_content)
    
    print(f"[i] Se identificaron {len(properties_extracted)} estructuras de inmuebles.")
    
    # PASO 3: Ejecución del Data Pipeline con Pandas
    print("[3] Enviando datos al pipeline de exportación (Pandas)...")
    success = save_data(properties_extracted, "reporte_inmobiliario")
    
    if success:
        print("=" * 60)
        print("[+] SPRINT COMPLETADO EXITOSAMENTE: Datos listos para el portafolio.")
        print("=" * 60)
    else:
        print("[-] El pipeline falló en la fase de persistencia.")

if __name__ == "__main__":
    run_pipeline()