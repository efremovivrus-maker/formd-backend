# FORMD AI Backend

MVP backend for FORMD AI.

## What it does

- `POST /generate-prompt` — creates a manufacturing-oriented visualization prompt.
- `GET /admin/config` — returns the current System Prompt and Manufacturing Rules.
- `PUT /admin/config` — saves a new configuration version.
- `GET /health` — health check.

Previous prompt/rules versions are archived under `data/versions/`.

## Local setup

### 1. Open this folder in Cursor

### 2. Create a virtual environment

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env`

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Fill in:

```env
OPENAI_API_KEY=...
ADMIN_TOKEN=...
OPENAI_MODEL=gpt-5
ALLOWED_ORIGINS=http://localhost:3000,https://your-tilda-domain.com
```

For `ADMIN_TOKEN`, use a long random value.

### 5. Run

```bash
uvicorn app.main:app --reload
```

Open:

- API docs: http://127.0.0.1:8000/docs
- Health: http://127.0.0.1:8000/health

## First test

In `/docs`, open `POST /generate-prompt` and use:

```json
{
  "request": "Хочу низкое терракотовое кресло в эстетике 1970-х, с плавной монолитной формой."
}
```

## Admin test

For `GET /admin/config` and `PUT /admin/config`, add this request header:

```text
X-Admin-Token: YOUR_ADMIN_TOKEN
```

## Tilda architecture

Public page:

```text
Tilda -> POST /generate-prompt -> FORMD backend -> OpenAI
```

Admin page:

```text
Tilda /admin-ai
  -> GET /admin/config
  -> edit textareas
  -> PUT /admin/config
```

Do not put `OPENAI_API_KEY` in Tilda.

For the MVP, the admin token can be entered into the private admin page
manually at session start. A production version should use proper admin
authentication rather than embedding the token in page HTML.
