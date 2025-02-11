
def count (stra):
    return len(stra.split())

def count_elements(stra):
    elements={}
    stra=list(stra)
    for a in stra:
        elements.update({a:0})
    for a in stra:
        elements.update({a:elements[a]+1})
    return elements


def main ():
    with open("books/frankenstein.txt","r") as f:
        a=f.read()
    numme=count(a)
    elements=count_elements(a)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{numme} wolds fount in the documment")
    x=elements.keys()
    for a in x:
        print(f"The {a} element was fount {elements[a]} times")
    print('--- End report ---')


main()