from Player import Player
from Team import Team
from Card import Card
from Deal import Deal
from MyGUI import MyGUI
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
class Game:
    # def StartGame(self,gui):
    def StartGame(self):
        root = tk.Tk();
        gui = MyGUI(root);

        # gui.WriteToConsole("Concerto game starts: \n");
        
        if gui.StartGameBtn["state"] == tk.NORMAL:
            root.mainloop()
            
        if gui.StartGameBtn["state"] == tk.DISABLED:
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
                    self.deal[i-1].StartDeal(TeamA,TeamB,gui,root);
                    self.deal[i-1].CalculateBonus(TeamA,TeamB,gui,root);
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
                    gui.WriteToConsole(TeamA.TeamName +" is the winner of the game");
                    gui.WriteToConsole(sum(TeamA.TeamScore)+Bonus);
                    break;
                elif sum(TeamB.TeamScore) > 100:
                    gui.WriteToConsole( TeamB.TeamName+" is the winner of the game");
                    gui.WriteToConsole(sum(TeamB.TeamScore)+Bonus);
                    break;
                #If 4 deals are completed
                elif len(self.deal) == 4:
                    if sum(TeamA.TeamScore) > sum(TeamB.TeamScore):
                        gui.WriteToConsole(TeamA.TeamName +"i s the winner of the game");
                        gui.WriteToConsole(sum(TeamA.TeamScore)+Bonus);
                        break;
                    elif sum(TeamA.TeamScore) == sum(TeamB.TeamScore):
                        gui.WriteToConsole("Both teams have tied for the game");
                        break;
                    else:
                        gui.WriteToConsole( TeamB.TeamName+" is the winner of the game");
                        gui.WriteToConsole(sum(TeamB.TeamScore)+Bonus);
                        break;
                else:
                    SetUpNextDeal = True;
                    i+=1;

game = Game();
game.StartGame();