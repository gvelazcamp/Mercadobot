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

# FUNCION PRINCIPAL - MEJORADA CON MUCHAS MAS RESPUESTAS
def get_bot_response(prompt):
    p = (prompt or "").lower()

    # 1) CONSULTA DE STOCK - AMPLIADO
    stock_kw = ["stock", "inventario", "cuanto", "cuánto", "hay", "disponible", "tengo", "tenemos", 
                "cantidad", "unidades", "productos", "articulos", "artículos", "mercaderia", "mercadería"]
    
    if any(w in p for w in stock_kw):
        # Notebooks
        if any(w in p for w in ["notebook", "laptop", "computadora", "pc", "dell", "hp", "lenovo", "thinkpad", "latitude", "probook"]):
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
        
        # Accesorios
        elif any(w in p for w in ["mouse", "teclado", "accesorio", "periférico", "periferico", "logitech", "webcam", "auricular", "cable"]):
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
        
        # Monitores
        elif any(w in p for w in ["monitor", "pantalla", "display", "lg", "samsung"]):
            return {
                "content": """📊 **Stock de Monitores - Actualizado HOY**

| Modelo | Central | Norte | Sur | Total | Precio Unit | Estado |
|--------|---------|-------|-----|-------|-------------|--------|
| LG 24" IPS Full HD | 45 | 18 | 15 | 78 | $47.500 | ✅ OK |
| Samsung 27" Curved | 32 | 12 | 12 | 56 | $68.900 | ✅ OK |
| Dell 32" 4K UHD | 12 | 4 | 6 | 22 | $125.000 | ⚠️ Bajo |

**Total monitores:** 156 unidades
**Valor inventario:** $10.234.500

**Análisis:**
- LG 24" es el más vendido (5/semana)
- Dell 32" 4K tiene baja rotación pero alto valor
- Samsung 27" Curved tiene demanda estable

Necesitas generar orden o ver más detalles?""",
                "buttons": "stock_monitores_acciones"
            }
        
        # Celulares
        elif any(w in p for w in ["celular", "telefono", "teléfono", "smartphone", "iphone", "samsung", "motorola", "móvil", "movil"]):
            return {
                "content": """📱 **Stock de Celulares - Actualizado HOY**

**SAMSUNG**
| Modelo | Stock | Precio | Estado |
|--------|-------|--------|--------|
| Galaxy S23 | 28 | $189.900 | ✅ OK |
| Galaxy A54 | 45 | $98.500 | ✅ OK |
| Galaxy A34 | 16 | $76.900 | ⚠️ Bajo |

**APPLE IPHONE**
| Modelo | Stock | Precio | Estado |
|--------|-------|--------|--------|
| iPhone 14 | 18 | $245.000 | ⚠️ Bajo |
| iPhone 13 | 27 | $198.500 | ✅ OK |

**MOTOROLA**
| Modelo | Stock | Precio | Estado |
|--------|-------|--------|--------|
| Moto G73 | 34 | $67.900 | ✅ OK |
| Moto Edge 40 | 21 | $125.000 | ✅ OK |

**Total celulares:** 189 unidades
**Valor total:** $24.567.800

Necesitas ver por deposito o generar pedidos?""",
                "buttons": "stock_celulares_acciones"
            }
        
        # Stock general
        else:
            return {
                "content": """📦 **Resumen General de Stock**

**CATEGORIAS PRINCIPALES:**

💻 **Informatica** (423 unidades - $32.914.500)
- Notebooks: 215 unid.
- Monitores: 156 unid.
- Impresoras: 52 unid.

🖱️ **Accesorios** (847 unidades - $1.892.300)
- Mouse: 344 unid.
- Teclados: 247 unid.
- Auriculares: 129 unid.
- Webcams: 27 unid. 🔴 CRITICO
- Otros: 100 unid.

📱 **Celulares** (189 unidades - $24.567.800)
- Samsung: 89 unid.
- iPhone: 45 unid.
- Motorola: 55 unid.

**VALOR TOTAL INVENTARIO:** $59.374.600

**ALERTAS:** 5 productos en stock critico
**PRODUCTOS EN TRANSITO:** $3.456.700

Que categoria queres consultar en detalle?""",
                "buttons": "stock_categorias"
            }

    # 2) ALERTAS - MEJORADO
    alerta_kw = ["alerta", "alertas", "bajo", "critico", "crítico", "reponer", "reposicion", "reposición", 
                 "falta", "faltan", "acabando", "poco", "minimo", "mínimo", "urgente"]
    
    if any(w in p for w in alerta_kw):
        return {
            "content": """🚨 **Alertas de Stock - Requieren atencion URGENTE**

**NIVEL CRITICO 🔴 (menos de 2 semanas)**

🔴 **Webcam Logitech C920**
- Stock actual: 27 unidades
- Stock minimo: 50 unidades
- Venta promedio: 12/semana
- **Dias restantes: 14 dias**
- ACCION: Pedir YA 100 unidades
- Proveedor recomendado: ImportGlobal ($4.200/u)

🔴 **Cable HDMI 2m**
- Stock: 18 unidades
- Minimo: 40 unidades
- Promedio: 8/semana
- **Dias: 16 dias**
- ACCION: Pedir 80 unidades
- Proveedor: DistriTech ($890/u)

🔴 **iPhone 14**
- Stock: 18 unidades
- Minimo: 30 unidades
- Promedio: 4/semana
- **Dias: 30 dias**
- ACCION: Pedir 25 unidades

**NIVEL BAJO ⚠️ (menos de 45 dias)**

⚠️ **Mouse MX Master** - 43u (Min: 60) → 48 dias
⚠️ **Teclado Mecanico RGB** - 61u (Min: 80) → 52 dias
⚠️ **Dell 32" 4K** - 22u (Min: 30) → 73 dias

**TOTAL INVERSIÓN NECESARIA:** $847.300

Queres generar ordenes de compra automaticas?""",
            "buttons": "alertas_acciones"
        }

    # 3) PROVEEDORES - AMPLIADO
    prov_kw = ["proveedor", "proveedores", "comprar", "compra", "precio", "precios", "cotizacion", "cotización",
               "distribuidor", "importador", "supplier", "quien", "quién", "vende", "contacto"]
    
    if any(w in p for w in prov_kw):
        return {
            "content": """🏢 **Proveedores Activos - Base de Datos**

**TECNOLOGIA & INFORMATICA**

📌 **TechSupply SA** ⭐⭐⭐⭐⭐ (98%)
- Productos: Notebooks, monitores, impresoras
- Tiempo entrega: 5-7 dias
- Forma pago: 30 dias
- Descuento volumen: 8% en +50 unid
- Ultimo pedido: 15/01/2026 - $2.350.000
- Contacto: ventas@techsupply.com.uy

📌 **Importadora Global** ⭐⭐⭐⭐ (87%)
- Productos: Perifericos, accesorios
- Tiempo entrega: 10-15 dias
- Forma pago: 15 dias
- Descuento: 10% en primera compra
- Ultimo pedido: 08/01/2026 - $890.000
- Contacto: pedidos@impglobal.com

📌 **DistriTech Uruguay** ⭐⭐⭐⭐½ (92%)
- Productos: Todo tipo
- Tiempo entrega: 3-5 dias (LOCAL) ⚡
- Forma pago: 45 dias
- Stock propio: Entrega inmediata
- Ultimo pedido: 22/01/2026 - $456.000
- Contacto: +598 2900 1234

**CELULARES & SMARTPHONES**

📌 **MobileWorld** ⭐⭐⭐⭐⭐ (96%)
- Productos: iPhone, Samsung, Motorola
- Tiempo entrega: 7-10 dias
- Forma pago: 30 dias
- Garantia: 12 meses oficial
- Ultimo pedido: 18/01/2026 - $3.450.000

Queres comparar precios de algun producto especifico?""",
            "buttons": "proveedores_acciones"
        }

    # 4) COMPARACION - MEJORADO
    comp_kw = ["comparar", "comparacion", "comparación", "mejor", "mas barato", "más barato", "economico", "económico",
               "conveniente", "opciones", "alternativas", "cotizar"]
    
    if any(w in p for w in comp_kw):
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
- **Mejor balance:** ImportGlobal

