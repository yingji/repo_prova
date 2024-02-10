import unittest
import numpy as np
from repo_prova.signal import Signal


class TestSignal(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        self.t = np.array([0, 1, 2, 3])
        self.fs = 1
        self.sig_names = ['ch1', 'ch2']
        self.signal = Signal(data=self.data, t=self.t, fs=self.fs, sig_names=self.sig_names)

    def test_init(self):
        # Test initialization with all parameters
        signal = Signal(data=self.data, t=self.t, fs=self.fs, sig_names=self.sig_names)
        self.assertEqual(signal.data.tolist(), self.data.tolist())
        self.assertEqual(signal.t.tolist(), self.t.tolist())
        self.assertEqual(signal.fs, self.fs)
        self.assertEqual(signal.sig_names, self.sig_names)

        # Test initialization with missing fs
        with self.assertRaises(IOError):
            Signal(data=self.data)

        # Test initialization with missing t
        signal = Signal(data=self.data, fs=self.fs)
        expected_t = np.arange(len(self.data)) / self.fs
        self.assertEqual(signal.t.tolist(), expected_t.tolist())

        # Test initialization with mismatching sig_names
        with self.assertRaises(ValueError):
            Signal(data=self.data, t=self.t, fs=self.fs, sig_names=['ch1'])

    def test_band_filter(self):
        # Test band_filter with valid frequency range
        freq_range = (1, 3)
        filtered_signal = self.signal.band_filter(freq_range=freq_range)
        self.assertIsInstance(filtered_signal, Signal)
        self.assertEqual(filtered_signal.fs, self.signal.fs)
        self.assertEqual(filtered_signal.t.tolist(), self.signal.t.tolist())
        self.assertEqual(filtered_signal.sig_names, self.signal.sig_names)

        # Test band_filter with invalid frequency range
        with self.assertRaises(ValueError):
            self.signal.band_filter(freq_range=(3, 1))

        # Test band_filter with frequency range out of bounds
        with self.assertRaises(ValueError):
            self.signal.band_filter(freq_range=(-1, 5))
    def test_power_spectral_density(self):
        # Test power_spectral_density output
        f, pxxf = self.signal.power_spectral_density()
        self.assertIsInstance(f, np.ndarray)
        self.assertIsInstance(pxxf, np.ndarray)
        self.assertEqual(pxxf.shape[1], self.data.shape[1])
        self.assertTrue((f >= 0).all())
        self.assertTrue((pxxf >= 0).all())
    def test_stats(self):
        # Test stats method output
        stats_df = self.signal.stats()
        self.assertIsInstance(stats_df, pd.DataFrame)
        self.assertEqual(list(stats_df.columns), self.sig_names)
        self.assertEqual(stats_df.shape[0], 8)
        # Check if basic statistics are present
        for stat in ['mean', 'std', 'min', '25%', '50%', '75%', 'max']:
            self.assertIn(stat, stats_df.index)


if __name__ == '__main__':
    unittest.main()
