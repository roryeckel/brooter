"""Concurrent brute force algorithms

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

import multiprocessing, time, signal

class BrutePool:
    """Brute-forcing pool"""

    @staticmethod
    def _initializer():
        """Ignore CTRL+C in the worker process."""
        signal.signal(signal.SIGINT, signal.SIG_IGN)

    def __init__(self, cases, fn, pcount=4, stop_when_found=True, previous_result=None, save_invalid=True):
        """Construct a brute force pool to check cases against fn, defaulting to 4 processes,
optionally with a previous set of results to skip"""
        self.pool = multiprocessing.Pool(pcount, initializer=BrutePool._initializer)
        self.cases = cases
        self.fn = fn
        self.result = multiprocessing.Manager().dict()
        self.previous_result = previous_result
        self.stop_when_found = stop_when_found
        self.save_invalid = save_invalid

    def is_running(self):
        return self.pool.is_alive()

    def _callback(self, t):
        """self.pool's apply_async callback to filter checks into self.results"""
        i, success = t
        if success is False and self.save_invalid:
            self.result[i] = success
        if self.stop_when_found and success is True:
            self.stop()

    def start(self, apply_delay=.025):
        """Launch the brute force, calling self.fn to check cases"""
        keys = None if self.previous_result is None else self.previous_result.keys()
        for case in self.cases:
            if keys is None or case not in keys:
                self.pool.apply_async(func=self.fn, args=(case,), callback=self._callback)
                if apply_delay != 0:
                    time.sleep(apply_delay)

    def stop(self):
        """Terminate all brute force processes and return self.result"""
        self.pool.close()
        self.pool.terminate()
        self.pool.join()

    def join(self):
        """Close and join the processes"""
        self.pool.close()
        self.pool.join()
