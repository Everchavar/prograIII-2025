import crud_academico

db = crud_academico.crud()

class crud_docentes:
    def consultar(self, buscar):
        sql = "SELECT * FROM docentes WHERE nombre LIKE %s"
        valores = (f"%{buscar}%",)
        return db.consultar(sql, valores)
    
    def administrar(self, datos):
        if datos['accion'] == "nuevo":
            sql = """
                INSERT INTO docentes (codigo, nombre, direccion, telefono, email, dui, escalafon)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            valores = (datos['codigo'], datos['nombre'], datos['direccion'], datos['telefono'], datos['email'], datos['dui'], datos['escalafon'])
        elif datos['accion'] == "modificar":
            sql = """
                UPDATE docentes SET codigo=%s, nombre=%s, direccion=%s, telefono=%s, email=%s, dui=%s, escalafon=%s
                WHERE idDocente=%s
            """
            valores = (datos['codigo'], datos['nombre'], datos['direccion'], datos['telefono'], datos['email'], datos['dui'], datos['escalafon'], datos['idDocente'])
        elif datos['accion'] == "eliminar":
            sql = "DELETE FROM docentes WHERE idDocente=%s"
            valores = (datos['idDocente'],)
        else:
            raise ValueError("Acción no reconocida")
        return db.ejecutar(sql, valores)