class Team:
    TeamScore = [];
    TeamName = "";
    PlayersInTeam = [];
    
    # Constructor to initialize team name and players in team
    def __init__(self, TeamName, PlayersInTeam,TeamScore):
        self.TeamName = TeamName;
        self.PlayersInTeam = PlayersInTeam;
        self.TeamScore = TeamScore;
    # Function to add players to team
    def add_player(self, player):
        self.PlayersInTeam.append(player);

    # Function to identify leading and non leading players
    def IdentifyLeadAndNonLead(self,HandNo):
        self.HandNo = HandNo;
        #Returns leading and non leading players
        if (self.TeamName == "NS"):
            if (self.HandNo == 1):
                return self.PlayersInTeam[0],self.PlayersInTeam[1];
            elif (self.HandNo == 3):
                return self.PlayersInTeam[1],self.PlayersInTeam[0];
            elif (self.HandNo == 5):
                return self.PlayersInTeam[0],self.PlayersInTeam[1];
            elif (self.HandNo == 7):
                return self.PlayersInTeam[1],self.PlayersInTeam[0];
        elif (self.TeamName == "EW"):
            if (self.HandNo == 2):
                return self.PlayersInTeam[0],self.PlayersInTeam[1];
            elif (self.HandNo == 4):
                return self.PlayersInTeam[1],self.PlayersInTeam[0];
            elif (self.HandNo == 6):
                return self.PlayersInTeam[0],self.PlayersInTeam[1];
            elif (self.HandNo == 8):
                return self.PlayersInTeam[1],self.PlayersInTeam[0];
