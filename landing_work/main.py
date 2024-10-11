import threading
from gui.gui import crear_gui
from core.script import iniciar_navegador, login, abrir_pestanas
from tkinter import messagebox

driver = None

def iniciar_sesion(email, password,ventana):
    global driver
    if not email or not password:
        messagebox.showwarning("Advertencia", "Por favor, introduce tu email y contraseña")
        return
    
    driver = iniciar_navegador()

    def ejecutar_script():
        try:
            login(driver, email, password)
            abrir_pestanas(driver)
            print("Todo ha sido abierto correctamente.")
            ventana.destroy()
            
        except Exception as e:
            print(f"Ocurrió un error: {e}")
    thread = threading.Thread(target=ejecutar_script)
    thread.start()

if __name__ == "__main__":
    crear_gui(iniciar_sesion)
