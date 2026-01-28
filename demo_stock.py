import os
import streamlit as st

# Configuracion de la pagina
st.set_page_config(
    page_title="Demo Stock - InventoryBot",
    page_icon="📦",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS personalizado
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stChatMessage {
        max-width: 800px;
        margin: 0 auto;
    }

    .stChatFloatingInputContainer {
        max-width: 800px;
        margin: 0 auto;
    }

    .custom-header {
        text-align: center;
        padding: 25px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        margin-bottom: 30px;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    .custom-header h1 {
        margin: 0;
        font-size: 28px;
        font-weight: 600;
        letter-spacing: -0.5px;
    }

    .custom-header p {
        margin: 10px 0 0 0;
        opacity: 0.9;
        font-size: 15px;
        font-weight: 400;
    }

    div[data-testid="column"] > div > div > button {
        width: 100%;
        border-radius: 8px;
        padding: 14px 20px;
        font-weight: 500;
        font-size: 15px;
        transition: all 0.2s ease;
        border: 1.5px solid #e5e7eb;
        background: white;
        color: #374151;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }

    div[data-testid="column"] > div > div > button:hover {
        background: #667eea;
        border-color: #667eea;
        color: white;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(102, 126, 234, 0.2);
    }

    .stCaption {
        color: #6b7280 !important;
        font-size: 14px !important;
        line-height: 1.8 !important;
    }
</style>
""", unsafe_allow_html=True)

# Header personalizado
st.markdown("""
<div class="custom-header">
    <h1>📦 InventoryBot - Gestion de Stock Inteligente</h1>
    <p>Control total de inventario, depositos y proveedores en tiempo real</p>
</div>
""", unsafe_allow_html=True)

BONUS_TEXTO = (
    "Este asistente consulta stock en tiempo real, genera alertas y automatiza pedidos a proveedores. "
    "No es una hoja de calculo estatica."
)

def maybe_append_bonus_once():
    if not st.session_state.get("bonus_shown", False):
        st.session_state.messages.append({
            "role": "assistant",
            "content": "💡 **{}**".format(BONUS_TEXTO),
            "show_buttons": None
        })
        st.session_state.bonus_shown = True

# Inicializar el chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """Hola! Soy tu asistente de inventario.

Puedo ayudarte con:
- Consulta de stock
- Alertas de reposicion
- Gestion de proveedores
- Reportes y analisis

Que necesitas consultar?""",
            "show_buttons": "inicial"
        }
    ]

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

if "bonus_shown" not in st.session_state:
    st.session_state.bonus_shown = False

# Funcion para agregar mensaje y ocultar botones
def add_message_and_hide_buttons(user_msg, bot_response, next_buttons=None, show_bonus_once=False):
    st.session_state.messages.append({"role": "user", "content": user_msg})
    bot_msg = {
        "role": "assistant",
        "content": bot_response,
        "show_buttons": next_buttons
    }
    st.session_state.messages.append(bot_msg)
    if show_bonus_once:
        maybe_append_bonus_once()
    st.session_state.button_clicked = True

# Funcion para obtener respuesta del bot
def get_bot_response(prompt):
    p = (prompt or "").lower()

    # 1) Consulta de stock general
    if any(word in p for word in ["stock", "inventario", "cuanto hay", "cuánto hay", "disponible"]):
        if "notebook" in p or "laptop" in p:
            return {
                "content": """📊 **Stock de Notebooks - Actualizado HOY 11:45am**

| Deposito | Dell Latitude | HP ProBook | Lenovo ThinkPad | Total |
|----------|---------------|------------|-----------------|-------|
| **Central** | 45 | 32 | 28 | 105 |
| **Norte** | 12 | 8 | 15 | 35 |
| **Sur** | 23 | 18 | 11 | 52 |
| **En transito** | 10 | 5 | 8 | 23 |
| **TOTAL** | **90** | **63** | **62** | **215** |

**Alertas:**
- HP ProBook en Deposito Norte (8 unid.) - Stock bajo
- Lenovo ThinkPad en Deposito Sur (11 unid.) - Reponer pronto

**Valor total inventario:** $18.450.000

Necesitas mas detalles de algun modelo?""",
                "buttons": "stock_notebook_acciones",
                "bonus_once": True
            }
        elif "mouse" in p or "teclado" in p or "accesorio" in p:
            return {
                "content": """📊 **Stock de Accesorios - Actualizado HOY**

| Producto | Central | Norte | Sur | Total | Estado |
|----------|---------|-------|-----|-------|--------|
| Mouse Logitech M170 | 145 | 67 | 89 | 301 | ✅ OK |
| Mouse Logitech MX Master | 23 | 12 | 8 | 43 | ⚠️ Bajo |
| Teclado Logitech K120 | 89 | 45 | 52 | 186 | ✅ OK |
| Teclado Mecanico RGB | 34 | 15 | 12 | 61 | ✅ OK |
| Webcam Logitech C920 | 15 | 8 | 4 | 27 | 🔴 Critico |
| Auriculares Bluetooth | 67 | 34 | 28 | 129 | ✅ OK |

**Alertas criticas:**
- Webcam C920: Solo 27 unidades (min: 50)
- Mouse MX Master Deposito Sur: 8 unid. (reponer)

**Recomendacion:** Generar orden de compra para Webcams

Queres ver proveedores disponibles?""",
                "buttons": "stock_accesorios_acciones"
            }
        else:
            return {
                "content": """📦 **Resumen General de Stock**

**CATEGORIAS PRINCIPALES:**

💻 **Informatica** (423 unidades)
- Notebooks: 215 unid.
- Monitores: 156 unid.
- Impresoras: 52 unid.

🖱️ **Accesorios** (847 unidades)
- Mouse: 344 unid.
- Teclados: 247 unid.
- Auriculares: 129 unid.
- Webcams: 27 unid. 🔴 CRITICO
- Otros: 100 unid.

📱 **Celulares** (189 unidades)
- Samsung: 89 unid.
- iPhone: 45 unid.
- Motorola: 55 unid.

**VALOR TOTAL INVENTARIO:** $45.678.900

**ALERTAS:** 3 productos en stock critico

Que categoria queres consultar?""",
                "buttons": "stock_categorias"
            }

    # 2) Alertas de stock bajo
    if any(word in p for word in ["alerta", "bajo", "critico", "crítico", "reponer", "reposicion", "reposición"]):
        return {
            "content": """🚨 **Alertas de Stock - Requieren atencion**

**NIVEL CRITICO (menos de 30 dias)**
🔴 Webcam Logitech C920
- Stock actual: 27 unidades
- Stock minimo: 50 unidades
- Venta promedio: 12/semana
- Dias restantes: 14 dias
- **ACCION:** Pedir YA 100 unidades

🔴 Cable HDMI 2m
- Stock: 18 unidades
- Minimo: 40 unidades
- Promedio: 8/semana
- Dias: 16 dias
- **ACCION:** Pedir 80 unidades

**NIVEL BAJO (menos de 60 dias)**
⚠️ Mouse MX Master
- Stock: 43 unidades
- Minimo: 60 unidades
- Promedio: 6/semana
- Dias: 48 dias

⚠️ Teclado Mecanico RGB
- Stock: 61 unidades
- Minimo: 80 unidades
- Promedio: 8/semana
- Dias: 52 dias

Queres generar ordenes de compra automaticas?""",
            "buttons": "alertas_acciones"
        }

    # 3) Consulta de proveedores
    if any(word in p for word in ["proveedor", "proveedores", "comprar", "precio", "cotizacion", "cotización"]):
        return {
            "content": """🏢 **Proveedores Activos**

**TECNOLOGIA**

📌 **TechSupply SA**
- Productos: Notebooks, monitores
- Calificacion: ⭐⭐⭐⭐⭐ (98%)
- Tiempo entrega: 5-7 dias
- Forma pago: 30 dias
- Ultimo pedido: 15/01/2026

📌 **Importadora Global**
- Productos: Perifericos, accesorios
- Calificacion: ⭐⭐⭐⭐ (87%)
- Tiempo entrega: 10-15 dias
- Forma pago: 15 dias
- Ultimo pedido: 08/01/2026

📌 **DistriTech Uruguay**
- Productos: Todo tipo
- Calificacion: ⭐⭐⭐⭐½ (92%)
- Tiempo entrega: 3-5 dias (LOCAL)
- Forma pago: 45 dias
- Ultimo pedido: 22/01/2026

**CELULARES**

📌 **MobileWorld**
- Productos: iPhone, Samsung
- Calificacion: ⭐⭐⭐⭐⭐ (96%)
- Tiempo entrega: 7-10 dias
- Forma pago: 30 dias

Queres comparar precios de algun producto?""",
            "buttons": "proveedores_acciones"
        }

    # 4) Comparacion de precios
    if any(word in p for word in ["comparar", "comparacion", "comparación", "mejor precio", "mas barato", "más barato"]):
        return {
            "content": """💰 **Comparacion de Precios - Webcam Logitech C920**

| Proveedor | Precio Unit. | Cant. Min | Total (100u) | Entrega | Pago |
|-----------|--------------|-----------|--------------|---------|------|
| **TechSupply** | $4.850 | 10 | $485.000 | 5-7d | 30d |
| **ImportGlobal** | $4.200 | 50 | **$420.000** ✅ | 10-15d | 15d |
| **DistriTech** | $5.100 | 5 | $510.000 | 3-5d ⚡ | 45d |

**Analisis:**
- **Mejor precio:** ImportGlobal (ahorro: $65.000)
- **Mas rapido:** DistriTech (3-5 dias)
- **Mejor balance:** ImportGlobal (precio + cantidad minima)

**Recomendacion:**
Pedir a ImportGlobal 100 unidades
- Total: $420.000
- Ahorro vs. DistriTech: $90.000
- Entrega estimada: 28/01 - 02/02

Genero la orden de compra?""",
            "buttons": "comparacion_acciones"
        }

    # 5) Movimientos de stock
    if any(word in p for word in ["movimiento", "entrada", "salida", "historial", "registro"]):
        return {
            "content": """📋 **Ultimos Movimientos - HOY 28/01/2026**

**ENTRADAS (Recepciones)**
✅ 09:15 - Dell Latitude 50u - Deposito Central
- Orden: #OC-2024-0089
- Proveedor: TechSupply

✅ 10:30 - Mouse Logitech 120u - Deposito Norte
- Orden: #OC-2024-0091
- Proveedor: ImportGlobal

**SALIDAS (Ventas/Despachos)**
📤  08:45 - Notebook HP 5u - Cliente: Empresa XYZ
- Deposito: Central
- Valor: $87.500

📤 11:20 - Teclados varios 45u - Cliente: Retail ABC
- Deposito: Sur
- Valor: $34.200

**TRANSFERENCIAS ENTRE DEPOSITOS**
🔄 14:30 - Mouse MX Master 20u
- Origen: Central
- Destino: Norte
- Estado: En transito

**AJUSTES DE INVENTARIO**
⚙️ 16:00 - Webcam C920 -2u
- Deposito: Sur
- Motivo: Producto defectuoso
- Responsable: J.Perez

Necesitas ver mas detalle de algun movimiento?""",
            "buttons": "movimientos_acciones"
        }

    # 6) Stock por deposito especifico
    if "deposito" in p or "depósito" in p:
        if "central" in p:
            return {
                "content": """🏢 **Deposito Central - Stock Detallado**

**Ubicacion:** Av. Italia 2500, Montevideo
**Responsable:** Juan Martinez
**Capacidad:** 85% ocupado

**STOCK POR CATEGORIA:**

💻 **Notebooks** (105 unidades - $9.450.000)
- Dell Latitude: 45u
- HP ProBook: 32u
- Lenovo ThinkPad: 28u

🖥️ **Monitores** (89 unidades - $4.230.000)
- LG 24": 45u
- Samsung 27": 32u
- Dell 32": 12u

🖱️ **Accesorios** (456 unidades - $892.000)
- Mouse: 145u
- Teclados: 89u
- Webcams: 15u
- Otros: 207u

**ULTIMOS MOVIMIENTOS:**
- Entrada: Dell Latitude 50u (hoy 09:15)
- Salida: HP ProBook 5u (hoy 08:45)
- Transferencia: Mouse MX 20u a Norte (hoy 14:30)

**ALERTAS:**
⚠️ Webcams en nivel bajo (15 unidades)

Necesitas otro deposito?""",
                "buttons": "depositos_otros"
            }
        elif "norte" in p:
            return {
                "content": """🏢 **Deposito Norte - Stock Detallado**

**Ubicacion:** Ruta 8 Km 23, Zonamerica
**Responsable:** Maria Rodriguez
**Capacidad:** 62% ocupado

**STOCK POR CATEGORIA:**

💻 **Notebooks** (35 unidades - $3.150.000)
- Dell Latitude: 12u
- HP ProBook: 8u ⚠️
- Lenovo ThinkPad: 15u

🖥️ **Monitores** (34 unidades - $1.615.000)
- LG 24": 18u
- Samsung 27": 12u
- Dell 32": 4u

🖱️ **Accesorios** (234 unidades - $456.000)
- Mouse: 67u
- Teclados: 45u
- Webcams: 8u
- Otros: 114u

**EN TRANSITO (llegada estimada hoy 18:00):**
🚚 Mouse MX Master: 20u desde Central

**ALERTAS:**
🔴 HP ProBook: Solo 8 unidades (critico)
⚠️ Webcams: 8 unidades (bajo)

Queres ver otro deposito?""",
                "buttons": "depositos_otros"
            }

    # 7) Generar orden de compra
    if any(word in p for word in ["orden", "pedido", "compra", "generar", "solicitar"]):
        return {
            "content": """📝 **Generar Orden de Compra**

Basado en alertas actuales, te sugiero:

**ORDEN RECOMENDADA #1**
🔴 **URGENTE - Webcam Logitech C920**
- Cantidad: 100 unidades
- Proveedor: ImportGlobal (mejor precio)
- Precio unitario: $4.200
- **Total: $420.000**
- Entrega: 10-15 dias
- Stock actual: 27u (critico)

**ORDEN RECOMENDADA #2**
⚠️ **Cable HDMI 2m**
- Cantidad: 80 unidades
- Proveedor: DistriTech (rapido)
- Precio unitario: $890
- **Total: $71.200**
- Entrega: 3-5 dias
- Stock actual: 18u (critico)

**ORDEN RECOMENDADA #3**
⚠️ **Mouse MX Master**
- Cantidad: 50 unidades
- Proveedor: ImportGlobal
- Precio unitario: $4.850
- **Total: $242.500**
- Entrega: 10-15 dias
- Stock actual: 43u (bajo)

**TOTAL ORDENES:** $733.700

Queres generar estas ordenes?""",
            "buttons": "generar_ordenes"
        }

    # 8) Reportes
    if any(word in p for word in ["reporte", "informe", "analisis", "análisis", "estadistica", "estadística"]):
        return {
            "content": """📊 **Reportes y Analisis Disponibles**

**REPORTES DE STOCK**
📈 Valorizacion de inventario
📉 Productos con baja rotacion
🔄 Rotacion de stock por categoria
📦 Stock por deposito comparativo

**REPORTES DE VENTAS**
💰 Productos mas vendidos (mensual)
📊 Analisis de demanda
🎯 Proyeccion de ventas

**REPORTES DE PROVEEDORES**
⭐ Ranking de proveedores
💵 Analisis de precios historicos
⏱️ Tiempos de entrega promedio

**REPORTES OPERATIVOS**
🚨 Alertas y excepciones
📋 Movimientos del dia
🔄 Transferencias entre depositos

Que reporte necesitas?""",
            "buttons": "reportes_opciones"
        }

    # Respuesta por defecto
    return {
        "content": """No entiendo bien tu consulta

Puedo ayudarte con:

• 📦 Consultar stock de productos
• 🚨 Ver alertas de reposicion
• 🏢 Informacion de proveedores
• 💰 Comparar precios
• 📋 Ver movimientos
• 📝 Generar ordenes de compra
• 📊 Reportes y analisis

Que necesitas?""",
        "buttons": "ayuda"
    }

# Mostrar mensajes del chat
for i, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("show_buttons"):
            button_type = message["show_buttons"]

            # Botones iniciales
            if button_type == "inicial":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📦 Consultar stock", key="btn_stock_{}".format(i), use_container_width=True):
                        response = get_bot_response("stock general")
                        add_message_and_hide_buttons("Ver stock general", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("🚨 Ver alertas", key="btn_alertas_{}".format(i), use_container_width=True):
                        response = get_bot_response("alertas")
                        add_message_and_hide_buttons("Ver alertas de stock", response["content"], response.get("buttons"))
                        st.rerun()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🏢 Proveedores", key="btn_prov_{}".format(i), use_container_width=True):
                        response = get_bot_response("proveedores")
                        add_message_and_hide_buttons("Ver proveedores", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("📊 Reportes", key="btn_rep_{}".format(i), use_container_width=True):
                        response = get_bot_response("reportes")
                        add_message_and_hide_buttons("Ver reportes", response["content"], response.get("buttons"))
                        st.rerun()

            # Acciones de stock notebooks
            elif button_type == "stock_notebook_acciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("💰 Comparar precios", key="btn_comp_{}".format(i), use_container_width=True):
                        response = get_bot_response("comparar precios")
                        add_message_and_hide_buttons("Comparar precios", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("📝 Generar orden", key="btn_orden_{}".format(i), use_container_width=True):
                        response = get_bot_response("generar orden")
                        add_message_and_hide_buttons("Generar orden de compra", response["content"], response.get("buttons"))
                        st.rerun()

            # Acciones de alertas
            elif button_type == "alertas_acciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ Generar ordenes auto", key="btn_auto_{}".format(i), use_container_width=True):
                        add_message_and_hide_buttons(
                            "Generar ordenes automaticas",
                            """✅ **Ordenes generadas automaticamente**

🔴 Orden #OC-2026-0156
- Producto: Webcam C920
- Cantidad: 100u
- Proveedor: ImportGlobal
- Total: $420.000
- Estado: Pendiente aprobacion

🔴 Orden #OC-2026-0157
- Producto: Cable HDMI 2m
- Cantidad: 80u
- Proveedor: DistriTech
- Total: $71.200
- Estado: Pendiente aprobacion

**Total:** $491.200

Las ordenes fueron enviadas a compras para aprobacion.
Recibiras notificacion cuando sean procesadas.

Necesitas algo mas?""",
                            "ayuda"
                        )
                        st.rerun()

                with col2:
                    if st.button("📊 Ver reporte completo", key="btn_rep_comp_{}".format(i), use_container_width=True):
                        response = get_bot_response("reportes")
                        add_message_and_hide_buttons("Ver reportes", response["content"], response.get("buttons"))
                        st.rerun()

            # Acciones de categorias de stock
            elif button_type == "stock_categorias":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("💻 Informatica", key="btn_info_{}".format(i), use_container_width=True):
                        response = get_bot_response("stock notebook")
                        add_message_and_hide_buttons("Ver stock informatica", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("🖱️ Accesorios", key="btn_acc_{}".format(i), use_container_width=True):
                        response = get_bot_response("stock accesorios")
                        add_message_and_hide_buttons("Ver stock accesorios", response["content"], response.get("buttons"))
                        st.rerun()

            # Acciones de proveedores
            elif button_type == "proveedores_acciones":
                if st.button("💰 Comparar precios producto", key="btn_comp_prod_{}".format(i), use_container_width=True):
                    response = get_bot_response("comparar precios")
                    add_message_and_hide_buttons("Comparar precios", response["content"], response.get("buttons"))
                    st.rerun()

            # Acciones de comparacion
            elif button_type == "comparacion_acciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ Generar orden ImportGlobal", key="btn_gen_imp_{}".format(i), use_container_width=True):
                        add_message_and_hide_buttons(
                            "Generar orden a ImportGlobal",
                            """✅ **Orden de Compra Generada**

**Orden:** #OC-2026-0158
**Fecha:** 28/01/2026 15:45

**Proveedor:** Importadora Global
**Producto:** Webcam Logitech C920
**Cantidad:** 100 unidades
**Precio unitario:** $4.200
**Total:** $420.000

**Condiciones:**
- Entrega: 10-15 dias habiles
- Forma pago: 15 dias fecha factura
- Entrega estimada: 02-07 Febrero

**Estado:** Enviada al proveedor
**Tracking:** Se enviara por email

La orden fue registrada y enviada.
Te notificaremos cuando sea confirmada.

Necesitas algo mas?""",
                            "ayuda"
                        )
                        st.rerun()

                with col2:
                    if st.button("🔍 Ver otras opciones", key="btn_otras_{}".format(i), use_container_width=True):
                        response = get_bot_response("proveedores")
                        add_message_and_hide_buttons("Ver otros proveedores", response["content"], response.get("buttons"))
                        st.rerun()

            # Otros depositos
            elif button_type == "depositos_otros":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🏢 Ver Deposito Norte", key="btn_norte_{}".format(i), use_container_width=True):
                        response = get_bot_response("deposito norte")
                        add_message_and_hide_buttons("Ver Deposito Norte", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("🏢 Ver Deposito Sur", key="btn_sur_{}".format(i), use_container_width=True):
                        add_message_and_hide_buttons(
                            "Ver Deposito Sur",
                            """🏢 **Deposito Sur - Stock Detallado**

**Ubicacion:** Ruta 1 Km 18, Canelones
**Responsable:** Carlos Lopez
**Capacidad:** 71% ocupado

**STOCK POR CATEGORIA:**

💻 **Notebooks** (52 unidades - $4.680.000)
- Dell Latitude: 23u
- HP ProBook: 18u
- Lenovo ThinkPad: 11u ⚠️

🖥️ **Monitores** (33 unidades - $1.568.000)
- LG 24": 15u
- Samsung 27": 12u
- Dell 32": 6u

🖱️ **Accesorios** (157 unidades - $306.000)
- Mouse: 89u
- Teclados: 52u
- Webcams: 4u 🔴
- Otros: 12u

**ALERTAS:**
🔴 Webcams: Solo 4 unidades (critico)
⚠️ Lenovo ThinkPad: 11 unidades (bajo)

Necesitas ver movimientos o generar ordenes?""",
                            "depositos_otros"
                        )
                        st.rerun()

            # Ayuda general
            elif button_type == "ayuda":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📦 Ver stock", key="btn_stock_ayuda_{}".format(i), use_container_width=True):
                        response = get_bot_response("stock general")
                        add_message_and_hide_buttons("Ver stock", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("🚨 Ver alertas", key="btn_alert_ayuda_{}".format(i), use_container_width=True):
                        response = get_bot_response("alertas")
                        add_message_and_hide_buttons("Ver alertas", response["content"], response.get("buttons"))
                        st.rerun()

# Ejemplos de consultas
st.markdown("---")
st.markdown("**💬 Ejemplos de consultas:**")
col1, col2 = st.columns(2)
with col1:
    st.caption("• Cual es el stock de notebooks")
    st.caption("• Mostrame las alertas de productos criticos")
    st.caption("• Quiero comparar precios de webcams")
    st.caption("• Ver stock del deposito central")
    st.caption("• Cuales son los ultimos movimientos")
with col2:
    st.caption("• Que proveedores tenemos activos")
    st.caption("• Generar orden de compra automatica")
    st.caption("• Stock de accesorios por deposito")
    st.caption("• Ver reporte de productos mas vendidos")
    st.caption("• Cuanto vale todo el inventario")

# Input del chat
if prompt := st.chat_input("Escribi tu consulta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = get_bot_response(prompt)
    st.session_state.messages.append({
        "role": "assistant",
        "content": response["content"],
        "show_buttons": response.get("buttons")
    })
    if response.get("bonus_once"):
        maybe_append_bonus_once()
    st.rerun()

# Footer
st.divider()
st.caption("💡 **Este es un demo interactivo.** El bot responde con datos de ejemplo.")
st.caption("🔌 En produccion conecta con tu ERP, sistema de inventario y proveedores reales.")

# Boton reset
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reiniciar"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """Hola! Soy tu asistente de inventario.

Puedo ayudarte con:
- Consulta de stock
- Alertas de reposicion
- Gestion de proveedores
- Reportes y analisis

Que necesitas consultar?""",
                "show_buttons": "inicial"
            }
        ]
        st.session_state.button_clicked = False
        st.session_state.bonus_shown = False
        st.rerun()
