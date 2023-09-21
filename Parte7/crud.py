from tortoise import Tortoise, run_async
from modelos import Item, Orden, Cliente, Sucursal, Categoria, Producto, Stock

async def crear_categoria():
    nombre = input('Ingrese el nombre de la categoria: ')
    categoria = Categoria(nombre = nombre)
    await categoria.save()

async def listar_categoria():
    categorias = await Categoria.all()
    for categoria in categorias:
        print(f"ID: {categoria.id} , Nombre: {categoria.nombre}")

async def obtener_categoria():
        id_categoria = int(input('Ingrese el ID de la categoria: '))
        categoria = await Categoria.get(id = id_categoria)
        print(f'ID : {categoria.id}, Nombre: {categoria.nombre}')
        print('----------------------------------------------------------------')

async def eliminar_categoria():
    id_categoria = int(input('Ingrese el ID de la categoria a eliminar: '))
    categoria = await Categoria.get(id = id_categoria)
    await categoria.delete()


DATABASE_URL = "postgres://postgres:postgres@localhost:5432/proyecto2"

async def main():
    await Tortoise.init(
        db_url=DATABASE_URL,
        modules={'models': ['__main__']}
    )
    
    while True:
        print('Seleccione una Tabla:')
        print('1. Categoria')
        print('2. Producto')
        print('3. Stock')
        print('4. Item')
        print('5. Orden')
        print('6. Cliente')
        print('7. Sucursal')
        print('q. Salir')
        
        choice = input('> ')
        
        if choice == 'q':
            break
        if choice == '1':
            print('Seleccione una accion:')
            print('1. Crear')
            print('2. Listar')
            print('3. Obtener')
            print('4. Eliminar')
        
            crud = input('> ')
            
            if crud == '1':
                await crear_categoria()
            elif crud == '2':
                await listar_categoria()
            elif crud == '3':
                await obtener_categoria()
            elif crud == '4':
                await eliminar_categoria()
        
if __name__ == "__main__":
    run_async(main())
