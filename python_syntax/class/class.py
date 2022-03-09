# 체스게임
'''
체스 피스
공격: 나이트 공격력 100 체력 50 회피 80% 
방어: 룩 공격력 30 체력 150 회피 20% 방어 80%
치유: 룩 공격력 0 치유 체력 50회복 체력 150 회피 20% 방어 0
지원: 비숍 공격력 10 체력 50 회피 20%  공격력 5%증가.
퀸 공격력 500 체력 300 회피 20% 방어 80% 공격력 5%증가.
킹 다른 체스피스 전멸일 경우 킹 VS 빌런 대결. 킹은 정해진 체력이 다 닳기 전까지 5번의 공격을 받는다.
공격은 피하는 방법 뿐이다. 5번을 모두 버티면 체스피스 승리 그전에 죽으면 게임 오버
np.round(data, n)
'''
from random import *

class chesspiece:
    def __init__(self,name,piece,rank,villan):
        self.name=name
        self.rank=rank
        self.piece=piece
        self.attack=[]
        self.hp=[]
        self.villan=villan
        self.a=1
    def entry(self):
        for i in range (len(self.name)):
            if self.piece[i]=="나이트":
                self.attack.append(70)
                self.hp.append(30)
                print("{}랭커 {} 계급 {}입장합니다.".format(self.rank[i],self.piece[i],self.name[i]))

            if self.piece[i]=="룩" and self.rank[i]=="A":
                self.attack.append(30)
                self.hp.append(50)
                print("{}랭커 {} 계급 {}입장합니다.".format(self.rank[i],self.piece[i],self.name[i]))

            if self.piece[i]=="룩" and self.rank[i]=="S":
                self.attack.append(0)
                self.hp.append(50)
                print("{}랭커 {} 계급 {}입장합니다.".format(self.rank[i],self.piece[i],self.name[i])) 

            if self.piece[i]=="비숍":
                self.attack.append(10)
                self.hp.append(30)
                print("{}랭커 {} 계급 {}입장합니다.".format(self.rank[i],self.piece[i],self.name[i])) 

            if self.piece[i]=="퀸":
                self.attack.append(100)
                self.hp.append(100)
                print("{}랭커 {} 계급 {}입장합니다.".format(self.rank[i],self.piece[i],self.name[i])) 

        print("킹 이안 입장합니다.") 
        print("\n")   
        print("현재 플레이어 이름 :   {}".format(self.name))
        print("현재 플레이어 계급 :   {}".format(self.piece))
        print("현재 플레이어 랭크 :   {}".format(self.rank))
        print("현재 플레이어 체력 :   {}".format(self.hp))
        print("현재 플레이어 공격력 : {}\n\n".format(self.attack))
        print("\n빌런 체력 : {}".format(self.villan))
    
    def advantage(self,a):
        if self.piece[a]=="비숍":
            for i in range(len(self.name)):
                self.attack[i] = self.attack[i]*105/100
            print("\n{} 계급의 능력으로 모든 플레이어의 공격력이 5% 증가하였습니다.".format(self.piece[a]))
            print("현재 각 플레이어의 공격력은")
            print(self.name)
            print("{}\n".format(self.attack))
        if self.piece[a]=="룩" and self.rank[a]=="S":
            for i in range(len(self.name)):
                self.hp[i]+=10
            self.hp[a]+=10        
            print("\n{}랭킹 {} 계급의 능력으로 모든 플레이어의 체력이 10만큼 회복하였습니다.".format(self.rank[a],self.piece[a]))
            print("{} 계급의 능력으로 자신의 체력이 10만큼 회복하였습니다.".format(self.piece[a]))
            print("현재 각 플레이어의 체력은")
            print(self.name)
            print("{}\n".format(self.hp))
        if self.piece[a]=="퀸":
            for i in range(len(self.name)):
                self.attack[i] = self.attack[i]*105/100
            print("\n{} 계급의 능력으로 모든 플레이어의 공격력이 5% 증가하였습니다.".format(self.piece[a]))
            print("현재 각 플레이어의 공격력은")
            print(self.name)
            print("{}\n".format(self.attack))

    def revenge(self,a,deal):
        if self.piece[a]=="나이트":
            d=randint(1,5)
            if d==1:
                self.hp[a]-=deal
                if self.hp[a]>0:
                    print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 {}".format(self.name[a],deal,self.hp[a]))
                else:
                    print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 0".format(self.name[a],deal))
            else:
                print("{}(이)가 빌런의 공격을 피했습니다. 현재 체력은 {}입니다.".format(self.name[a],self.hp[a])) 
        if self.piece[a]=="비숍":
            d=randint(1,5)
            if d==1:
                print("{}(이)가 빌런의 공격을 피했습니다. 현재 체력은 {}입니다.".format(self.name[a],self.hp[a]))               
            elif d==2:
                self.hp[a]-=deal
                if self.hp[a]>0:
                    print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 {}".format(self.name[a],deal,self.hp[a]))
                else:
                    print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 0".format(self.name[a],deal))
            elif d==3:
                if ("룩" in self.piece):
                    print("{}(이)가 빌런의 공격을 받았습니다. 그러나 룩의 결계가 {}을 보호 해주었습니다. 현재 체력은 {}입니다.".format(self.name[a],self.name[a],self.hp[a]))
                else:
                    self.hp[a]-=deal
                    if self.hp[a]>0:
                        print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 {}".format(self.name[a],deal,self.hp[a]))
                    else:
                        print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 0".format(self.name[a],deal))
            elif d==4:
                if ("퀸" in self.piece):
                    q=self.piece.index("퀸")
                    if self.hp[q]>self.hp[a]:
                        self.hp[q]-=deal
                        print("{}(이)가 빌런의 공격을 받았습니다. 퀸이 대신 공격을 받아 주었습니다. 퀸의 체력이 대신 {}만큼 깎입니다.\n퀸의 현재 체력은 {}, {}의 현재 체력은 {}입니다.".format(self.name[a],deal,self.hp[q],self.name[a],self.hp[a]))
                    else:
                        self.hp[a]-=deal
                        if self.hp[a]>0:
                            print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 {}".format(self.name[a],deal,self.hp[a]))
                        else:
                            print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 0".format(self.name[a],deal))
                else:
                    self.hp[a]-=deal
                    if self.hp[a]>0:
                        print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 {}".format(self.name[a],deal,self.hp[a]))
                    else:
                        print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 0".format(self.name[a],deal))
            else:
                if ("나이트" in self.piece):
                    print("{}(이)가 빌런의 공격을 받았습니다. 나이트가 {}을 데리고 공격을 피했습니다. 현재 체력은 {}입니다.".format(self.name[a],self.name[a],self.hp[a]))
                else:
                    self.hp[a]-=deal
                    if self.hp[a]>0:
                        print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 {}".format(self.name[a],deal,self.hp[a]))
                    else:
                        print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 0".format(self.name[a],deal))
        if (self.piece[a]=="룩" and self.rank[a]=="S"): 
            d=randint(1,5)
            if d==1:
                print("{}(이)가 빌런의 공격을 피했습니다. 현재 체력은 {}입니다.".format(self.name[a],self.hp[a]))               
            elif d==2:
                self.hp[a]-=deal
                if self.hp[a]>0:
                    print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 {}".format(self.name[a],deal,self.hp[a]))
                else:
                    print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 0".format(self.name[a],deal))
            elif d==3:
                if ("룩" in self.piece):
                    print("{}(이)가 빌런의 공격을 받았습니다. 그러나 룩의 결계가 {}을 보호 해주었습니다. 현재 체력은 {}입니다.".format(self.name[a],self.name[a],self.hp[a]))
                else:
                    self.hp[a]-=deal
                    if self.hp[a]>0:
                        print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 {}".format(self.name[a],deal,self.hp[a]))
                    else:
                        print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 0".format(self.name[a],deal))
            elif d==4:
                if ("퀸" in self.piece):
                    q=self.piece.index("퀸")
                    if self.hp[q]>self.hp[a]:
                        self.hp[q]-=deal
                        print("{}(이)가 빌런의 공격을 받았습니다. 퀸이 대신 공격을 받아 주었습니다. 퀸의 체력이 대신 {}만큼 깎입니다.\n퀸의 현재 체력은 {}, {}의 현재 체력은 {}입니다.".format(self.name[a],deal,self.hp[q],self.name[a],self.hp[a]))
                    else:
                        self.hp[a]-=deal
                        if self.hp[a]>0:
                            print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 {}".format(self.name[a],deal,self.hp[a]))
                        else:
                            print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 0".format(self.name[a],deal))
                else:
                    self.hp[a]-=deal
                    if self.hp[a]>0:
                        print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 {}".format(self.name[a],deal,self.hp[a]))
                    else:
                        print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 0".format(self.name[a],deal))
            else:
                if ("나이트" in self.piece):
                    print("{}(이)가 빌런의 공격을 받았습니다. 나이트가 {}을 데리고 공격을 피했습니다. 현재 체력은 {}입니다.".format(self.name[a],self.name[a],self.hp[a]))
                else:
                    self.hp[a]-=deal
                    if self.hp[a]>0:
                        print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 {}".format(self.name[a],deal,self.hp[a]))
                    else:
                        print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 0".format(self.name[a],deal))
        if self.piece[a]=="룩" and self.rank[a]=="A":
            d=randint(1,5)
            defence=randint(1,5)
            if d==1:
                print("{}(이)가 빌런의 공격을 피했습니다. 현재 체력은 {}입니다.".format(self.name[a],self.hp[a])) 
            elif d!=1 and defence!=1:
                print("{}(이)가 빌런의 공격을 방어했습니다. 현재 체력은 {}입니다.".format(self.name[a],self.hp[a])) 
            elif defence==1 and d!=1:
                self.hp[a]-=deal
                if self.hp[a]>0:
                    print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 {}".format(self.name[a],deal,self.hp[a]))
                else:
                    print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 0".format(self.name[a],deal))
        if self.piece[a]=="퀸":
            d=randint(1,5)
            defence=randint(1,5)
            if d==1:
                print("{}(이)가 빌런의 공격을 피했습니다. 현재 체력은 {}입니다.".format(self.name[a],self.hp[a])) 
            elif d!=1 and defence!=1:
                print("{}(이)가 빌런의 공격을 방어했습니다. 현재 체력은 {}입니다.".format(self.name[a],self.hp[a]))              
            elif defence==1 and d!=1:
                self.hp[a]-=deal
                if self.hp[a]>0:
                    print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 {}".format(self.name[a],deal,self.hp[a]))
                else:
                    print("{}(이)가 빌런의 공격을 피하지 못하였습니다. 체력이 {}만큼 깎입니다. 남은 체력은 0".format(self.name[a],deal))
    
    def check_die(self,num):
        if self.hp[num]<=0:
            print("\n{} 계급 {}(이)가 전사하였습니다.\n\n".format(self.piece[num],self.name[num]))
            del self.name[num]
            del self.rank[num]
            del self.piece[num]
            del self.attack[num]
            del self.hp[num]
        else:
            pass

    def game_attack(self,round):
        round+=1
        print("\n\n\n\nround {}\n".format(round))
        for i in range (len(self.name)):
            print("\n\n{}번째 공격을 시작합니다.\n".format(i+1))
            i+=1
            self.a=randint(0,len(self.name)-1)
            for j in range(len(self.name)):
                if j==self.a:
                    print("{} 계급 {}(이)가 공격합니다.".format(self.piece[j],self.name[j]))
                    self.villan -= self.attack[j]
                    if self.villan<=0:
                        self.villan=0
                    print("{}의 공격으로 빌런의 체력이 {}깎였습니다. 남은 빌런의 체력은 {}입니다.".format(self.name[j],self.attack[j],self.villan))
                    if self.villan>0:
                        self.advantage(j)                           
                        print("빌런이 {}에게 반격합니다.".format(self.name[j]))
                        self.revenge(j,70)
                        self.check_die(j)
                        break
            if self.villan<=0:
                break    
            
        if self.villan<=0:
            print("\n\n\n\n축하합니다. 빌런을 물리쳤습니다!!")
            print("남은 player : {}".format(self.name))
            for i in range(len(self.name)):
                print("{}의 체력 : {}".format(self.name[i],self.hp[i]))
                print("{}의 현재 공격력 : {}".format(self.name[i],self.attack[i]))
            return(self.villan)
        else:
            if len(self.name)==0:
                self.end_game()
                return(self.villan)
            if len(self.name)==1:
                self.game_attack(round)
                return(self.villan)
            if len(self.name)>1:
                self.whole_attack(round)
                return(self.villan)
                
    def whole_attack(self,round):   
        check=[]
        print("\n\n빌런의 광역공격이 시작됩니다.")             
        print("빌런이 팀 전체에 공격을 합니다. 모든 팀원의 체력이 100 씩 깎입니다.\n")
        for i in range(len(self.name)):
            self.revenge(i,100)
            if self.hp[i]<=0:
                check.append(i)
        if len(check)==0:
            pass
        else:
            for i in range (len(check)):
                if i>=1:
                    check[i]-=i
                print("\n{} 계급 {}(이)가 전사하였습니다.\n\n".format(self.piece[check[i]],self.name[check[i]]))
                del self.name[check[i]]
                del self.rank[check[i]]
                del self.piece[check[i]]
                del self.attack[check[i]]
                del self.hp[check[i]]
        if len(self.name)==0:
            self.end_game()
            return(self.villan)
        else:
            print("\n현재 남아있는 player : {}\n\n".format(self.name))
            self.game_attack(round)
            return(self.villan)


    def end_game(self):
        print("플레이어가 모두 사망했습니다. 킹 이안은 이곳에서 홀로 도망쳐야 합니다.")
        print("3번의 공격을 모두 피하면 성공적으로 도망칠 수 있습니다.\n건투를 빕니다.")
        for i in range (3):
            run=randint(1,2)
            print("{}번째 시도".format(i+1))
            if run==1:
                print("탈출 실패!! 킹 역시 빌런에게 사망하고 말았다...")
                break
            else:
                if i==2:
                    print("탈출 성공!! 승리하셨습니다.")
                    break
                else:
                    print("무사히 피했습니다.")
                    continue


class main(chesspiece):
    def __init__(self, name, piece, rank, villan):
        super().__init__(name, piece, rank, villan)
        chesspiece.entry(self)
        chesspiece.game_attack(self,0)

            
            

villan=1000
name=["시아","에드윈","세르엘","디오","로웬"]
piece=["퀸","나이트","비숍","룩","룩"]
rank=["none","A","A","A","S"]
chess_game=main(name,piece,rank,villan)

