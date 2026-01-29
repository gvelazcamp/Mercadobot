import streamlit as st

st.set_page_config(
    page_title="Demo Turnos - AppointmentBot",
    page_icon="📅",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stChatMessage { max-width: 800px; margin: 0 auto; }
    .stChatFloatingInputContainer { max-width: 800px; margin: 0 auto; }
    .custom-header {
        text-align: center; padding: 25px;
        background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
        border-radius: 12px; margin-bottom: 30px; color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .custom-header h1 { margin: 0; font-size: 28px; font-weight: 600; }
    .custom-header p { margin: 10px 0 0 0; opacity: 0.9; font-size: 15px; }
    div[data-testid="column"] > div > div > button {
        width: 100%; border-radius: 8px; padding: 14px 20px; font-weight: 500;
        font-size: 15px; transition: all 0.2s ease; border: 1.5px solid #e5e7eb;
        background: white; color: #374151; box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    div[data-testid="column"] > div > div > button:hover {
        background: #4a90e2; border-color: #4a90e2; color: white;
        transform: translateY(-1px); box-shadow: 0 4px 8px rgba(74, 144, 226, 0.3);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-bottom: 15px;">
    <span style="display: inline-block; background: linear-gradient(135deg, #4a90e2 0%, #5ba3f5 100%);
        color: white; padding: 10px 24px; border-radius: 25px; font-weight: 600; font-size: 14px;
        box-shadow: 0 2px 8px rgba(74, 144, 226, 0.4);">
        🎯 Imaginate este demo con tus datos - Tu agenda, tus servicios, tus reglas
    </span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="custom-header">
    <h1>📅 AppointmentBot - Sistema de Turnos Inteligente</h1>
    <p>Reservá tu turno en segundos con nuestro asistente</p>
</div>
""", unsafe_allow_html=True)

BONUS = "Este asistente gestiona tu agenda automáticamente, envía recordatorios y reduce inasistencias hasta un 60%."

def maybe_bonus():
    if not st.session_state.get("bonus_shown", False):
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"💡 **{BONUS}**",
            "show_buttons": None
        })
        st.session_state.bonus_shown = True

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": """¡Hola! Soy tu asistente de turnos 📅

Puedo ayudarte con:
✅ Ver disponibilidad y reservar
✅ Cambiar o cancelar turnos
✅ Información y horarios
✅ Recordatorios automáticos

¿Qué necesitás?""",
        "show_buttons": "inicial"
    }]

if "selected_date" not in st.session_state:
    st.session_state.selected_date = None

if "selected_time" not in st.session_state:
    st.session_state.selected_time = None

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

if "bonus_shown" not in st.session_state:
    st.session_state.bonus_shown = False

def add_msg(user, bot, btns=None, bonus=False):
    st.session_state.messages.append({"role": "user", "content": user})
    st.session_state.messages.append({"role": "assistant", "content": bot, "show_buttons": btns})
    if bonus:
        maybe_bonus()

def get_response(prompt):
    p = (prompt or "").lower().strip()
    
    # VER CALENDARIO
    if any(k in p for k in ["turno", "reserva", "disponible", "agenda", "cuando", "cuándo", "calendario", "ver", "mostrar"]):
        return {
            "content": """📅 **Calendario de Turnos - Próximos 14 Días**

**SEMANA 1 (Ene-Feb 2024)**

| Día | Fecha | Disponibilidad |
|-----|-------|----------------|
| 🟦 **Lun** | 29 Ene | ✅ **8 turnos** - Muy disponible |
| 🟦 **Mar** | 30 Ene | ✅ **9 turnos** - Muy disponible |
| 🟦 **Mié** | 31 Ene | ✅ **7 turnos** - Disponible |
| 🟦 **Jue** | 1 Feb | ✅ **8 turnos** - Muy disponible |
| 🟧 **Vie** | 2 Feb | ⚡ **6 turnos** - Pocos espacios |
| 🟧 **Sáb** | 3 Feb | ⚠️ **3 turnos** - Casi lleno |
| ⬜ **Dom** | 4 Feb | ❌ **Cerrado** |

**SEMANA 2 (Feb 2024)**

| Día | Fecha | Disponibilidad |
|-----|-------|----------------|
| 🟦 **Lun** | 5 Feb | ✅ **8 turnos** - Muy disponible |
| 🟦 **Mar** | 6 Feb | ✅ **9 turnos** - Muy disponible |
| 🟦 **Mié** | 7 Feb | ✅ **7 turnos** - Disponible |
| 🟦 **Jue** | 8 Feb | ✅ **8 turnos** - Muy disponible |
| 🟧 **Vie** | 9 Feb | ⚡ **6 turnos** - Pocos espacios |
| 🟧 **Sáb** | 10 Feb | ⚠️ **3 turnos** - Casi lleno |
| ⬜ **Dom** | 11 Feb | ❌ **Cerrado** |

---

**📊 LEYENDA:**
- 🟦 Azul: Muchos turnos (6-9)
- 🟧 Naranja: Pocos turnos (3-5)
- ⬜ Gris: Cerrado

**💡 RECOMENDACIONES:**
- Los **miércoles y jueves** tienen más espacios
- **Sábados** se llenan rápido - reservá con anticipación
- **Lunes mañana** suele ser tranquilo

**🎯 PARA RESERVAR:**
Elegí un día usando los botones o escribí:
- "Quiero el martes 30"
- "Dame turno para el jueves 1"
- "El viernes 2 de febrero"
- "Próximo miércoles"

👇 **Usá los botones para reservar rápido**""",
            "buttons": "fecha_rapida",
            "bonus_once": True
        }
    
    # SELECCIÓN DE DÍA
    if any(k in p for k in ["lunes", "martes", "miercoles", "miércoles", "jueves", "viernes", "sabado", "sábado"]) or any(k in p for k in ["30", "31", "1 ", "2 ", "3 "]):
        
        if "martes" in p or "30" in p:
            fecha = "Martes 30 de Enero"
            turnos_totales = 9
        elif "miercoles" in p or "miércoles" in p or "31" in p:
            fecha = "Miércoles 31 de Enero"
            turnos_totales = 7
        elif "jueves" in p or ("1" in p and "feb" in p):
            fecha = "Jueves 1 de Febrero"
            turnos_totales = 8
        elif "viernes" in p or ("2" in p and ("feb" in p or "febrero" in p)):
            fecha = "Viernes 2 de Febrero"
            turnos_totales = 6
        else:
            fecha = "Martes 30 de Enero"
            turnos_totales = 9
        
        st.session_state.selected_date = fecha
        
        return {
            "content": f"""✅ **Perfecto! {fecha}**

⏰ **Horarios Disponibles - {turnos_totales} espacios**

---

**🌅 TURNO MAÑANA (9:00 - 13:00)**

| Hora | Estado | Duración |
|------|--------|----------|
| 09:00 | ✅ **Disponible** | 30-45 min |
| 09:30 | ✅ **Disponible** | 30-45 min |
| 10:00 | ❌ Ocupado | - |
| 10:30 | ✅ **Disponible** | 30-45 min |
| 11:00 | ✅ **Disponible** | 30-45 min |
| 11:30 | ✅ **Disponible** | 30-45 min |
| 12:00 | ✅ **Disponible** | 30-45 min |
| 12:30 | ✅ **Disponible** | 30-45 min |

**🌇 TURNO TARDE (14:30 - 19:00)**

| Hora | Estado | Duración |
|------|--------|----------|
| 14:00 | ✅ **Disponible** | 30-45 min |
| 14:30 | ✅ **Disponible** | 30-45 min |
| 15:00 | ❌ Ocupado | - |
| 15:30 | ✅ **Disponible** | 30-45 min |
| 16:00 | ✅ **Disponible** | 30-45 min |
| 16:30 | ✅ **Disponible** | 30-45 min |
| 17:00 | ❌ Ocupado | - |
| 17:30 | ✅ **Disponible** | 30-45 min |
| 18:00 | ✅ **Disponible** | 30-45 min |

---

**💡 RECOMENDACIONES:**
- **Menos espera:** 9:00am, 11:00am, 14:30pm
- **Más popular:** 10:00am, 15:00pm, 17:00pm
- **Último turno:** 18:00pm

**🎯 PARA CONFIRMAR:**
Elegí el horario con los botones o escribí:
- "Quiero a las 9:30"
- "El de las 14:00"
- "15:30 está bien"
- "A las 11"

👇 **Horarios más solicitados**""",
            "buttons": "horario_rapido"
        }
    
    # SELECCIÓN DE HORARIO
    if any(h in p for h in ["9:", "10:", "11:", "12:", "14:", "15:", "16:", "17:", "18:"]) or any(h in p for h in ["9am", "2pm", "3pm"]):
        if "9:30" in p or "930" in p:
            hora = "09:30"
        elif "14:00" in p or "1400" in p or "2pm" in p or "14" in p:
            hora = "14:00"
        elif "15:30" in p or "1530" in p:
            hora = "15:30"
        elif "11" in p:
            hora = "11:00"
        else:
            hora = "14:00"
        
        st.session_state.selected_time = hora
        fecha = st.session_state.selected_date or "Martes 30 de Enero"
        
        return {
            "content": f"""🎉 **¡Excelente elección!**

---

**📋 RESUMEN DE TU TURNO:**

📅 **Fecha:** {fecha}  
🕐 **Hora:** {hora}  
⏱️ **Duración:** 30-45 minutos  
📍 **Lugar:** Av. 18 de Julio 1850, Montevideo

---

**✅ PARA CONFIRMAR NECESITO:**

Por favor dame estos datos:
1️⃣ **Nombre completo**
2️⃣ **Teléfono / WhatsApp**
3️⃣ **Email**
4️⃣ **Motivo** (opcional)

**EJEMPLO:**
"Juan Pérez, 099 123 456, juan@email.com, control general"

O simplemente:
"Juan Pérez, 099123456, juan@email.com"

---

**🔔 INCLUYE:**
✅ Confirmación inmediata por email
✅ Recordatorio WhatsApp 24hs antes
✅ Recordatorio SMS 2hs antes
✅ Link Google Calendar

**📋 POLÍTICAS:**
✅ Cancelación gratis (+24hs antes)
✅ Llegá 10 minutos antes
✅ Traé documento de identidad

---

💬 **Dame tus datos para confirmar el turno**""",
            "buttons": "confirmar_datos"
        }
    
    # CONFIRMACIÓN
    if (any(k in p for k in ["confirmo", "confirmar", "si", "sí", "ok", "dale"]) and 
        ("@" in p or "099" in p or "098" in p or "095" in p or "094" in p or "093" in p or "092" in p or "091" in p)):
        
        return {
            "content": """✅ **¡TURNO CONFIRMADO EXITOSAMENTE!**

🎊 Tu reserva está confirmada

---

**📋 DETALLES DE TU TURNO:**

📅 **Fecha:** Martes 30 de Enero 2024  
🕐 **Hora:** 14:00 hs  
👤 **Paciente:** Juan Pérez  
📱 **WhatsApp:** 099 123 456  
📧 **Email:** juan@email.com  

**📍 Ubicación:**  
Av. 18 de Julio 1850, Montevideo  
🚇 Metro Tres Cruces (3 cuadras)  
🚌 Ómnibus 64, 180, 187, 121

**🔖 Código:** #TURNO-300124-1400

---

**📨 TE ENVIAMOS:**

✅ **Confirmación por email** → Enviado ✅  
✅ **Recordatorio 24hs antes** → Programado 📅  
✅ **Recordatorio 2hs antes** → Programado ⏰  
✅ **Link Google Calendar** → Enviado 📆

---

**💡 TIPS PARA TU VISITA:**

🎒 **Qué traer:**
• Documento de identidad
• Credencial (si tenés)
• Estudios previos (si hay)
• Lista de medicamentos

⏰ **Cuándo llegar:**
• Llegá 10 minutos antes
• Evitá llegar muy temprano

🚗 **Estacionamiento:**
• En la puerta: $100/hora
• Garaje cercano: $150
• Zona azul disponible

---

**🔄 ¿NECESITÁS CAMBIAR O CANCELAR?**

Avisá con 24hs de anticipación:
📱 WhatsApp: 099 123 456  
📞 Teléfono: 2908 5555  
✉️ Email: turnos@clinica.uy

---

**🎉 ¡Nos vemos el martes 30 a las 14:00!**

¿Necesitás algo más?""",
            "buttons": "post_confirmacion"
        }
    
    # CANCELAR/CAMBIAR
    if any(k in p for k in ["cancelar", "cambiar", "modificar", "mover", "reprogramar", "no puedo"]):
        return {
            "content": """🔄 **Gestión de Turnos**

**OPCIONES DISPONIBLES:**

1️⃣ **CAMBIAR DE FECHA/HORA**
2️⃣ **CANCELAR TURNO**
3️⃣ **CONSULTAR MI TURNO**

---

**📝 PARA GESTIONAR TU TURNO:**

Dame esta información:
• Tu nombre completo
• Fecha actual del turno
• Hora actual del turno
• Qué querés hacer (cambiar/cancelar)

**Si es cambio:**
• Nueva fecha preferida
• Nuevo horario preferido

---

**📋 POLÍTICAS:**

✅ **+48 horas antes**
- Cambio o cancelación SIN CARGO
- Reprogramación inmediata
- Total flexibilidad

✅ **24-48 horas antes**
- Cambio o cancelación OK
- Sin penalización
- Avisá cuanto antes

⚠️ **Menos de 24hs**
- Entendemos emergencias
- Avisá igual para liberar el turno
- Alguien más puede necesitarlo

🔴 **Sin aviso**
- Afecta a otros pacientes
- Próximo turno requiere confirmación

---

**💡 EXCEPCIONES (sin cargo):**
- Emergencias médicas
- Casos de fuerza mayor
- Primera cancelación
- Problemas de transporte

---

**📱 FORMAS DE CONTACTO:**

1. **Este chat** - Dame los datos ahora
2. **WhatsApp:** 099 123 456 ⚡ Más rápido
3. **Teléfono:** 2908 5555
4. **Email:** turnos@clinica.uy

---

**EJEMPLO:**
"Juan Pérez, tengo turno el martes 30/1 a las 14:00, quiero cambiarlo al jueves 1/2 a las 10:00"

¿Qué necesitás gestionar?""",
            "buttons": "gestion_opciones"
        }
    
    # INFORMACIÓN
    if any(k in p for k in ["horario", "atencion", "atención", "donde", "dónde", "ubicacion", "ubicación", "info", "información"]):
        return {
            "content": """ℹ️ **Información del Consultorio**

---

**⏰ HORARIOS DE ATENCIÓN:**

**Lunes a Viernes:**
🕐 Mañana: 9:00 - 13:00
🕒 Tarde: 14:30 - 19:00

**Sábados:**
🕐 Mañana: 9:00 - 13:00
❌ Tarde: Cerrado

**Domingos y Feriados:**
❌ Cerrado

---

**📍 UBICACIÓN:**

🏢 **Dirección:**  
Av. 18 de Julio 1850, Montevideo  
Entre Yaguarón y Río Branco

🗺️ **Referencias:**
• Frente a la plaza
• A 2 cuadras del banco
• Edificio de 3 pisos

---

**🚇 CÓMO LLEGAR:**

**En Metro:**
• Estación Tres Cruces (3 cuadras)
• 5 minutos caminando

**En Ómnibus:**
• Líneas: 64, 180, 187, 121, 142
• Parada: 18 de Julio y Yaguarón

**En Auto:**
• Estacionamiento en la puerta ($100/h)
• Garaje cercano ($150 - convenio)
• Zona azul disponible

**En Taxi/Uber:**
• Dirección exacta en GPS
• Hay dónde parar al frente

---

**📞 CONTACTO:**

☎️ **Teléfono:** 2908 5555  
📱 **WhatsApp:** 099 123 456  
✉️ **Email:** info@clinica.uy  
🌐 **Web:** www.clinica.uy

**Horario de atención telefónica:**  
Lun-Vie: 9:00-18:00  
Sáb: 9:00-13:00

---

**🏥 SERVICIOS:**

✅ Consultas generales  
✅ Primera consulta  
✅ Seguimientos  
✅ Certificados médicos  
✅ Estudios básicos  
✅ Atención familiar

---

**💳 MEDIOS DE PAGO:**

✅ Efectivo  
✅ Débito (todas)  
✅ Crédito (hasta 3 cuotas)  
✅ Transferencia  
✅ Mutuales con convenio

---

**♿ ACCESIBILIDAD:**

✅ Rampa de acceso  
✅ Ascensor disponible  
✅ Baño adaptado  
✅ Estacionamiento preferencial

¿Necesitás algo más?""",
            "buttons": "info_acciones"
        }
    
    # RECORDATORIOS
    if any(k in p for k in ["recordatorio", "aviso", "notificacion", "notificación", "mensaje", "whatsapp", "sms"]):
        return {
            "content": """🔔 **Sistema de Recordatorios Automáticos**

Todos los turnos incluyen recordatorios sin cargo!

---

**📱 CÓMO FUNCIONA:**

**48 horas antes:**
📧 **Email con confirmación**
• Detalle completo del turno
• Botón "Confirmar asistencia"
• Botón "Cancelar/Modificar"
• Cómo llegar + mapa

**24 horas antes:**
📱 **WhatsApp**
• "Hola Juan! Mañana tenés turno a las 14:00"
• Link Google Maps
• Respuesta rápida: 1=Confirmo, 2=Cancelo

**2 horas antes:**
💬 **SMS recordatorio**
• "Tu turno es HOY a las 14:00"
• "Te esperamos!"
• Mensaje corto y directo

---

**📊 RESULTADOS:**

Con recordatorios automáticos:
✅ 60% menos inasistencias
✅ 85% tasa de confirmación
✅ Mejor organización de agenda
✅ Menos llamadas manuales

---

**⚙️ PERSONALIZACIÓN:**

Podés elegir:
📧 Solo email
📱 Solo WhatsApp
💬 Solo SMS
🔔 Todos los canales (recomendado)

**También podés:**
• Elegir horario preferido
• Frecuencia de recordatorios
• Idioma del mensaje

---

**🔕 DESACTIVAR:**

Si no querés recordatorios:
• Respondé STOP a cualquier mensaje
• Avisanos por este chat
• Llamá al 2908 5555

---

**❓ PREGUNTAS FRECUENTES:**

**¿Me cobran?**
No, todos los recordatorios son gratis

**¿Puedo cambiar mis preferencias?**
Sí, en cualquier momento

**¿Y si cambié de número?**
Avisanos para actualizar

**¿Funcionan de madrugada?**
No, solo entre 9am y 8pm

---

¿Querés activar los recordatorios?""",
            "buttons": "recordatorios_config"
        }
    
    # DEFAULT
    return {
        "content": """❓ **No entendí bien, pero puedo ayudarte con:**

**📅 RESERVAR TURNO**
• Ver calendario completo
• Elegir fecha disponible
• Seleccionar horario
• Confirmar tu turno

**🔄 GESTIONAR TURNO**
• Cambiar fecha/hora
• Cancelar turno
• Consultar mi turno
• Reprogramar

**ℹ️ INFORMACIÓN**
• Horarios de atención
• Ubicación y cómo llegar
• Servicios disponibles
• Medios de pago
• Contacto

**🔔 RECORDATORIOS**
• Cómo funcionan
• Activar/desactivar
• Personalizar

---

**💡 INTENTÁ CON ESTAS FRASES:**

"Ver calendario"  
"Quiero turno para el martes"  
"Cambiar mi turno"  
"Dónde queda el consultorio"  
"Cómo llego"  
"Activar recordatorios"  
"Cancelar turno"  
"Horarios de atención"

¿Qué necesitás?""",
        "buttons": "ayuda"
    }

# Mostrar mensajes
for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
        if msg.get("show_buttons"):
            bt = msg["show_buttons"]
            
            if bt == "inicial":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📅 Ver calendario", key=f"cal_{i}", use_container_width=True):
                        r = get_response("calendario")
                        add_msg("Ver calendario completo", r["content"], r.get("buttons"), r.get("bonus_once"))
                        st.rerun()
                with col2:
                    if st.button("ℹ️ Información", key=f"info_{i}", use_container_width=True):
                        r = get_response("informacion")
                        add_msg("Ver información", r["content"], r.get("buttons"))
                        st.rerun()
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🔄 Gestionar turno", key=f"gest_{i}", use_container_width=True):
                        r = get_response("cancelar")
                        add_msg("Gestionar mi turno", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("🔔 Recordatorios", key=f"rec_{i}", use_container_width=True):
                        r = get_response("recordatorios")
                        add_msg("Sobre recordatorios", r["content"], r.get("buttons"))
                        st.rerun()
            
            elif bt == "fecha_rapida":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Mar 30 Ene", key=f"mar_{i}", use_container_width=True):
                        r = get_response("martes 30")
                        add_msg("Martes 30 de Enero", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("Mié 31 Ene", key=f"mie_{i}", use_container_width=True):
                        r = get_response("miércoles 31")
                        add_msg("Miércoles 31 de Enero", r["content"], r.get("buttons"))
                        st.rerun()
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Jue 1 Feb", key=f"jue_{i}", use_container_width=True):
                        r = get_response("jueves 1")
                        add_msg("Jueves 1 de Febrero", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("Vie 2 Feb", key=f"vie_{i}", use_container_width=True):
                        r = get_response("viernes 2")
                        add_msg("Viernes 2 de Febrero", r["content"], r.get("buttons"))
                        st.rerun()
            
            elif bt == "horario_rapido":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("09:30", key=f"h1_{i}", use_container_width=True):
                        r = get_response("9:30")
                        add_msg("Quiero a las 9:30", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("14:00", key=f"h2_{i}", use_container_width=True):
                        r = get_response("14:00")
                        add_msg("Quiero a las 14:00", r["content"], r.get("buttons"))
                        st.rerun()
                with col3:
                    if st.button("15:30", key=f"h3_{i}", use_container_width=True):
                        r = get_response("15:30")
                        add_msg("Quiero a las 15:30", r["content"], r.get("buttons"))
                        st.rerun()
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("11:00", key=f"h4_{i}", use_container_width=True):
                        r = get_response("11:00")
                        add_msg("Quiero a las 11:00", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("16:00", key=f"h5_{i}", use_container_width=True):
                        r = get_response("16:00")
                        add_msg("Quiero a las 16:00", r["content"], r.get("buttons"))
                        st.rerun()
                with col3:
                    if st.button("18:00", key=f"h6_{i}", use_container_width=True):
                        r = get_response("18:00")
                        add_msg("Quiero a las 18:00", r["content"], r.get("buttons"))
                        st.rerun()
            
            elif bt == "ayuda":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📅 Ver calendario", key=f"cal_h_{i}", use_container_width=True):
                        r = get_response("calendario")
                        add_msg("Ver calendario", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("ℹ️ Info", key=f"info_h_{i}", use_container_width=True):
                        r = get_response("informacion")
                        add_msg("Ver info", r["content"], r.get("buttons"))
                        st.rerun()

# EJEMPLOS - MUCHOS MÁS!
st.markdown("---")
st.markdown("**💬 Probá estas consultas:**")

col1, col2, col3 = st.columns(3)
with col1:
    st.caption("**📅 Reservas:**")
    st.caption("• Ver calendario")
    st.caption("• Quiero turno martes")
    st.caption("• El jueves 1")
    st.caption("• A las 14:00")
    st.caption("• 9:30 de la mañana")
    st.caption("• Confirmo mi turno")

with col2:
    st.caption("**🔄 Gestión:**")
    st.caption("• Cambiar mi turno")
    st.caption("• Cancelar turno")
    st.caption("• No puedo ir")
    st.caption("• Reprogramar")
    st.caption("• Consultar mi turno")
    st.caption("• Mover para otro día")

with col3:
    st.caption("**ℹ️ Información:**")
    st.caption("• Dónde queda")
    st.caption("• Cómo llego")
    st.caption("• Horarios")
    st.caption("• Teléfono")
    st.caption("• Recordatorios")
    st.caption("• Qué servicios tienen")

# Input
if prompt := st.chat_input("Escribí tu consulta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    r = get_response(prompt)
    st.session_state.messages.append({
        "role": "assistant",
        "content": r["content"],
        "show_buttons": r.get("buttons")
    })
    if r.get("bonus_once"):
        maybe_bonus()
    st.rerun()

# Footer
st.divider()
st.caption("💡 Demo interactivo - Sistema profesional de turnos con calendario")
st.caption("🔌 En producción sincroniza con Google Calendar, WhatsApp API y tu CRM")

# Reset
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reiniciar"):
        st.session_state.messages = [{
            "role": "assistant",
            "content": """¡Hola! Soy tu asistente de turnos 📅

Puedo ayudarte con:
✅ Ver disponibilidad y reservar
✅ Cambiar o cancelar turnos
✅ Información y horarios
✅ Recordatorios automáticos

¿Qué necesitás?""",
            "show_buttons": "inicial"
        }]
        st.session_state.selected_date = None
        st.session_state.selected_time = None
        st.session_state.button_clicked = False
        st.session_state.bonus_shown = False
        st.rerun()
