def mostrar_menu():
    print("Bienvenido a la caja registradora")
    print("1. Agregar producto")
    print("2. Mostrar total")
    print("3. Salir")
 def agregar_ producto(carrito):
     producto = input("Ingrese el nombre del producto: ")
     precio = float(input("Ingrese el nombre del producto"))
     carrito.append((producto, precio))
     print(f"{producto} agregado al carrito por ${precio:.2f}")
                    
 def mostrar_total(carrito):
     total = sum(item[1] for item in carrito)                 
     print(f"Total a pagar: ${total:.2f}")
    
 def main():
     carrito = []
     while True:
       mostrar_menu()
       opcion = input("Seleccione una opcion: ")
     
       if opcion == "1":
        agregar_producto(carrito)
       elif opcion == "2":
         mostrar_total( carrito)
       elif opcion == "3":
        print("gracias por usar la caja Registradora. ¡Hasta luego!")
        break
       else:
         print("Opcion invalida. Por favor, selecione una opcion valida") 
         
if_name_ == "_main_":
   main()   