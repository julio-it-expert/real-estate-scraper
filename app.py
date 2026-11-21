import streamlit as st
import pandas as pd
import os
import time
from core.parser import extract_properties
from core.pipeline import save_data
from main import MOCK_HTML_PORTAL

# Configuración de la página
st.set_page_config(
    page_title="Real Estate Data Pipeline | Demo",
    page_icon="🏢",
    layout="wide"
)

# Encabezado principal
st.title("🏢 Real Estate Data Pipeline (Entorno Sandbox)")
st.markdown("""
Esta demostración interactiva muestra cómo el sistema extrae, limpia y estructura datos inmobiliarios 
desde código HTML desordenado hacia reportes analíticos listos para usar.
""")

st.divider()

# Barra lateral con información técnica (útil para reclutadores)
with st.sidebar:
    st.header("⚙️ Arquitectura del Sistema")
    st.info("""
    - **Extracción:** BeautifulSoup4 + Regex
    - **Limpieza:** Pandas DataFrames
    - **Modo:** Sandbox (Datos simulados)
    """)
    mostrar_html = st.checkbox("Ver HTML de origen (Raw Data)", value=False)

if mostrar_html:
    with st.expander("Código HTML crudo que procesará el Scraper", expanded=True):
        st.code(MOCK_HTML_PORTAL, language="html")

# Botón principal de acción para el cliente
col1, col2 = st.columns([1, 3])
with col1:
    ejecutar = st.button("Ejecutar Extracción de Datos", type="primary", use_container_width=True)

if ejecutar:
    # Simulación visual del proceso paso a paso
    with st.status("Ejecutando pipeline de datos...", expanded=True) as status:
        st.write("🌐 [1/3] Conectando con fuente de datos simulada...")
        time.sleep(0.6)
        
        st.write("🔍 [2/3] Analizando estructura DOM con BeautifulSoup4 y Regex...")
        properties_extracted = extract_properties(MOCK_HTML_PORTAL)
        time.sleep(0.6)
        
        st.write("🧹 [3/3] Limpiando valores financieros y generando reporte en Pandas...")
        os.makedirs("data", exist_ok=True)
        nombre_archivo = "reporte_demo"
        save_data(properties_extracted, nombre_archivo)
        time.sleep(0.5)
        
        status.update(label="✅ ¡Extracción completada con éxito!", state="complete", expanded=False)

    # Mostrar resultados si se extrajeron datos
    if properties_extracted:
        df = pd.DataFrame(properties_extracted)
        
        st.subheader("📊 Datos Estructurados Resultantes")
        st.dataframe(df, use_container_width=True)
        
        # Métricas rápidas para dar impacto visual al cliente
        m1, m2 = st.columns(2)
        m1.metric("Total de Propiedades Procesadas", len(df))
        m2.metric("Estado del Pipeline", "100% Operativo")

        st.subheader("📥 Descargar Reportes Generados")
        btn_col1, btn_col2, _ = st.columns([1, 1, 2])
        
        # Botón para descargar Excel si tu pipeline lo generó
        excel_path = f"data/{nombre_archivo}.xlsx"
        if os.path.exists(excel_path):
            with open(excel_path, "rb") as file:
                btn_col1.download_button(
                    label="📄 Descargar Excel (.xlsx)",
                    data=file,
                    file_name="reporte_inmobiliario.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    use_container_width=True
                )

        # Botón para descargar CSV (siempre disponible desde Pandas)
        csv_data = df.to_csv(index=False).encode('utf-8')
        btn_col2.download_button(
            label="📊 Descargar CSV (.csv)",
            data=csv_data,
            file_name="reporte_inmobiliario.csv",
            mime="text/csv",
            use_container_width=True
        )
    else:
        st.error("No se pudieron extraer propiedades del HTML.")
