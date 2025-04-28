def find_team_with_highest_points(football_clubs):
    """
    Function to find football team with highest points

    Args: 
    football_clubs: list of football clubs with properties: name, wins, loss, draws, scored, conceded

    Returns:
    winner: team with highest points
    """

    def calculate_score(team):
        """
        Function to calculate score of team
        """
        points = team["wins"] * 3 + team["draws"]
        goal_diff = team["scored"] - team["conceded"]
        return (points, goal_diff)
    
    best_team = max(football_clubs, key=calculate_score)
    return best_team["name"]


football_clubs = [{"name": "Manchester United","wins": 30,"loss": 3,"draws": 5,"scored": 88,"conceded": 20,},
                {"name": "Arsenal","wins": 24,"loss": 6,"draws": 8,"scored": 98,"conceded": 29,},
                {"name": "Chelsea","wins": 22,"loss": 8,"draws": 8,"scored": 98,"conceded": 29,}]


print(find_team_with_highest_points(football_clubs))