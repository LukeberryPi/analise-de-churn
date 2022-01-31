import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import os

# importar a base de dados
df = pd.read_csv(
    r"C:\Users\lukef\Desktop\progprojects\Intensivão\aula2\telecom_users.csv")

# visualizar a base de dados
#     entender quais as informações disponíveis
#     descobrir as cagadas da base de dados
df = df.drop("Unnamed: 0", axis=1)
print(df)

# tratamento de dados
#     valores em formatação incorreta
df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors="coerce")

#     valores vazios
df = df.dropna(how="all", axis=1)
df = df.dropna(how="any", axis=0)
print(df.info())

# análise inicial
# como estão nossos cancelamentos
print(df["Churn"].value_counts())
print(df["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# análise completa
# comparar cada coluna da minha tabela com a tabela de cancelamentos

# criar a tabela (histograma)
# fazer download de cada tabela de comparação com o Churn (histograma)
if not os.path.exists("gráficos"):
    os.mkdir("gráficos")

for col in df.columns:
    graph = px.histogram(df, x=col, color="Churn")
    graph.write_image("gráficos/graph_" + col + "_vs_Churn.jpeg")

conclusions = open("conclusions.txt", "w")
conclusions.write("""
   Suas conclusões:
   - Clientes com contrato mensal tem MUITO mais chance de cancelar:
      - Podemos fazer promoções para o cliente ir para o contrato anual

   - Famílias maiores tendem a cancelar menos do que famílias menores:
      - Podemos fazer promoções para a pessoa pegar uma linha adicional 
      de telefone

   - MesesComoCliente baixos tem MUITO cancelamento, clientes com pouco
   tempo de casa:
      - A primeira experiência do cliente na operadora pode ser ruim
      - Talvez a captação de clientes tá trazendo clientes desqualificados

   - Quanto mais serviços o cliente tem, menos chance dele cancelar:
      - Podemos fazer promoções com mais serviços pro cliente

   - Tem alguma coisa no nosso serviço de Fibra que tá fazendo os clientes
   cancelarem:
      - Temos que agir sobre a Fibra

   - Clientes no boleto tem MUITO mais chance de cancelar, então temos que
   agir para eles irem para outras formas de pagamento.
""")
