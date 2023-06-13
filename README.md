# Sistema de Gestão de Propostas de Empréstimo Pessoal

Este é um desafio técnico para criar um sistema de gestão de propostas de empréstimo pessoal utilizando a seguinte stack:

- Django
- Django Rest Framework
- Django Celery

## Desafio

O objetivo deste desafio é criar um sistema onde os usuários possam cadastrar propostas de empréstimo pessoal e realizar sua avaliação através de uma fila RabbitMQ utilizando o Django Celery.

### Estrutura da Proposta

O administrador do sistema poderá cadastrar os campos que devem constar na proposta através do django-admin. Por exemplo, os seguintes campos podem ser cadastrados:

- Nome Completo
- CPF
- Endereço
- Valor do Empréstimo Pretendido

### Página de Preenchimento da Proposta

Deve ser criada uma página onde o possível cliente poderá preencher a proposta, utilizando os campos cadastrados anteriormente. É importante ressaltar que o frontend não deve fazer comunicação direta com o Django, toda a comunicação deve ser feita através do Django Rest Framework. O desenvolvedor pode utilizar um framework de sua preferência, como React, Vue, Angular, ou mesmo HTML com JS.

### Avaliação da Proposta

Após o preenchimento da proposta, a API deve registrar as informações no banco de dados e enviar a proposta para uma fila RabbitMQ. O Django Celery será responsável por avaliar a proposta, atribuindo um status de "Negada" ou "Aprovada". Para fins de teste, desenvolva um algoritmo onde metade das propostas serão negadas e metade serão aprovadas. Após a avaliação, o Django Celery deverá atualizar o status da proposta no banco de dados.

### Visualização no Admin

Dentro do Admin, será possível visualizar as propostas cadastradas juntamente com seus respectivos status, indicando se foram "Aprovadas" ou "Negadas".

## Requisitos da Entrega do Projeto

Para a entrega do projeto, certifique-se que tudo esteja em ambiente docker, preferencialmente, crie um docker-compose.yaml para que o projeto seja executado do modo mais simples possível, não se esqueça também dos seguintes detalhes

1. Crie um README com as orientações para executar seu projeto
2. Crie um usuário / senha padrão para o admin do sistema
3. Caso algo em seu código não esteja inteligível, por favor, comente o trecho, imagine que outras pessoas darão manutenção no sistema

## O que será avaliado no seu código
- Organização do código
- Separação de responsabilidades e manutenabilidade do sistema
- Bom funcionamento e performance

## O que *NÃO* será avaliado no seu código
- Layout do front-end
- CSS
- Habilidade com Javascript (conseguindo realizar as chamadas à API estará 'good enough')

## Prazo para entrega do desafio

Consideramos que o prazo ideal para entrega desse desafio é de 1 semana, mas caso precise de mais tempo, favor avisar através do e-mail code-challenge@digitalsys.com.br

## Como devo enviar o código feito?

Para enviar o desafio, por favor nos envie o link de seu github no e-mail code-challenge@digitalsys.com.br.

### Boa sorte =) 



