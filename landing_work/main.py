from gui.gui import crear_gui
from core.script import iniciar_navegador, login, abrir_pestanas
from tkinter import messagebox

driver = None

def iniciar_sesion(email, password):
    global driver
    if not email or not password:
        messagebox.showwarning("Advertencia", "Por favor, introduce tu email y contraseña")
        return
    
    driver = iniciar_navegador()

    try:
        login(driver, email, password)
        abrir_pestanas(driver)
        print("Todo ha sido abierto correctamente.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    crear_gui(iniciar_sesion)
