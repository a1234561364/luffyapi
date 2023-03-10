from django.middleware.csrf import CsrfViewMiddleware

from django.utils.deprecation import MiddlewareMixin


class MyMiddle(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8008'
        if request.method == "OPTIONS":
            # 可以加*
            response["Access-Control-Allow-Headers"] = "Content-Type"
            response["Access-Control-Allow-Headers"] = "authorization"
        return response
