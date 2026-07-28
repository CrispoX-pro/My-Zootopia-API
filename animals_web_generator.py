import data_fetcher


def serialize_animal(animal):
    """
    Converts animal data into HTML format.
    """

    output = '<li class="cards__item">\n'

    output += f'<div class="card__title">{animal["name"]}</div>\n'

    output += '<p class="card__text">\n'

    characteristics = animal.get("characteristics", {})

    if "diet" in characteristics:
        output += f'<strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    if "locations" in animal:
        if len(animal["locations"]) > 0:
            output += f'<strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    if "type" in characteristics:
        output += f'<strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += "</p>\n"
    output += "</li>\n"

    return output


def load_template():
    """
    Reads the HTML template.
    """

    with open("animals_template.html", "r") as file:
        return file.read()


def create_website(animals):
    """
    Creates the final HTML website.
    """

    template = load_template()

    animals_info = ""

    for animal in animals:
        animals_info += serialize_animal(animal)

    if animals_info == "":
        animals_info = "<h2>Dieses Tier existiert nicht.</h2>"

    html = template.replace(
        "__REPLACE_ANIMALS_INFO__",
        animals_info
    )

    with open("animals.html", "w") as file:
        file.write(html)


def main():

    animal_name = input("Please enter an animal: ")

    animals = data_fetcher.fetch_data(animal_name)

    create_website(animals)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()