**Recomendacion:**
Pedir a ImportGlobal 100 unidades
- Total: $420.000
- Ahorro vs. DistriTech: $90.000
- Entrega estimada: 28/01 - 02/02

Genero la orden de compra?""",
            "buttons": "comparacion_acciones"
        }

    # 5) MOVIMIENTOS - AMPLIADO
    mov_kw = ["movimiento", "movimientos", "entrada", "entradas", "salida", "salidas", "historial", "registro", 
              "operacion", "operaciones", "transaccion", "transacciones", "actividad", "ultimos", "últimos", "hoy"]
    
    if any(w in p for w in mov_kw):
        return {
            "content": """📋 **Movimientos de Stock - HOY 29/01/2026**

**ENTRADAS (Recepciones) ✅**

✅ **09:15** - Dell Latitude E5470 (50 unidades)
- Orden: #OC-2024-0089
- Proveedor: TechSupply
- Deposito: Central
- Valor: $4.375.000
- Recibido por: J.Martinez

✅ **10:30** - Mouse Logitech M170 (120 unidades)
- Orden: #OC-2024-0091
- Proveedor: ImportGlobal
- Deposito: Norte
- Valor: $180.000

**SALIDAS (Ventas/Despachos) 📤**

📤 **08:45** - Notebook HP ProBook x5
- Cliente: Empresa XYZ SA
- Deposito: Central
- Valor: $437.500

