if resistance_ohm <= 0:
    raise ValueError("Resistance must be positive")
     def test_invalid_resistance(self):
        for resistance in (0, -5):
            with self.assertRaises(ValueError):
                analyze_dc(12, resistance)
                git diff
python -m unittest -v
git add electrical.py test_electrical.py
git diff --staged
git commit -m "feat: validate positive resistance"
git switch main
git merge --no-ff feature/input-validation -m "merge: input validation"
git log --oneline --graph --decorate --all