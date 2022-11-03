from flask import Flask
from src.routes.routes import routes


app = Flask(__name__)


app.add_url_rule(routes["index_route"],view_func=routes["indexcontroller"])

app.add_url_rule(routes["index_admin_route"],view_func=routes["indexgacontroller"])

app.add_url_rule(routes["delete_route"],view_func=routes["delete_controller"])

app.add_url_rule(routes["update_route"],view_func=routes["update_controller"])

app.add_url_rule(routes["update_gerente_route"],view_func=routes["update_gerente_controller"])

app.add_url_rule(routes["cadastro_route"],view_func=routes["cadastro_cliente_controller"])

app.add_url_rule(routes["login_route"],view_func=routes["login_controller"])

app.add_url_rule(routes["login_cliente_validacao_route"],view_func=routes["login_cliente_validacao_controller"])

app.add_url_rule(routes["home_user_route"],view_func=routes["home_user_controller"])

app.add_url_rule(routes["dados_user_route"],view_func=routes["dados_user_controller"])

app.add_url_rule(routes["pagina_deposito_route"],view_func=routes["pagina_deposito_controller"])

app.add_url_rule(routes["realizar_deposito_route"],view_func=routes["realizar_deposito_controller"])

app.add_url_rule(routes["pagina_saque_route"],view_func=routes["pagina_saque_controller"])

app.add_url_rule(routes["realizar_saque_route"],view_func=routes["realizar_saque_controller"])

app.add_url_rule(routes["pagina_transferencia_route"],view_func=routes["pagina_transferencia_controller"])

app.add_url_rule(routes["realizar_transferencia_route"],view_func=routes["realizar_tranferencia_controller"])

app.add_url_rule(routes["pagina_transferencia_gerente_route"],view_func=routes["pagina_transferencia_gerente_controller"])

app.add_url_rule(routes["realizar_transferencia_gerente_route"],view_func=routes["realizar_tranferencia_gerente_controller"])

app.add_url_rule(routes["home_user_id_route"],view_func=routes["home_user_id_controller"])

app.add_url_rule(routes["home_gerente_agencia_id_route"],view_func=routes["home_gerente_agencia_id_controller"])

app.add_url_rule(routes["link_gerenciar_contas"],view_func=routes["link_gerenciar_contas_controller"])

app.add_url_rule(routes["aprovar_contas"],view_func=routes["aprovar_contas_controller"])

app.add_url_rule(routes["link_modo_gerente_contas"],view_func=routes["modo_gerente_contas_controller"])

app.add_url_rule(routes["link_aprovacao_deposito"],view_func=routes["link_aprovacao_deposito_controller"])

app.add_url_rule(routes["aprovacao_deposito"],view_func=routes["aprovacao_deposito_controller"])

app.add_url_rule(routes["link_extrato"],view_func=routes["link_extrato_controller"])

app.add_url_rule(routes["link_extrato_gerente"],view_func=routes["link_extrato_gerente_controller"])

app.add_url_rule(routes["gerar_extrato"],view_func=routes["gerar_extrato_controller"])

app.register_error_handler(routes["not_found_route"], routes["not_found_controller"])

app.add_url_rule(routes["pagina_deposito_gerente_route"],view_func=routes["pagina_deposito_gerente_controller"])

app.add_url_rule(routes["realizar_deposito_gerente_route"],view_func=routes["realizar_deposito_gerente_controller"])

app.add_url_rule(routes["pagina_saque_gerente_route"],view_func=routes["pagina_gerente_saque_controller"])

app.add_url_rule(routes["home_gerente_conta"],view_func=routes["home_gerente_conta_controller"])

app.add_url_rule(routes["link_cadastro"],view_func=routes["link_cadastro_controller"])

app.add_url_rule(routes["cadastro_execucao"],view_func=routes["cadastro_execucao_controller"])

app.add_url_rule(routes["verificar_aprovacao"],view_func=routes["verificar_aprovacao_controller"])

app.add_url_rule(routes["solicitacao_deletar"],view_func=routes["solicitacao_deletar_controller"])

app.add_url_rule(routes["home_gerente_geral_id_route"],view_func=routes["home_gerente_geral_id_controller"])

app.add_url_rule(routes["area_cliente_route"],view_func=routes["area_cliente_controller"])

app.add_url_rule(routes["funcionario_route"],view_func=routes["funcionario_controller"])

app.add_url_rule(routes["gerenciar_gerentes_link_route"],view_func=routes["gerenciar_gerentes_controller"])

app.add_url_rule(routes["gerenciar_banco_link_route"],view_func=routes["gerenciar_banco_controller"])

app.add_url_rule(routes["gerenciar_agencias_link_route"],view_func=routes["gerenciar_agencias_controller"])

app.add_url_rule(routes["cadastro_GA_route"],view_func=routes["cadastro_GA_controller"])

app.add_url_rule(routes["banco_dados_route"],view_func=routes["banco_dados_controller"])

app.add_url_rule(routes["entrada_route"],view_func=routes["verifica_entrada_controller"])

app.add_url_rule(routes["criar_agencia_route"],view_func=routes["criar_agencia_controller"])

""" app.add_url_rule(routes["realizar_transferencia_route"],view_func=routes["realizar_transferencia_controller"]) """

