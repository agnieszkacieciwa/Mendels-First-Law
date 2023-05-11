from collections import Counter

genotype1 = input("Enter the first genotype according to the Aa convention: ").upper()
genotype2 = input("Enter the second genotype: ").upper()

if genotype1 == genotype2:
    print("Both genotypes describe the same trait.")
else:
    print("The genotypes do not describe the same trait.")
    input("Press Enter to exit the program.")
    import sys
    sys.exit()

allele1, allele2, allele3, allele4 = genotype1[0], genotype1[1], genotype2[0], genotype2[1]

o1 = allele1 + allele4
o2 = allele1 + allele3
o3 = allele2 + allele4
if allele1 == allele2 and allele3 == allele4 and allele1 != allele3:
    o4 = allele2 + allele3
else:
    o4 = allele3 + allele2

offspring = [o1, o2, o3, o4]

count_offspring = Counter(offspring)
total_offspring = sum(count_offspring.values())

print("Possible combinations of offspring genotypes are:", set(offspring), "In the ratio:")
for genotype, count in count_offspring.items():
    percentage = count / total_offspring * 100
    print(f"{genotype}: {percentage:.2f}%")

input("Press Enter to exit the program.")
