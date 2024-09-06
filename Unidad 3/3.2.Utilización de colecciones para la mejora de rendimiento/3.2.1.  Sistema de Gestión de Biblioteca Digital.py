# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (autor, titulo)  # Tupla inmutable para autor y título
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.datos[1]}, Autor: {self.datos[0]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        self.libros_prestados = [libro for libro in self.libros_prestados if libro.isbn != isbn]

    def __str__(self):
        libros = ', '.join([libro.datos[1] for libro in self.libros_prestados]) or "No tiene libros prestados."
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {libros}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor
        self.ids_usuarios = set()  # Conjunto para asegurarse de que los IDs de usuario sean únicos

    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.datos[1]}' agregado correctamente.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} removido.")
        else:
            print(f"Libro con ISBN {isbn} no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print(f"El ID de usuario {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario {usuario.nombre} registrado correctamente.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} ha sido dado de baja.")
        else:
            print(f"Usuario con ID {id_usuario} no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return
        if isbn not in self.libros:
            print(f"Libro con ISBN {isbn} no disponible.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros[isbn]
        usuario.prestar_libro(libro)
        del self.libros[isbn]
        print(f"Libro '{libro.datos[1]}' prestado a {usuario.nombre}.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        libro_devuelto = next((libro for libro in usuario.libros_prestados if libro.isbn == isbn), None)
        if libro_devuelto:
            usuario.devolver_libro(isbn)
            self.libros[isbn] = libro_devuelto
            print(f"Libro '{libro_devuelto.datos[1]}' devuelto por {usuario.nombre}.")
        else:
            print(f"El usuario no tiene prestado el libro con ISBN {isbn}.")

    def buscar_libros(self, criterio, valor):
        encontrados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.datos[1].lower():
                encontrados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.datos[0].lower():
                encontrados.append(libro)
            elif criterio == "categoria" and valor.lower() == libro.categoria.lower():
                encontrados.append(libro)

        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros por {criterio}: {valor}.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print(f"El usuario {usuario.nombre} no tiene libros prestados.")


# Ejemplo de uso:
if __name__ == "__main__":
    # Crear la biblioteca
    biblioteca = Biblioteca()

    # Agregar libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "1234567890")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "0987654321")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario("Ana Pérez", 1)
    usuario2 = Usuario("Carlos López", 2)

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libro
    biblioteca.prestar_libro(1, "1234567890")

    # Listar libros prestados
    biblioteca.listar_libros_prestados(1)

    # Devolver libro
    biblioteca.devolver_libro(1, "1234567890")

    # Buscar libros
    biblioteca.buscar_libros("autor", "Cervantes")

