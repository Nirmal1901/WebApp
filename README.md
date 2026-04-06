# NuOps Demo App

A simple User Management REST API used to demonstrate **NuOps CI Auto-Healer**.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/users` | List all users |
| GET | `/users/<id>` | Get user by ID |
| POST | `/users` | Create new user |
| DELETE | `/users/<id>` | Delete user |

## Run Locally

```bash
pip install -r requirements.txt
python app/main.py
```

## Run Tests

```bash
pytest tests/ -v
```

## CI/CD

This repo uses GitHub Actions. Every push runs:
1. Install dependencies
2. Run pytest test suite
3. Check 80% code coverage

NuOps monitors the pipeline and auto-creates GitHub Issues when CI fails.
