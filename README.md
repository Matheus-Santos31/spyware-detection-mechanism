# spyware-detection-mechanism

Repositório dedicado ao meu trabalho de conclusão de curso de Bacharelado em Sistemas de Informação - UFU

Na pasta src, se encontra a seguinte estrutura onde é possível observar em pastas separadas os desempenhos dos modelos no Baseline e o desempenho dos modelos Otimizados, e também alguns arquivos utilizados na preparação do dataset para o treinamento e validação dos modelos.

├── Baseline/
│ ├── BaseLine.ipynb # Notebook com os modelos de baseline
│ └── (Gráficos gerados pelo baseline)
│
├── OptimizedModels/
│ ├── OptimizedModels.ipynb # Notebook com os modelos após seleção de features
│ └── (Gráficos gerados pelos modelos otimizados)
│
├── Helpers/ # Scripts auxiliares de preparação do dataset
│ └── (Arquivos de definição do class_spy e caracter_spy)
│
├── Obfuscated-Malmem2022.csv # Dataset completo com todas as amostras e features
├── caracter_spy.csv # Subconjunto com 55 features apenas de spywares e amostras benignas
└── class_spy.csv # Gabarito das classes (spyware ou benigno)
