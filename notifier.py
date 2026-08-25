import requests
import config 

def notify(course, outcome, message):
    payload={
        "course_name": course["name"],
        "outcome": outcome,
        "message": message
    }
    try:
        requests.post(config.webhook_url, json=payload)
    except:
        print("notify: failed to send notification")