📤 **11:20** - Teclados Logitech K120 x45
- Cliente: Retail ABC
- Deposito: Sur
- Valor: $171.000

**TRANSFERENCIAS ENTRE DEPOSITOS 🔄**

🔄 **14:30** - Mouse MX Master (20 unidades)
- Origen: Deposito Central
- Destino: Deposito Norte
- Estado: En transito (llegada 18:00)

**AJUSTES DE INVENTARIO ⚙️**

⚙️ **16:00** - Webcam C920 (-2 unidades)
- Deposito: Sur
- Motivo: Producto defectuoso

**RESUMEN DEL DIA:**
- Entradas: $7.017.500 (195 unidades)
- Salidas: $1.254.000 (53 unidades)
- Balance: +$5.763.500 (+142 unidades)

Necesitas ver algun movimiento en detalle?""",
            "buttons": "movimientos_acciones"
        }

    # 6) DEPOSITOS - MEJORADO
    dep_kw = ["deposito", "depósito", "almacen", "almacén", "bodega", "central", "norte", "sur", 
              "ubicacion", "ubicación", "donde", "dónde"]
    
    if any(w in p for w in dep_kw):
        if "central" in p:
            return {
                "content": """🏢 **Deposito Central - Info Completa**

**DATOS GENERALES:**

| Campo | Detalle |
|-------|---------|
| 📍 Ubicacion | Av. Italia 2500, Montevideo |
| 👤 Responsable | Juan Martinez |
| 📞 Contacto | +598 2408 1234 |
| ⏰ Horario | Lun-Vie 8:00-18:00 |
| 📦 Capacidad | 1.200 m² (85% ocupado) |

**STOCK POR CATEGORIA:**

| Categoria | Producto | Stock | Valor Unit | Total |
|-----------|----------|-------|------------|-------|
| 💻 **Notebooks** | Dell Latitude | 45u | $210.000 | $9.450.000 |
| | HP ProBook | 32u | | |
| | Lenovo ThinkPad | 28u | | |
| | **Subtotal** | **105u** | | **$9.450.000** |
| 🖥️ **Monitores** | LG 24" | 45u | $47.500 | $4.230.000 |
| | Samsung 27" | 32u | | |
| | Dell 32" | 12u | | |
| | **Subtotal** | **89u** | | **$4.230.000** |
| 🖱️ **Accesorios** | Mouse | 145u | - | $892.000 |
| | Teclados | 89u | | |
| | Webcams | 15u | | |
| | Otros | 207u | | |
| | **Subtotal** | **456u** | | **$892.000** |

