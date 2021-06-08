import random


def run():

    print(" ")
    print("  Welcome to training English Words")
    print(" ")
    
    # Abrimos fichero y creamos lista de palabras
    listWord = []
    with open("3k-english-words.txt") as fname:
        for lineas in fname:
            listWord.append(lineas.strip('\n'))
    #print (listWord)
    print("    The list to learn is of: " + str(len(listWord)) + " words.")
    
    # Dividimos la lista en X listas de 'n' num de palabras. Y creamos multilista
    n = int(input("    How many words do you want to practice?: "))
    listoflists=[listWord[i:i + n] for i in range(0, len(listWord), n)]
    #print(listoflists)
    num_listas = len(listoflists)

    # Seleccionamos la lista que queremos practicar
    print("    You have ** " + str(num_listas) + " ** lists of "+ str(n) +" words to practice.")
    choice = int(input("    Please, select the list that you want to practice (from 0 to " + str(num_listas-1) + "): "))
    print(" ")

    # Practicando la lista de palabras...

    print("  Training English Words.... ")
    print("  (Press 'Enter' to next word and 'q' to Exit)")
    print(" ")
    count = 0
    while True:
        aleatorio = random.choice(listoflists[choice])
        print("--- #" + str(count) + "  " + aleatorio)
        print("https://www.wordreference.com/definition/"+aleatorio)
        print("https://sentencedict.com/"+ aleatorio +".html")
        count = count + 1
        if input() == "q":
            break

def main():
    run()

if __name__ == '__main__':
    main()