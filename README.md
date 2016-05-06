# Discordant SNP Search
This script searches for discordant SNPs between child and parent 23andMe genome files. The SNPs that this script flags up may possibly come from miscalls, mutations or microdeletions.

The gender is passed to the script to take into account that the Y-chromosome is only passed from father to son, the MT DNA from mother to child, and the X-chromosome from both parents to daughter or from mother to son.

The script will only work between two 23andMe files of the same version. They also need to have the same number of lines which they should have if the download option "Data set" was set the same for both of them (e.g. "All DNA").

##Requirements
* Python3

##Usage
```
python dss.py <CHILD_FILE> <CHILD_GENDER:M/F> <PARENT_1_FILE> <PARENT_1_GENDER:M/F> [<PARENT_2_FILE> <PARENT_2_GENDER:M/F>]
```
Input of a second parent is optional. Gender is given as "M" for male and "F" for female.

##Usage Example
###Single parent input
```
python dss.py 23andme_son_v4.txt M 23andme_mother_v4.txt F > output1.txt
```

###Both parents input
```
python dss.py 23andme_daughter_v4.txt F 23andme_mother_v4.txt F 23andme_father_v4.txt M > output2.txt
```

##Output Example
The output SNPs are ordered: child, parent 1, parent2.
###Output if single parent input
```
rs10942597	5	89807395	CC	TT
rs2914928	5	97048466	CC	TT
i5021721	6	29895831	DD	II
```

###Output if both parents input
If both parents are input, the exclamation mark indicates the SNP that is most likely discordant.
```
rs2119299	11	134294730	TT!	CC	CC
rs2657880	12	56863770	CC	GG	--
i6044032	12	70049234	II	II	DD!
rs3117866	13	26278338	AA	GG!	AG
```
