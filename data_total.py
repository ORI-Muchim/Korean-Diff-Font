def extract_first_characters_from_file(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    first_characters = ''.join([line[0] for line in content if line.strip()])
    return first_characters

def write_to_file(output_file_path, content):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

input_path = './korean_stroke.txt'
output_path = './total_kor.txt'

result = extract_first_characters_from_file(input_path)
write_to_file(output_path, result)
