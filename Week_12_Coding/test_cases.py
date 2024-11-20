import unittest
from pump_simulation import InfusionPump
class TestInfusionPump(unittest.TestCase):
    def test_initial_state(self):
        pump = InfusionPump()
        self.assertFalse(pump.is_running)
        self.assertEqual(pump.current_dosage, 0)
    def test_start_infusion(self):
        pump = InfusionPump()
        pump.start_infusion(40)
        self.assertTrue(pump.is_running)
        self.assertEqual(pump.current_dosage, 40)
    def test_stop_infusion(self):
        pump = InfusionPump()
        pump.start_infusion(50)
        pump.stop_infusion()
        self.assertFalse(pump.is_running)
        self.assertEqual(pump.current_dosage, 0)
    def test_exceed_max_dosage(self):
        pump = InfusionPump()
        with self.assertRaises(ValueError):
            pump.start_infusion(150)  # Exceeds max_dosage
if __name__ == '__main__':
    unittest.main()