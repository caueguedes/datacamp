import pandas as pd
# pd.[read_excel, read_json, read_html, read_pickle, read_sql, read_csv]

data = {'Sym': ['APPL', 'AMZN'],
        'Price': [105.00, 117.05],
        'Date': ['2015/12/31', '2015/12/31']}

data_list_dict =  [{'Sym': 'APPL', 'Price': 105.00, 'Date': '2015/12/31'},
              {'Sym': 'APPL', 'Price': 117.05, 'Date': '2017/12/01'}]

data_list = [['APPL', 105.00, '2015/12/31'],
             ['APPL', 117.05, '2017/12/01']]
columns = ['Sym', 'Price', 'Date']

df = pd.DataFrame(data)
row, column = '2015-12-31', 'Sym'
df.loc(row, column)
# axis=0 -> axis='rows'
# axis=1 -> axis='columns'

# pce = pcdg + pcndg + pcesv

pce['pcdg'] = pcdg # another df
pce['pcndg'] = pcndg
pce['pcsev'] = pcescv
pce['pce'] = pce['pcdg'] + pce['pcndg'] + pce['pcsev']
pce.drop(columns=['pcdg', 'pcndg'], axis=1, inplace=True)

pce.drop(['2015/12/31'], inplace=True)
