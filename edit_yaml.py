import yaml

def get_char_count(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        return len(content)

def update_yaml_config(file_path, config_data):
    with open(file_path, 'w') as file:
        yaml.dump(config_data, file, default_flow_style=False)
