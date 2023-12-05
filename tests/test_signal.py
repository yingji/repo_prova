import os
import wfdb
import numpy as np
from repo_prova.signal import Signal
import unittest

current_path = os.path.abspath(__file__)

class TestSignal(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(IOError): # missing fs and t
            Signal(data = np.zeros(6))
        with self.assertRaises(ValueError): # mismatched signal names
            Signal(data = np.hstack((np.arange(9)[..., None], np.ones(9)[..., None] )),
                   t=np.arange(9),
                   sig_names=['ciao'])


class TestNSTSignal(unittest.TestCase):

    def setUp(self):
        record = wfdb.rdrecord('resources/nstdb/118e06')
        # wfdb.plot_wfdb(record=record, title='Example signals')
        self.sig = Signal(
            data = record.p_signal, fs= record.fs, 
            sig_names=record.sig_name
        )
    
    def test_filter(self):
        sig_filt = self.sig.band_filter([0.5, 40])
        np.testing.assert_almost_equal(
            np.average(sig_filt.data, axis=0),
            np.zeros(2),
            decimal=3
            )
    
    def test_power_spectral_density(self):
        f, pxx = self.sig.power_spectral_density()
        for i in range(pxx.shape[1]):
            self.assertTrue(0.05<f[np.argmax(pxx[:,i])]<100)
    
if __name__ == '__main__':
    unittest.main()