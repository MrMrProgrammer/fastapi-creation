"""
This module defines the raw folder and file structure for different FastAPI project architectures.
Each architecture is stored as a nested dictionary where keys are folder or file names,
and values are either:
- another dictionary (for a folder),
- an empty string (for a file).
"""

LAYOUTS = {
    # 1. Simple / Flat Structure
    "simple": {
        "main.py": "",
        "requirements.txt": "",
        ".env": "",
        "README.md": ""
    },

    # 2. Basic Modular Structure
    "modular": {
        "app": {
            "__init__.py": "",
            "main.py": "",
            "models.py": "",
            "routes.py": "",
            "schemas.py": "",
            "database.py": "",
            "config.py": ""
        },
        "tests": {},
        "requirements.txt": "",
        ".env": "",
        "README.md": ""
    },

    # 3. Domain-Driven Structure
    "ddd": {
        "app": {
            "__init__.py": "",
            "main.py": "",
            "core": {
                "__init__.py": "",
                "config.py": "",
                "database.py": "",
                "security.py": "",
                "dependencies.py": ""
            },
            "users": {
                "__init__.py": "",
                "models.py": "",
                "routes.py": "",
                "schemas.py": "",
                "services.py": "",
                "dependencies.py": ""
            },
            "products": {
                "__init__.py": "",
                "models.py": "",
                "routes.py": "",
                "schemas.py": "",
                "services.py": ""
            },
            "shared": {
                "__init__.py": "",
                "utils.py": "",
                "exceptions.py": ""
            }
        },
        "tests": {
            "users": {},
            "products": {}
        },
        "requirements.txt": "",
        ".env": "",
        "README.md": ""
    },

    # 4. Layered Architecture
    "layered": {
        "app": {
            "__init__.py": "",
            "main.py": "",
            "api": {
                "__init__.py": "",
                "v1": {
                    "__init__.py": "",
                    "endpoints": {},
                    "router.py": ""
                },
                "dependencies.py": ""
            },
            "core": {
                "__init__.py": "",
                "config.py": "",
                "database.py": "",
                "security.py": ""
            },
            "models": {
                "__init__.py": ""
            },
            "schemas": {
                "__init__.py": ""
            },
            "services": {
                "__init__.py": ""
            },
            "repositories": {
                "__init__.py": ""
            }
        },
        "tests": {},
        "requirements.txt": "",
        ".env": "",
        "README.md": ""
    },

    # 5. Clean Architecture
    "clean": {
        "src": {
            "domain": {
                "__init__.py": "",
                "entities": {},
                "repositories": {},
                "services": {}
            },
            "application": {
                "__init__.py": "",
                "use_cases": {},
                "services": {}
            },
            "infrastructure": {
                "__init__.py": "",
                "database": {},
                "repositories": {},
                "external": {}
            },
            "presentation": {
                "__init__.py": "",
                "api": {},
                "schemas": {}
            }
        },
        "tests": {},
        "main.py": "",
        "requirements.txt": "",
        "README.md": ""
    },

    # 6. Microservices Structure
    "microservices": {
        "services": {
            "user_service": {
                "app": {
                    "main.py": ""
                },
                "Dockerfile": "",
                "requirements.txt": "",
                ".env": ""
            },
            "product_service": {
                "app": {
                    "main.py": ""
                },
                "Dockerfile": "",
                "requirements.txt": "",
                ".env": ""
            },
            "notification_service": {
                "app": {},
                "Dockerfile": "",
                "requirements.txt": ""
            }
        },
        "shared": {},
        "gateway": {
            "main.py": ""
        },
        "docker-compose.yml": "",
        "kubernetes": {},
        "README.md": ""
    },

    # 7. Feature-Based Structure
    "feature": {
        "app": {
            "__init__.py": "",
            "main.py": "",
            "core": {},
            "features": {},
            "shared": {}
        },
        "tests": {},
        "requirements.txt": "",
        ".env": "",
        "README.md": ""
    },

    # 8. Hexagonal Architecture
    "hexagonal": {
        "src": {
            "adapters": {
                "__init__.py": "",
                "inbound": {
                    "__init__.py": "",
                    "web": {}
                },
                "outbound": {
                    "__init__.py": ""
                }
            },
            "application": {
                "__init__.py": "",
                "ports": {},
                "services": {}
            },
            "domain": {
                "__init__.py": "",
                "entities": {},
                "value_objects": {},
                "exceptions": {}
            }
        },
        "tests": {},
        "main.py": "",
        "requirements.txt": "",
        "README.md": ""
    }
}
