from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from fibonacci.dynamic import fibonacci_dynamic


@api_view(http_method_names=["GET"])
def get_fibonacci_n(request: Request) -> Response:
    try:
        n = int(request.query_params["n"])
    except:
        return Response(
            {"status": "failed", "error": "n must be a an integer > 0"}, status=422
        )
    if n < 0:
        return Response(
            {"status": "failed", "error": "n must be a an integer > 0"}, status=422
        )
    else:
        return Response(
            {
                "status": "success",
                "number": f"{n}",
                "fibonacci_value": f"{fibonacci_dynamic(n)}",
            },
            status=200,
        )
