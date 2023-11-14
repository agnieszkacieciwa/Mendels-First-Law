# Mendel's-First-Law

This program calculates the possible combinations of offspring genotypes and their ratios based on the provided parent genotypes, following the First Mendel's Law - the principle of genetic inheritance. This means that offspring inherit one allele from each parent, and the alleles segregate randomly, resulting in a 50% chance for the offspring to receive either allele. 
It is designed to work with genotypes following the Aa convention.

## Requirements
- Python 3.x
- `collections` module

## Usage

1. Run the program by executing the Python script.
2. Enter the genotype of the first parent according to the Aa convention.
3. Enter the genotype of the second parent.
4. The program will determine if the genotypes describe the same trait or not.
5. It will then calculate the possible combinations of offspring genotypes and display them along with their respective ratios.

## How It Works

1. The program prompts the user to enter two genotypes.
2. It checks if the genotypes describe the same trait or not.
3. If the genotypes are different, it displays a message and waits for the user to press Enter to exit the program.
4. If the genotypes are the same, it continues to calculate the possible combinations of offspring genotypes.
5. The program assigns the alleles from the parent genotypes to variables.
6. It calculates the combinations of offspring genotypes based on the alleles.
7. The program utilizes the Counter class from the collections module to count the occurrences of each genotype combination.
8. It calculates the ratios of each genotype combination based on the counts.
9. The results are displayed, showing the possible combinations of offspring genotypes and their respective ratios.
10. The program waits for the user to press Enter to exit.

Please ensure that you provide valid genotypes following the Aa convention for accurate results.


## License

This project is licensed under the MIT License.
