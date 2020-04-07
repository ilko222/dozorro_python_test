# Setup
Create vitrual env in the test dir
```bash
virtualenv test_env
```
Virtualenv activate
```bash
test_env/Scripts/activate
```
Install dependenciss
```bash
test_env/Scripts/pip.exe install -r requirements.txt
```
# GMAIL
You need to add your gmail credentials into the 
dozorro_python_test/Tests/user_credentials.py file.

# Run test with allure reporting
```bash
test_env/Scripts/py.test --alluredir=reports ./tests/test_dozorro.py
```
When test compleated run to generate and open Allure report:
```bash
allure serve reports
```