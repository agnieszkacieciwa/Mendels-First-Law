import unittest
from unittest.mock import patch
from io import StringIO
from Mendels_First_Law import get_valid_genotype, calculate_offspring_genotypes, display_offspring_genotypes

class TestMendelsFirstLaw(unittest.TestCase):

    def setUp(self):
        self.genotype_input = ['AA', 'Aa', 'aa']
        self.patcher = patch('builtins.input', side_effect=lambda _: self.genotype_input.pop(0))
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_get_valid_genotype(self):
        self.assertEqual(get_valid_genotype("Prompt"), 'AA')

    def test_calculate_offspring_genotypes(self):
        count_offspring, total_offspring = calculate_offspring_genotypes('AA', 'Aa')
        self.assertEqual(count_offspring, {('A', 'a'): 2, ('A', 'A'): 2})
        self.assertEqual(total_offspring, 4)

    @patch('sys.stdout', new_callable=StringIO)
    def assert_display_offspring_genotypes_output(self, genotype_counts, total_offspring, expected_output, mock_stdout):
        display_offspring_genotypes(genotype_counts, total_offspring)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

    def test_display_offspring_genotypes(self):
        genotype_counts = {('A', 'A'): 1, ('A', 'a'): 1}
        total_offspring = 2
        expected_output = "Possible combinations of offspring genotypes are: [('A', 'A'), ('A', 'a')] In the ratio:\nAA: 50.00%\nAa: 50.00%"
        self.assert_display_offspring_genotypes_output(genotype_counts, total_offspring, expected_output)

if __name__ == '__main__':
    unittest.main()
