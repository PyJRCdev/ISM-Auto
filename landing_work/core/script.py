from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Iniciar el navegador
def iniciar_navegador():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
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
