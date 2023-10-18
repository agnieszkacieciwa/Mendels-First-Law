import sys
from collections import Counter

# Function to get a valid genotype
def get_valid_genotype(prompt):
    while True:
        genotype = input(prompt)
        if len(genotype) == 2:
            return genotype
        else:
            print("Invalid input. Please enter a valid genotype with two characters.")

# Function to calculate offspring genotypes
def calculate_offspring_genotypes(genotype1, genotype2):
    # Split the genotypes into alleles
    allele1, allele2 = genotype1[0], genotype1[1]
    allele3, allele4 = genotype2[0], genotype2[1]

    # Generate the possible combinations of offspring genotypes
    o1 = allele1 + allele4
    o2 = allele1 + allele3
    o3 = allele2 + allele4
    if allele1 == allele2 and allele3 == allele4 and allele1 != allele3:
        o4 = allele2 + allele3
    else:
        o4 = allele3 + allele2
    offspring = [o1, o2, o3, o4]

    # Count the occurrences of each offspring genotype
    count_offspring = Counter(offspring)
    total_offspring = sum(count_offspring.values())

    return count_offspring, total_offspring

# Print the possible combinations of offspring genotypes and their corresponding percentages
def display_offspring_genotypes(count_offspring, total_offspring):
    print("Possible combinations of offspring genotypes are:", set(count_offspring.keys()), "In the ratio:")
    for genotype, count in count_offspring.items():
        percentage = count / total_offspring * 100
        print(f"{genotype}: {percentage:.2f}%")

def main():
    genotype1 = get_valid_genotype("Enter the first genotype: ")
    genotype2 = get_valid_genotype("Enter the second genotype: ")

    # Check if both genotypes describe the same trait
    if genotype1.upper() == genotype2.upper():
                print("Both genotypes describe the same trait.")
    else:
        print("The genotypes do not describe the same trait.")
        input("Press Enter to exit the program.")
        sys.exit()

    count_offspring, total_offspring = calculate_offspring_genotypes(genotype1, genotype2)
    display_offspring_genotypes(count_offspring, total_offspring)

    input("Press Enter to exit the program.")
    sys.exit()

if __name__ == "__main__":
    main()
