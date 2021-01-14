import requests

class Player:
    def __init__(self, first_name, last_name, season=2020):
        self.first_name = first_name
        self.last_name = last_name
        self.season = season   
        self.url = 'https://www.balldontlie.io/api/v1/'
        self.player_route = 'players/'
        self.info = self.get_info()
    
    def get_player_id(self):      
        payload= {"search": self.last_name}
        players_search = requests.get(self.url + self.player_route, params=payload)
        if players_search.status_code == 404:
            return None
        players = players_search.json()['data']
        for player in players:
            if player['first_name'] == self.first_name:
                return player['id']
        return None

    def _get_stats(self, id):
        payload = {"season": self.season, "player_ids[]": id}
        route = "season_averages"
        stats = requests.get(self.url + route, params=payload).json()
        
        return stats

    def get_photo(self):
        photo = requests.get(f"https://nba-players.herokuapp.com/players/{first_name}/{last_name}")
        return photo
    def get_info(self):
        id = self.get_player_id()
        if id == None:
            return None
        info_route = f"players/{id}"

        info = requests.get(self.url + info_route).json()
        info['stats'] = self._get_stats(id)
        return info

    def get_points(self):
        player = self.info['stats']['data'][0]
        return player['pts']

    
    def __repr__(self):
        return f"{self.info}"


