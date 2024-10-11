import tkinter as tk
import os
from core.remember_login import save_data, load_data

# Función para centrar la ventana
def centrar_ventana(ventana, ancho, alto):
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    
    x = (ancho_pantalla // 2) - (ancho // 2)
    y = (alto_pantalla // 2) - (alto // 2)
    
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Crear la ventana principal
def crear_gui(iniciar_sesion_func):
    ventana = tk.Tk()
    ventana.title("Portal")
    
    # Obtener la ruta del icono
    icono_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'ism.ico')
    ventana.iconbitmap(icono_path)  # Cambiar el icono de la ventana

    ancho_ventana = 420
    alto_ventana = 300
    centrar_ventana(ventana, ancho_ventana, alto_ventana)
    
    # Cargar credenciales almacenadas, si existen
    saved_data = load_data()

    # Frame principal
    frame = tk.Frame(ventana, bg="#ef7d00", padx=20, pady=20)
    frame.pack(expand=True, fill='both')

    email_label = tk.Label(frame, text="Email:", bg="#ef7d00", fg="#FFFFFF", font=("Arial", 12,"bold"))
    email_label.pack(pady=5)
    email_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    email_entry.pack(pady=5)
    
    password_label = tk.Label(frame, text="Contraseña:", bg="#ef7d00", fg="#FFFFFF", font=("Arial", 12,"bold"))
    password_label.pack(pady=5)
    password_entry = tk.Entry(frame, show="*", font=("Arial", 12), width=30)
    password_entry.pack(pady=5)

    recordar_var = tk.BooleanVar()
    recordar_check = tk.Checkbutton(frame, text="Recordar", variable=recordar_var, bg="#FFFFFF", font=("Arial", 12, "bold"))
    recordar_check.pack(pady=10)
    
    # Si hay datos guardados, rellenar los campos automáticamente
    if saved_data:
        email_entry.insert(0, saved_data.get("email", ""))
        password_entry.insert(0, saved_data.get("password", ""))
        recordar_var.set(True)  # Marcamos la casilla si ya se guardaron datos

    login_button = tk.Button(frame, text="Iniciar sesión", bg="#FFFFFF", font=("Arial", 12, "bold"), command=lambda: [save_data(email_entry.get(), password_entry.get(), recordar_var.get()), iniciar_sesion_func(email_entry.get(), password_entry.get(), ventana)])
    login_button.pack(pady=20)

    ventana.mainloop()
