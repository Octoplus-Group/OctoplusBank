from flask import Flask
from src.routes.routes import routes


app = Flask(__name__)


app.add_url_rule(routes["index_route"],view_func=routes["indexcontroller"])

app.add_url_rule(routes["delete_route"],view_func=routes["delete_controller"])

app.add_url_rule(routes["update_route"],view_func=routes["update_controller"])

app.add_url_rule(routes["cadastro_route"],view_func=routes["cadastro_cliente_controller"])

app.add_url_rule(routes["login_route"],view_func=routes["login_controller"])

app.add_url_rule(routes["login_cliente_validacao_route"],view_func=routes["login_cliente_validacao_controller"])

app.add_url_rule(routes["home_user_route"],view_func=routes["home_user_controller"])

app.add_url_rule(routes["dados_user_route"],view_func=routes["dados_user_controller"])

app.add_url_rule(routes["pagina_deposito_route"],view_func=routes["pagina_deposito_controller"])

app.add_url_rule(routes["realizar_deposito_route"],view_func=routes["realizar_deposito_controller"])

app.add_url_rule(routes["pagina_saque_route"],view_func=routes["pagina_saque_controller"])

app.add_url_rule(routes["realizar_saque_route"],view_func=routes["realizar_saque_controller"])

app.add_url_rule(routes["home_user_id_route"],view_func=routes["home_user_id_controller"])

app.register_error_handler(routes["not_found_route"], routes["not_found_controller"])

""" app.add_url_rule(routes["realizar_transferencia_route"],view_func=routes["realizar_transferencia_controller"]) """

