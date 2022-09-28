<h1 align="center"> 1º API - 🏦 Banco Octoplus  🐙  </h1>
<h2 align="center"> FATEC Profº Jessen Vidal, SJC - 1º Semestre DSM - 2022/2</h2>
<hr>
<p align="center">
 <a href="#sobre">Sobre</a> •
 <a href="#equipe">Equipe</a> • 
 <a href="#tecnologias">Tecnologias utilizadas</a> •
 <a href="#comousar">Como Utilizar</a> • 
 <a href="#demonstracao">Demonstração</a> • 
 <a href="#userstories">User Stories</a> • 
 <a href="#backlogS">Backlog da Sprint</a> •
 <a href="#burndown">Burndown da Sprint</a> •
</p>
<hr>

<h2 id="sobre"> :bookmark_tabs: Sobre o projeto </h2>
O tema a ser abordado neste API é o desenvolvimento de um sistema para um Internet Banking; monitorando e controlando operações bancárias e reduzindo a necessidade de interações presenciais.
<br>
<br>

> Baseado na Metodologia Scrum
<br>

_Projeto de um banco fictício, representado pelo Profº Fabrício Galende Marques de Carvalho._

<h2 id="equipe"> :man_technologist: Equipe :woman_technologist: </h2>

Integrantes da Equipe | Função | LinkedIn | Github |
:--------- | :------: | :-------: | :-------:
Gabriel B. Briscese | SM | [LinkedIn](https://www.linkedin.com/in/gabriel-brosig-briscese-344a5587) | [Github](https://github.com/Briscese)
Thiago F. Zani | PO | [LinkedIn](https://www.linkedin.com/in/thiago-zani-1b8503249) | [Github](https://github.com/zani19)   
Gabriela S. Barbosa | DT | [LinkedIn](https://www.linkedin.com/in/gabriela-barbosa-51a095195) | [Github](https://github.com/gabidsbarbosa)
Igor K. Sasaki | DT | [LinkedIn](https://www.linkedin.com/in/igor-kenzo-miyazaki-sasaki-4782b5249) | [Github](https://github.com/IgorKenzoMS)
Jean L. Faria | DT | [LinkedIn](https://www.linkedin.com/in/jean-faria-5a4b201b9/)| [Github](https://github.com/jeejinf)
Lucas F. Romero | DT | [LinkedIn](https://www.linkedin.com/in/lucas-romero-8b1b32240/) | [Github](https://github.com/LucasRomero2003)

<br> 

`SM - Scrum Master` | `PO - Product Owner` | `DT - Development Team`

<br>

<h2 id="tecnologias">💻 Tecnologias Utilizadas</h2>

![Tecnologias (700 × 400 px)](https://user-images.githubusercontent.com/111452998/190876489-eddd44d1-2326-4c3e-b815-3787abab4887.png)

<br>
<h2 id="userstories"> :mag: User Stories </h2>

<h4>Histórias para definir o escopo do projeto:</h4>

| Código (US) | Quem       | O que?                                                                                                                                                   | Para                                                |
| :----: | :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
|  #01   | Cliente | Eu, enquanto cliente, desejo solicitar abertura de uma ou mais contas (corrente ou poupança),                     | para poder realizar as minhas transações financeiras.
|  #02   | Cliente | Eu, enquanto cliente, desejo solicitar a exclusão de uma ou mais contas (corrente ou poupança),                     | para não ser mais cliente do banco. 
|  #03   | Cliente | Eu, enquanto cliente, desejo solicitar alterações dos meus dados cadastrais, | para corrigir dados desatualizados ou errados.
|  #04   | Cliente | Eu, enquanto cliente, desejo fazer um depósito em espécie no caixa eletrônico do banco, | para guardar o meu dinheiro no banco.
|  #05   | Cliente | Eu, enquanto cliente, desejo fazer um saque em espécie no caixa eletrônico do banco, | para retirar o meu dinheiro do banco.

<br>
<h2 id="comousar"> :wrench: Como utilizar </h2>

<h3>Possuir o Python 3.10+ na sua máquina</h3>
<h3>Abrir o CMD na pasta OctoplusBank e digitar:</h3>

```python
	python -m venv venv
```

```python
	venv\Scripts\Activate.ps1
```

<h3>Instalar os pré-requisitos digitando:</h3>

```python
	pip install -r requirements.txt
```

<h3>Importar o database chamado 'Banco' para o seu 'MySQL' utilizando o Dump</h3>

<h3>Fazer as alterações devidas (root/senha) no arquivo db.sql</h3>

<h3>Executar:</h3>

```python
	py main.py
```

<h3>Abrir o site em: 'http://localhost:4000/'</h3>

<br>
<h2 id="demonstracao"> 🎉 Demonstração do Programa </h2>
<br>
<h3> Sprint 01 </h3>

![gifSprint1](https://user-images.githubusercontent.com/111452998/191324088-233ba443-30fc-443a-93ec-c2ff57b2d3ac.gif)


<h2 id="backlogS">🗂️ Backlog das Sprints</h2>
<br>

`RF - Requisito Funcional` `RNF - Requisito Não Funcional`

<br>

 [![Generic badge](https://img.shields.io/badge/SPRINT%201-CONCLUÍDA-green)](https://shields.io/)

| Item do Backlog do Produto | Descrição                                                                      | User Story |
| :------------------------: | :----------------------------------------------------------------------------- | :--------: |
|  RNF U e P                 | Levantamento de Requisitos                             | #32, #36, #37-40, #43, #45 |
|  RF 3                      | Criação do primeiro modelo funcional, cadastro de cliente, conta e transções de saque e depósito. |#11-15 |

<br>
<hr>
<br>

 [![Generic badge](https://img.shields.io/badge/SPRINT%202-NÃO%20INICIADO-red)](https://shields.io/)

| Item do Backlog do Produto | Descrição                                                                      | User Story |
| :------------------------: | :----------------------------------------------------------------------------- | :--------: |
|           RF 01            | ----------------------------------------                                       |    #01     |
|           RF 3             | ----------------------------------------                                       |    #02     |
|           RF 02            | ----------------------------------------                                       |    #10     |
<br>
<hr>
<br>

 [![Generic badge](https://img.shields.io/badge/SPRINT%203-NÃO%20INICIADO-red)](https://shields.io/)

| Item do Backlog do Produto | Descrição                                                                      | User Story |
| :------------------------: | :----------------------------------------------------------------------------- | :--------: |
|           RF 01            | ----------------------------------------                                       |    #01     |
|           RNF 01           | ----------------------------------------                                       |    #02     |
|           RF 02            | ----------------------------------------                                       |    #10     |
<br>
<hr>
<br>

 [![Generic badge](https://img.shields.io/badge/SPRINT%204-NÃO%20INICIADO-red)](https://shields.io/)

| Item do Backlog do Produto | Descrição                                                                      | User Story |
| :------------------------: | :----------------------------------------------------------------------------- | :--------: |
|           RF 01            | ----------------------------------------                                       |    #01     |
|           RNF 01           | ----------------------------------------                                       |    #02     |
|           RF 02            | ----------------------------------------                                       |    #10     |
<br>
<br>

<br>
<h2 id="burndown">📉 Burndown das Sprints</h2>
<br>

<h3> Sprint 1: [29/08/22-18/09/22]</h3> 

![burndown1](https://user-images.githubusercontent.com/111452998/190554708-f6c5fb7b-270f-4eed-bac7-b8c628bbbf88.png)

<br>
<br>

<h3> Sprint 2: [19/09/22-09/10/22]</h3> 

<br>
<br>

<h3> Sprint 3: [13/10/22-06/11/22]</h3> 

<br>
<br>

<h3> Sprint 4: [07/11/22-27/11/22]</h3> 

<br>
<br>


