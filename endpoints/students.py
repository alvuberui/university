from silence.decorators import endpoint

@endpoint(
    route="/students",
    method="GET",
    sql="SELECT * FROM Students",
    description="Obtiene todos los alumnos",
)
def get_all():
    pass

########################################################################

@endpoint(
    route="/students/$id",
    method="GET",
    sql="SELECT * FROM Students WHERE studentId = $id",
    description="Obtiene el estudaindo con identificador",
)
def get_by_id():
    pass

########################################################################

@endpoint(
    route="/students",
    method="POST",
    sql="INSERT INTO Students (accessMethod, dni,firstName, surname, birthDate, email) VALUES ($a, $d, $fn, $sn, $b, $e)",
    description="insertar un estudiante",
)
def get_by_id(a,d,fn,sn,b,e):
    pass

########################################################################

@endpoint(
    route="/students/$id",
    method="DELETE",
    sql="DELETE FROM Students WHERE StudentId = $id",
    description="Elimina el estudiante con identificador d",
)
def delete_by_id():
    pass

########################################################################

@endpoint(
    route="/students/$id",
    method="PUT",
    sql="UPDATE Students SET accessMethod=$a, dni=$d, firstName=$fn, surname=$sn, birthDate=$b, email=$e WHERE StudentId = $id",
    description="Modifica un estudiante"
)
def update_by_id(a,d,fn,sn,b,e):
    pass

