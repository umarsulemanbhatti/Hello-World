# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_nl_1 = "Ruud Gullit"
player_nl_2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = f"{player_nl_1} {goal_0}, {player_nl_2} {goal_1}"
report = f"{player_nl_1} scored in the {goal_0}nd minute\n{player_nl_2} scored in the {goal_1}th minute"
player = "Hans van Breukelen"
first_name = player[(player.find("Hans")):(player.find(" van"))]
last_name = player[player.find("van"):]
last_name_len = len(player[player.find("van"):])
name_short = str(first_name[:1])+". "+str(last_name)
chant = str((first_name)+"! ")*3 + str(first_name+"!")
good_chant = chant[-1] != " "
print(chant)
print(good_chant)