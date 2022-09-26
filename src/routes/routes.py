from src.controllers.controller import *
from src.controllers.erros import NotFoundController

routes ={
    "index_route":"/","indexcontroller":IndexController.as_view("index"),
    "not_found_route":404,"not_found_controller": NotFoundController.as_view("not_found"),
    "delete_route":"/delete/cliente/<int:id>","delete_controller":DeleteClienteController.as_view("delete"),
    "update_route":"/update/cliente/<int:id>","update_controller":UpdateClienteController.as_view("update"),
    "cadastro_route":"/cadastro_cliente","cadastro_cliente_controller":CadastroClienteController.as_view("cadastro"),
    "login_route":"/login_cliente","login_controller":LoginController.as_view("login"),
    "login_cliente_validacao_route":"/login_cliente_validacao","login_cliente_validacao_controller":LoginValicaoController.as_view("loginvalidacao"),
    "home_user_route":"/home_user","home_user_controller":HomeUserController.as_view("homeuser"),
    "dados_user_route":"/dados_user/cliente/<int:id>","dados_user_controller":DadosController.as_view("dadosuser"),
    "pagina_deposito_route":"/pagina_deposito/cliente/<int:id>","pagina_deposito_controller":paginaDepositoController.as_view("paginadeposito"),
    "realizar_deposito_route":"/realizar_deposito/cliente/<int:id>","realizar_deposito_controller":realizarDepositoController.as_view("realizardeposito"),
    "pagina_saque_route":"/pagina_saque/cliente/<int:id>","pagina_saque_controller":paginaSaqueController.as_view("paginasaque"),
    "realizar_saque_route":"/realizar_saque/cliente/<int:id>","realizar_saque_controller":realizarSaqueController.as_view("realizarsaque"),

     "home_user_id_route":"/home_user/<int:id>","home_user_id_controller":HomeUserIDController.as_view("homeuserid"),

}


