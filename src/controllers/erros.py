from flask.views import MethodView

class NotFoundController(MethodView):
    def get(self,error):
        return f"PAGINA NAO ENCONTRADA {error}"