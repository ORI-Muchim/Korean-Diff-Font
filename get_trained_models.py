import os
import requests

trained_models = './trained_models/model700000.pt'

def get_model():
    if not os.path.isfile(trained_models):
        url1 = 'https://doc-0s-0s-docs.googleusercontent.com/docs/securesc/4t4fg3cla8f4ta3umhgl0o0i7t7983vo/bdssedcnlm683607gkgo6vd3vv1tavnf/1695234000000/09615949827588626005/09615949827588626005/1CCYPSh7MQTCaZ-DqP2XbjJx0SXL7uD-q?e=download&ax=AA75yW7tsITMejDMPh6ti4sK0ZEcViiKxqJoRgRJ3TXYy278joI9DgaEqntMQ91stvMs0gGILHa_--2nsL9Ful4Q1uXpo1d5azL8F48A61wGZy-qtTzGKn9GAYTUpSkxt2lacqm3y70gM0B534lsoUj9LHNqxphhiEUPk4Ji3rNO8xpDtflwqz4VbyQTwZtKXBnBb_0U2dYEhIcYqAFSLoHED-Ha4t7UmW7oZKLv8OMvYdNS-rZi3VPEAl7GqlHUMCZ0WKLI7qV-d4ZWiaIcajyRDjCJpEhLNiyNF-KvnN8CbE1tUSPhLQHN-VY9nzUQfUIPpXmiPUa7IQU86SQC4Dcmz0fqa4VxmX8kfORNtlwQ7ExooXKcR2JJ4xMcd2iq9OErmxA8BhFfRugVYCNxblDx2b004CiJOrn3d1K_9Ukjyclz3wXEcTalWeiUkJUXy3oG5DU7KeCQnLUPolMCt-ortserc8193BArtxUxOwI1OsCeZyxlPaj5A8xVRv1DYuYPeX_cLlmSFdjQIe_4pWhrMFXu4_ndtAoq6n_7MT-0vq_KCpjQiRYEiDvi4SnJ6Qc4aP7mq834nzVF2GO2muvx3MgglmEuexiq6WWb1tKVeZDx2M6-wpi1K6ymwFyiBake_l6H5nPk31RLQ6EIxi8-pdsCcO4TQsLoZWfxee005_GC2BbsBzXxVJix4qdex2vMYvr-hWSYQgExT-Q9-nYIAQvNpZGrdrglBUobHRfUimjdhCg1osaMEDd3-8fRPgdJ1vVuKgAVkhRQ_aDvOGbo1clWg81mNsYBJsO9yvH5syxH90EaaCdkX8HiYY72BgJ04HpbndeD4uoUXCvZMejj8edRodwbrrM5IagIz0qRsP-tqF7bUPWtb79odDxID4HNB0qTYxx9qD8nd9ZYgI-4qJnizZcEG93WJ0ii_oPjaTs_cW6m9RCelkHDEf139wII5MWHH4rHrsxmCASNx8e-1w8502mIA7kaZf5zF2d9acRkf0fVsDSXfyqxBewPOw9zb3UdkdBbylgT1xZ5WWxU2kS6QoQ7haHZ2vCMqvxUq0wubl_y4FSP2w&uuid=cab75580-d372-4ba3-bf52-fe48992451f8&authuser=2'
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
