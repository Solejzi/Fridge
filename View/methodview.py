from flask.views import MethodView


class MView(MethodView):
    def __init__(self):
        self.template = ''
        self.objects = {}

    def get(self, *args, **kwargs):
        """ Responds to GET requests """
        raise NotImplemented

    def post(self, *args, **kwargs):
        """ Responds to POST requests """
        raise NotImplemented

    def put(self, *args, **kwargs):
        """ Responds to PUT requests """
        raise NotImplemented

    def patch(self, *args, **kwargs):
        """ Responds to PATCH requests """
        raise NotImplemented

    def delete(self, *args, **kwargs):
        """ Responds to DELETE requests """
        raise NotImplemented

