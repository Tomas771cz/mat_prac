=== Přihlášení ===
Admin již přítomný admin účet má následující přihlašovací údaje 
jméno: admin 
heslo: randompassword

=== Nahrání na web pomocí pythonanywhere ===
Založte si účet na pythonanywhere

Do bash konzole napište následující příkazy:
git clone https://github.com/Tomas771cz/mat_prac
mkvirtualenv --python=python3.10 mat_prac-virtualenv
pip install django
pip install pillow
cd /home/"název vašeho účtu"/mat_prac/mat_prac
python manage.py migrate

Poté běžte do sekce Web a tam v sekci code dejte tyto adresy
/home/"název vašeho účtu"/mat_prac/mat_prac
/home/"název vašeho účtu"/

Následně klikněte na odkaz u WSGI configuration, vymažte z něj vše a zkopírujte následující kód:
import os
import sys


path = '/home/"název vašeho účtu"/mat_prac/mat_prac/mat_prac'
if path not in sys.path:
     sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mat_prac/settings.py'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


V sekci Virtualenv zadejte:
/home/"název vašeho účtu"/.virtualenvs/mat_prac-virtualenv

V sekci static files zadejte:
/static/        /home/"název vašeho účtu"/mat_prac/mat_prac/static

Dále stačí jen na vršku stránky zmáčknout tlačítko reload a vše by mělo být připravené.


