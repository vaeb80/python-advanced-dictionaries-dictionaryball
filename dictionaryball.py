def strip_list(l):
    return list(map(lambda s: s.strip(), l))

def transpose(data):
    return [*zip(*data)]

def build_player_dictionary(data_list):
    dictionary = {}
    attributes = data_list[0]
    player_list = data_list[1:]
    for player in player_list:
        dictionary[player[0]] = {}
        for i in range (1, len(attributes)):
            dictionary[player[0]][attributes[i]] = int(player[i])
    return dictionary
        
def get_attribute_list_from_line(line):
    number_list = strip_list(line.split('|')[1:-1])
    number_list[0].strip('*')
    number_list[0].replace(' ', '_')
    number_list[0] = str.lower(number_list[0])
    
def build_team_dictionary(filename):
    with open(filename, 'r') as team_file:
        dictionary = {}
        lines = team_file.readlines()
        
        dictionary['team_name'] = lines[0][13:].strip()
        dictionary['colors'] = strip_list(lines[1][10:].split(','))
        
        data_list = []
        for line in lines[5:]:
            l = strip_list(line.split('|')[1:-1])
            l[0] =  l[0].lower().replace(' ', '_').strip('*')
            data_list.append(l)
            
        dictionary['players'] = build_player_dictionary(transpose(data_list))
    return dictionary
        
    
def game_dict():
   return dictionary

dictionary = {'home': build_team_dictionary('home-data.txt'), 
              'away' : build_team_dictionary('away-data.txt')}

    
def get_player_attribute(player_name, attribute):
   try: 
        return game_dict()['home']['players'][player_name][attribute]
   except KeyError:
        try:  
            return game_dict()['away']['players'][player_name][attribute] 
        except KeyError:
            return None
    

def num_points_scored(player_name):
   return get_player_attribute(player_name, 'points')
    
    

def shoe_size(player_name):
   return get_player_attribute(player_name, 'shoe')


def team_colors(team_name):
     if game_dict()['home']['team_name'] == team_name:
         return game_dict()['home']['colors']
     elif game_dict()['away']['team_name'] == team_name:
         return game_dict()['away']['colors']
     else:
         return None

def team_names():
    return [game_dict()['home']['team_name'], game_dict()['away']['team_name']]

def player_numbers(team_name):
    try:
        numbers =[]
        if game_dict()['home']['team_name'] == team_name:
            for player in list(game_dict()['home']['players'].keys()):
                numbers.append(game_dict()['home']['players'][player]['number'])
            return numbers
        else:
            for player in list(game_dict()['away']['players'].keys()):
                numbers.append(game_dict()['away']['players'][player]['number'])
            return numbers
    except KeyError:
        return None
    
    
def player_stats(player_name):
    try: 
        return game_dict()['home']['players'][player_name]
    except KeyError:
        try:  
            return game_dict()['away']['players'][player_name]
        except KeyError:
            return None

def home_team_name():
    return game_dict()['home']['team_name']

def most_points_scored():
    places = ['home', 'away']
    player_points =[]
    for place in places:
        for player in list(game_dict()[place]['players'].keys()):
            player_points.append((player, 
                             game_dict()[place]['players'][player]['points']))
    return sorted(player_points, key= lambda x: x[1], reverse=True )[1][0]

def winning_team():
    teams = []
    places = ['home', 'away']
    for place in places:
        team_points =[]
        for player in list(game_dict()[place]['players'].keys()):
            team_points.append( 
                             game_dict()[place]['players'][player]['points'])
        if place == 'home': 
            teams.append(('home', sum(team_points)))
        elif place == 'away':
            teams.append(('away' , sum(team_points)))
        else:
            break
    place = sorted(teams, key= lambda x: x[1], reverse=True )[0][0]
    return game_dict()[place]['team_name']

def player_with_longest_name(game_dict):
    places = ['home', 'away']
    name_length =[]
    for place in places:
        for player in list(game_dict()[place]['players'].keys()):
            name_length.append((player, 
                             len(player)))
    return sorted(name_length, key= lambda x: x[1], reverse=True )[0][0]

def long_name_steals_a_ton(game_dict):
    pwln = player_with_longest_name(game_dict)
    places = ['home', 'away']
    most_steals =[]
    for place in places:
        for player in list(game_dict()[place]['players'].keys()):
            most_steals.append((player, 
                             game_dict()[place]['players'][player]['steals']))
    pwms = sorted(most_steals, key= lambda x: x[1], reverse=True )[0][0]
    return pwln == pwms



#print(dictionary)

#print(num_points_scored(dictionary, 'Jeff Adrien'))

#print(team_colors(dictionary, 'Broolyn Nets'))

#home_dict = build_team_dictionary('away-data.txt')
#print(home_dict['team_name'])
#print(home_dict['colors'])
#print(home_dict['players'])