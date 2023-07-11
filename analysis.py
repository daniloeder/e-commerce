class Analyzer:
    def __init__(self, df):
        self.df = df

    def summary(self):
        return self.df.describe()

    def top_selling_products(self):
        return self.df.groupby('Product')['Total'].sum().sort_values(ascending=False)

    def top_stores(self):
        return self.df.groupby('Store')['Total'].sum().sort_values(ascending=False)

    def customer_spending(self, customer_id):
        return self.df[self.df['Customer'] == customer_id]['Total'].sum()

    def sales_by_product(self, product_id):
        return self.df[self.df['Product'] == product_id]['Total'].sum()
