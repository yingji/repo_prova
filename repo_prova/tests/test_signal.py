import unittest
import numpy as np
from repo_prova.signal import Signal


class TestSignal(unittest.TestCase):

    def setUp(self):
        # Create a signal with a cosine function
        self.t = np.linspace(0, 1, 500, endpoint=False)
        self.freq = 5  # 5 Hz cosine wave
        self.cosine_signal = np.cos(2 * np.pi * self.freq * self.t)
        self.signal = Signal(data=self.cosine_signal.reshape(-1, 1), t=self.t)

    def test_init(self):
        # Test Signal initialization
        self.assertEqual(self.signal.data.shape, (500, 1))
        self.assertEqual(self.signal.t.shape, (500,))
        self.assertEqual(self.signal.fs, 500)  # Sample rate
        self.assertEqual(self.signal.sig_names, ['ch0'])

    def test_band_filter(self):
        # Test band filter
        filtered_signal = self.signal.band_filter(freq_range=(1, 10))
        self.assertIsInstance(filtered_signal, Signal)

    def test_power_spectral_density(self):
        # Test power spectral density
        f, pxxf = self.signal.power_spectral_density()
        self.assertEqual(len(f), 513)  # Length of the frequency array
        self.assertEqual(pxxf.shape, (513, 1))  # Shape of the power spectral density array

    def test_stats(self):
        # Test statistics
        stats = self.signal.stats()
        self.assertIn('mean', stats)
        self.assertIn('std', stats)
        self.assertIn('min', stats)
        self.assertIn('25%', stats)
        self.assertIn('50%', stats)
        self.assertIn('75%', stats)
        self.assertIn('max', stats)


if __name__ == '__main__':
    unittest.main()