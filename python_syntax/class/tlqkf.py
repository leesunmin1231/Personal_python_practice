from random import*
class player_entry:
    def __init__(self,player,speed):
        self.player=player
        self.speed=speed
    def entry(self):
        for i in range (len(self.player)):
            print("{}번 선수 입장합니다. 선수 이름: {}, {}속도로 달립니다.".format(i+1,self.player[i],self.speed[i]))
        print("\n\n게임을 시작합니다.\n")
class game_start(player_entry):
    def __init__(self,player,speed):
        self.player=player
        self.speed=speed
    def item(self):
        for i in range(len(self.player)):
            it=randint(1,2)
            if it==1:
                self.speed[i] +=20
                print("{} 선수 가속 아이템을 획득합니다. 속도 {}으로 달립니다.".format(self.player[i],self.speed[i]))
            elif it==2:
                self.speed[i] -=20
                print("{} 선수 감속 아이템을 획득합니다. 속도 {}으로 달립니다.".format(self.player[i],self.speed[i]))
    def fly(self):
        for i in range(len(self.player)):
            it=randint(1,2)
            if it==1:
                self.speed[i] +=100
                print("{} 선수 날개 아이템을 획득합니다. 속도 {}으로 날아갑니다.".format(self.player[i],self.speed[i]))
            else:
                print("{} 선수 날개 아이템을 얻지 못하였습니다. 원래 속도로 달립니다.".format(self.player[i]))
    def main(self):
        total =1000
        time=[]
        print("\n\n   <선수 기록>")
        for i in range(len(self.player)):
            player_time=total/self.speed[i]
            time.append(player_time)
        for i in range(len(self.player)):
            time[i]=round(time[i],1)
            print({self.player[i]:"{}초".format(time[i])})

class main_game(game_start):

    def __init__(self,player,speed):
        game=player_entry(player,speed)
        game.__init__(player,speed)
        print("\n<선수 입장>\n")
        game.entry()
        main=game_start(player,speed)
        main.item()   
        print("\n\n")
        main.fly()
        main.main()



player=["짱구","맹구","훈이","철수","유리"]
speed=[50,40,30,160,80]
game=main_game(player,speed)




