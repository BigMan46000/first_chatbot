import time

print('Whut up Big Hommie?!')
time.sleep(2)
response = input("How you doin? (good or bad):")
if response == 'good':
    print('Man, Glad to hear that!')
    print('I hope your day keeps going well!')
    quit()
if response == 'bad':
    mood = input('You want to talk about it (yes or no):')
    if mood == 'no':
        print('Ok, I undertand')
        print('Goodbye')
        quit()
    if mood == 'yes':
        ans = input('Did you get punched in the face (yes or no):')
        if ans == 'yes':
            print('DDDDDAAAAAANNNNNNNGGGGGG!!!!!!!')
            print("H, E, doubule hockey sticks!!!")
            print("You should have used Taekwondo")
            who = input("Was it a boy or a girl:")
            if who == 'girl':
                print('Man, you gotta do better')
                quit()
            if who == 'boy':
                print('Next time kick him in the family jeweles')
        if ans == 'no':
            print('Oh ok... Good')
