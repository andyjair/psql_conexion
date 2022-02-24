from conexion import conexion


@conexion
def select_persona(cur):
    SQL = 'select * from persona'
    cur.execute(SQL)
    datos = cur.fetchall()
    return datos


@conexion
def select_estudiante(cur):
    SQL = 'select * from estudiante'
    cur.execute(SQL)
    datos = cur.fetchall()
    return datos


if __name__ == '__main__':
    print(select_persona())
    print(select_estudiante())
