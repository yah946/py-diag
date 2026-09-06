





def write_shopping_list(path, items):
    file = open(path,'w',encoding='utf-8')
    for item in items:
        file.write(item+'\n')
    file.close()
def add_article(path, article):
    file = open(path,'a',encoding='utf-8')
    file.write(article+'\n')
    file.close()
def read_file(path):
    file = open(path,'r',encoding='utf-8')
    return file.readlines()
def count_lines(path):
    return len(read_file(path))

def main():
    articles = ["apples", "milk", "bread"]
    modes_a_identifier = ["r", "w", "a", "x", "rb", "r+"]
    # write_shopping_list("courses.txt", articles)
    # add_article("courses.txt", "eggs")
    # print(read_file("courses.txt"))
    # print(count_lines("courses.txt"))
    

main()