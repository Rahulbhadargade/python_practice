# it is the process of creating new collection in less numbers of instruction
# TYPES 
#1.LIST COMPREHENTION - 
# SYNTAX 1
l = [i for i in range(1, 51)]
#SYNTAX 2 - VAR = [VAL FOR VAL IN RANGE/COLL IF COND]
l = [i for i in range(1,51) if i%2 == 0]
print(l)
#SYNTAX 3 - VAR = [VAL,VAL2,VALN..... FOR VAL1 IN R/COLL FOR VAL2 IN R/COLL FOR VALN IN R/COLL IF COND]
#2.SET COMPREHENTION - 
#3.DICT COMPREHENTION - 