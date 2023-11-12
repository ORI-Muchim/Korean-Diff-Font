import os
import requests

trained_models = './trained_models/model800000.pt'

def get_model():
    if not os.path.isfile(trained_models):
        urls = [
            'https://github.com/ORI-Muchim/Korean-Diff-Font/releases/download/1.0/ema_0.9999_800000.pt',
            'https://github.com/ORI-Muchim/Korean-Diff-Font/releases/download/1.0/model800000.pt',
            'https://github.com/ORI-Muchim/Korean-Diff-Font/releases/download/1.0/opt800000.pt'
        ]

        directory = os.path.dirname(trained_models)
        if not os.path.exists(directory):
            os.makedirs(directory)

        print("Downloading Trained Models...")
        for url in urls:
            filename = os.path.join(directory, url.split('/')[-1])
            response = requests.get(url, allow_redirects=True)
            with open(filename, 'wb') as file:
                file.write(response.content)
        print("Saving Trained Models...")
        
    else:
        print('Skipping... Model exists.')

get_model()
