# Data Science/Computer Vision problems

Nesse repositório, foram abordados quatro cenários com diferentes perspectivas de problemas da área de Ciência de Dados e Visão Computacional.

Os cenários abordados foram:

- CENÁRIO I: Análise de um conjunto de dados de compras: detecção de anomalias e investigações possíveis
- CENÁRIO II: Transformação de dados: json para DataFrame
- CENÁRIO III: Classificação de imagens com Machine Learning em dois grupos (dia e noite)
- CENÁRIO IV: Proposta de arquitetura para sistema de detecção do problema anterior.

O CENÁRIO I está disponível no notebook data_analysis.

O CENÁRIO II está disponível no arquivo data_ingestion.py.

O CENÁRIO III está disponível no notebook day-night.

Os arquivos disponíveis no diretório src foram utilizados para facilitar a análise do Cenário III.


## Setup information

Para a execução dos algoritmos, é sugerido a criação de um ambiente conda:

    ```conda create --name day-night python==3.8```

Instalação dos requirements:

    ```pip install -r requirements.txt```

Extração do conjunto de dados AMOS para a pasta raíz do projeto, bem como dos outros datasets utilizados neste projeto.
