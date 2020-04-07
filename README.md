#Create vitrual env in the test dir
virtualenv test_env
#Virtualenv activate
test_env/Scripts/activate
#Install dependenciss
test_env/Scripts/pip.exe install -r requirements.txt

#Run testt with allure reporting
test_env/Scripts/py.test --alluredir=reports ./tests/test_dozorro.py
#when test compleated run to generate and open Allure report:
allure serve reports