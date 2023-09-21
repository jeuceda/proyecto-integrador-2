from tortoise import fields, models, Tortoise, run_async

class Categoria(models.Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length = 255)
    productos = fields.ReverseRelation['Producto']
    
class Producto(models.Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length = 255)
    marca = fields.CharField(max_length = 255)
    categoria_id = fields.ForeignKeyField('models.Categoria', related_name='productos')
    precio_unitario = fields.FloatField()
    items = fields.ReverseRelation['Item']
    stocks = fields.ReverseRelation['Stock']

class Stock(models.Model):
    id = fields.IntField(pk=True)
    sucursal_id = fields.ForeignKeyField('models.Sucursal', related_name='stocks')
    producto_id = fields.ForeignKeyField('models.Producto', related_name = 'stocks')
    cantidad = fields.IntField()
    

class Item(models.Model):
    id = fields.IntField(pk=True)
    orden_id = fields.ForeignKeyField('models.Orden', related_name='items')
    producto_id = fields.ForeignKeyField('models.Producto',related_name='items')
    cantidad = fields.IntField()
    monto_venta = fields.FloatField()

class Orden(models.Model):
    id = fields.IntField(pk=True)
    cliente = fields.ForeignKeyField('models.Cliente', related_name='ordenes')
    sucursal = fields.ForeignKeyField('models.Sucursal', related_name='ordenes')
    fecha = fields.DateField()
    total = fields.FloatField()
    items = fields.ReverseRelation['Item']

class Sucursal(models.Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=255)
    direccion = fields.CharField(max_length=255)
    stocks = fields.ReverseRelation["Stock"]
    ordenes = fields.ReverseRelation["Orden"]

class Cliente(models.Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=255)
    telefono = fields.CharField(max_length=255)
    ordenes = fields.ReverseRelation["Orden"]
    
