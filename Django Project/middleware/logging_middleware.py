from django.utils.timezone import localtime

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f'[{localtime()}] Request: {request.path} {request.method}')

        response = self.get_response(request)

        print(f'[{localtime()}] Response: {response.status_code}')

        return response