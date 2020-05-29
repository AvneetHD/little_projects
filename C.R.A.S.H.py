import random
name = input('What is your name?')
starts = ("greetings", "hi", "howdy", "welcome", "bonjour", "buenas noches", "buenos dias", "good day", "good morning",
          "hey", "hi-ya", "how are you", "how goes it", "howdy-do", "shalom", "what's happening", "what's up", "hallo"
          , "Përshëndetje", "iwi selami new", "marhabaan", "Barev DZez", "Salam", "Hyālō", "kaixo", "dobry dzień",
          "zdravo", "Zdraveĭte", "haallo", "Hola", "Kumusta", "Nǐ hǎo", "Nǐ hǎo", "Hallo", "Kamusta", "Geiá sou",
          "aloha", "namaskaar", "Sata srī akāla", "buna", "")

while True:
    hellos = random.choice(starts)
    print('{0} {1}'.format(name, hellos))
