import crud_academico

db = crud_academico.crud()

class crud_materias:
    def consultar(self, buscar):
        sql = "SELECT * FROM materias WHERE nombre LIKE %s"
        valores = (f"%{buscar}%",)
        return db.consultar(sql, valores)
    
    def administrar(self, datos):
        if datos['accion'] == "nuevo":
            sql = """
                INSERT INTO materias (uv, nombre, docente)
                VALUES (%s, %s, %s)
            """
            valores = (datos['uv'], datos['nombre'], datos['docente'])
        elif datos['accion'] == "modificar":
            sql = """
                UPDATE materias SET uv=%s, nombre=%s, docente=%s
                WHERE idMateria=%s
            """
            valores = (datos['uv'], datos['nombre'], datos['docente'], datos['idMateria'])
        elif datos['accion'] == "eliminar":
            sql = "DELETE FROM materias WHERE idMateria=%s"
            valores = (datos['idMateria'],)
        else:
            raise ValueError("Acción no reconocida")
        return db.ejecutar(sql, valores)