# ...existing code...
cantidad_s = input("Introduce la cantidad de cifras: ").strip()
numero = input("Introduce el número con esas cifras: ").strip()

num_s = numero.lstrip('+-')
digitos = "0123456789"

if not cantidad_s.isdigit() or not num_s.isdigit():
    print("Entrada inválida.")
else:
    # convertir cantidad_s a entero sin usar int()
    cantidad = 0
    for ch in cantidad_s:
        cantidad = cantidad * 10 + digitos.find(ch)

    # contar cifras de num_s sin usar len()
    cuenta = 0
    for _ in num_s:
        cuenta += 1

    if cuenta != cantidad:
        print("Longitud incorrecta")
    else:
        producto = 1
        for c in num_s:
            producto = producto * digitos.find(c)

        # contar cifras pares en el producto usando métodos de string para iterar sus dígitos
        prod_s = str(producto)
        pares = 0
        for d in prod_s:
            if digitos.find(d) % 2 == 0:
                pares += 1

        print(f"Producto: {producto}")
        print(f"Cifras pares en el producto: {pares}")
# ...existing code...