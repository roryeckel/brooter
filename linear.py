"""Linear, non-concurrent brute force algorithms

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

def Brute(cases, fn, stop_when_found=True, previous_result=None):
    keys = None if previous_result is None else previous_result.keys()
    for case in cases:
        if keys is None or case not in keys:
            res = fn(case)
            if (res is None or None in res) or (stop_when_found and res[1] is True):
                return res
            yield res
