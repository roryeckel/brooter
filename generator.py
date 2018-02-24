"""Generation and filtering for br00ter

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

from itertools import chain, product, islice

def TableGenerator(charset, minlength, maxlength):
    """Return a generator containing all combinations of a charset"""
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(minlength, maxlength + 1)))

def resume_filter(table, at):
    """Iterate a generator until value == at to filter previously attempted combos"""
    while next(table) != at:
        pass
