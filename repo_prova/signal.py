# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:35:20 2023

@author: wuy
"""

import numpy as np
try:
    import scipy.signal as spsgn
    import scipy.stats as spstats
except ImportError:
    spsgn = None
    spstats = None
try:
    import pandas as pd
except ImportError:
    pd = None
from typing import List
# import matplotlib.pyplot as plt


class Signal():
    """
    a class for signal pricessing
    """
    
    def __init__(self, data: np.ndarray, 
                 t: np.array = None, fs: int = None,
                 sig_names: List[str] = None
                 ):
        """
        
        Parameters
        ----------
        data : np.ndarray
            signal data.
        t : np.array, optional
            timestamp. The default is None.
        fs : int, optional
            sample rate. The default is None.
        sig_names: list of str, optional
            signal names
        """
        if t is None and fs is None:
            raise IOError("Either t or fs must given")
        
        if t is not None:
            self.t = t
        else:
            self.t = np.arange(len(data))/fs
        if fs is not None:
            self.fs = fs
        else:
            self.fs = int(1/spstats.mode(np.diff(t))[0])
        self.data = data
        if sig_names is None:
            self.sig_names = [f'ch{i}' for i in range(self.data.shape[1])]
        else:
            if len(sig_names) != self.data.shape[1]:
                raise ValueError(
                    "Mismatching size: signal_names must have same number of the given signals"
                    )
            self.sig_names = sig_names
    
    def band_filter(self, freq_range, order=3):
        """Zero-phase filter"""
        
        b_hp, a_hp = spsgn.butter(order, freq_range[0] * 2 / self.fs, btype='high')
        b_lp, a_lp = spsgn.butter(order, freq_range[1] * 2 / self.fs, btype='low')
        filt_data = spsgn.filtfilt(
            b_hp, a_hp, 
            spsgn.filtfilt(b_lp, a_lp, self.data, axis=0), 
            axis=0
        )
        return Signal(data=filt_data, t=self.t, fs=self.fs, sig_names=self.sig_names)
    
    def power_spectral_density(self):
        nblock = 1024
        overlap = 128
        sig_pxxf = []
        win = spsgn.hanning(nblock, True)
        for i in range(self.data.shape[1]):
            f, pxxf = spsgn.welch(
                self.data[:,i], self.fs, 
                window=win, noverlap=overlap, nfft=nblock, 
                detrend='constant', return_onesided=True
                )
            sig_pxxf.append(pxxf[..., None])
        # plt.semilogy(f, pxxf, '-o')
        # plt.plot(f, pxxf2, '-o')
        return f, np.hstack(sig_pxxf)
    
    def stats(self):
        df = pd.DataFrame(self.data, columns=self.sig_names)
        return df.describe()