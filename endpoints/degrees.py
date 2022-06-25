from silence.decorators import endpoint

@endpoint(
    route="/degrees",
    method="GET",
    sql="SELECT * FROM Degrees",
    description="Obtiene todos los grados",
)
def get_all():
    pass

########################################################################

@endpoint(
    route="/degrees/$id",
    method="GET",
    sql="SELECT * FROM degrees WHERE degreeId = $id",
    description="Obtiene el grado con identificador",
)
def get_by_id():
    pass

########################################################################

@endpoint(
    route="/degrees",
    method="POST",
    sql="INSERT INTO Degrees (name, years) VALUES ($n,$y)",
    description="insertar un grado con valores n,y",
)
def get_by_id(n,y):
    pass

########################################################################

@endpoint(
    route="/degrees/$degreeId",
    method="DELETE",
    sql="DELETE FROM Degrees WHERE degreeId = $degreeId",
    description="Elimina el grado con identificador d",
)
def delete_by_id():
    pass

########################################################################

@endpoint(
    route="/degrees/$id",
    method="PUT",
    sql="UPDATE Degrees SET name=$n, years=$y WHERE degreeId = $id",
    description="Modifica un grado con identificador id para que sus atributos name, year tengas los valores n,y"
)
def update_by_id(n, y):
    pass

