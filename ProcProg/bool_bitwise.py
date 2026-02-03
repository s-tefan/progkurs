# a and b -> b om bool(a)==True, False om bool(a)=False, oavsett typ 
print(True and 3, 3 and True)
# a or b -> a om bool(a)==True, b om bool(a)==False. Obs att b inte kollas om Bool(a)==True
print(3 or True, False or 5)

'''Bitvisa binära operatorer |,&,^ returnerar int med bitvis värdering.
False tolkas som 0, True tolkas som 1.
Undantag! Om båda operanderna är bool returneras bool.
Unära operatorn ~ returnerar bitvis även med bool, som då tolkas som 0 eller 1.
bool(~True) -> bool(-2) -> True
'''
print(True|2, 2|True)
print(~True, ~False, bool(~True), bool(~False))