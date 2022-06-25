from silence.decorators import endpoint

@endpoint(
    route="/subjects",
    method="GET",
    sql="SELECT * FROM Subjects",
    description="Obtiene todos las asignaturas",
)
def get_all():
    pass

########################################################################

@endpoint(
    route="/subjects/$id",
    method="GET",
    sql="SELECT * FROM Subjects WHERE subjectId = $id",
    description="Obtiene asingatura con identificador",
)
def get_by_id():
    pass

########################################################################

@endpoint(
    route="/degrees/$id/subjects",
    method="GET",
    sql="SELECT * FROM Subjects WHERE degreeId = $id",
    description="Obtiene asingatura con identificador",
)
def get_by_id():
    pass

########################################################################

@endpoint(
    route="/subjects",
    method="POST",
    sql="INSERT INTO Subjects (name, acronym, credits, course, type, degreeId, departmentId) VALUES ($n,$a, $c, $co, $t, $d, $dp)",
    description="insertar una asignatura",
)
def get_by_id(n,a, c, co, t, d, dp):
    pass

########################################################################

@endpoint(
    route="/subjects/$Id",
    method="DELETE",
    sql="DELETE FROM Subjects WHERE subjectId = $Id",
    description="Elimina el grado con identificador d",
)
def delete_by_id():
    pass

########################################################################

@endpoint(
    route="/subjects/$id",
    method="PUT",
    sql="UPDATE Subjects SET name=$n, acronym=$a, credits=$c, course=$co, type=$t, degreeId=$d, departmentId=$dp WHERE subjectId = $id",
    description="Modifica un grado con identificador id para que sus atributos name, year tengas los valores n,y"
)
def update_by_id(n,a, c, co, t, d, dp):
    pass