from silence.decorators import endpoint

@endpoint(
    route="/groups",
    method="GET",
    sql="SELECT * FROM Groups",
    description="Obtiene todos los grupos",
)
def get_all():
    pass

########################################################################

@endpoint(
    route="/groups/$id",
    method="GET",
    sql="SELECT * FROM Groups WHERE groupId = $id",
    description="Obtiene asingatura con identificador",
)
def get_by_id():
    pass

########################################################################

@endpoint(
    route="/classrooms/$id/groups",
    method="GET",
    sql="SELECT * FROM Groups WHERE classroomId = $id",
    description="Obtiene los grupos que dan clases en el aula id",
)
def get_by_id():
    pass

########################################################################

@endpoint(
    route="/groups",
    method="POST",
    sql="INSERT INTO Groups (name, activity, year, subjectId, classroomId) VALUES ($n,$a,$y,$s,$c)",
    description="insertar un grupo",
)
def get_by_id(n,a,y,s,c):
    pass

########################################################################

@endpoint(
    route="/groups/$Id",
    method="DELETE",
    sql="DELETE FROM Groups WHERE groupId = $Id",
    description="Elimina el grupo a través de su id",
)
def delete_by_id():
    pass

########################################################################

@endpoint(
    route="/groups/$id",
    method="PUT",
    sql="UPDATE Groups SET name=$n, activity=$a, year=$y, subjectId=$s, classroomId=$ci WHERE groupId = $id",
    description="Modifica un grupo con identificador id"
)
def update_by_id(n,a,y,s,ci):
    pass