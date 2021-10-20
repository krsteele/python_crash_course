# 10-8: Cats and Dogs, 10-9: Silent Cats and Dogs

pet_files = ['cats.txt', 'dogs.txt']

def print_names(filename):
    try:
        with open(filename) as f:
            names = f.readlines()
    except FileNotFoundError:
        # print(f"The file {filename} does not exist.")
        pass
    else:
        print(f"Here are the pet names listed in {filename}: ")
        for name in names:
            print(f"- {name.rstrip()}")


for file in pet_files:
    filename = f"chapter10/{file}"
    print_names(filename)