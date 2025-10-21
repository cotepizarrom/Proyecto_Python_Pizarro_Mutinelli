# Proyecto_Python_Pizarro_Mutinelli
Repositorio de mi proyecto
# 🧾 Proyecto Django — Consultora SUR Consulting

Este proyecto fue desarrollado como entrega del curso de **Python** y tiene como objetivo construir una aplicación web utilizando el **patrón MVT de Django**, aplicada a una **consultora de servicios contables, financieros y laborales**.

---

## 📌 Características principales

- ✅ Implementación de **patrón MVT** (Model–View–Template).  
- 🧱 **3 Modelos**: `Cliente`, `Servicio` y `Lead`.  
- 📝 Formularios para crear registros de cada modelo.  
- 🔍 Buscador de clientes en la base de datos.  
- 🧭 Navegación clara mediante herencia de templates (`base.html`).  
- 🛡️ Panel de administración activo y funcional.  
- 🧰 Uso de Bootstrap para mejorar la interfaz.

---

## 🧱 Modelos

### 🧑 `Cliente`
- Nombre de empresa  
- RUT  
- Nombre de contacto  
- Correo electrónico  
- Teléfono  
- Fecha de ingreso

### 🧾 `Servicio`
- Nombre del servicio (Contabilidad, Control de Gestión, Payroll, etc.)  
- Descripción  
- Precio base mensual

### 📞 `Lead`
- Nombre y apellido  
- Correo electrónico  
- Empresa  
- Servicio de interés  
- Comentarios  
- Estado (nuevo, contactado, cerrado)

---

## 🧭 Rutas principales

| URL                        | Descripción                        |
|----------------------------|------------------------------------|
| `/`                        | Página de inicio                  |
| `/clientes/nuevo/`         | Formulario para crear un cliente  |
| `/servicios/nuevo/`        | Formulario para crear un servicio |
| `/leads/nuevo/`            | Formulario de contacto (lead)     |
| `/clientes/buscar/`        | Buscador de clientes              |
| `/admin/`                  | Panel de administración           |

---

