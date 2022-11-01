from rest_framework.throttling import SimpleRateThrottle


class SMSthrottling(SimpleRateThrottle):
    scope = 'sms'

    def get_cache_key(self, request, view):
        telephone = request.query_params.get('telephone')
        # cache_format = 'throttle_%(scope)s_%(ident)s'
        return self.cache_format % {'scope': self.scope, 'ident': telephone}
