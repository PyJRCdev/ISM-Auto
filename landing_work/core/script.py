import platform
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_ruta_perfil_chrome():
    sistema = platform.system()
    ruta_perfil = ""

    if sistema == "Windows":
        ruta_perfil = os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'Google', 'Chrome', 'User Data')
    elif sistema == "Linux":
        ruta_perfil = os.path.join(os.getenv('HOME'), '.config', 'google-chrome')
    elif sistema == "Darwin":  # macOS
        ruta_perfil = os.path.join(os.getenv('HOME'), 'Library', 'Application Support', 'Google', 'Chrome')
    
    return ruta_perfil

# Iniciar el navegador
def iniciar_navegador():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    ruta_perfil_chrome = obtener_ruta_perfil_chrome()     # Obtener la ruta del perfil de Chrome
    if ruta_perfil_chrome and os.path.exists(ruta_perfil_chrome):
        chrome_options.add_argument(f"--user-data-dir={ruta_perfil_chrome}")
        print(f"Usando el perfil de Chrome en: {ruta_perfil_chrome}")
    else:
        print(f"No se encontró la ruta del perfil de Chrome: {ruta_perfil_chrome}. Usando perfil vacío.")
    
    # Eliminar el mensaje "Chrome controlado por software automatizado"
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

# Iniciar sesión en la página
def login(driver, email, password):
    driver.get('https://portal.ismgroup.es/App/Empleados/Inicio.aspx')
    time.sleep(2)
    
    email_field = driver.find_element(By.ID, 'tbUsuario')
    password_field = driver.find_element(By.ID, 'tbContrasena')
    
    email_field.send_keys(email)
    password_field.send_keys(password)
    
    login_button = driver.find_element(By.ID, 'bIniciarSesion')  
    login_button.click()        
    time.sleep(3)

# Abrir múltiples pestañas con los filtros
def abrir_pestanas(driver):
    filtros = ['SERGIO', 'Técnicos', 'UNICAJA', 'Sergio_proyectos']
    
    for filtro in filtros:
        matic_button = driver.find_element(By.ID, 'ContentPlaceHolder1_LinkButton1')
        matic_button.click()
        time.sleep(3)
        
        driver.switch_to.window(driver.window_handles[-1])

        try:
            if filtro == 'SERGIO':
                filtro_menu = Select(driver.find_element(By.ID, 'ContenidoPrincipal_ContenidoServicios_wucPanelFiltro_ddlZona'))
                filtro_menu.select_by_visible_text(filtro)
                time.sleep(1)
            
            elif filtro == 'Técnicos':
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ContenidoPrincipal_ContenidoServicios_wucPanelFiltro_ibTecnicos')))
                tecnico_boton = driver.find_element(By.ID, 'ContenidoPrincipal_ContenidoServicios_wucPanelFiltro_ibTecnicos')
                tecnico_boton.click()
            
            elif filtro == 'UNICAJA':
                filtro_menu = Select(driver.find_element(By.ID, 'ContenidoPrincipal_ContenidoServicios_wucPanelFiltro_ddlZona'))
                filtro_menu.select_by_visible_text(filtro)
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ContenidoPrincipal_ContenidoServicios_wucPanelFiltro_ibProyectos')))
                proyecto_boton = driver.find_element(By.ID, 'ContenidoPrincipal_ContenidoServicios_wucPanelFiltro_ibProyectos')
                proyecto_boton.click()

            elif filtro == 'Sergio_proyectos':
                menu_historico = driver.find_element(By.XPATH, "//a[@title='Histórico']")
                menu_historico.click()
                time.sleep(3)
                filtro_menu = Select(driver.find_element(By.ID, 'ContenidoPrincipal_ContenidoServicios_wucPanelFiltro_ddlZona'))
                filtro_menu.select_by_visible_text('SERGIO')
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ContenidoPrincipal_ContenidoServicios_wucPanelFiltro_ibProyectos')))
                proyecto_boton = driver.find_element(By.ID, 'ContenidoPrincipal_ContenidoServicios_wucPanelFiltro_ibProyectos')
                proyecto_boton.click()
            
            time.sleep(2)
        except Exception as e:
            print(f"Error al seleccionar el filtro {filtro}: {e}")
        
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)