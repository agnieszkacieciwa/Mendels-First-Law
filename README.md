# Mendel's-First-Law
This program allows users to input two genotypes and calculates the possible combinations of offspring genotypes and their ratios based on the provided parent genotypes, following the First Mendel's Law, also known as the Law of Equal Segregation - the principle of genetic inheritance. This means that offspring inherit one allele from each parent, and the alleles segregate randomly, resulting in a 50% chance for the offspring to receive either allele. It is designed to work with genotypes following the Aa (AA, aa), Bb (BB, Bb), etc. convention.

For example, one parent with the Aa genotype has two alleles: A and a, meaning that the offspring has a 50% chance of inheriting allele A and a 50% chance of inheriting allele a (from this one parent).

## Requirements
- Python 3.x
- `collections` and `unittest` module

## Mendel's First Law

### Script Structure:
1. `get_valid_genotype(prompt):`
- A function to obtain a valid genotype from the user, ensuring that it consists of two alleles of the same case (either both uppercase or both lowercase).
2. `calculate_offspring_genotypes(genotype1, genotype2):`
- A function to calculate the possible combinations of offspring genotypes based on the input genotypes.
- It uses defaultdict to count the occurrences of each offspring genotype.
- The script considers equal segregation of alleles and handles distinct allele cases.
3. `display_offspring_genotypes(count_offspring, total_offspring):`
- A function to print the possible combinations of offspring genotypes and their corresponding percentages.
- It sorts the genotypes for display and calculates the percentage of each genotype in the offspring.
4. `main():`
- The main function where the user enters two genotypes, and the script checks if they describe the same trait.
- It then calculates and displays the possible combinations of offspring genotypes.

### How to Use:
1. Run the script.
2. Enter the first genotype when prompted.
3. Enter the second genotype when prompted.
4. The script will display the possible combinations of offspring genotypes and their percentages.
5. Press Enter to exit the program.

## Testing Mendel's First Law

### Overview
Testing is crucial to ensure the accuracy and reliability of the Mendel's First Law script. The testing script, `test-Mendels-First-Law.py`, uses the unittest module to perform unit tests on the functions within `Mendels-First-Law.py`.

### Test Cases:
1. `test_get_valid_genotype:`
- Ensures that the get_valid_genotype function correctly handles and validates user input for genotypes.
2. `test_calculate_offspring_genotypes:`
- Tests the calculate_offspring_genotypes function to ensure it accurately calculates the possible combinations of offspring genotypes and the total number of offspring.
3. `test_display_offspring_genotypes:`
- Checks the output of the display_offspring_genotypes function against expected values for a given set of genotype counts and total offspring.

### How to Run Tests:
1. Run the testing script.
2. The script will perform the defined test cases and report any failures or errors.

## Exapmle  of usage

### Mendel's-First-Law
![obraz](https://github.com/agnieszkacieciwa/Mendels-First-Law/assets/88035266/57157d98-8f3c-48e9-be92-63227506ca8e)

### Mendel's-First-Law-Unit-Test
![obraz](https://github.com/agnieszkacieciwa/Mendels-First-Law/assets/88035266/293c0d34-c085-4141-8802-aa93b5828bed)
