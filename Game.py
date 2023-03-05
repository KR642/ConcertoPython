from Player import Player
from Team import Team
from Card import Card
from Deal import Deal
class Game:
    def StartGame(self):
        print("Concerto game starts: \n");
        self.deal =[];
        # 4 Player object created
        player1 = Player("A","1",[]); 
        player2 = Player("C","2",[]);
        player3 = Player("B","3",[]);
        player4 = Player("D","4",[]);

        # Assign players to different teams
        TeamA = Team("Team A","NS",[],[]);
        TeamB = Team("Team B","EW",[],[]);
        TeamA.add_player(player1);
        TeamA.add_player(player3);
        TeamB.add_player(player2);
        TeamB.add_player(player4);

        i = 1;
        TotalDeals = 4;
        while(i<=TotalDeals):
            card = Card();
            cards = [];
            cards = card.GenerateDeckAndShuffle();

            #Divide and allocate cards to 4 players
            deck1,deck2,deck3,deck4 = [],[],[],[];
            deck1,deck2,deck3,deck4 = card.DivideCards(cards);
            #Allocate cards to players after shuffling
            player1.ReceiveCards(deck1);
            player2.ReceiveCards(deck2);
            player3.ReceiveCards(deck3);
            player4.ReceiveCards(deck4);

            if(i%2!=0):
                TeamA.TeamPos = "NS";
                TeamB.TeamPos = "EW";
                self.deal.append(Deal());
                self.deal[i-1].StartDeal(TeamA,TeamB);
                self.deal[i-1].CalculateBonus(TeamA,TeamB);
            elif(i%2==0):
                TeamA.TeamPos = "EW";
                TeamB.TeamPos = "NS";
                self.deal.append(Deal());
                self.deal[i-1].StartDeal(TeamB,TeamA);
                self.deal[i-1].CalculateBonus(TeamB,TeamA);

            # Check game score
            DealLeft = TotalDeals-i; #Will be dynamically fetched when written in a loop
            Bonus = 100+100*DealLeft; #Bonus to be added
            SetUpNextDeal = False;
            if sum(TeamA.TeamScore) > 100:
                print(TeamA.TeamName +" is the winner of the game");
                print(sum(TeamA.TeamScore)+Bonus);
                break;
            elif sum(TeamB.TeamScore) > 100:
                print( TeamB.TeamName+" is the winner of the game");
                print(sum(TeamB.TeamScore)+Bonus);
                break;
            #If 4 deals are completed
            elif len(self.deal) == 4:
                if sum(TeamA.TeamScore) > sum(TeamB.TeamScore):
                    print(TeamA.TeamName +"i s the winner of the game");
                    print(sum(TeamA.TeamScore)+Bonus);
                    break;
                elif sum(TeamA.TeamScore) == sum(TeamB.TeamScore):
                    print("Both teams have tied for the game");
                    break;
                else:
                    print( TeamB.TeamName+" is the winner of the game");
                    print(sum(TeamB.TeamScore)+Bonus);
                    break;
            else:
                SetUpNextDeal = True;
                i+=1;

    
game = Game();
game.StartGame();