# 🌐 Proyecto Final — Aplicación Web en Django  
### **SUR Consulting Blog**

Este proyecto fue desarrollado como entrega final del curso **Python - Coderhouse**.  
Consiste en una aplicación web tipo blog con funcionalidades completas de autenticación, administración, perfil de usuario, mensajería interna y gestión de contenido (CRUD de páginas).

---

## 🚀 Descripción General

La aplicación simula el sitio web interno de **SUR Consulting**, una consultora financiera y contable.  
Permite crear y gestionar publicaciones, perfiles de usuario, y enviar mensajes entre miembros registrados.

### Funcionalidades principales:
- **Home y About:** páginas informativas accesibles públicamente.  
- **Gestión de páginas (CRUD):**
  - Crear, editar, eliminar y listar páginas con título, subtítulo, contenido enriquecido (CKEditor), imagen y fecha.
  - Búsqueda por título/subtítulo y mensajes de “sin resultados”.
- **Autenticación de usuarios:**
  - Registro (`signup`), login, logout y cambio de contraseña.
- **Perfil de usuario:**
  - Avatar, biografía y fecha de cumpleaños.
  - Edición de perfil con subida de imagen.
- **Mensajería interna:**
  - Bandeja de entrada (Inbox).
  - Envío y recepción de mensajes entre usuarios.
  - Estado de lectura y vista de conversación.
- **Diseño visual inspirado en la identidad de SUR Consulting:**
  - Colores: `#0C5957` y `#56CED1`
  - Estructura limpia, moderna y responsive.

---

## ⚙️ Tecnologías utilizadas
- **Lenguaje:** Python 3.13  
- **Framework:** Django 5.2.7  
- **Base de datos:** SQLite3 (entorno local)
- **Editor de texto enriquecido:** django-ckeditor  
- **Manejo de imágenes:** Pillow  
- **Frontend:** HTML5, CSS3, Bootstrap base

---

## 📂 Estructura del proyecto
Proyecto_Python_Pizarro_Mutinelli/
│
├── proyecto_coder/ # Configuración principal
├── pages/ # CRUD de páginas (modelo principal)
├── accounts/ # Registro, login y perfil de usuario
├── messaging/ # Mensajería interna
├── templates/ # Plantillas base (base.html, etc.)
├── media/ # Carpeta para imágenes de usuario y páginas
├── static/ # Archivos estáticos (CSS, íconos, etc.)
├── requirements.txt # Librerías necesarias
├── .gitignore # Archivos a excluir del repo
└── manage.py


---

## 🧠 Instalación y uso local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/cotepizarrom/Proyecto_Python_Pizarro_Mutinelli.git
   cd Proyecto_Python_Pizarro_Mutinelli
