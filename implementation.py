#Task 1

def pi_day():
    months = ('January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December')
    pi_day = months[2]
    print(pi_day)

pi_day()

def fruits_veggies():
    fruits_and_veggies = {'guava', 'pitaya', 'lime', 'kiwi', 'grapes'}
    fruits_and_veggies_2 = {'pineapple', 'pomegranate', 'sweet potato', 'artichoke'}
    fruits_and_veggies.update(fruits_and_veggies_2)
    for items in fruits_and_veggies:
        print(items)

fruits_veggies()


def user_profile():
    user_profile = {
        'First name': 'Jean',
        'Last name': 'Sibelius',
        'Email address':'jean.sib@proton.com',
        'Phone number': 2067897899
    }

    print(f'''
    First name: {user_profile['First name']} 
    Last name: {user_profile['Last name']}.
    Email address: {user_profile['Email address']}
    Phone number: {user_profile['Phone number']}
    ''')
user_profile()
