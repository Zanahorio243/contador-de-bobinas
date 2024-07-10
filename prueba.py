# Inicialización del inventario de bobinas
inventarioInicial = int(input("Introduce el número total de bobinas en el inventario al inicio del turno:"))
inventarioActual = inventarioInicial
bobinasBajadas = 0
bobinasSubidas = 0

# Registro de bobinas bajadas y subidas en cada hora del turno
for hora in range(1, 8):
    bobinasBajadasHora = int(input(f"Introduce el número de bobinas bajadas en la hora {hora}:"))
    bobinasSubidasHora = int(input(f"Introduce el número de bobinas subidas en la hora {hora}:"))
    bobinasBajadas += bobinasBajadasHora
    bobinasSubidas += bobinasSubidasHora
    inventarioActual = inventarioActual - bobinasBajadasHora + bobinasSubidasHora

# Verificación para asegurarse de que el inventario no sea negativo
if inventarioActual < 0:
    print("Error: Las bobinas bajadas exceden el inventario disponible.")
else:
    # Mostrar el resumen del turno
    print("Resumen del Turno:")
    print(f"Bobinas bajadas en el turno de 8 horas: {bobinasBajadas}")
    print(f"Bobinas subidas en el turno de 8 horas: {bobinasSubidas}")
    print(f"Bobinas restantes en el inventario: {inventarioActual}")

# Funcionalidades adicionales (debes implementar estas funciones)
def ControlCalidadProduccion():
    pass

def GestionInventarioAlmacen():
    pass

def PlanificacionTurnosEmpleados():
    pass