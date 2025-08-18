import json, os, sys, time, socket

APP_NAME = "pwd_gen_app"
LOG_PATH = os.environ.get("APP_LOG_PATH", "./logs/app.log")
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

def log_event(event_type, user=None, details=None):
    evt = {"ts": int(time.time()*1000), "app": APP_NAME, "host": socket.gethostname(),
           "event": event_type, "user": user, "details": details or {}}
    line = json.dumps(evt, separators=(",", ":"), ensure_ascii=False)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    #print(line, file=sys.stdout, flush=True)