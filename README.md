Este projeto é uma mera tentativa de enviar mensagens de bom dia através do WhatsApp para uma lista de pessoas que estão contidas em uma planilha em excel.

Foram usadas as bibliotecas: Selenium Webdriver, time, openpyxl e urlib.

Observação: este código permite que seja enviadas mensagens sem que o whatsapp solicite a autenticação via QRCODE toda vez que requisitado, para isso foi criada uma pasta
no repositório do Chrome chamada Profile Selenium, vide abaixo:

    options.add_argument(r'user-data-dir=C:\Users\r.carvalho\AppData\Local\Google\Chrome\User Data\Profile Selenium')
