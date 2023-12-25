'''
import pandas as pd
dr=pd.read_excel('011.xlsx')
i=0
'''

from selenium import webdriver
from selenium.webdriver.firefox.options import Options 
from time import sleep
options = Options() 
options.add_argument("-headless")

driver=webdriver.Firefox(options=options)
driver.get('https://web.eitaa.com/')
sleep(5)
#تایع بازگشت به اول 
def error():
    driver.refresh()
    enter()
def enter():      
    #دریافت شماره تلفن از کاربر 

    phon_number=int(input('شماره رو بده بیاد '))
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]').send_keys(phon_number)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[3]/button/div").click()

        #دریافت کد تایید ورود به ایتا
    try:
        rejester=int(input('enter the key'))
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div[3]/div/input').send_keys(rejester)
        sleep(7)
    except:
        error()
        print('shomare eshtebah vared shode lotfan dobare say konid')

def add_contact(i):
    bog=[]# لیتی از افراد که به هر دلیلی نرم افزار اونارو باگ کرده
    havent=[] #لیستی که ایتا نداشتن 
    try:
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[1]').click()
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[3]/div[3]').click()
    except:
        try:
            sleep(10)
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[1]').click()
            sleep(3)
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[3]/div[3]').click()
        except:
            error()

        
    #adding phone number to eitaa 
    for number in dr['تلفن همراه'][i:]:
        if str(number)=='nan' :
            i+=1
            continue
        else:
            try:
                driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/span').click()
                havent.append(number)

            except:
                pass

            try:
                sleep(3)
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div[2]/button/div').click()
                sleep(2)
                driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[1]/div[1]').send_keys(str(dr['نام'][i]+' '+dr['نام خانوادگي'][i]))#name of contact
                driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/div[1]').send_keys(int(number))#number of contact
                driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/button/div').click()
                sleep(4)
            except:
                try:
                    sleep(10)
                    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div[2]/button/div').click()
                    sleep(2)
                    driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[1]/div[1]').send_keys(str(dr['نام'][i]+' '+dr['نام خانوادگي'][i]))#name of contact
                    driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/div[1]').send_keys(int(number))#number of contact
                    driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/button/div').click()
                    sleep(4)
                except:
                    try:
                        driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/span').click()
                        havent.append(number)
                        
                    except:
                        print('bog')
                        bog.append(number)
                        i+=1
                        continue
            # -----------------   در صورت نداشتن ایتا به شخص بعدی رجوع میکند    -----------------------
            try:
                driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/span').click()
                havent.append(number)

            except:
                pass
            i+=1
            print(i)
    driver. close()
    return print('boged',bog,'havnat=',havent)
        
def send_massage(i): 

    bog=[]
    for a in dr['شماره دانشجو'] :
        if str(a)=='nan' :
            i+=1
            continue
        else:
            phone=dr['تلفن همراه'][i]
            w=int(phone)
            z=dr['نام'][i]+' '+dr['نام خانوادگي'][i]
            text_to_send=f'''
    🔷اطلاعیه آموزشی 🔷
    جناب  {z} دانشجوی محترم دکترای گروه حقوق بین الملل
    سلام علیکم 
    امتحان آزمون جامع گروه حقوق بین الملل در تاریخ 26/10/402 برگزار خواهد شد.
    در صورت نیاز به راهنمائی به  آی دی ایتا : 
    @lawFaculty
    یا با شماره 02532103624 تماس حاصل فرمائید 
    با تشکر و تقدیم احترام 
    آموزش دانشکده حقوق
    '''
            try:
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[1]').click()
            except:
                error()
                send_massage()
            try:    
                sleep(3)
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[3]/div[3]').click()
                sleep(3)
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/input').send_keys('+'+str(98)+str(w))
                sleep(3)


                try:
                    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[2]/ul/li/div[1]').click()
                except:
                    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div[1]/button').click()
                    i+=1
                    continue  
                sleep(3)
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/div[4]/div/div[1]/div[7]/div[1]/div[1]').send_keys(text_to_send)
                sleep(2)
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/div[4]/div/div[4]/button/div').click()
                sleep(3)
                i+=1
            except:
                continue
                bog.append(w)

            print(i)
    driver. close()
    return print(bog)
    
enter()
add_contact(i)
