import sys
import pandas as pd
from datetime import datetime

def solution(min_date='2020-02-01', max_date='2020-06-30', top= 3):
    # Import data
    sales_full = pd.read_csv('sales.csv',  parse_dates=['date'],index_col= ['date'])
    min_date = pd.to_datetime(min_date, format='%Y-%m-%d').date()
    max_date = pd.to_datetime(max_date, format='%Y-%m-%d').date()

    products = pd.read_csv('product.csv')
    products = products.rename(columns={'id': 'product_id', 'name': 'product_name'})

    store = pd.read_csv('store.csv')
    store = store.rename(columns={'id': 'store_id', 'name': 'store_name'})

    # Create a time window for wanted sales data
    max_date = str(max_date)
    min_date = str(min_date)
    sales = sales_full.loc[min_date:max_date]


    # Join tables
    sales = sales.reset_index().merge(store, left_on='store', right_on='store_id', how='left').set_index('date')
    sales = sales.reset_index().merge(products, left_on='product', right_on='product_id', how='left').set_index('date')



    # Create a list for wanted features
    wanted_features = ['product_name', 'store_name', 'brand', 'city']

    # Get ordered by quantity dictionaries for product, stores, brands and cities
    for feature in wanted_features:
        globals()['df_%s_' %feature] = sales.groupby(feature).sum().sort_values(by = ['quantity'], ascending=False)
        globals()['top_%s_dict' %feature] = globals()['df_%s_' %feature].to_dict()['quantity']
        print(' --top seller %s product --name quantity' % feature, end=' ')
        for i in list(globals()['top_%s_dict' %feature])[:top]:
            print(i, globals()['top_%s_dict' %feature][i], end= ' ')

        globals()['top_%s_to_return' % feature] = []

        for j in list(globals()['top_%s_to_return' % feature])[:top]:
            globals()['top_%s_to_return' % feature].append(str(str(j) + ' ' + str(globals()['top_%s_dict' %feature][i])))

if __name__ == '__main__':
    cmdargs = list(sys.argv)

    min_date_index = sys.argv.index('--min-date')
    max_date_index = sys.argv.index('--max-date')
    top_index = sys.argv.index('--top')

    arg_min_date = str(cmdargs[min_date_index+1])
    arg_max_date = str(cmdargs[max_date_index + 1])
    arg_top = int(cmdargs[top_index + 1])

    solution(min_date=arg_min_date, max_date=arg_max_date, top=arg_top)