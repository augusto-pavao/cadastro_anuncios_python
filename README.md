# cadastro_anuncios_python
Tarefa de seleção para vaga

Sistema de Cadastro de Anúncios desenvolvido em Python 3.8
Módulos utilizados: ver arquivo 'requirements.txt'

1. Montagem do projeto

Este projeto foi desenvolvido com os seguintes pacotes:
Anacoda Spyder 4.1.5 (Python 3.8)
Mysql: mysql-installer-community-8.0.24.0

a) Instale se necessário os módulos utilizados (ver arquivo requirements.txt) com o comando pip install [módulo]

b) No diretório de seu projeto copie:
- os módulos cadastro_anuncios.py e calculadora_anuncios.py
- o arquivo parametros_reperc.xlxs (ajuste os parâmetros de repercussão)

2. Módulos do aplicativo

Este aplicativo é composto de dois módulos:
	- calculadora_anuncios.py
	- cadastro_anuncios.py

2.1 Módulo calculadora_anuncios

Este módulo recebe como entrada (argumento de sistema) o "valor total investido" em um anúncio e retorna as quantidades máximas de:
- visualizações
- cliques
- compartilhamentos 

que o anúncio poderá ter, armazenados no arquivo repercussao.txt, asalvo no mesmo diretório do projeto. 

No caso da importação deste módulo por outros módulos  deve ser chamada a função main() tendo como parâmetro o investimento toal, como exemplo:

import calcuadora_anuncios as calc

...

reperc = []

inv_total = 100

reperc = calc.main(inv_total)

...

O cálculo da repercussão é feito a partir de dados de análise de anúncios anteriores feito pela agência.
O arquivo parametros_reperc.xlxs contém esse dados, que podem ser então atualizados/modificados conforme o histórico da agência. 

2.1.1 Descrição dos parâmetros de repercussão:

- cota_vis: cota em reais que gera visualizações
- vis_by_cota: número de visualizações geradas por uma cota em reais

- cota_cliks: cota de visualizações que gera cliks
- cliks_by_cota: número de cliks gerados por uma cota de visualizações

- cota_comp: cota de cliks que gera compartilhamentos
- comp_by_cota: número de compartilhamentos gerados por uma cota de cliks

- cota_new_vis: cota de compartilhamentos que gera novas visualizações
- new_vis_by_cota: número de novas visualizações geradas por uma cota de compartilhamentos

- max_comp: número máximo de compartilhamentos (sequência)

OBS: somente quantidades interias de cotas são consisderadas, assim se 100 visualizações geram 12 cliques, 120 visualizações também geram 12 cliques, apeasn ao atingor 200 visualizações outros 12 cliques serão gerados.

2.1.2 Exemplo: Considere os seguintes dados da análise dos anúncios anteriores realizados pela agência, onde são determinados os parâmetros de repercussão:

- a cada 100 pessoas que visualizam o anúncio 12 clicam nele (cota_cliks = 100 e cliks_by_cota = 12).

- a cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais (cota_comp = 20 e comp_by_cota = 3).

- cada compartilhamento nas redes sociais gera 40 novas visualizações (cota_new_vis = 1 e new_vis_by_cota = 40.

- 30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido (cota_vis = 1 e vis_by_cota = 30).

- o mesmo anúncio é compartilhado no máximo 4 vezes em sequência [(1ª pessoa -> compartilha -> 2ª pessoa -> compartilha - > 3ª pessoa -> compartilha -> 4ª pessoa] (max_comp = 4).


2.2 Módulo cadastro_anuncios

Este módulo é um sistema simples de cadastro de anúncios que também permite gerar relatórios. 
A interface de usuário foi desenvolvida com o módulo tkinter e os dados são armazenados em um banco de dados mysql.
Para visualização do relatório é utilzado o browser.

Para o cadastro de um anúncios são necesários os seguintes campos:

- nome do anúncio
- cliente
- data de início
- data de término
- investimento diário

Ao ser efetuado o cadastro de um anúncio é executado o módulo calculadora_anuncios que retorna os seguintes valores:
- quantidade máxima de visualizações
- quantidade máxima de cliques
- quantidade máxima de compartilhamentos

Esses valores são agregados as dados de cadastro e formam um registro completo do anúncio que é inserido em um banco de dados mysql

Podem ser gerados relatórios a partir das seguintes definições (filtros), equivalentes aos campos na respectiva tela de relatório:
- cliente
- data inicial de pesquisa
- data final de pesquisa

O relatório retornará, portanto, todos os anúncios do cliente especificado que foram 'publicados' em intervalos contidos nas datas de pesquisa.

Campos do relatório:
- cliente
- nome do anúncio
- valor total investido
- quantidade máxima de visualizações
- quantidade máxima de cliques
- quantidade máxima de compartilhamentos

A visualização do relatório é feita no browser.


