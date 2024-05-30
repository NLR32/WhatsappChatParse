
import re


# Finds person who texted
def parse_name(input_string):
    start_index = input_string.find("M] ") + len("M] ")
    end_index = input_string.find(":", start_index)

    if start_index != -1 and end_index != -1:
        parsed_string = input_string[start_index:end_index].strip()
        return parsed_string
    else:
        return None



# def parse_for_length(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()
#
#     # Use regular expression to find matches between "M] " and "["
#
#     matches = re.findall(pattern, content)
#
#     return matches

def parse():
    file = open('FILEPATH','r')
    lines = file.readlines()

    text_dict = {'temp': 0}
    sticker_dict = {'temp': 0}
    img_dict = {'temp': 0}
    text_index = 0
    sticker_index = 0;
    img_index = 0
    longest = ''
    for l in lines:

        name = parse_name(l)

        # counting images sent
        if "image omitted" in l:
            if name in img_dict:
                img_dict[name] += 1
            else:
                img_dict[name] = 1
            img_index +=1

        # counting stickers sent
        if "sticker omitted" in l:
            if name in sticker_dict:
                sticker_dict[name] += 1
            else:
                sticker_dict[name] = 1
            sticker_index +=1

        # counting texts sent
        if (name != None):
            if name in text_dict:
                text_dict[name] += 1
            else:
                text_dict[name] = 1
            text_index +=1

    # printing text stats
    print("text stats\n")
    orderedList = sorted(text_dict.items(), key=lambda item: item[1], reverse=True)
    for num, i in enumerate(orderedList):
        print(f'{num+1}: {i[0]}: {i[1]}')
    print(f'number of texts: {text_index}\n')

    print("\n\n")

    # printing sticker stats
    print("sticker stats\n")
    orderedList = sorted(sticker_dict.items(), key=lambda item: item[1], reverse=True)
    for num, i in enumerate(orderedList):
        print(f'{num + 1}: {i[0]}: {i[1]}')
    print(f'number of stickers: {sticker_index}\n')

    # printing image stats
    print("image stats\n")
    orderedList = sorted(img_dict.items(), key=lambda item: item[1], reverse=True)
    for num, i in enumerate(orderedList):
        print(f'{num + 1}: {i[0]}: {i[1]}')
    print(f'number of images: {img_index}\n')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
