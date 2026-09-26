# Repository Guidelines

## Project Structure & Module Organization

This repository contains a FastAPI backend and a Svelte/Vite frontend for a Q&A platform.

- `main.py` wires the FastAPI app and routers.
- `database.py` and `models.py` define SQLAlchemy setup and persisted models.
- `domain/<feature>/` contains backend feature modules. Follow the existing `*_schema.py`, `*_crud.py`, and `*_router.py` pattern.
- `migrations/` contains Alembic migration scripts.
- `frontend/src/` contains Svelte routes, components, stores, API helpers, CSS, and assets. Public assets live in `frontend/public/`.

No test directory exists yet. Add backend tests under `tests/` and frontend tests near the relevant component or under `frontend/src/__tests__/` when adding test tooling.

## Build, Test, and Development Commands

- `uv sync` installs backend dependencies from `pyproject.toml` and `uv.lock`.
- `uv run uvicorn main:app --reload --port 8000 --host 127.0.0.1` starts the API server.
- `uv run alembic upgrade head` applies database migrations.
- `npm install --prefix frontend` installs frontend dependencies.
- `npm run dev --prefix frontend` starts the Vite dev server.
- `npm run build --prefix frontend` builds the production frontend bundle.
- `npm run preview --prefix frontend` previews the production build.

## Coding Style & Naming Conventions

Use 4-space indentation for Python and keep modules grouped by domain. Name backend files with the existing suffixes, for example `question_schema.py`, `question_crud.py`, and `question_router.py`. Prefer Pydantic v2 models for schemas, and keep database access in CRUD modules rather than route handlers.

Frontend components use `PascalCase.svelte`; route views live under `frontend/src/routes/`. Use `frontend/src/lib/api.js` for API calls.

## Testing Guidelines

There is no configured automated test suite at present. When adding backend tests, prefer `pytest` with FastAPI `TestClient`, and name files `test_<feature>.py`. Add frontend tests only after adding an explicit runner such as Vitest.

Before submitting changes, at minimum run `uv run alembic upgrade head` for schema work and `npm run build --prefix frontend` for frontend work.

## Commit & Pull Request Guidelines

Recent history uses short messages, sometimes with emoji, such as `✨ Implement Answer Comment system...`. Keep commits imperative and feature-focused, for example `Add question tag validation`.

Pull requests should include a concise summary, linked issue if available, migration notes for database changes, and screenshots for visible UI changes. Mention the commands you ran and any missing tests.

## Security & Configuration Tips

Do not commit local secrets, generated logs, or private database snapshots. Set `SECRET_KEY` in the backend environment for non-local deployments, and keep database configuration environment-specific.
