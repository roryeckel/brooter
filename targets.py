"""Basic brute force target templates (http basic authentication, etc.)

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

import requests

class BasicAuthTarget:
    """Basic authentication over HTTP for br00ter"""

    def __init__(self, url, session, username, reset_session=False):
        self.url = url
        self.session = session
        self._reset_session = reset_session
        self.username = username

    def test(self, combo):
        """Test a combo"""
        while True:
            try:
                print('Checking {}'.format(combo))
                print('Cookies: {}'.format(self.session.cookies))
                res = self.session.get(self.url, auth=(self.username, combo))
                print(res)
                succ = res.status_code == 200
                print(('Successful combo {}' if succ else '{} incorrect').format(combo))
                break
            except KeyboardInterrupt:
                return None, False
            except:
                print('{} checking {}, retrying'.format(e, combo))
        return combo, succ

class FormAuthTarget:
    """Form-based authentication over HTTP for br00ter"""

    def __init__(self):
        pass
