import pickle

with open("profile.pickle","rb") as profile_file:
    profile=pickle.load(profile_file)
    print(profile)

with open("chess.txt","w",encoding="utf8") as chessman:
    chessman_num='"king":"1","queen":"1","bishop":"2","rook":"2","knight":"2","pawn":"8"'
    chessman.write(chessman_num)

with open("chess.txt","r",encoding="utf8") as chessman:
    print(chessman.read())