**RESUMEN:**
- 💰 Valor Total: **$23.517.000**
- 📦 Total Unidades: **650**
- 🚨 Alertas: 1

**ALERTAS ACTIVAS:**
| Producto | Stock | Minimo | Estado |
|----------|-------|--------|--------|
| Webcam C920 | 15u | 25u | ⚠️ Bajo |

Necesitas ver otro deposito?""",
                "buttons": "depositos_otros"
            }
        elif "norte" in p:
            return {
                "content": """🏢 **Deposito Norte - Info Completa**

**DATOS GENERALES:**

| Campo | Detalle |
|-------|---------|
| 📍 Ubicacion | Ruta 8 Km 23, Zonamerica |
| 👤 Responsable | Maria Rodriguez |
| 📞 Contacto | +598 2518 5678 |
| 📦 Capacidad | 800 m² (62% ocupado) |

**STOCK POR CATEGORIA:**

| Categoria | Producto | Stock | Estado | Valor |
|-----------|----------|-------|--------|-------|
| 💻 **Notebooks** | Dell Latitude | 12u | ✅ OK | $3.150.000 |
| | HP ProBook | 8u | 🔴 **CRITICO** | |
| | Lenovo ThinkPad | 15u | ✅ OK | |
| | **Subtotal** | **35u** | | **$3.150.000** |
| 🖥️ **Monitores** | LG/Samsung/Dell | 34u | ✅ OK | **$1.615.000** |
| 🖱️ **Accesorios** | Varios | 234u | ⚠️ Algunos bajos | **$456.000** |

**RESUMEN:**
- 💰 Valor Total: **$11.455.000**
- 📦 Total Unidades: **303**
- 🚨 Alertas: 2 críticas

**EN TRANSITO:**
| Producto | Cantidad | Origen | Llegada |
|----------|----------|--------|---------|
| 🚚 Mouse MX Master | 20u | Central | Hoy 18:00 |

**ALERTAS CRITICAS:**
| Producto | Stock Actual | Minimo | Estado |
|----------|--------------|--------|--------|
| HP ProBook | 8u | 15u | 🔴 Crítico |
| Webcams | 8u | 15u | ⚠️ Bajo |

Queres ver otro deposito?""",
                "buttons": "depositos_otros"
            }

    # 7) ORDENES - AMPLIADO
    orden_kw = ["orden", "ordenes", "pedido", "pedidos", "compra", "compras", "generar", "crear", 
                "solicitar", "pedir", "oc"]
    
    if any(w in p for w in orden_kw):
        return {
            "content": """📝 **Generar Orden de Compra**

Basado en alertas actuales:

**ORDEN RECOMENDADA #1**
🔴 **URGENTE - Webcam Logitech C920**
- Cantidad: 100 unidades
- Proveedor: ImportGlobal
- Precio unitario: $4.200
- **Total: $420.000**
- Entrega: 10-15 dias
- Stock actual: 27u (critico)

**ORDEN RECOMENDADA #2**
⚠️ **Cable HDMI 2m**
- Cantidad: 80 unidades
- Proveedor: DistriTech
- Precio unitario: $890
- **Total: $71.200**
- Entrega: 3-5 dias

**ORDEN RECOMENDADA #3**
⚠️ **Mouse MX Master**
- Cantidad: 50 unidades
- Proveedor: ImportGlobal
- Precio unitario: $4.850
- **Total: $242.500**

**TOTAL ORDENES:** $733.700

Queres generar estas ordenes?""",
            "buttons": "generar_ordenes"
        }

    # 8) REPORTES - AMPLIADO
    rep_kw = ["reporte", "reportes", "informe", "analisis", "análisis", "estadistica", "estadística",
              "grafico", "gráfico", "dashboard", "kpi"]
    
    if any(w in p for w in rep_kw):
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

    # 9) VENTAS - NUEVO
    venta_kw = ["venta", "ventas", "vendido", "vendimos", "factura", "cliente", "ingreso"]
    
    if any(w in p for w in venta_kw):
        return {
            "content": """💰 **Resumen de Ventas**

