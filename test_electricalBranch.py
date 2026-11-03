if resistance_ohm <= 0:
    raise ValueError("Resistance must be positive")
     def test_invalid_resistance(self):
        for resistance in (0, -5):
            with self.assertRaises(ValueError):
                analyze_dc(12, resistance)