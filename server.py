from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import parse
from urllib.parse import urlparse, parse_qs
import json 
import crud_alumno
import crud_docentes
import crud_materias

port = 3000

crudAlumno = crud_alumno.crud_alumno()
crudDocente = crud_docentes.crud_docentes()
crudMateria = crud_materias.crud_materias()

def do_GET(self):
    print(f"=== GET: {self.path} ===")  # ← Agrega esto
    url_parseada = urlparse(self.path)
    path = url_parseada.path
    parametros = parse_qs(url_parseada.query)

class miServidor(SimpleHTTPRequestHandler):
    def do_GET(self):
        url_parseada = urlparse(self.path)
        path = url_parseada.path
        parametros = parse_qs(url_parseada.query)

        if self.path=="/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return
        if self.path == "/":
            self.path = "index.html"
            return SimpleHTTPRequestHandler.do_GET(self)
        if self.path == "/alumnos":
            alumnos = crudAlumno.consultar("")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(alumnos).encode('utf-8'))
        if self.path == "/docentes":
            docentes = crudDocente.consultar("")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(docentes).encode('utf-8'))
        if self.path == "/materias":
            materias = crudMateria.consultar("")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(materias).encode('utf-8'))
        if path == "/vistas":
            self.path = '/modulos/'+ parametros['form'][0] +'.html'
            return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        longitud = int(self.headers['Content-Length'])
        datos = self.rfile.read(longitud)
        datos = datos.decode("utf-8")
        datos = parse.unquote(datos)
        datos = json.loads(datos)
        resp = {}
        if self.path == "/alumnos":
            resp = {"msg": crudAlumno.administrar(datos)}
        elif self.path == "/docentes":
            resp = {"msg": crudDocente.administrar(datos)}
        elif self.path == "/materias":
            resp = {"msg": crudMateria.administrar(datos)}
        else:
            resp = {"msg": "Ruta no soportada"}
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(resp).encode("utf-8"))

print("Servidor ejecutandose en el puerto", port)
server = HTTPServer(("localhost", port), miServidor)
server.serve_forever()