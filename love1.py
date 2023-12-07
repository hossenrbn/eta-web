from selenium import webdriver
from selenium.webdriver.firefox.options import Options 
from time import sleep

driver=webdriver.Firefox()
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

def add_contact()     
    bog=[]# لیتی از افراد که به هر دلیلی نرم افزار اونارو باگ کرده
    havent=[] #لیستی که ایتا نداشتن 
    try:
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[1]').click()
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[3]/div[3]').click()
    except:
        error()
        
    #adding phone number to eitaa 
    for number in dr['تلفن'][i:]:
        try:
            sleep(3)
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div[2]/button/div').click()
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[1]/div[1]').send_keys(str(dr['نام'][i]+' '+dr['نام خانوادگی'][i]))#name of contact
            driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/div[1]').send_keys(int(number))#number of contact
            driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/button/div').click()
            sleep(4)
        except:
            continue
            bog.append(number)
            
        # -----------------   در صورت نداشتن ایتا به شخص بعدی رجوع میکند    -----------------------
        try:
            driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/span').click()
            havent.append(number)

        except:
            pass
        i+=1
        print(i)
return print(bog,havent)
        
def send_massage(): 
    bog=[]
    for a in dr['name'] :
        phone=dr['تلفن همراه'][i]
        w=int(phone)
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
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/div[4]/div/div[1]/div[7]/div[1]/div[1]').send_keys('this name is'+str(a)+'text for sending to evreone ')
            sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/div/div[4]/div/div[4]/button/div').click()
            sleep(3)
            i+=1
        except:
            continue
            bog.append(w)

    
enter()
