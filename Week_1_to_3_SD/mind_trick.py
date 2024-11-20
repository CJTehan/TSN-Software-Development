# Creating a mind trick flowchart in code
print('Hello and welcome one and all, are you ready to see some magic?')
def welcome():
    print('Hello, here is a trick the will truly blow your mind')
welcome()

name = input('What is your name?\n')
print(f'It is a pleasure to meet you {name}, I am Merlin the magician')
print('Pick a number between 1 and 10')
selected_number = int(input())
print('Excellent, now I want you to multiply that number by 2')
answer = int(selected_number) * 2
print(answer)
print('Now multiply that new number you got by 5')
multiplied_number = int(answer) * 5
print(multiplied_number)
print('Next, I want you to divide the total you have now with the original number you chose')
divided_total = (multiplied_number // selected_number)
print(divided_total)
print('Just before I get you to answer the final question') 
print('be prepared to have your mind blown as you question if magic is real!')
print('Now one last step for you, I want you to subtract 7 from your final answer')
trick_complete = int(divided_total) - 7
print(trick_complete)
input('')
print('Now to reveal to you the answer I have always known you would get')
input('')
input('')
input('')
print('Your number is 3! I knew it all along')

def end():
    print(f'Thank you one and all for attending, especially you {name}!')
    print('Until next time where I will once again amaze you')
end()