**HOY (29/01/2026):**
- Total: $1.254.000
- Unidades: 53
- Facturas: 7

**SEMANA:**
- Total: $8.945.600
- Crecimiento: +12.3%

**MES (Enero):**
- Total: $34.567.800
- Meta: $38.000.000 (91%)

**TOP 5 CLIENTES:**
1. Empresa XYZ: $4.567.000
2. Retail ABC: $3.234.000
3. TechCorp: $2.890.000

Queres ver mas detalles?""",
            "buttons": "ventas_analisis"
        }

    # 10) VALOR INVENTARIO - NUEVO
    valor_kw = ["valor", "vale", "cuanto vale", "cuánto vale", "precio total"]
    
    if any(w in p for w in valor_kw) and "inventario" in p:
        return {
            "content": """💰 **Valorizacion Total de Inventario**

**POR CATEGORIA:**
- 💻 Informatica: $32.914.000
- 📱 Celulares: $24.567.800
- 🖱️ Accesorios: $1.892.300

**VALOR TOTAL:** $59.374.100

**POR DEPOSITO:**
- Central: $23.517.000 (40%)
- Norte: $11.455.000 (19%)
- Sur: $15.942.800 (27%)
- En transito: $8.459.300 (14%)

**INDICADORES:**
- Rotacion promedio: 45 dias
- Stock critico: $1.567.800

Queres ver detalle de alguna categoria?""",
            "buttons": "valor_acciones"
        }

    # RESPUESTA DEFAULT - MEJORADA
    return {
        "content": """❓ No entendi tu consulta. Puedo ayudarte con:

**📦 STOCK & INVENTARIO**
• Consultar stock de productos
• Ver por categoria o deposito
• Valor total del inventario

**🚨 ALERTAS**
• Productos con stock bajo
• Alertas urgentes

**🏢 PROVEEDORES**
• Lista de proveedores
• Comparar precios
• Generar ordenes

**📊 REPORTES**
• Ventas y analisis
• Movimientos del dia

**Ejemplos:**
- "Cuanto stock de notebooks"
- "Que productos estan criticos"
- "Comparar precios webcams"
- "Ver deposito central"

Proba escribir tu consulta! 😊""",
            "buttons": "ayuda_ampliada"
        }

# Mostrar mensajes
for i, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("show_buttons"):
            button_type = message["show_buttons"]

            if button_type == "inicial":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📦 Consultar stock", key=f"btn_stock_{i}", use_container_width=True):
                        response = get_bot_response("stock general")
                        add_message_and_hide_buttons("Ver stock general", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("🚨 Ver alertas", key=f"btn_alertas_{i}", use_container_width=True):
                        response = get_bot_response("alertas")
                        add_message_and_hide_buttons("Ver alertas", response["content"], response.get("buttons"))
                        st.rerun()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🏢 Proveedores", key=f"btn_prov_{i}", use_container_width=True):
                        response = get_bot_response("proveedores")
                        add_message_and_hide_buttons("Ver proveedores", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("📊 Reportes", key=f"btn_rep_{i}", use_container_width=True):
                        response = get_bot_response("reportes")
                        add_message_and_hide_buttons("Ver reportes", response["content"], response.get("buttons"))
                        st.rerun()

            # Acciones stock notebooks
            elif button_type == "stock_notebook_acciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("💰 Comparar precios", key=f"btn_comp_{i}", use_container_width=True):
                        response = get_bot_response("comparar precios")
                        add_message_and_hide_buttons("Comparar precios", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("📝 Generar orden", key=f"btn_orden_{i}", use_container_width=True):
                        response = get_bot_response("generar orden")
                        add_message_and_hide_buttons("Generar orden", response["content"], response.get("buttons"))
                        st.rerun()

            # Alertas acciones
            elif button_type == "alertas_acciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ Generar ordenes auto", key=f"btn_auto_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Generar ordenes automaticas",
                            """✅ **Ordenes generadas automaticamente**

🔴 Orden #OC-2026-0156
- Webcam C920: 100u
- Total: $420.000
- Estado: Pendiente aprobacion

