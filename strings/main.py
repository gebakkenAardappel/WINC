# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
from lib2to3.pgen2.token import NEWLINE

scorer0 = "Ruud Gullit"
scorer1 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = scorer0 +" "+str(goal_0) +", "+scorer1 +" "+str(goal_1)
print (scorers)
report= scorer0 +" scored in the "+str(goal_0) +"nd minute" +"\n" +scorer1 +" scored in the "+str(goal_1) +"th minute"
print (report)

player="Marco van Basten"
eerste_spatie=player.find(" ")
first_name=player[0:eerste_spatie]
print(first_name)
last_name=player[eerste_spatie+1:]
last_name_len=len(last_name)
print(last_name_len)
name_short=player[0]+". "+last_name
print(name_short)
shout=first_name+"! "
#herhaal net zo vaak als dat er letters in de voornaam zitten, de laatste keer mag geen spatie bevatten
chant=shout*(eerste_spatie-1)+first_name+"!"
print (chant)
good_chant= (chant[-1] != " ")
print(good_chant)
