#https://www.benavides.com.mx/cuidado-y-prevencion?gclid=CjwKCAiA_5WvBhBAEiwAZtCU7031DurGpWclcdVZGIv5KCcgYwQKCHlZZt0V4GDl8GuaLRTC3fQBnxoCa4wQAvD_BwE
#https://www.coppel.com
#https://www.walmart.com.mx/?utm_source=google&utm_medium=cpc&utm_advertiser=wmea_brand-kw&utm_campaign=&utm_term=walmart_e&utm_content=&gad_source=1&gclid=CjwKCAiA_5WvBhBAEiwAZtCU7xzrVvOPA8omshBkXmI53M3WfCOpsxg2X4UeqwNk4TkStoEdUaAuFRoCFXUQAvD_BwE
#https://www.soriana.com/?gad_source=1&gclid=CjwKCAiA_5WvBhBAEiwAZtCU78Ssp_4DBzLGwlZZXrPHiBQpjZRhD8eOebYpV-RzkaCGf7saKJji4xoCWQUQAvD_BwE
#https://www.sams.com.mx/?gad_source=1&gclid=CjwKCAiA_5WvBhBAEiwAZtCU71ubAV_LnmRQGUGB8nRJeUOz9pGWaNPvwmQhGknfYxSi0Z6drIrFOhoC_EgQAvD_BwE
from bs4 import BeautifulSoup
import requests

website = 'https://www.sams.com.mx/?gad_source=1&gclid=CjwKCAiA_5WvBhBAEiwAZtCU71ubAV_LnmRQGUGB8nRJeUOz9pGWaNPvwmQhGknfYxSi0Z6drIrFOhoC_EgQAvD_BwE'
results = requests.get(website)
content = results.text

soup = BeautifulSoup(content,'lxml')
print(soup.prettify())