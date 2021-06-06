import pandas as pd
import code_3_9_1

class KivanoBot:
    help_text = '''
    /categories выдать названия всех категорий
    /categories {название категории} выдать товары этой категории
    /product {название продукта} выдать информацию о данном товаре
    '''
    __advertisement = pd.read_csv('kivano.csv')
    categories = set(__advertisement.category)
    categories.remove('category')
