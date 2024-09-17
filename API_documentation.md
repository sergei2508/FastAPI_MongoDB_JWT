# API Documentation

## Overview
Esta API permite la gestión de usuarios, incluyendo autenticación y operaciones CRUD. Todos los endpoints requieren `application/json` como `Content-Type`.

## Endpoints

### 1. **Login**
**Method:** `POST`  
**URL:** `/api/v1/users/login`

#### Headers
| Header       | Value             |
|--------------|-------------------|
| Content-Type | application/json  |

#### Body (Request)
```json
{
  "mobile_phone": "string",
  "password": "string"
}
```

#### Response (200 OK)
```json
{
  "user": {
    "first_name": "string",
    "last_name": "string",
    "date_birth": "YYYY-MM-DD",
    "mobile_phone": "string",
    "email": "email@example.com",
    "password": "string",
    "address": "string"
  },
  "access_token": "token",
  "token_type": "bearer"
}
```

---

### 2. **Get All Users**
**Method:** `GET`  
**URL:** `/api/v1/users`

#### Headers
| Header       | Value             |
|--------------|-------------------|
| Content-Type | application/json  |

#### Response (200 OK)
```json
[
  {
    "id": "integer",
    "first_name": "string",
    "last_name": "string",
    "date_birth": "YYYY-MM-DD",
    "mobile_phone": "string",
    "email": "email@example.com",
    "address": "string",
    "session_active": "boolean"
  }
]
```

---

### 3. **Get User by ID**
**Method:** `GET`  
**URL:** `/api/v1/users/{id_user}`

#### Headers
| Header       | Value             |
|--------------|-------------------|
| Content-Type | application/json  |

#### Response (200 OK)
```json
{
  "id": "integer",
  "first_name": "string",
  "last_name": "string",
  "date_birth": "YYYY-MM-DD",
  "mobile_phone": "string",
  "email": "email@example.com",
  "address": "string",
  "session_active": "boolean"
}
```

---

### 4. **Create User**
**Method:** `POST`  
**URL:** `/api/v1/users`

#### Headers
| Header       | Value             |
|--------------|-------------------|
| Content-Type | application/json  |

#### Body (Request)
```json
{
  "first_name": "string",
  "last_name": "string",
  "date_birth": "YYYY-MM-DD",
  "mobile_phone": "string",
  "email": "email@example.com",
  "password": "string",
  "address": "string"
}
```

#### Response (200 OK)
```json
{
  "first_name": "string",
  "last_name": "string",
  "date_birth": "YYYY-MM-DD",
  "mobile_phone": "string",
  "email": "email@example.com",
  "password": "string",
  "address": "string"
}
```

---

### 5. **Update User**
**Method:** `PUT`  
**URL:** `/api/v1/users/{id_user}`

#### Headers
| Header       | Value             |
|--------------|-------------------|
| Content-Type | application/json  |

#### Body (Request)
```json
{
  "first_name": "string",
  "last_name": "string",
  "date_birth": "YYYY-MM-DD",
  "mobile_phone": "string",
  "email": "email@example.com",
  "password": "string",
  "address": "string"
}
```

#### Response (200 OK)
```json
{
  "first_name": "string",
  "last_name": "string",
  "date_birth": "YYYY-MM-DD",
  "mobile_phone": "string",
  "email": "email@example.com",
  "password": "string",
  "address": "string"
}
```

---

### 6. **Delete User**
**Method:** `DELETE`  
**URL:** `/api/v1/users/{id_user}`

#### Headers
| Header       | Value             |
|--------------|-------------------|
| Content-Type | application/json  |

#### Response (200 OK)
```json
{
  "message": "User deleted successfully"
}
```

---

## Status Codes
- **200 OK:** La solicitud fue exitosa.
- **400 Bad Request:** La solicitud contiene errores o parámetros inválidos.
- **404 Not Found:** El recurso solicitado no fue encontrado.
- **500 Internal Server Error:** Ocurrió un error en el servidor.

---
