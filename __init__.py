"""Easy and extensible brute force algorithms and utilities framework for Python

Please use responsibly, I, ex0dus, do not take responsibility for misuse or damages

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
__all__ = ['concurrent', 'linear', 'generator']

from .linear import Brute
from .concurrent import BrutePool
from .generator import TableGenerator, FileGenerator
