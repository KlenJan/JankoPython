for i in range(1,21):
    if i in [4,13]:
        print(f"{i} is unlucky")
    elif i%2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")