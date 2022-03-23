from peewee import CharField, FloatField, IntegerField, Model, SqliteDatabase

DATABASE = './db/database.db'

database = SqliteDatabase(DATABASE)


class BaseModel(Model):
    class Meta:
        database = database


class Product(BaseModel):
    brand = CharField()
    model = CharField()
    processor = CharField()
    ram = IntegerField()
    screen_size = FloatField()
    price = FloatField()


def create_tables():
    with database:
        database.create_tables([Product])


def add_product(product_dict):
    with database:
        Product.create(
            brand=product_dict['brand'],
            model=product_dict['model'],
            processor=product_dict['processor'],
            ram=product_dict['ram'],
            screen_size=product_dict['screen_size'],
            price=product_dict['price'],
        )


def get_all_products():
    with database:
        return [
            {
                'brand': product.brand,
                'model': product.model,
                'processor': product.processor,
                'ram': product.ram,
                'screen_size': product.screen_size,
                'price': product.price,
            }
            for product in Product.select()
        ]


def delete_all_products():
    with database:
        Product.delete().execute()
