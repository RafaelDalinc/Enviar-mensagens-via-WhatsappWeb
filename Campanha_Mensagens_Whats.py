from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import openpyxl
from urllib.parse import quote

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(r'user-data-dir=C:\Users\r.carvalho\AppData\Local\Google\Chrome\User Data\Profile Selenium')
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

#carregando a planilha
try:       
    workbook = openpyxl.load_workbook('campanha.xlsx')
    pagina_pessoas = workbook['Planilha1']
except FileNotFoundError:
    print('arquivo não encontrado')
else:
    pass
#abrindo o whatsapp
driver.get('https://web.whatsapp.com/')
driver.maximize_window()

#Aguarda enquanto não tiver o sidebar montado na tela
while len(driver.find_elements('id','side')) < 1:
    sleep(1)
sleep(2)

#Loop para montar a mensagem de cada um e dispara o envio. 
for linha in pagina_pessoas.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    texto_campanha = linha[2].value
    mensagem = f'{nome},'
    mensagem += f'\n{texto_campanha}'
    link_mensagem = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
    driver.get(link_mensagem)  
    #Aguarda enquanto não tiver o id Main na página
    while len(driver.find_elements('id','main')) < 1:
        sleep(1)  
    sleep(2)  
    driver.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    sleep(2)
    print(f'Mensagem enviadas para {nome}')  
        
driver.close()
print('Mensagens enviadas com sucesso')


