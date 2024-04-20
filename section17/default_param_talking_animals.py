def speak(animal="dog"):
    if animal == "pig":
        return 'oink'
    if animal == "duck":
        return 'quack'
    if animal == "cat":
        return 'meow'
    if animal == "dog":  # This is the default value
        return 'woof'
    return '?'
