"""Automatic webapp vulnerability detection

/:-:/.           `-----`          ./:-:/
-/   o`      -+//::----//+o-    ``o   /-
+.    --::--o:            `/o::---    .+
::-:-::.``.d`  E x 0 d u S -y``-:-----:
       `--+s`-             :`m--`       
          -h:`.    ` `   `..:h`         
          //`smso:.oo+.:+hNo`s:         
         `-s +dsNmshohsmhhd/ y-         
   ....-:-+o  `..`-mNm-`..`  o+:--..-`  
  /-`````-/o+:/y  .s-s`  s+:/+:. ````o  
  -:--  +`    :h//-/:/-++h/   `o  `:-/  
     ::-+      +/:m/N/d/:o     ::-+`    
                /h.` `.h+"""
__author__ = 'ex0dus'
__version__ = '1.0'

from bs4 import BeautifulSoup
import requests

COMMON_FORM_IDENTIFIERS = ('login', 'name', 'mail', 'password', 'user', 'pass')

def _in(data1, data2):
    if isinstance(data1, str):
        data1 = data1.lower()
    if isinstance(data2, str):
        data2 = data2.lower()
    for d in data2:
        if d in data1:
            return True
    return False

class Form():
    """Contains information about an HTML login form"""

    INPUT_USER = 'username'
    INPUT_PASSWORD = 'password'
    INPUT_ARBITRARY = 'data'
    INPUT_HIDDEN = 'hidden'

    def __init__(self, url, html):
        self.url = url
        self.html = html
        self.inputs = dict()
        form_children = self.html.findAll('input')
        for child in form_children:
            if child.has_attr('type'):
                input_type = child['type'].lower()
                if input_type == 'password':
                    self.inputs[child] = self.INPUT_PASSWORD
                elif input_type == 'text':
                    if child.has_attr('value'):
                        self.inputs[child] = self.INPUT_ARBITRARY
                    else:
                        self.inputs[child] = self.INPUT_USER
                elif input_type == 'hidden':
                    self.inputs[child] = self.INPUT_HIDDEN

    def generate_data(self, login, password, use_hidden=True):
        """Generate a data dict to be used for requests"""
        data = dict()
        for input_html, input_type in self.inputs.items():
            if input_type == self.INPUT_USER:
                data[input_html['name']] = login
            elif input_type == self.INPUT_PASSWORD:
                data[input_html['name']] = password
            elif input_type == self.INPUT_ARBITRARY or (use_hidden and input_type == self.INPUT_HIDDEN):
                data[input_html['name']] = input_html['value']
        return data

    def __str__(self):
        return str(self.inputs)

    def __repr__(self):
        return str(self)

def scan_forms(url):
    text = requests.get(url).text
    html = BeautifulSoup(text, 'html.parser')
    forms = list()
    for form in html.findAll('form'):
        form_children = form.findAll('input')
        for child in form_children:
            if child.has_attr('name') and _in(child['name'], COMMON_FORM_IDENTIFIERS):
                forms.append(form)
                break
    return [Form(url, f) for f in forms]
