import pandas as pd
import yagmail

# import databae
# visualize the database
# earned by each store
# product quantity for each store
# average sell for each store
# send e-mail with reports

sales_table = pd.read_excel('Vendas.xlsx')

pd.set_option('display.max_columns', None)


# sales for each store
sum_sales_store = sales_table[['ID Loja','Valor Final']].groupby('ID Loja').sum()
#print(sum_sales_store)

#sales quantity per store
sales_per_store = sales_table[['ID Loja','Quantidade']].groupby('ID Loja').sum()
#print(sales_per_store)

#average ticket
average_ticket = (sum_sales_store['Valor Final'] / sales_per_store['Quantidade']).to_frame()
print(average_ticket)

# send report
yag = yagmail.SMTP("contato@biconnectgroup.com", "Luck762@")

yag.send(
    to="lucastavaresprojetos@gmail.com",
    subject="Análise de Vendas",
    contents="<h1>Olá! Segue o relatório.</h1>"
)

print("E-mail enviado!")