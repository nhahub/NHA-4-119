# LEXORA Frontend Pro

Modern React + Vite frontend for the LEXORA AI Content Generation System.

## Tech Stack

- React
- Vite
- Custom CSS
- FastAPI backend integration

## Run Locally

```bash
npm install --registry=https://registry.npmjs.org/
copy .env.example .env
npm run dev
```

Then open:

```text
http://localhost:5173
```

## Environment

`.env` should contain:

```env
VITE_API_BASE_URL=http://localhost:8000
```

## Pages

- Home
- Generate
- Workflow
- Team

## Backend Endpoints Used

- `POST /api/v1/generate`
- `GET /api/v1/jobs/{job_id}`
- `GET /api/v1/jobs/{job_id}/result`

## Notes

- No login/signup.
- No history page.
- No debug details shown to users.
- Dropdowns use `None` as the default option.
- Empty `None` values are not sent to the backend.
