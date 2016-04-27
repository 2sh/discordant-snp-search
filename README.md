# Discordant SNP Search
This script searches for discordant SNPs between child and parent 23andMe genome files. The SNPs that this script flags up may possibly come from miscalls, mutations or microdeletions.

The gender passed to script to take into account that the Y-chromosome is only passed from father to son, the MT DNA from mother to child, and the X-chromosome from both parents to daughter or from mother to son.

The script will only work between two 23andMe files of the same version and have the same number of lines which they should have if the data set "All DNA" was chosen.

##Requirements
* Python3

##Usage
```
python dss.py <CHILD_FILE> <PARENT_FILE> <CHILD_GENDER:M/F> <PARENT_GENDER:M/F>
```
Gender is given as "M" for male and "F" for female.

##Usage Example
```
python dss.py 23andme_son_v4.txt 23andme_mother_v4.txt M F > output.txt
```

##Output Example
```
rs10942597	5	89807395	CC!TT
rs2914928	5	97048466	CC!TT
i5021721	6	29895831	DD!II
```
To the left of the exclamation mark is the child's genotype and to the right the parent's genotype.
