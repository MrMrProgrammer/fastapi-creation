# FastAPI Creation Templates & Architecture

### 1. Simple / Flat Structure
- **Purpose:** Minimal project setup for small projects or prototypes.
- **Size/Use case:** Quick prototypes or learning purposes.
- **Structure Example:**
```
project/
├── main.py
├── requirements.txt
├── .env
└── README.md
```

### 2. Basic Modular Structure
- **Purpose:** Organize code into reusable modules.
- **Size/Use case:** Medium projects with potential for code reuse.
- **Structure Example:**
```
project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   ├── database.py
│   └── config.py
├── tests/
├── requirements.txt
├── .env
└── README.md
```

### 3. Domain-Driven Design (DDD)
- **Purpose:** Organize complex business logic around domain models.
- **Size/Use case:** Ideal for large projects with complex domain rules.
- **Structure Example:**
```
project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── security.py
│   │   └── dependencies.py
│   └── shared/
│       ├── __init__.py
│       ├── utils.py
│       └── exceptions.py
├── tests/
├── requirements.txt
├── .env
└── README.md
```

### 4. Layered (N-tier)
- **Purpose:** Classic separation into presentation, business, and data layers.
- **Size/Use case:** Suitable for small to medium projects.
- **Structure Example:**
```
project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   └── router.py
│   │   └── dependencies.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   └── security.py
│   ├── models/
│   │   └── __init__.py
│   ├── schemas/
│   │   └── __init__.py
│   ├── services/
│   │   └── __init__.py
│   └── repositories/
│       └── __init__.py
├── tests/
├── requirements.txt
├── .env
└── README.md
```

### 5. Clean Architecture
- **Purpose:** Separate core domain, application, and infrastructure concerns.
- **Size/Use case:** Large projects with complex business rules.
- **Structure Example:**
```
project/
├── src/
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities/
│   │   ├── repositories/
│   │   └── services/
│   ├── application/
│   │   ├── __init__.py
│   │   ├── use_cases/
│   │   └── services/
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   ├── database/
│   │   ├── repositories/
│   │   └── external/
│   └── presentation/
│       ├── __init__.py
│       ├── api/
│       └── schemas/
├── tests/
├── main.py
├── requirements.txt
└── README.md
```

### 6. Microservices
- **Purpose:** Split application into independent services.
- **Size/Use case:** Large-scale applications requiring distributed architecture.
- **Structure Example:**
```
project/
├── services/
├── shared/
├── gateway/
├── docker-compose.yml
├── kubernetes/
└── README.md
```

### 7. Feature-Based
- **Purpose:** Group functionality by features rather than layers.
- **Size/Use case:** Medium projects where teams work on independent features.
- **Structure Example:**
```
project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   ├── features/
│   └── shared/
├── tests/
├── requirements.txt
├── .env
└── README.md
```

### 8. Hexagonal Architecture
- **Purpose:** Isolate core domain logic from external dependencies.
- **Size/Use case:** Medium to large projects with complex integrations.
- **Structure Example:**
```
project/
├── src/
│   ├── adapters/
│   │   ├── __init__.py
│   │   ├── inbound/
│   │   └── outbound/
│   ├── application/
│   │   ├── __init__.py
│   │   ├── ports/
│   │   └── services/
│   └── domain/
│       ├── __init__.py
│       ├── entities/
│       ├── value_objects/
│       └── exceptions/
├── tests/
├── main.py
├── requirements.txt
└── README.md
```

---

## Choosing a Template

- **Small projects / prototypes:** Simple or Layered  
- **Medium projects:** Feature-Based, Modular, Clean  
- **Large projects / complex domain:** DDD, Hexagonal, Microservices

> For more details and usage examples, refer to the CLI prompts when running `fastapi-creation create`.

---

Back to the main page: [README.md](./README.md)
