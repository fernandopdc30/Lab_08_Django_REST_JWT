# PRACTICA-REST - API REST para gestión académica

Este proyecto demuestra cómo usar un API REST para gestionar cursos, profesores, estudiantes, cargas de trabajo e inscripciones.

## 🚀 Requisitos previos

- Python instalado
- `pip install requests` (si se usará `test_api_examples.py`)
- Servidor Django corriendo en:
http://127.0.0.1:8000/
- Base de datos migrada y con modelos activos
- Postman (opcional para probar endpoints)

---

## 📁 Colección Postman

Se incluye el archivo `iw.postman_collection.json` que puede importarse directamente en Postman para probar los siguientes endpoints:

1. **Listar Cursos**
 - `GET http://127.0.0.1:8000/api/courses/`

2. **Crear Curso**
 - `POST http://127.0.0.1:8000/api/courses/`
 - JSON de ejemplo:
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

3. **Crear Profesor**
 - `POST http://127.0.0.1:8000/api/teachers/`
 - JSON de ejemplo:
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

4. **Actualizar Profesor**
 - `PUT http://127.0.0.1:8000/api/teachers/1/`
 - JSON de ejemplo:
   ```json
   {
     "names": "Juan Carlos",
     "father_surname": "García",
     "mother_surname": "López",
     "email": "juancarlos.actualizado@universidad.edu",
     "phone": "+51987654321",
     "show_phone": false
   }
   ```

5. **Eliminar Profesor**
 - `DELETE http://127.0.0.1:8000/api/teachers/1/`

6. **Crear Estudiante**
 - `POST http://127.0.0.1:8000/api/students/`
 - JSON de ejemplo:
   ```json
   {
     "cui": 20220001,
     "names": "Marycielo",
     "father_surname": "Bedoya",
     "mother_surname": "Pinto",
     "email": "marycielo.bedoya@estudiante.edu",
     "phone": "+51987123456"
   }
   ```

7. **Crear Carga de Trabajo**
 - `POST http://127.0.0.1:8000/api/workloads/`
 - JSON de ejemplo:
   ```json
   {
     "course": 2,
     "group": "A",
     "laboratory": "lab01",
     "capacity": 25,
     "teacher": 2
   }
   ```

8. **Crear Inscripción**
 - `POST http://127.0.0.1:8000/api/inscriptions/`
 - JSON esperado:
   ```json
   {
     "workload": 2,
     "student": 1
   }
   ```

---

## 📌 Notas adicionales

- Asegúrese de que los IDs utilizados (por ejemplo `teacher: 2`, `course: 2`, etc.) existan previamente.
- Puede usar el archivo `test_api_examples.py` para automatizar las pruebas por consola.

---

## ✍ Autora

Marycielo Bedoya Pinto  
GitHub: [@mary1508](https://github.com/mary1508)
