from typing import List

sentences = {
	'saudacoes': [
		'Olá ! Sou Janet Assistente deste grupo, qualquer coisa só me chamar',
		'Olá, eu sou a Janet qualquer coisa só chamar',
		'Oi !!!! Sou a Janet prazer em te conhecer, se precisar de algo me falar'
	],
	'quemsoueu': 'Eu sou Janet,'
	             ' a assistente desde grupo, '
	             'qualquer coisa que vocês precisarem podem me pedir, '
	             'oque eu não souber '
	             'ou fazer entre em contato com meu criador.'
	             'Para saber mais sobres meus comandos use $help.'
}

seuConvite = 'Seu convite está aqui:'

wait: List[str] = [
	'Um momento, vou pegar para você !',
	'Deixa ver se eu consigo achar...',
	'Aguarde por favor...',
	'Espere for favor !',
]

ambiguities = 'Ambiguações'
ambiguitiesDescriptions = 'Parece que eu encontrei mais de um tópico, ' \
                          'por favor especifique qual você quer'

help = {
	       'title':
		       {
			       'title': 'Help',
			       'description': 'use o comando .help <comando> para ter mais detalhes do comando que você quer.'
		       },
	       'commands': {
		       'name': 'Comandos',
		       'value': '- wiki\n- hello\n- pet\n- invite'
	       },
	       'wiki': {
		       'title': 'Wiki',
		       'description': 'Pesquisa algo ou alguma coisa na wikia.',
		       'name': '***Sintaxe***',
		       'value': '.wiki <oque_você_quer_pesquisar> \n .wiki sun \n.wiki Barack_Obama'
	       },
	       'pet': {
		       'title': 'Pet',
		       'description': 'Manda foto de um cachorro ou de um gato',
		       'name': '***Sintaxe***',
		       'value': '.invite <subcommando>\n .pet dogs \n .pet cats'
	       },
	       'invite': {
		       'title': 'Invite',
		       'description': 'Gera um convite para entrar na guild.',
		       'name': '***Sintaxe***',
		       'value': '.pet <max_uses> <unico> <publico>\n .invite 10 sim nao \n _.invite 1 no yes'
	       },
	       'greetings': {
		       'title': 'Greetings',
		       'description': 'Manda um oi para alguem, saudaçações e quem é Janet',
		       'fields': [
			       {
				       'name': '***Sintaxe***',
				       'value': '.hello <@user> \n .hello @fulanodetal'
			       },
			       {
				       'name': '***Sintaxe***',
				       'value': '.greeting'
			       }
		       ],
	       },
       },
