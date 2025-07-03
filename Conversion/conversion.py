def menu_principal():
    print("Calculadora de Conversiónes de Unidades")
    print("1. Moneda")
    print("2. Masa")
    print("3. Volumen")
    print("4. Longitud")
    print("5. Almacenamiento")
    print("6. Tiempo")
    print("0. Salir")
    return input("Elige una opción y elije bien  : ")

def menu_moneda():
    print("\nuna moneda pal ciego:")
    print("1. USD a EUR")
    print("2. EUR a USD")
    print("3. MXN a USD")
    print("4. USD a MXN")
    print("5. EUR a MXN")
    return input(" Ojo al dato elige una nueva opción no seas imbecil : ")

def menu_masa():
    print("\nConversión de Masa gordas:")
    print("1. Kilogramos a Libras")
    print("2. Libras a Kilogramos")
    print("3. Gramos a Onzas")
    print("4. Onzas a Gramos")
    print("5. Toneladas a Kilogramos")
    return input(" Ojo al dato elige una nueva opción no seas imbecil : ")

def menu_volumen():
    print("\nConversión de Volumen de la musica xd:")
    print("1. Litros a Mililitros")
    print("2. Mililitros a Litros")
    print("3. Galones a Litros")
    print("4. Litros a Galones")
    print("5. Metros cúbicos a Litros")
    return input(" Ojo al dato elige una nueva opción no seas imbecil : ")

def menu_longitud():
    print("\nConversión de Longitud de un meteorito xd:")
    print("1. Metros a Pies")
    print("2. Pies a Metros")
    print("3. Kilómetros a Millas")
    print("4. Millas a Kilómetros")
    print("5. Centímetros a Pulgadas")
    return input(" Ojo al dato elige una nueva opción no seas imbecil : ")

def menu_almacenamiento():
    print("\nConversión de Almacenamiento dimensional xd:")
    print("1. Megabytes a Gigabytes")
    print("2. Gigabytes a Megabytes")
    print("3. Kilobytes a Megabytes")
    print("4. Megabytes a Kilobytes")
    print("5. Terabytes a Gigabytes")
    return input(" Ojo al dato elige una nueva opción no seas imbecil : ")

def menu_tiempo():
    print("\nConversión de Tiempo s0y yisus:")
    print("1. Horas a Minutos")
    print("2. Minutos a Segundos")
    print("3. Días a Horas")
    print("4. Semanas a Días")
    print("5. Años a Días")
    return input(" Ojo al dato elige una nueva opción no seas imbecil : ")

# Funciones de conversión
def usd_a_eur(cantidad): return cantidad * 0.92
def eur_a_usd(cantidad): return cantidad * 1.09
def mxn_a_usd(cantidad): return cantidad * 0.055
def usd_a_mxn(cantidad): return cantidad * 18.0
def eur_a_mxn(cantidad): return cantidad * 19.5

def kg_a_lb(cantidad): return cantidad * 2.20462
def lb_a_kg(cantidad): return cantidad * 0.453592
def g_a_oz(cantidad): return cantidad * 0.035274
def oz_a_g(cantidad): return cantidad * 28.3495
def ton_a_kg(cantidad): return cantidad * 1000

def l_a_ml(cantidad): return cantidad * 1000
def ml_a_l(cantidad): return cantidad / 1000
def gal_a_l(cantidad): return cantidad * 3.78541
def l_a_gal(cantidad): return cantidad / 3.78541
def m3_a_l(cantidad): return cantidad * 1000

def m_a_ft(cantidad): return cantidad * 3.28084
def ft_a_m(cantidad): return cantidad * 0.3048
def km_a_mi(cantidad): return cantidad * 0.621371
def mi_a_km(cantidad): return cantidad * 1.60934
def cm_a_in(cantidad): return cantidad * 0.393701

def mb_a_gb(cantidad): return cantidad / 1024
def gb_a_mb(cantidad): return cantidad * 1024
def kb_a_mb(cantidad): return cantidad / 1024
def mb_a_kb(cantidad): return cantidad * 1024
def tb_a_gb(cantidad): return cantidad * 1024

def h_a_min(cantidad): return cantidad * 60
def min_a_seg(cantidad): return cantidad * 60
def d_a_h(cantidad): return cantidad * 24
def sem_a_d(cantidad): return cantidad * 7
def anio_a_d(cantidad): return cantidad * 365

def ejecutar_conversion(categoria, opcion, cantidad):
    if categoria == "1":
        funciones = [usd_a_eur, eur_a_usd, mxn_a_usd, usd_a_mxn, eur_a_mxn]
    elif categoria == "2":
        funciones = [kg_a_lb, lb_a_kg, g_a_oz, oz_a_g, ton_a_kg]
    elif categoria == "3":
        funciones = [l_a_ml, ml_a_l, gal_a_l, l_a_gal, m3_a_l]
    elif categoria == "4":
        funciones = [m_a_ft, ft_a_m, km_a_mi, mi_a_km, cm_a_in]
    elif categoria == "5":
        funciones = [mb_a_gb, gb_a_mb, kb_a_mb, mb_a_kb, tb_a_gb]
    elif categoria == "6":
        funciones = [h_a_min, min_a_seg, d_a_h, sem_a_d, anio_a_d]
    else:
        return None
    return funciones[int(opcion)-1](cantidad)

def main():
    while True:
        categoria = menu_principal()
        if categoria == "0":
            print("¡Hasta luego insolente xd!")
            break
        if categoria == "1":
            opcion = menu_moneda()
        elif categoria == "2":
            opcion = menu_masa()
        elif categoria == "3":
            opcion = menu_volumen()
        elif categoria == "4":
            opcion = menu_longitud()
        elif categoria == "5":
            opcion = menu_almacenamiento()
        elif categoria == "6":
            opcion = menu_tiempo()
        else:
            print("Opción inválida elige uno bien pndjo.")
            continue
        try:
            cantidad = float(input("Introduce la cantidad a convertir: "))
            resultado = ejecutar_conversion(categoria, opcion, cantidad)
            print(f"Resultado: {resultado}\n")
        except Exception as e:
            print("Error en la conversión. Intenta de nuevo pndjo1.\n")

if __name__ == "__main__":
    main()