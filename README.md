# Data Science/Computer Vision problems

Nesse repositório, foram abordados quatro cenários com diferentes perspectivas de problemas da área de Ciência de Dados e Visão Computacional.

Os cenários abordados foram:

- I: Análise de um conjunto de dados de compras: detecção de anomalias e investigações possíveis (disponível no notebook data_analysis)
- II: Transformação de dados: json para DataFrame (disponível no arquivo data_ingestion.py)
- III: Classificação de imagens com Machine Learning em dois grupos: dia e noite (disponível no notebook day-night)
- IV: Proposta de arquitetura para sistema de detecção do problema anterior.

Os arquivos disponíveis no diretório src foram utilizados para facilitar a análise do Cenário III.

A proposta de arquitetura foi desenhada utilizando a ferramenta draw.io e está disponível no arquivo arquitetura.png.

## Setup information

Para a execução dos algoritmos, é sugerido a criação de um ambiente conda:

    ```conda create --name day-night python==3.8```

Instalação dos requirements:

    ```pip install -r requirements.txt```

Extração do conjunto de dados AMOS para o diretório data/ do projeto e os outros outros datasets para o diretório raíz do projeto.
