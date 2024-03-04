## Setup
```
  $ python -m virtualenv venv
  $ venv/Scripts/activate
  $ pip install -r requirements.txt
  $ python main.py
```
**Update the .env file**

### Setup arduino
    Open Arduino Uno
    Tools > Manage Libraries
    Search "firmata"
    Install 2.5.9

    Upload StandardFirmata.ino


## Creating speech service on azure portal
Create speech service by clicking on the link:
https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/SpeechServices

To get the API key, go to the `Microsoft Azure Portal Resources <https://portal.azure.com/>`__ page, go to "All Resources" > "Add" > "See All" > Search "Speech > "Create", and fill in the form to make a "Speech" resource. On the resulting page (which is also accessible from the "All Resources" page in the Azure Portal), go to the "Show Access Keys" page, which will have two API keys, either of which can be used for the `key` parameter. Microsoft Azure Speech API keys are 32-character lowercase hexadecimal strings.