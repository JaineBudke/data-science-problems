# Data Science/Computer Vision problems

Nesse repositório, foram abordados quatro cenários com diferentes perspectivas de problemas da área de Ciência de Dados e Visão Computacional.

Os cenários abordados foram:

- I: Análise de um conjunto de dados de compras: detecção de anomalias e investigações possíveis (disponível no notebook data_analysis)
- II: Transformação de dados: json para DataFrame (disponível no arquivo data_ingestion.py)
- III: Classificação de imagens com Machine Learning em dois grupos: dia e noite (disponível no notebook day-night)
- IV: Proposta de arquitetura para sistema de detecção do problema anterior.

Os arquivos disponíveis no diretório src foram utilizados para facilitar a análise do Cenário III.

A proposta de arquitetura foi desenhada utilizando a ferramenta draw.io:

![alt text](https://github.com/jainebudke/data-science-problems/blob/main/arquitetura.png?raw=true)

O fluxo proposto segue:
- Utilizar um serviço de streaming para salvar as imagens processadas no Storage, assim como processar, extrair features e salvá-las em uma feature store;
- Treinar o algoritmo (utilizando as features extraídas) em uma máquina no VertexAI;
- Salvar modelo treinado no MLFlow, ferramenta de versionamento de modelos;
- Utilizar a Cloud Run para deploy do modelo, criando uma API para classificar novas imagens;
- Os resultados das predições podem ser salvos também no BigQuery, a fim de ter um histórico dos dados dos usuários e classificações;
- Por fim, uma ferramenta de visualização, como a Looker, pode ser utilizada para analisar os resultados.


## Setup information

Para a execução dos algoritmos, é sugerido a criação de um ambiente conda:

    ```conda create --name day-night python==3.8```

Instalação dos requirements:

    ```pip install -r requirements.txt```

Extração do conjunto de dados AMOS para o diretório data/ do projeto e os outros outros datasets para o diretório raíz do projeto.
