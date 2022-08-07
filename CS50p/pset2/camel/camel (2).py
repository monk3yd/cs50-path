def main():
    camel_var_name = input("camelCase: ")
    snake_var_name = camel_to_snake(camel_var_name)
    print(snake_var_name)


def camel_to_snake(camel_var_name):
    # Get all capital case indexes in camel
    caps_indexes = [
        index for index in range(len(camel_var_name)) if camel_var_name[index].isupper()
    ]
    # print(f"All camel caps indexes: {caps_indexes}")

    counter = 0
    # For each cap letter index in list
    for index in caps_indexes:
        if counter != 0:
            index += counter

        # print(f"Index turn: {index}")
        camel_var_name = insert_dash(camel_var_name, index)
        counter += 1

    return camel_var_name.lower()


def insert_dash(string, index):
    # index an underscore _ into camel_var
    return string[:index] + "_" + string[index:]


if __name__ == "__main__":
    main()
