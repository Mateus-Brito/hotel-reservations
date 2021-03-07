# Reservas de Hotel

Endpoints:
- Escolher uma data e hora de check-in e check-out, o hotel que deseja se hospedar, o número do quarto ("/painel/reservas/novo/")
- Visualizar as reservas feitas pelo usuário ("/painel")
- Deletar uma reserva ("/painel/<uuid>/delete")
- Login do usuário. ("/accounts/login/")
- Cadastro do usuário. ("/accounts/signup/")
- Usuário esqueceu a senha. ("/accounts/password/reset/")
- Funcionalidades do Admin(já implementadas pelo django) ("/admin")


Estorias de usuário:
Sendo o usuário no qual deseja se hóspedar, eu desejo:

- Visualizar as datas de check-in e check-out
- Informar meus dados cadastrais e ficarem salvos
- Informar quantidade de hóspedes
- Informar quantos quartos
- marcar hospedagem
- cancelar hospedagem

Sendo o dono do estabelecimento, eu desejo:
- Os dados dos clientes (nome, email)
- visualizar os check-in e check-out dos hóspedes
- visualizar quais quartos o cliente selecionou

# Variáveis de ambiente

```
SECRET_KEY=YOUR_SECRET_KEY
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, .localhost
```
