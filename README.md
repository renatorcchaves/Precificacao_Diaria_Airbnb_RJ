# **Projeto Airbnb RJ** - Ferramenta para Previsão da Diária de um Imóvel

### Contexto

No Airbnb, qualquer pessoa que tenha um quarto ou um imóvel de qualquer tipo (apartamento, casa, chalé, pousada, etc.) pode ofertar o seu imóvel para ser alugado por diária.

Você cria o seu perfil de host (pessoa que disponibiliza um imóvel para aluguel por diária) e cria o anúncio do seu imóvel.

Nesse anúncio, o host deve descrever as características do imóvel da forma mais completa possível, de forma a ajudar os locadores/viajantes a escolherem o melhor imóvel para eles (e de forma a tornar o seu anúncio mais atrativo)

Existem dezenas de personalizações possíveis no seu anúncio, desde quantidade mínima de diária, preço, quantidade de quartos, até regras de cancelamento, taxa extra para hóspedes extras, exigência de verificação de identidade do locador, etc.

### Objetivo do Projeto

Construir um modelo de previsão de preço que permita uma pessoa comum que possui um imóvel possa saber quanto deve cobrar pela diária do seu imóvel.

Ou ainda, para o locador comum, dado o imóvel que ele está buscando, ajudar a saber se aquele imóvel está com preço atrativo (abaixo da média para imóveis com as mesmas características) ou não.

### Fonte dos dados

- As bases de dados foram retiradas do site kaggle: https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro
- As bases de dados são os preços dos imóveis obtidos e suas respectivas características em cada mês.
- Os preços são dados em reais (R$)
- Temos bases de abril de 2018 a maio de 2020, com exceção de junho de 2018 que não possui base de dados

### Ponderações Iniciais no Projeto

- Acredito que a sazonalidade pode ser um fator importante, visto que meses como dezembro costumam ser bem caros no RJ
- A localização do imóvel deve fazer muita diferença no preço, já que no Rio de Janeiro a localização pode mudar completamente as características do lugar (segurança, beleza natural, pontos turísticos)
- Adicionais/Comodidades/Número de hóspedes podem ter um impacto significativo, visto que temos muitos prédios e casas antigos no Rio de Janeiro

A ideia do projeto é entender como esses fatores impactam no preço da diária e se temos outros fatores não tão intuitivos que são extremamente importantes.

### Simulações para Previsão de Valor do Imóvel
- Por fim, será desenvolvido um modelo de machine learning que possa ser usado na plataforma Streamlit, onde iremos fornecer alguns dados de entrada a respeito do imóvel e com isso será feito a previsão do valor da diária de um imóvel do airbnb no Rio de Janeiro

### Ponderações Finais do Projeto

- Após a criação do modelo de machine learning, pode-se entender quais variáveis tem maior impacto no preço da diária do imóvel. Abaixo, temos o grau de importância percentual de cada feature na precificação da diária.

![Importância de cada feature](relatorios/Importancia%20cada%20feature%20para%20o%20Modelo%20Extra%20Trees.png)


