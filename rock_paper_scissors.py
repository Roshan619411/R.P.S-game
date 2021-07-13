import random
# input from user and computer
def play():
    user=input("What's your choice?,'r'for rock,'p'for paper,'s'for scissor\n")
    computer=random.choice(['r','p','s'])

    if user==computer:
        return 'It is a tie'

    if is_win(user,computer):
        return 'you won!'

    return 'you lost!'
#return true if player wins
#r>s,s>p,p>r
def is_win(player,opponent):
    if(player=='r'and opponent=='s')or(player=='s'and opponent=='p')or(player=='p'and opponent=='r'):
        return True
print(play())                   





































