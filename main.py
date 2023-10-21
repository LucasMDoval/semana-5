from bankLibrary import account

imported_account = account("NG999999999", 0)

def menu_chatbot():
    print("Que quieres hacer con la cuenta?")
    print("1. Depositar dinero")
    print("2. Sacar dinero")
    opcion = input("Ingrese el número de la opción deseada: ")
    
    if opcion == "1":
        deposit_ask = float(input("¿Cuanto dinero quieres depositar en la cuenta?"))
        imported_account.deposit(deposit_ask)    
    
    elif opcion == "2":
        withdraw_ask = float(input("¿Cuanto dinero quieres sacar de la cuenta?"))
        if withdraw_ask > imported_account.get_balance():
            print ("No puedes sacar mas dinero del que tienes, inserte otra cantidad")
        else:
            imported_account.withdraw(withdraw_ask)

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

    print(f"Saldo actual de la cuenta: {imported_account.get_balance()}$")


print(f"La cuenta con IBAN {imported_account.get_number()} tiene un saldo de {imported_account.get_balance()}$")

menu_chatbot()


