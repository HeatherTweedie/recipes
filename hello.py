def main():
    name = input('What is your name?')
    print(f'Hello {name}')
    valid = False
    while valid == False:
        cheese_opinion = input('Do you like cheese?')
        if cheese_opinion == 'yes':
            recipe = 'Caprese salad'
            valid = True
        elif cheese_opinion == "no":
            recipe = 'Veggie chili'
            valid = True
        else:
            print("Please answer yes or no.")
            valid = False

    print (f"Ok {name}, try some {recipe}!")

main()
