import tkinter as tk

def calcular_precio_final():
    costo_producto = float(costo_producto_entry.get())
    precio_total_civa = float(precio_total_civa_entry.get())
    iibb = precio_total_civa * 0.05
    impuesto_cd = precio_total_civa * 0.006
    tci = precio_total_civa * 0.0106
    fondo_solidario = precio_total_civa * 0.014
    economia_local = precio_total_civa * 0.0175
    costo_empaquetado = 50
    sirtac = precio_total_civa * 0.017
    costo_financiero_tarjeta = precio_total_civa * 0.02
    costo_envio = 1200
    precio_total_sin_iva = precio_total_civa - iibb - impuesto_cd - tci - fondo_solidario - economia_local - costo_empaquetado - sirtac - costo_financiero_tarjeta - costo_envio
    precio_final = precio_total_sin_iva / 1.21
    margen = (precio_final - costo_producto) / precio_total_civa * 100

    # Actualizar etiquetas
    iibb_label.config(text="IIBB: {:.2f} ARS".format(iibb), font=("Arial", 11))
    impuesto_cd_label.config(text="Impuesto CD: {:.2f} ARS".format(impuesto_cd), font=("Arial", 11))
    tci_label.config(text="TCI: {:.2f} ARS".format(tci), font=("Arial", 11))
    fondo_solidario_label.config(text="Fondo Solidario: {:.2f} ARS".format(fondo_solidario), font=("Arial", 11))
    economia_local_label.config(text="Economía Local: {:.2f} ARS".format(economia_local), font=("Arial", 11))
    costo_empaquetado_label.config(text="Costo de Empaquetado: {:.2f} ARS".format(costo_empaquetado), font=("Arial", 11))
    sirtac_label.config(text="SIRTAC: {:.2f} ARS".format(sirtac), font=("Arial", 11))
    costo_financiero_tarjeta_label.config(text="Costo Financiero de Tarjeta: {:.2f} ARS".format(costo_financiero_tarjeta), font=("Arial", 11))
    costo_envio_label.config(text="Costo de Envío: {:.2f} ARS".format(costo_envio), font=("Arial", 11))
    precio_final_label.config(text="El Precio Final es: {:.2f} ARS".format(precio_final), font=("Arial", 16))
    margen_label.config(text="Margen de Ganancia: {:.2f}% ({:.2f} ARS)".format(margen, precio_final - costo_producto), font=("Arial", 16))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Precio Final")

# Crear los elementos de la interfaz
costo_producto_label = tk.Label(ventana, text="Costo del producto en ARS:", font=("Arial", 11))
costo_producto_label.grid(row=0, column=0, sticky="nsew")
costo_producto_label.place(relx=0.5,rely=0.5,anchor="center")
costo_producto_entry = tk.Entry(ventana, font=("Arial", 11))
costo_producto_entry.grid(row=0, column=1)
precio_total_civa_label = tk.Label(ventana, text="Precio total con IVA en ARS:", font=("Arial", 11))
precio_total_civa_label.grid(row=1, column=0, sticky="nsew")
precio_total_civa_entry = tk.Entry(ventana, font=("Arial", 11))
precio_total_civa_entry.grid(row=1, column=1)
iibb_label = tk.Label(ventana, text="", font=("Arial", 11))
iibb_label.grid(row=2, column=0, sticky="nsew")
impuesto_cd_label = tk.Label(ventana, text="", font=("Arial", 11))
impuesto_cd_label.grid(row=3, column=0, sticky="nsew")
tci_label = tk.Label(ventana, text="", font=("Arial", 11))
tci_label.grid(row=4, column=0, sticky="nsew")
fondo_solidario_label = tk.Label(ventana, text="", font=("Arial", 11))
fondo_solidario_label.grid(row=5, column=0, sticky="nsew")
economia_local_label = tk.Label(ventana, text="", font=("Arial", 11))
economia_local_label.grid(row=6, column=0, sticky="nsew")
costo_empaquetado_label = tk.Label(ventana, text="", font=("Arial", 11))
costo_empaquetado_label.grid(row=7, column=0, sticky="nsew")
sirtac_label = tk.Label(ventana, text="", font=("Arial", 11))
sirtac_label.grid(row=8, column=0, sticky="nsew")
costo_financiero_tarjeta_label = tk.Label(ventana, text="", font=("Arial", 11))
costo_financiero_tarjeta_label.grid(row=9,columnspan=2)
costo_envio_label = tk.Label(ventana,text="",font=("Arial", 11))
costo_envio_label.grid(row=10,columnspan=2)

calcular_btn = tk.Button(ventana,text="Calcular",font=("Arial",12),command=calcular_precio_final)
calcular_btn.grid(row=11,columnspan=2)

# Crear un nuevo marco con fondo gris
frame_final = tk.Frame(ventana,bg="gray")
frame_final.grid(row=12,columnspan=2)

# Agregar las etiquetas al marco
precio_final_label = tk.Label(frame_final,text="",font=("Arial",16),bg="gray")
precio_final_label.pack(padx=(5),pady=(5))
margen_label = tk.Label(frame_final,text="",font=("Arial",16),bg="gray")
margen_label.pack(padx=(5),pady=(5))

# Configurar el tamaño y posición de la ventana
ventana.geometry("500x600+200+50")

ventana.mainloop()