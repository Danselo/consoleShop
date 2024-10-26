from database_connection import ClearConsole,Login

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
            pass

#MENU DE ADMINISTRADOR

def Admin_Sesion():
    print("=====================================")
    print("========BIENVENIDO ADMIN=============")
    print("======================================")
    print("1. Registrar Producto ")
    print("2. Imprimir ")




