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
import os

def _not_equals(one, two):
    """one != two"""
    return one != two

def _true(item):
    return True

def generator_length(gen):
    """Return the length of the iterable, otherwise sum(1 for _ in generator)"""
    try:
        return len(gen)
    except TypeError:
        return sum(1 for _ in gen)

def resume_filter(gen, at, exp=_not_equals):
    """Iterate a generator until value == at to filter previously attempted combos"""
    while exp(next(gen), at):
        pass

def skip_generator(gen, count):
    """Skip count items in a generator"""
    for i in range(count):
        next(gen)

class TableGenerator:
    """Brute force table combination generator"""
    
    def _generator(self):
        return (''.join(candidate)
                          for candidate in chain.from_iterable(product(self.charset, repeat=i)
                          for i in range(self.minlength, self.maxlength + 1)))
                
    def __init__(self, charset, minlength, maxlength, filter_check=_true):
        """Initialize the generator"""
        self.charset = charset
        self.minlength = minlength
        self.maxlength = maxlength
        self.filter_check = filter_check
        self.reset()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.reset()

    def reset(self):
        """Reset the generator to the first combination"""
        self._iterator = self._generator()

    def __len__(self):
        return generator_length(self._generator())

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            val = next(self._iterator)
            if self.filter_check(val):
                return val

class FileGenerator:
    """Brute force table file loader"""

    def __init__(self, file, filter_check=_true):
        if isinstance(file, str):
            self.file = open(file, 'r')
        else:
            self.file = file
        self.filter_check = filter_check

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def reset(self):
        """Reset the table to the first combination"""
        self.file.seek(0)

    def __len__(self):
        pos = self.file.tell()
        self.reset()
        count = 0
        for line in self.file:
            count += 1
        self.file.seek(pos)
        return count

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            line = self.file.readline().strip()
            if line:
                if self.filter_check(line):
                    return line
            else:
                raise StopIteration
        
    def close(self):
        """Close the file-like object"""
        self.file.close()
