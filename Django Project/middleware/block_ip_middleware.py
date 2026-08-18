from django.http import HttpResponseForbidden
from pathlib import Path
import environ
import os

env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

BLOCKED_IPS = env.list("BLOCKED_IPS")

class BlockIpMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")

        if ip in BLOCKED_IPS:
            return HttpResponseForbidden("You are blocked")
        
        return self.get_response(request)
