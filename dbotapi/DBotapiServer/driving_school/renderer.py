import json

from rest_framework.renderers import JSONRenderer


class UserBaseJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):

        errors = data.get('errors', None)

        # mode = data.get('mode', None)
        
        if errors is not None:
            return super(UserBaseJSONRenderer, self).render(data)


        return json.dumps({
            'user': data
        })