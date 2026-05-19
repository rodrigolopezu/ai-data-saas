# AI Data Analytics SaaS

Plataforma web que permite subir un archivo de datos (CSV/Excel) y obtener
automáticamente un dashboard interactivo con gráficos e insights generados por IA.

## Stack
- **Frontend**: Next.js 14, shadcn/ui, Tailwind, Recharts
- **Backend**: FastAPI, Pandas, Anthropic SDK
- **Base de datos**: Supabase (PostgreSQL)
- **Deploy**: Vercel (frontend) + Railway (backend)

## Desarrollo local
```bash
docker compose up
```
Frontend: http://localhost:3000  
Backend: http://localhost:8000

## Arquitectura
Ver `/docs` para diagramas de arquitectura y decisiones de diseño.