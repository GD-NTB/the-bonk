import requests

name = input('Enter a Geometry Dash user\'s profile name: ')
response = requests.get('https://gdbrowser.com/api/profile/' + name)

data = response.json()

if response.text != '-1':

    print('\nUsername: ' + str(data['username']))
    print('Player ID: ' + str(data['playerID']))
    print('Moderator: ' + ('No' if str(data['moderator']) == '0' else 'Mod' if str(data['moderator']) == '1' else 'Elder'))

    print('\nGlobal rank: ' + (('#' + str(data['rank'])) if str(data['rank']) != '0' else 'None'))
    print('Demons: ' + str(data['demons']))
    print('Creator points: ' + str(data['cp']))

    print('\nStars: ' + str(data['stars']) + ' \u2605')
    print('Diamonds: ' + str(data['diamonds']) + ' \u2666')
    print('Coins: ' + str(data['coins']) + ' \u00a4')

else:
    print('\nAccount \'' + name + '\' does not exist!')