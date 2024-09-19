# FastAPI MongoDB JWT API

Este proyecto es una API basada en FastAPI y MongoDB que utiliza JWT (JSON Web Tokens) para la autenticación de usuarios. Está diseñada para facilitar la gestión de usuarios, protegiendo endpoints con autenticación segura mediante tokens JWT.

Puedes probar los endpoints directamente en la [API desplegada aquí](https://app-p970.onrender.com/api/v1/users).

Para autenticarte en la API, puedes usar las siguientes credenciales enviando una solicitud `POST` al endpoint `/users/login` con el siguiente cuerpo JSON:

```json
{
    "mobile_phone": "1234567890",
    "password": "password"
}
```
## Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu entorno:

- Docker
- Docker Compose
- Git

## Instalación y configuración

Sigue estos pasos para configurar y desplegar el proyecto en tu entorno local:

### 1. Clonar el repositorio

```bash
git clone https://github.com/sergei2508/FastAPI_MongoDB_JWT_API.git
```

### 2. Navegar al directorio de despliegue del proyecto

```bash
cd FastAPI_MongoDB_JWT_API/
```

### 3. Configurar las variables de entorno

Crea un archivo `.env` en el directorio raíz del proyecto y agrega las siguientes variables de entorno necesarias para que el proyecto funcione correctamente:

#### MongoDB
```bash
MONGO_INITDB_ROOT_USERNAME=your_mongodb_username
MONGO_INITDB_ROOT_PASSWORD=your_mongodb_password
MONGO_INITDB_DATABASE=your_database_name
DATABASE_URL=mongodb://your_mongodb_username:your_mongodb_password@localhost:27017/your_database_name
```

#### JWT
```bash
ACCESS_TOKEN_EXPIRES_IN=30  # Expira en 30 minutos
JWT_ALGORITHM=RS256
JWT_PRIVATE_KEY=your_private_key
JWT_PUBLIC_KEY=your_public_key
```

### 4. Desplegar con Docker Compose

Una vez que hayas configurado las variables de entorno, puedes construir y desplegar el proyecto usando Docker Compose. Esto iniciará la aplicación FastAPI y un contenedor de MongoDB.

```bash
docker-compose up --build
```

## Endpoints principales

La API ofrece varios endpoints. A continuación, se listan los más importantes:

- **POST /users/login:** Autenticación de usuarios y generación de tokens JWT.
- **POST /users:** Registro de nuevos usuarios.
- **GET /users:** Obtención de la lista de usuarios (requiere autenticación).
- **GET /users/{id}:** Obtención de información de un usuario específico por su ID.
- **PUT /users/{id}:** Actualización de la información de un usuario.
- **DELETE /users/{id}:** Eliminación de un usuario.


## Variables de Entorno

Aquí tienes un resumen de las variables de entorno que necesitas configurar en el archivo `.env` para ejecutar este proyecto correctamente:

### MongoDB

- **MONGO_INITDB_ROOT_USERNAME:** El nombre de usuario de MongoDB.
- **MONGO_INITDB_ROOT_PASSWORD:** La contraseña de MongoDB.
- **MONGO_INITDB_DATABASE:** El nombre de la base de datos que se va a utilizar.
- **DATABASE_URL:** La URL de conexión a MongoDB en el formato `mongodb://<user>:<password>@<host>:<port>/<database>`.

### JWT

- **ACCESS_TOKEN_EXPIRES_IN:** El tiempo de expiración del token de acceso (en minutos).
- **JWT_ALGORITHM:** El algoritmo utilizado para la firma del token (por ejemplo, RS256).
- **JWT_PRIVATE_KEY:** La clave privada utilizada para firmar los tokens JWT.
- **JWT_PUBLIC_KEY:** La clave pública utilizada para verificar los tokens JWT.

## Ejecución de pruebas

Para ejecutar las pruebas unitarias de la aplicación, puedes usar `pytest`:

```bash
pytest
```

## Tecnologías utilizadas

Este proyecto ha sido construido utilizando las siguientes tecnologías y herramientas:

- **FastAPI:** Framework de Python para construir APIs modernas y de alto rendimiento.
- **MongoDB:** Base de datos NoSQL para almacenar los datos de usuarios.
- **Docker:** Plataforma para desarrollar, enviar y ejecutar aplicaciones dentro de contenedores.
- **JWT (JSON Web Tokens):** Estándar para la autenticación segura basada en tokens.

--- 
