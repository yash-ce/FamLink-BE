import typing as _
from rest_framework import serializers  # type: ignore
from rest_framework.request import Request  # type: ignore
from rest_framework.response import Response  # type: ignore


def validate_request(serializer: _.Type[serializers.Serializer]) -> _.Callable:
    """
    Validation helper for views:
        * Throws validation error with proper format
        * Provides a extra parameter to view method with sanitized data
        * Merge query params and request body
    """
    def decorator(func: _.Callable):
        def wrapper(self, req: Request, *args, **kwargs):
            query_params = {}
            # ignoring extra query params with same key name
            for key in req.query_params:
                query_params[key] = req.query_params[key]

            # creating serializer from query params and request body
            _all = {**req.data, **query_params, **kwargs}
            serialized = serializer(data=_all)

            # validating data
            if not serialized.is_valid():
                return Response({
                    'success': False,
                    'code': 422,
                    'errors': serialized.errors,
                    'message': 'Some entities failed.'
                }, status=422)

            # calling view method
            return func(self, req, serialized.data, *args)
        return wrapper
    return decorator