def a_des_doublons(list):
    return len(list) != len(set(list))
def unique_tags(tags):
    tags_set = set()
    for tag in tags:
        for article in tag:
            tags_set.add(article)
    return tags_set
def main():
    atelier_python = ["Ali", "Sara", "Lina", "Karim"]
    atelier_java = ["Sara", "Omar", "Lina", "Yasmine"]
    tags_articles = [
        ["python", "web", "api"],
        ["python", "data"],
        ["web", "css"],
    ]

    atelier_python_set = set(atelier_python)
    atelier_java_set = set(atelier_java)
    print("Inscrits aux deux ateliers: ",atelier_python_set & atelier_java_set)
    print("Inscrits a au moins un atelier: ",atelier_python_set | atelier_java_set)
    print("Uniquement Python: ",atelier_python_set - atelier_java_set)

    print(a_des_doublons(["Ali", "Sara", "Lina"]))
    print(a_des_doublons( ["Ali", "Sara", "Ali"]))

    coordonnees = {[1, 2], [3, 4]}

    print(unique_tags(tags_articles))

    




main()