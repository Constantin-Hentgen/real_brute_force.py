import os

liste = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","p","q","r","s","t","u","v","w","x","y","z"]
mot = input("Enter a password based on letters :  ")
chaine = str()

def test(chaine,mot):
    if chaine == mot:
        print('password hacked')

def brute_force():
    for l in liste:
        chaine = l
        test(chaine,mot)

        for l1 in liste:
            chaine = l + l1
            test(chaine,mot)

            for l2 in liste:
                chaine = l + l1 + l2
                test(chaine,mot)

                for l3 in liste:
                    chaine = l + l1 + l2 + l3
                    test(chaine,mot)
                        
                    for l4 in liste:
                        chaine = l1 + l2 + l3 + l4
                        test(chaine,mot)
brute_force()

os.system('Pause')
