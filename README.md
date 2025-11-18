````markdown
# 📚 Mi Biblioteca Personal Web

Una aplicación web Full Stack diseñada para gestionar, visualizar y llevar el control de una colección personal de libros. Este proyecto permite ver los libros en una "estantería" virtual, filtrar búsquedas instantáneamente y marcar el progreso de lectura.

## 🚀 Características

* **Estantería Visual:** Diseño moderno tipo *grid* (cuadrícula) para mostrar las portadas de los libros.
* **Buscador en Tiempo Real:** Filtra libros por título o autor instantáneamente mientras escribes (sin recargar la página).
* **Estado de Lectura:** Botón interactivo para marcar libros como "Leídos" o "Pendientes". El cambio se guarda en la base de datos automáticamente sin refrescar la web.
* **Contador Dinámico:** Muestra el total de libros guardados en la colección.
* **Diseño Responsivo:** Se adapta a diferentes tamaños de pantalla.

## 🛠️ Tecnologías Utilizadas

### Backend (El Cerebro)
* **Python 3:** Lenguaje principal.
* **Flask:** Micro-framework web para manejar las rutas y la lógica del servidor.
* **MySQL Connector:** Para la comunicación entre Python y la base de datos.

### Database (La Memoria)
* **MySQL:** Base de datos relacional para almacenar autores, libros y sus relaciones.

### Frontend (La Cara)
* **HTML5 & Jinja2:** Estructura de la página y motor de plantillas para mostrar datos dinámicos.
* **CSS3:** Diseño personalizado usando CSS Grid, Flexbox y Variables CSS.
* **JavaScript (Vanilla):** Lógica del lado del cliente para el buscador y las peticiones asíncronas (AJAX/Fetch).

---

## ⚙️ Guía de Instalación y Ejecución

Sigue estos pasos para poner en marcha el proyecto en tu computadora local.

### 1. Prerrequisitos
Asegúrate de tener instalado lo siguiente:
* [Python](https://www.python.org/downloads/) (versión 3.x).
* [MySQL Server](https://dev.mysql.com/downloads/mysql/) (o XAMPP).
* Un gestor de base de datos como **MySQL Workbench**.

### 2. Configuración de la Base de Datos
Necesitas crear la estructura de la base de datos. Abre tu MySQL Workbench y ejecuta el siguiente script SQL:

```sql
DROP DATABASE IF EXISTS biblioteca_personal;
CREATE DATABASE biblioteca_personal;
USE biblioteca_personal;

-- Tabla de Autores
CREATE TABLE Autores(
    id_autor INT AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50),
    PRIMARY KEY (id_autor)
);

-- Tabla de Libros
CREATE TABLE Libros(
    id_libro INT AUTO_INCREMENT,
    titulo VARCHAR(255) NOT NULL,
    anio_publicacion INT,
    leido BOOLEAN DEFAULT FALSE, -- Columna para el estado de lectura
    portada VARCHAR(255),        -- (Opcional) Para guardar el nombre del archivo de imagen
    PRIMARY KEY (id_libro)
);

-- Tabla Puente (Relación Muchos a Muchos)
CREATE TABLE Libros_Autores(
    id_libro INT,
    id_autor INT,
    PRIMARY KEY (id_libro, id_autor),
    FOREIGN KEY (id_libro) REFERENCES Libros(id_libro),
    FOREIGN KEY (id_autor) REFERENCES Autores(id_autor)
);

-- (Opcional) Insertar datos de prueba
INSERT INTO Autores(nombre, nacionalidad) VALUES ('Franz Kafka', 'Checo');
INSERT INTO Libros(titulo, anio_publicacion, leido) VALUES ('La Metamorfosis', 1915, FALSE);
INSERT INTO Libros_Autores(id_libro, id_autor) VALUES (1, 1);
````

### 3\. Instalación de Dependencias de Python

Abre tu terminal en la carpeta del proyecto e instala las librerías necesarias:

```bash
pip install Flask mysql-connector-python
```

### 4\. Conexión a la Base de Datos

Abre el archivo `app.py` y busca la sección de configuración `db_config`. Asegúrate de poner **tu contraseña** de MySQL:

```python
db_config = {
    'user': 'root',
    'password': 'TU_CONTRASEÑA_AQUI',  <-- ¡Cambia esto!
    'host': '127.0.0.1',
    'database': 'biblioteca_personal'
}
```

### 5\. ¡A Ejecutar\!

En tu terminal, ejecuta el siguiente comando:

```bash
python app.py
```

Verás un mensaje indicando que el servidor está corriendo. Abre tu navegador web e ingresa a:
👉 **https://www.google.com/search?q=http://127.0.0.1:5000/**

-----

## 📂 Estructura del Proyecto

  * **`app.py`**: El archivo principal. Conecta con la base de datos, gestiona las rutas (`/` y `/alternar_leido`) y sirve la página web.
  * **`templates/`**:
      * `index.html`: La estructura visual de la página. Usa Jinja2 para recibir la lista de libros desde Python.
  * **`static/`**:
      * `style.css`: Todos los estilos visuales (colores, fuentes, grid).
      * `script.js`: El código que hace funcionar el buscador y el botón de "Leído".
      * `img/`: Carpeta donde se guardan los iconos SVG (`eye.svg`, `eye-check.svg`) y las portadas de los libros.

## 🔮 Próximas Mejoras (Roadmap)

  * [ ] Añadir un formulario web para agregar libros nuevos sin usar código SQL.
  * [ ] Permitir subir imágenes de portadas reales desde el formulario.
  * [ ] Crear una página de estadísticas (libros leídos vs. no leídos).

-----

*Proyecto creado con fines de aprendizaje y pasión por los libros.*

```
```
