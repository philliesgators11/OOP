class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition
class NFLTeam:
    def __init__(self, teamName, playerList):
        self.teamName = teamName
        self.playerList = playerList
    def displayTeam(self):
        print(self.teamName)
        print("Players:")
        for player in self.playerList:
            print(f"{player.playerName} - {player.playerPosition}")
player1 = Player("Joe Montana", "Quarterback")
player2 = Player("Barry Sanders", "Running Back")
player3 = Player("Jerry Rice", "Wide Reciever")
player4 = Player("Rob Gronkowski", "Tight End")
player5 = Player("Jordan Mailata", "Right Tackle")
player6 = Player("Quenton Nelson", "Right Guard")
player7 = Player("Jason Kelce", "Center")
player8 = Player("Joe Thuney", "Left Guard")
player9 = Player("Joe Alt", "Left Tackle")
player10 = Player("Graham Gano", "Kicker")

playerList = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]
team = NFLTeam("Valencia Pumas", playerList)
team.displayTeam()
