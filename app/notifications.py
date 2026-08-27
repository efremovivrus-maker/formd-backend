import os
import httpx


def send_n8n_event(event: str, **data):
    webhook_url = os.getenv("N8N_WEBHOOK_URL")

    if not webhook_url:
        print("N8N_WEBHOOK_URL is not configured")
        return

    payload = {
        "event": event,
        **data,
    }

    try:
        response = httpx.post(
            webhook_url,
            json=payload,
            timeout=5.0,
        )
        response.raise_for_status()

    except Exception as exc:
        # Ошибка мониторинга не должна ломать FORMD
        print(f"Failed to send n8n event: {exc}")