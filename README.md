# PRACTICA-REST - API REST para gestión académica con autenticación JWT 🔐

Este proyecto demuestra cómo usar un API REST para gestionar cursos, profesores, estudiantes, cargas de trabajo e inscripciones, ahora protegido con autenticación mediante **JSON Web Tokens (JWT)**.

---

## 🚀 Requisitos previos

- Python 3.8 o superior
- pip
- Git
- Postman (opcional para probar endpoints)

---

## ⚙️ Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/fernandopdc30/Lab_08_Django_REST_JWT
cd Lab_08_Django_REST_JWT

cd django-enrollments
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Si no existe requirements.txt, puedes generarlo así:

```bash
pip freeze > requirements.txt
```

### 3. Aplicar migraciones y crear superusuario

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Sigue los pasos y crea un usuario con contraseña.

---

## 🔐 Autenticación con JWT

Se ha implementado JWT con `djangorestframework-simplejwt`.

### 1. Obtener un token JWT

Realiza un POST a:

```
POST http://127.0.0.1:8000/api/token/
```

Con el siguiente JSON en el body (usa el usuario que creaste):

```json
{
  "username": "fer",
  "password": "fer123"
}
```

Respuesta esperada:

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1..."
}
```

### 2. Usar el token para acceder a los endpoints

En Postman, añade a la pestaña Authorization:
- **Tipo:** Bearer Token
- **Token:** pega el valor del campo `access` (sin comillas)

O directamente en headers:

```
Authorization: Bearer TU_TOKEN_AQUI
```


## 📁 Endpoints disponibles

Todos los siguientes endpoints ahora requieren autenticación con JWT:

- **Cursos**: `GET/POST` → `/api/courses/`
- **Profesores**: `GET/POST/PUT/DELETE` → `/api/teachers/`
- **Estudiantes**: `GET/POST` → `/api/students/`
- **Cargas de Trabajo**: `GET/POST` → `/api/workloads/`
- **Inscripciones**: `GET/POST` → `/api/inscriptions/`

Si no envías un token válido, obtendrás `401 Unauthorized`.

---

## 📁 Ejemplos de JSON para probar

### Crear Curso

```json
{
  "curriculum": 2023,
  "year": 3,
  "semester": 5,
  "code": "CUR405",
  "name": "como usar rest",
  "acronym": "PROG-WEB",
  "credits": 4.0,
  "theory_hours": 2.0,
  "practice_hours": 2.0,
  "laboratory_hours": 2.0,
  "laboratory": true
}
```

### Crear Profesor

```json
{
  "names": "Juan Carlos",
  "father_surname": "Gomez Boza",
  "mother_surname": "López",
  "email": "juan.gomez@universidad.edu",
  "phone": "+51987654321",
  "show_phone": true
}
```
---

## ✅ Verificación rápida

| Acción | Ruta | Token necesario |
|--------|------|----------------|
| Obtener token | `/api/token/` | ❌ |
| Listar cursos | `/api/courses/` | ✅ |
| Crear profesor | `/api/teachers/` | ✅ |

---

## ✍ Autora

**Fernando Perez Del Castillo**  
GitHub: https://github.com/fernandopdc30

---

## 🛠 Tecnologías usadas

- Django
- Django REST Framework
- SimpleJWT
- SQLite (por defecto)

---

## 📹 Video demostración

Se incluye video (solo para el docente) en el que se muestra:
- Acceso con JWT
- Comprobación con y sin token
- Endpoints funcionando en Postman
