from src.controllers.controller import *
from src.controllers.erros import NotFoundController

routes ={
    "index_route":"/","indexcontroller":IndexController.as_view("index"),
    "index_admin_route":"/gerenteagencia","indexgacontroller":IndexController.as_view("indexga"),
    "not_found_route":404,"not_found_controller": NotFoundController.as_view("not_found"),
    "delete_route":"/delete/cliente/<int:id>","delete_controller":DeleteClienteController.as_view("delete"),
    "update_route":"/update/cliente/<int:id>","update_controller":UpdateClienteController.as_view("update"),
    "cadastro_route":"/cadastro_cliente","cadastro_cliente_controller":CadastroClienteController.as_view("cadastro"),
    "login_route":"/login_cliente","login_controller":LoginController.as_view("login"),
    "login_cliente_validacao_route":"/login_cliente_validacao","login_cliente_validacao_controller":LoginValicaoController.as_view("loginvalidacao"),
    "home_user_route":"/home_user","home_user_controller":HomeUserController.as_view("homeuser"),
    "dados_user_route":"/dados_user/cliente/<int:id>","dados_user_controller":DadosController.as_view("dadosuser"),
    "pagina_deposito_route":"/pagina_deposito/<int:id>","pagina_deposito_controller":paginaDepositoController.as_view("paginadeposito"),
    "realizar_deposito_route":"/realizar_deposito/<int:id>","realizar_deposito_controller":realizarDepositoController.as_view("realizardeposito"),
    "pagina_saque_route":"/pagina_saque/cliente/<int:id>","pagina_saque_controller":paginaSaqueController.as_view("paginasaque"),
    "realizar_saque_route":"/realizar_saque/cliente/<int:id>","realizar_saque_controller":realizarSaqueController.as_view("realizarsaque"),
    "home_user_id_route":"/home_user/<int:id>","home_user_id_controller":HomeUserIDController.as_view("homeuserid"),
    "home_gerente_agencia_id_route":"/home_gerente_agencia/<int:id>","home_gerente_agencia_id_controller":HomeGerenteAgenciaController.as_view("homegaid"),
    "link_gerenciar_contas":"/link_gerenciar_contas/<int:id>","link_gerenciar_contas_controller":LinkGerenciarContasController.as_view("linkgcontas"),
    "aprovar_contas":"/aprovar_contas/<int:id>","aprovar_contas_controller":AprovacaoContaController.as_view("aprovacaodeconta"),
    "link_modo_gerente_contas":"/link_modo_gerente_contas/<int:id>","modo_gerente_contas_controller":ModoGerenteAgenciaController.as_view("modogerente"),
    "link_aprovacao_deposito":"/link_aprovacao_deposito/<int:id>","link_aprovacao_deposito_controller":LinkAprovacaoDepositoController.as_view("linkaprovacaodeposito"),
    "aprovacao_deposito":"/aprovacao_deposito/<int:id>","aprovacao_deposito_controller":ExecucaoDepositoController.as_view("aprovacaodeposito"),
    "link_extrato":"/link_extrato/<int:id>","link_extrato_controller":LinkExtratoController.as_view("linkextrato"),
    "gerar_extrato":"/gerar_extrato/<int:id>","gerar_extrato_controller":GerarExtratoController.as_view("gerarextrato"),
    "pagina_deposito_gerente_route":"/pagina_deposito_gerente/cliente/<int:id>","pagina_deposito_gerente_controller":paginaDepositoGerenteController.as_view("paginadepositogerente"),
    "realizar_deposito_gerente_route":"/realizar_gerente_deposito/cliente/<int:id>","realizar_deposito_gerente_controller":realizarDepositoGerenteController.as_view("realizardepositogerente"),
    "pagina_saque_gerente_route":"/pagina_gerente_saque/cliente/<int:id>","pagina_gerente_saque_controller":paginaSaqueGerenteController.as_view("paginasaquegerente"),
    "realizar_saque_gerente_route":"/realizar_saque_gerente/cliente/<int:id>","realizar_saque_gerente_controller":realizarSaqueGerenteController.as_view("realizarsaquegerente"),
}


