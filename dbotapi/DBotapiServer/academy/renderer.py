import json

from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework.renderers import JSONRenderer


class AcademyJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):

        if type(data) is not ReturnList:
            errors = data.get('errors', None)
        
        else:
            errors = data[0].get('errors', None)
        
        if errors is not None:
            return super(AcademyJSONRenderer, self).render(data)
        

        return json.dumps(
            {
                'result': data
            }
        )