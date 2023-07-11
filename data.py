from faker import Faker
import pandas as pd
import numpy as np

class DataGenerator:
    def __init__(self, seed=0):
        self.fake = Faker()
        self.fake.seed_instance(seed)
        np.random.seed(seed)

    def generate_data(self, num_products=20, num_customers=100, num_purchases=1000):
        products = [f'Product {i}' for i in range(1, num_products + 1)]
        customers = [f'Customer {i}' for i in range(1, num_customers + 1)]
        stores = [self.fake.company() for _ in range(10)]

        data = {
            'Store': np.random.choice(stores, num_purchases),
            'Customer': np.random.choice(customers, num_purchases),
            'Product': np.random.choice(products, num_purchases),
            'Quantity': np.random.randint(1, 6, num_purchases),
            'Price': np.random.uniform(10.0, 100.0, num_purchases),
        }

        df = pd.DataFrame(data)
        df['Total'] = df['Quantity'] * df['Price']

        return df