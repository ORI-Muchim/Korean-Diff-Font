import os
import requests

trained_models = './trained_models/model700000.pt'

def get_model():
    if not os.path.isfile(trained_models):
        url1 = 'https://doc-0g-0s-docs.googleusercontent.com/docs/securesc/4t4fg3cla8f4ta3umhgl0o0i7t7983vo/t90nunrpu61mo7sutfs649umpuab2kaa/1695306600000/09615949827588626005/09615949827588626005/1sZ-o143eSlGq_nsflgmmEwTHBtgNujrF?e=download&ax=AA75yW4AMK0Twshr6SdIO0KkQmS-XA_dlQcax49AChhfpdrExg5PKQuy4BeeKX-dX9nGafERudSSI7k7R7gg50vm6YPtvZgK2xJjr2VGfGCbhICUUXoZd7yPzJg-_KKnQ0IVV8Zel8pthFK1ke8yWjBuAQFykFDEPAU1uJM5sYbyasDEAXgwwK56-C0lWfs94LHHM8nAHT5eO1XkaOQ-yc42hFbm4nK3Qp7dESESCQzHpdzZsAwIYTBr_GQ0z5ot8pOMT-x2rlWEFLhgbWb1vF3nABy0iwwWqmAb0HFgnS5qF0zpNZlIy-FqB1JPP3UFSINyjEsqYNas2L1EFVVd9-XtSpJ-rKQ3XV4GZlQ0FOlBv0LoivHcK-ilvL-hOyOR3_toVvzEXN2htIT1feeQjqmw9jGkqsMdQlYVRj65mBwZUqiIn_aSQ4H_jyAAFpJApsyboUtPxkNfXquYRdSb7eQ_NZVp6-3dUAPuP6SpXl95g1XRzGSkDghJrNTIRq81V1fJnYQHrwDmnzHnhbBVgAusxJUVc6I-8A4LfKmVtDNg2f-oNl7QUcSMIvFAmRt9W9Mt5p-grVy7h70Z521S-wdY_OWLkIQ0GQ2VGaLrblbyLXIojnQaxSZXkYoZo-c1qrTNpcTKGGBKZK6_LAWV14QX66BzknzU5rOuQJ5xagfm-vEDAMNFcoDF2VjHnRBL3mxoY5DfDpPKwIVWWX8o0w58Sf5HNqcWGc-QnIz2HHEoF41d9fctXD5xS44uzswW6Tg5d5wKDPNaMNZ3rOvDejGU42WUHsMQCTbNQD7f6EwwXNd7iXqHh9eP1Rr48EtYskAmrj8UEDso4R76PSOXaPL5qio8ZTP_tJJd-8U-6bCbd3R_OhHm0V7OjkMUXZH2Zi6ItH0u5K_uREfyhcilw-xq8hGD8TBsQygq9QjiQt9lwbResxu-iYPQjY03J3fcDTYBA7zsqaK64uegPt4gWRCpRBf-CW6nDsXdPRPbK0ews1thrK1GWsLiKYWelk8Z2Iq41p0cfr4H7j6OnAcg3_EQf_2x3w48s1HCm7vTJfopnMz_czfJ6QcXHA&uuid=c66bf128-a355-4971-92bc-80673c21a9b0&authuser=2&nonce=9okjla8lvhjk2&user=09615949827588626005&hash=gqh9lnierbd57fc08dctccfe6rb7com5'
        url2 = 'https://doc-10-0s-docs.googleusercontent.com/docs/securesc/4t4fg3cla8f4ta3umhgl0o0i7t7983vo/7vjq26eeuncj9qvo63ms7hjfbpo1od6f/1695234075000/09615949827588626005/09615949827588626005/1yUbbEtcaBcHgyu2YjOAs2jgTGGyHa5uc?e=download&ax=AA75yW6LQNSThR1T8t1XQZcpy9MO_Gcz2Mel2PcWTo9yuu-3SC7lqItbVmpJoUyv3d2hv3MBKr2sWZ2mK0yZl0IqxykntXS_lx9EwefGEfRYpvyL10i_BXn6a0ZPoFy62_s2gB8YtImi1KLrDFjQn89f11NGhk0My6zc8sG5b1X9WM62IHVEIHykhwMwSRcsskq2p3ChbIXDH4kbIKVs_HUIkz2fV0tgF0MhT3BHedxI1Un1r8bQymdIs8WVPRuVVgMXmw2BzJltOCZBajPWQuIo_8ug-ot5mpl9Minma0mnkb5IdMWJmEwNq0-0qqisFAUS6BHlL_FwRvNIGEmqU19qHGSK8ToISRbs_u5w_fFVSzCijFZNR4YnKiQTz2QgcCj95C_IfU_UXWWp8cfMaeax81PihVq6Dbi3npl9UNyj2Gl1bd08llJ1eq1qIzUH7Rh5ygUCbxwY4lf-bCLWtvd2C-Vop36qqtJCgB5eHFtQZFi-n035csexqjz9nMYHeqW1fl-s1ZPwP7QNci_FvPII-iW13J5TGiLkuriuQjGCc7UzJIdaG4PSyfYmitcxsVEqldoI0ghbVdiZEFLS2XPdzPSDZQnsg7iSnJ9oAZiO4nrHd4mbiS8VhnVH7sw0zSNG86yR7v-YZR98X7sWkPFrVlzL0fnLDSd4rLb3EIm5hQi2eQsy-Wjc2A5buDRrm7OoguXm43MYSiqOomHHcmleJ5rgoC7qM-Q0TrnzAkMaQwMOD57IC4GOLON6quaLDU3hKLjcStJXqLvw0gVZO0LQ7mt_wpvv-KpaeG8wCx1_l5HHJAB3d6q6SFvFNZIvN2l7dLS8Im3kfMR6k36r_DuMgDiDnzKA8P5ORFQbM1OxEZrxHrhVk1Fg9__l2OPcoKr77SR3Q_ZYbgr_bdzJacySusVXriQfyLVB7jlxLv9iycqUnqeIDewkU8-QXWCC7OUDMnKC1AEAv6llLP73uRfF4SyILBgBOUEPT4yDBKP1M4zXoBj6V3NNabmq0clzM2e1KbCvXr3S_NJpx0IoA3N7djCyoCxG3GASixX7CqRG3-68ycXun_kKqQ&uuid=219b5c0a-e271-4360-9813-272c05b9143a&authuser=2'

        print("Downloading Trained Model...")
        response1 = requests.get(url1, allow_redirects=True)

        print("Downloading A Collection Of Fonts...")
        response2 = requests.get(url2, allow_redirects=True)

        directory = './'

        trained_models2 = os.path.join(directory, 'trained_models.zip')
        ttf_folder = os.path.join(directory, 'ttf_folder.zip')

        with open(trained_models2, 'wb') as file:
            file.write(response1.content)
        print("Saving Trained Model...")

        with open(ttf_folder, 'wb') as file:
            file.write(response2.content)
        print("Saving A Collection Of Fonts...")
        
        
        # Unzip ./trained_models.zip
        print('Unzip ./trained_models.zip')
        os.system("unzip ./trained_models.zip")

        print('Unzip ./ttf_folder.zip')
        os.system("unzip ./ttf_folder.zip")
        
    else:
        print('Skipping... Model exists.')
