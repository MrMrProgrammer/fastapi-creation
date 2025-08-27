# FastAPI Creation Templates & Architecture


### 2. Domain-Driven Design (DDD)
- **Purpose:** Organize complex business logic around domain models.
- **Size/Use case:** Ideal for large projects with complex domain rules.
- **Structure Example:**
```
src/
├── domain/
├── application/
├── infrastructure/
└── interfaces/
```


### 3. Feature-Based
- **Purpose:** Group functionality by features rather than layers.
- **Size/Use case:** Medium projects where teams work on independent features.
- **Structure Example:**
```
project/
├── users/
├── posts/
└── comments/
```


### 4. Hexagonal Architecture
- **Purpose:** Isolate core domain logic from external dependencies.
- **Size/Use case:** Medium to large projects with complex integrations.
- **Structure Example:**
```
core/
├── ports/
├── adapters/
└── application/
```


### 5. Layered (N-tier)
- **Purpose:** Classic separation into presentation, business, and data layers.
- **Size/Use case:** Suitable for small to medium projects.
- **Structure Example:**
```
app/
├── controllers/
├── services/
└── repositories/
```


### 6. Microservices
- **Purpose:** Split application into independent services.
- **Size/Use case:** Large-scale applications requiring distributed architecture.
- **Structure Example:**
```
services/
├── auth/
├── users/
└── payments/
```


### 7. Modular
- **Purpose:** Organize code into reusable modules.
- **Size/Use case:** Medium projects with potential for code reuse.
- **Structure Example:**
```
modules/
├── core/
├── auth/
└── blog/
```


### 8. Simple
- **Purpose:** Minimal project setup for small projects or prototypes.
- **Size/Use case:** Quick prototypes or learning purposes.
- **Structure Example:**
```
app/
├── main.py
├── routes.py
└── models.py
```


---


## Choosing a Template


- **Small projects / prototypes:** Simple or Layered
- **Medium projects:** Feature-Based, Modular, Clean
- **Large projects / complex domain:** DDD, Hexagonal, Microservices


> For more details and usage examples, refer to the CLI prompts when running `fastapi-creation create`.


---


Back to the main page: [README.md](./README.md)