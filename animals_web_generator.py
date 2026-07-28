import data_fetcher
import os


def serialize_animal(animal):
    """
    Converts animal data into HTML.
    """

    print("\n--- Serializing animal ---")
    print(animal)

    output = '<li class="cards__item">\n'

    output += f'<div class="card__title">{animal["name"]}</div>\n'

    output += '<p class="card__text">\n'

    characteristics = animal.get("characteristics", {})

    if "diet" in characteristics:
        output += f'<strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    if "locations" in animal and animal["locations"]:
        output += f'<strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    if "type" in characteristics:
        output += f'<strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += "</p>\n"
    output += "</li>\n"

    print("\n--- Generated HTML ---")
    print(output)

    return output


def load_template():
    """
    Loads HTML template.
    """

    template_path = os.path.abspath("animals_template.html")

    print("\n--- Loading Template ---")
    print("Template path:")
    print(template_path)

    with open("animals_template.html", "r") as file:
        template = file.read()

    print("\nPlaceholder found:")
    print("__REPLACE_ANIMALS_INFO__" in template)

    return template


def create_website(animals):

    print("\n=== Creating Website ===")
    print("Number of animals:", len(animals))

    template = load_template()

    animals_info = ""

    for animal in animals:
        animals_info += serialize_animal(animal)

    print("\n=== COMPLETE ANIMAL HTML ===")
    print(animals_info)

    if not animals_info:
        animals_info = "<h2>Dieses Tier existiert nicht.</h2>"

    html = template.replace(
        "__REPLACE_ANIMALS_INFO__",
        animals_info
    )

    print("\n=== FINAL HTML BEFORE WRITING ===")
    print(html[:1000])

    output_path = os.path.abspath("animals.html")

    print("\nWriting file:")
    print(output_path)

    with open("animals.html", "w") as file:
        file.write(html)

    print("\nanimals.html successfully written!")

    # Kontrolle: Datei wieder einlesen
    with open("animals.html", "r") as file:
        saved_content = file.read()

    print("\n=== SAVED FILE CHECK ===")
    print(saved_content[:1000])

    print("\nSpider Monkey exists in saved file:")
    print("Spider Monkey" in saved_content)

    print("\nAmerican Foxhound exists in saved file:")
    print("American Foxhound" in saved_content)


def main():

    animal_name = input("Please enter an animal: ")

    print("\n=== Fetching Data ===")
    print("Search:")
    print(animal_name)

    animals = data_fetcher.fetch_data(animal_name)

    print("\n=== API RESULT ===")
    print(animals)

    print("\n=== FOUND ANIMALS ===")

    for animal in animals:
        print(animal["name"])

    create_website(animals)

    print("\nWebsite was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()