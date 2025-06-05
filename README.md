# Python Todo App - End-to-End Type Safety

🚀 **Built in 3 hours**

This project demonstrates complete end-to-end type safety from a Python FastAPI backend to a Vue.js TypeScript frontend, achieved in just 3 hours with minimal prior Python experience.

## What Was Accomplished

- **Full-stack type safety** from Python Pydantic models to TypeScript interfaces
- **Complete CRUD API** with FastAPI and proper response models
- **Modern Vue.js frontend** with TypeScript and openapi-fetch
- **Automatic type generation** from OpenAPI schema
- **Real-time UI updates** with TanStack Query mutations

## Stack

### Backend (Python)
- **FastAPI** - Modern Python web framework
- **Pydantic** - Data validation and serialization
- **CORS** middleware for frontend communication

### Frontend (Vue.js + TypeScript)
- **Vue 3** with Composition API
- **TypeScript** for type safety
- **TanStack Query** for state management
- **openapi-fetch** for type-safe API calls
- **TailwindCSS** for styling
- **Vite** for build tooling

### Type Safety Pipeline
```
Python Pydantic Models → FastAPI OpenAPI Schema → TypeScript Types → Vue Components
```

## Commands

```bash
# Backend
make dev              # Start FastAPI server with hot reload
make install          # Install Python dependencies with uv
make test             # Run pytest tests

# Frontend (cd client/)
npm run dev           # Start Vite dev server
npm run build         # Build for production
npm run preview       # Preview production build
npm run generate-types # Generate TypeScript types from API
```

## API Documentation

Visit `http://127.0.0.1:8000/docs` when the server is running to see the auto-generated Swagger documentation with all endpoints and schemas.
