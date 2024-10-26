from database_connection import ClearConsole,Login,Eliminar_Usuario,Listar_Personas,Buscar_usario_id,Buscar_Usuario_Correo

def Menu_Sesion():
    print("")
    print("============BIENVENIDO A LA TIENDA =========")
    print("=============================================")
    print("1. Iniciar Sesion ")
    print("2. Registarse ")
    print("3. Salir ")
    print("=============================================")

    try:
        opcion = int(input(" Que deseas hacer (1/3): ").strip())
    except:
        print("Has digitado algo incorrecto intenta de nuevo")
        result = False
    else:
        result = opcion

    if result == 1:
        ClearConsole()
        Verificación_Login()




def Verificación_Login():
    print("=============== DESEAS INICIAR SESION? ===========")
    print("==========================================")
    print("1. Iniciar sesion")
    print("2. Volver")
    print("==========================================")
    try:
        opcion = int(input("Digite la opcion que deseas (1/2) : ").strip())
    except:
        result = False
    else:
        result = opcion
    finally:
        if result == 1:
            ClearConsole()
            return Iniciar_Sesion()
        elif result == 2:
            ClearConsole()
            return Menu_Sesion()



def Iniciar_Sesion():
    print("================INICIA SESION============")
    print("=========================================")
    try:
        correo = input("Digite su correo electronico: ").strip().lower()
        contraseña = input("Digite su contraseña: ")
    except:
        result = False
    else:
        result = Login(correo,contraseña)
    finally:
        if result == False:
            ClearConsole()
            print("")
            print("HA OCURRIDO UN ERROR AL INCIAR SESION INTENTALO NUEVAMENTE")
            print("")
            Verificación_Login()
        elif result == ():
            ClearConsole()
            print("")
            print("=============================================")
            print("DATOS INCORRECTOS INTENTALO DE NUEVO")
            print("=============================================")
        else:
            if result[0] == "admin@gmail.com" and result[1] == "1234":
                return Admin_Sesion()

#MENU DE ADMINISTRADOR

def Admin_Sesion():
    print("=====================================")
    print("========BIENVENIDO ADMIN=============")
    print("======================================")
    print("1. Productos ")
    print("2. Usuarios ")
    print("3. Salir")
    print("======================================")
    try:
        opcion = int(input("Digite una opcion (1/3): ").strip())
    except:
        result = False
    else:
        result = opcion
    finally:
        if opcion == False:
            ClearConsole()
            print("OCURRIO UN ERROR INTENTALO DE NUEVO")
            return Admin_Sesion()
        elif opcion == 1:
            #Menu Productos
            pass
        elif opcion == 2:
            ClearConsole()
            return Usuario_Menu()
        elif opcion == 3:
            return Menu_Sesion()
        else:
            print("OPCION INCORRECTA INTENTALO DE NUEVO")



def Usuario_Menu():
    print("======================================")
    print("============USUARIOS================")
    print("=================================")
    print("1. Registrar un nuevo usuario ")
    print("2. Listar Usuarios ")
    print("4. Buscar Usuario por identificador ")
    print("5. Buscar Usuario por correo ")
    print("6. Eliminar un usuario ")
    print("7. Volver")
    print("=============Nota==============")
    print("Al elegirlo no se puede revertir")
    print("=================================")
    try:
        opcion = int(input("Que deseas hacer? ").strip())
    except:
        print("HA OCURRIDO UN ERROR INTENTALO DE NUEVO ")
        return Usuario_Menu()
    else:
        result = opcion
    finally:
        if result == 1:
            ClearConsole()
            pass
        elif result == 2:
            ClearConsole()
            return Listar_Usuarios()
        elif result == 3:
            ClearConsole()
            pass
        elif result == 4:
            pass
        elif result == 5:
            pass
        elif result == 6:
            ClearConsole()
            return Eliminar_Usuario()
        elif result == 7:
            ClearConsole()
            return Admin_Sesion()




def Eliminar_Usuario():
    print("======================================")
    print("============Eliminar Usuario================")
    print("=================================")
    try:
         id = int(input("Digite el id del usuario a eliminar: ").strip())
    except:
        ClearConsole()
        print("HA OCURRIDO UN ERROR INTENTALO DE NUEVO ")
        return Usuario_Menu()
    else:
        result = Eliminar_Usuario(id)
        if result == []:
            ClearConsole()
            print("Usuario no encontrado intentalo de nuevo")
            Usuario_Menu()
        elif result == False:
            ClearConsole()
            print("Ha ocurrido un error al eliminar usuario intentalo de nuevo ")
            Usuario_Menu()
        else:
            ClearConsole()
            print("EL USUARIO SE A ELIMINADO DE MANERA SATISFACTORIA")
            return Usuario_Menu()


def Listar_Usuarios():
    print("======================================")
    print("============Lista de Usuarios================")
    print("=================================")
    print(Listar_Personas())
    print("================================")
    print("Digite cualquier cosa para volver: ")
    opcion = input("").strip()
    ClearConsole()
    return Usuario_Menu()

