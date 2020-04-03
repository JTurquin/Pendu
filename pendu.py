from random import randrange
def generation_liste():

    file = open("words.txt",'r')
    lignes  = file.readlines()

    words = list()
    file.close()

    for ligne in lignes:
        if(ligne != "\n"):
            words.append(ligne)

    words.sort()
    return words

number = lambda x : randrange(x)
words = generation_liste()


def generation_cache(chaine):

    tmp = ""
    for lettre in chaine:
        if(lettre != "\n") : 
            tmp += "*"

    print(len(chaine))
    print(len(tmp))
    return tmp

words_r = words[number(len(words))]
words_cache = generation_cache(words_r)
def convert_str_to_list(word) :

    new_list = list()
    for lettre in word :
        if(lettre != "\n"):
            new_list.append(lettre)
    return new_list

def verification(words):

    word_convert = convert_str_to_list(words)
    letre = input("Entrer une lettre : ")
    indice = 0
    for recherche in words :
        
        indice += 1

    return new_words


print("Le mot est : " + words_r)
print("Le mot cacher est : " + words_cache)
words_cache = verification(words_r)
print("voici le nouveau mot : " + words_cache)
