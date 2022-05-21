def main():
    name = input('What is your name?')
    print(f'Hello {name}')

    while True:
        cheese_opinion = input('Do you like cheese?')
        if cheese_opinion in ('yes', 'no'):
            break
        print("Please answer yes or no.")
    
    if cheese_opinion == 'yes':
        recipe = 'Caprese salad'
    elif cheese_opinion == "no":
        recipe = 'Veggie chili'

    print (f"Ok {name}, try some {recipe}!")

main()
