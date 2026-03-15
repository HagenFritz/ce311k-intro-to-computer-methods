# Introduction to APIs

## API Basics

### What Are APIs  
- Set of rules for software systems to communicate  
- Like a waiter: request > kitchen > response  
- Common uses: weather apps, payment systems, social media posting  

### Benefits of APIs  
- Save cost and dev time  
- Reuse existing services  
- Interoperability across systems  
- Scale easily  
- Enable rapid innovation and automation  

### API Architecture  
- REST (lightweight, stateless, most common)  
- SOAP (heavier, XML-based, strict rules)  

### How APIs Work  
- Client sends **request** → Server sends **response**  
- Communication follows **HTTP** protocol  

## HTTP Protocol

### HTTP Methods  
- `GET` – Retrieve data  
- `POST` – Create new data  
- `PUT` / `PATCH` – Update/replace data  
- `DELETE` – Remove data  

### HTTP Status Codes

- **`100s` – Informational (Request in Progress)**
- **`200s` – Success (Request was successful)**
  - `200 OK` – The request was successful, and the server returned the requested data (common for `GET` requests).
  - `201 Created` – The request was successful, and a new resource was created (common for `POST` requests).
  - `202 Accepted` – The request has been accepted for processing, but the processing is not complete (useful for long-running operations).
  - `204 No Content` – The request was successful, but there is no content to return (commonly used for `DELETE` requests).

- **`300s` – Redirect (Further Action Needed)**
- **`400s` – Client Error (The request contains bad syntax or cannot be fulfilled)**
  - `400 Bad Request` – The server cannot process the request due to malformed syntax (common error for incorrectly formatted data).
  - `401 Unauthorized` – Authentication is required, or the credentials provided are incorrect.
  - `403 Forbidden` – The server understands the request but refuses to authorize it (e.g., permission issues).
  - `404 Not Found` – The requested resource could not be found on the server.
  - `405 Method Not Allowed` – The HTTP method used is not allowed for the requested resource (e.g., `POST` used on a `GET`-only endpoint).
  - `408 Request Timeout` – The server timed out waiting for the client to send data.
  - `429 Too Many Requests` – The user has sent too many requests in a given amount of time (rate limiting).

- **`500s` – Server Error (The server failed to fulfill the request)**
  - `500 Internal Server Error` – A generic error message when the server encounters an unexpected condition.
  - `502 Bad Gateway` – The server, while acting as a gateway or proxy, received an invalid response from an upstream server.
  - `503 Service Unavailable` – The server is temporarily unable to handle the request due to overload or maintenance.
  - `504 Gateway Timeout` – The server, acting as a gateway or proxy, did not receive a timely response from the upstream server.

## HTTP Requests/Responses

### HTTP Request Structure  
1. **Start Line** – Method + URL + HTTP version  
2. **Headers** – Extra info (e.g., content type, auth)  
3. **Blank Line** – Separates headers from body  
4. **Body** – Only for methods like `POST` or `PATCH`; contains data  

### HTTP Response Structure  
1. **Start Line** – Status code + HTTP version  
2. **Headers** – Extra info (e.g., content type, auth)  
3. **Blank Line** – Separates headers from body  
4. **Body** – Contains response data  

## Example: GET  
```
GET /api/users?username=newuser HTTP/1.1  
Host: example.com  
```

**Response:**  
```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 76

{
  "id": 123,
  "username": "newuser",
  "email": "newuser@example.com"
}
```

## Example: POST  
```
POST /api/users HTTP/1.1  
Content-Type: application/json  

{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "securepassword"
}
```

**Response:**  
```http
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: 76

{
  "id": 123,
  "username": "newuser",
  "email": "newuser@example.com"
}
```

## Example: PATCH  
```
PATCH /api/users/123 HTTP/1.1  
Content-Type: application/json  

{ "bio": "Updated bio" }
```

**Response:**  
```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 95

{
  "id": 123,
  "username": "newuser",
  "email": "newuser@example.com",
  "bio": "Updated bio"
}
```

## Example: DELETE  
```
DELETE /api/users/123 HTTP/1.1  
```

**Response:**  
```http
HTTP/1.1 204 No Content
Content-Length: 0
```