🔴 Orden #OC-2026-0157
- Cable HDMI 2m: 80u
- Total: $71.200
- Estado: Pendiente

**Total:** $491.200

Las ordenes fueron enviadas a compras.

Necesitas algo mas?""",
                            "ayuda_ampliada"
                        )
                        st.rerun()

                with col2:
                    if st.button("📊 Ver reporte", key=f"btn_rep_comp_{i}", use_container_width=True):
                        response = get_bot_response("reportes")
                        add_message_and_hide_buttons("Ver reportes", response["content"], response.get("buttons"))
                        st.rerun()

            # Categorias stock
            elif button_type == "stock_categorias":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("💻 Informatica", key=f"btn_info_{i}", use_container_width=True):
                        response = get_bot_response("stock notebook")
                        add_message_and_hide_buttons("Ver informatica", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("🖱️ Accesorios", key=f"btn_acc_{i}", use_container_width=True):
                        response = get_bot_response("stock accesorios")
                        add_message_and_hide_buttons("Ver accesorios", response["content"], response.get("buttons"))
                        st.rerun()

            # Proveedores acciones
            elif button_type == "proveedores_acciones":
                if st.button("💰 Comparar precios", key=f"btn_comp_prod_{i}", use_container_width=True):
                    response = get_bot_response("comparar precios")
                    add_message_and_hide_buttons("Comparar precios", response["content"], response.get("buttons"))
                    st.rerun()

            # Comparacion acciones
            elif button_type == "comparacion_acciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ Generar orden", key=f"btn_gen_imp_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Generar orden",
                            """✅ **Orden de Compra Generada**

**Orden:** #OC-2026-0158
**Proveedor:** Importadora Global
**Producto:** Webcam C920
**Cantidad:** 100u
**Total:** $420.000

**Entrega:** 10-15 dias
**Estado:** Enviada

La orden fue registrada.

Necesitas algo mas?""",
                            "ayuda_ampliada"
                        )
                        st.rerun()

                with col2:
                    if st.button("🔍 Ver otras opciones", key=f"btn_otras_{i}", use_container_width=True):
                        response = get_bot_response("proveedores")
                        add_message_and_hide_buttons("Ver proveedores", response["content"], response.get("buttons"))
                        st.rerun()

            # Depositos
            elif button_type == "depositos_otros":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🏢 Deposito Norte", key=f"btn_norte_{i}", use_container_width=True):
                        response = get_bot_response("deposito norte")
                        add_message_and_hide_buttons("Ver Norte", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("🏢 Deposito Central", key=f"btn_cent_{i}", use_container_width=True):
                        response = get_bot_response("deposito central")
                        add_message_and_hide_buttons("Ver Central", response["content"], response.get("buttons"))
                        st.rerun()

            # Ayuda
            elif button_type == "ayuda_ampliada":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📦 Ver stock", key=f"btn_stock_ayuda_{i}", use_container_width=True):
                        response = get_bot_response("stock")
                        add_message_and_hide_buttons("Ver stock", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("🚨 Ver alertas", key=f"btn_alert_ayuda_{i}", use_container_width=True):
                        response = get_bot_response("alertas")
                        add_message_and_hide_buttons("Ver alertas", response["content"], response.get("buttons"))
                        st.rerun()

# Ejemplos
st.markdown("---")
st.markdown("**💬 Ejemplos de consultas:**")
col1, col2 = st.columns(2)
with col1:
    st.caption("• Cual es el stock de notebooks")
    st.caption("• Mostrame las alertas criticas")
    st.caption("• Comparar precios de webcams")
    st.caption("• Ver deposito central")
    st.caption("• Ultimos movimientos")
with col2:
    st.caption("• Proveedores activos")
    st.caption("• Generar orden automatica")
    st.caption("• Stock de accesorios")
    st.caption("• Productos mas vendidos")
    st.caption("• Cuanto vale el inventario")

# Input
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
st.caption("💡 **Demo interactivo.** Datos de ejemplo.")
st.caption("🔌 En produccion conecta con tu ERP real.")

# Reset
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
