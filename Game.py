from Player import Player
from Team import Team
from Card import Card
from Deal import Deal
class Game:
    def StartGame(self):
        print("Concerto game starts: \n");

        # 4 Player object created
        player1 = Player("North","1"); 
        player2 = Player("East","2");
        player3 = Player("South","3");
        player4 = Player("West","4");

        # Assign players to different teams
        NS = Team("NS",[]);
        EW = Team("EW",[]);
        NS.add_player(player1);
        NS.add_player(player3);
        EW.add_player(player2);
        EW.add_player(player4);
        

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

        #test deal obj creation
        deal = Deal();
        deal.StartDeal(NS,EW);
        

game = Game();
game.StartGame();
