import requests

class SlackNotifier:
    def __init__(self, webhook_url=None):
        self.webhook_url = webhook_url

    def send_error(self, message):
        if not self.webhook_url:
            print(f"Error (Simulado en Slack): {message}")
            return
            
        payload = {"text": f"🚨 *Pipeline Failure*: {message}"}
        try:
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
        except Exception as e:
            print(f"Failed to send Slack notification: {e}")