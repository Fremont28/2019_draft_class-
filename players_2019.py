import numpy as np 
import pandas as pd 


##6/13/19---update based on over and under by position 
tr=pd.read_csv("train_high.csv",encoding="latin-1") #Former NBA Draft Picks 
te=pd.read_csv("test_high.csv",encoding="latin-1") #Current 2019 Draft Prospects 
tr.pos1.unique()

def pos_flex(x):
    if x==1:
        return "center"
    if x==2:
        return "forward"
    else:
        return "guard"

tr['pos_name']=tr['pos1'].apply(pos_flex)


#train median (positions)- fix drb, stl, blk, orb
tr_pos=tr.groupby('pos_name')[["Height..No.Shoes.","Height..With.Shoes.","Wingspan","Standing.reach","Weight","Body.Fat","Hand..Length.","Hand..Width.","ORB","DRB","BLK"]].median()
tr_pos.columns=['height_no_shoes1','height_w_shoes1','wingspan1','standing.reach1','weight1','body.fat1','hand.length1','hand.width1','orb1','drb1','blk1']

#centers 
tr_center=tr[tr.pos_name=="center"]
tr_center.shape #31 centers 
tr_center_pos=tr_pos.iloc[0,]
tr_center_pos=pd.DataFrame(tr_center_pos)
tr_center_pos=tr_center_pos.T 
tr_center_pos.reset_index(level=0,inplace=True)
tr_c=tr_center_pos
tr_c=pd.concat([tr_c]*31)
tr_c.reset_index(level=0,inplace=True)
tr_c=tr_c.iloc[:,0:13]
tr_center.reset_index(level=0,inplace=True)

ca=pd.concat([tr_c,tr_center],axis=1) 
ca['height_diff']=ca['Height..No.Shoes.']-ca['height_no_shoes1']
ca['wingspan_diff']=ca['Wingspan']-ca['wingspan1']
ca['reach_diff']=ca['Standing.reach']-ca['standing.reach1']
ca['weight_diff']=ca['Weight']-ca['weight1']
ca['bodyF_diff']=ca['Body.Fat']-ca['body.fat1']
ca['handL_diff']=ca['Hand..Length.']-ca['hand.length1']
ca['orb_diff']=ca['ORB']-ca['orb1']
ca['drb_diff']=ca['DRB']-ca['drb1']
ca['blk_diff']=ca['BLK']-ca['blk1']
ca=ca.drop('level_0',1)

#forwards 
tr_forward=tr[tr.pos_name=="forward"]
tr_forward.shape #115 fowards 
tr_forward_pos=tr_pos.iloc[1,]
tr_forward_pos=pd.DataFrame(tr_forward_pos)
tr_forward_pos=tr_forward_pos.T 
tr_forward_pos.reset_index(level=0,inplace=True)
tr_f=tr_forward_pos
tr_f=pd.concat([tr_f]*115)
tr_f.reset_index(level=0,inplace=True)
tr_f=tr_f.iloc[:,1:13]
tr_forward.reset_index(level=0,inplace=True)

fo=pd.concat([tr_f,tr_forward],axis=1) 
fo['height_diff']=fo['Height..No.Shoes.']-fo['height_no_shoes1']
fo['wingspan_diff']=fo['Wingspan']-fo['wingspan1']
fo['reach_diff']=fo['Standing.reach']-fo['standing.reach1']
fo['weight_diff']=fo['Weight']-fo['weight1']
fo['bodyF_diff']=fo['Body.Fat']-fo['body.fat1']
fo['handL_diff']=fo['Hand..Length.']-fo['hand.length1']
fo['orb_diff']=fo['ORB']-fo['orb1']
fo['drb_diff']=fo['DRB']-fo['drb1']
fo['blk_diff']=fo['BLK']-fo['blk1']


#guards
tr_guard=tr[tr.pos_name=="guard"]
tr_guard.shape #129 gaurds 
tr_guard_pos=tr_pos.iloc[2,]
tr_guard_pos=pd.DataFrame(tr_guard_pos)
tr_guard_pos=tr_guard_pos.T 
tr_guard_pos.reset_index(level=0,inplace=True)
tr_g=tr_guard_pos
tr_g=tr_g.drop('index',1)
tr_g.reset_index(level=0,inplace=True)
tr_g=pd.concat([tr_g]*129)
tr_g.reset_index(level=0,inplace=True)
tr_g=tr_g.iloc[:,1:13]
tr_guard.reset_index(level=0,inplace=True)

gu=pd.concat([tr_g,tr_guard],axis=1) 
gu['height_diff']=gu['Height..No.Shoes.']-gu['height_no_shoes1']
gu['wingspan_diff']=gu['Wingspan']-gu['wingspan1']
gu['reach_diff']=gu['Standing.reach']-gu['standing.reach1']
gu['weight_diff']=gu['Weight']-gu['weight1']
gu['bodyF_diff']=gu['Body.Fat']-gu['body.fat1']
gu['handL_diff']=gu['Hand..Length.']-gu['hand.length1']
gu['orb_diff']=gu['ORB']-gu['orb1']
gu['drb_diff']=gu['DRB']-gu['drb1']
gu['blk_diff']=gu['BLK']-gu['blk1']

all_past=pd.concat([ca,gu,fo],axis=0)
all_past.to_csv("all_past.csv")


#2019 Draft Class --------------------------
te['pos_name']=te['pos1'].apply(pos_flex)

#test median (positions)
te_pos=te.groupby('pos_name')[["Height.w.o.Shoes","draft_lotto","Wingspan","Standing.Reach","Weight","Body.Fat..","Hand.Length","Hand.Width","ORB","DRB","BLK"]].median()
te_pos.columns=['height_no_shoes1','height_w_shoes1','wingspan1','standing.reach1','weight1','body.fat1','hand.length1','hand.width1','orb1','drb1','blk1']

#centers 
te_center=te[te.pos_name=="center"]
te_center.shape #11 centers 
te_center_pos=te_pos.iloc[0,]
te_center_pos=pd.DataFrame(te_center_pos)
te_center_pos=te_center_pos.T 
te_center_pos.reset_index(level=0,inplace=True)
te_c=te_center_pos
te_c=pd.concat([te_c]*11)
te_c.reset_index(level=0,inplace=True)
te_c=tr_c.iloc[:,0:13]
te_center.reset_index(level=0,inplace=True)

ca1=pd.concat([te_c,te_center],axis=1) 
ca1['height_diff']=ca1['Height.w.o.Shoes']-ca1['height_no_shoes1']
ca1['wingspan_diff']=ca1['Wingspan']-ca1['wingspan1']
ca1['reach_diff']=ca1['Standing.Reach']-ca1['standing.reach1']
ca1['weight_diff']=ca1['Weight']-ca1['weight1']
ca1['bodyF_diff']=ca1['Body.Fat..']-ca1['body.fat1']
ca1['handL_diff']=ca1['Hand.Length']-ca1['hand.length1']
ca1['orb_diff']=ca1['ORB']-ca1['orb1']
ca1['drb_diff']=ca1['DRB']-ca1['drb1']
ca1['blk_diff']=ca1['BLK']-ca1['blk1']
ca1=ca1.drop('level_0',1)

ca1=ca1[["Player","School","Conf","Age","G","MP","FG","FGA","FG.","X2P","X2PA","X2P.","X3P",
"X3PA","X2P.","X3P","X3PA","X3P","FT","FTA","FT.","AST","STL","height_diff",
"wingspan_diff","reach_diff","weight_diff","bodyF_diff","handL_diff","TOV","PF","orb_diff",
"drb_diff","blk_diff"]]
ca1=ca1.dropna()

#forwards 
tr_forward=te[te.pos_name=="forward"]
tr_forward.shape #31 fowards 
tr_forward_pos=te_pos.iloc[1,]
tr_forward_pos=pd.DataFrame(tr_forward_pos)
tr_forward_pos=tr_forward_pos.T 
tr_forward_pos.reset_index(level=0,inplace=True)
tr_f=tr_forward_pos
tr_f=pd.concat([tr_f]*31)
tr_f.reset_index(level=0,inplace=True)
tr_f=tr_f.iloc[:,1:13]
tr_forward.reset_index(level=0,inplace=True)

fo=pd.concat([tr_f,tr_forward],axis=1) 
fo['height_diff']=fo['Height.w.o.Shoes']-fo['height_no_shoes1']
fo['wingspan_diff']=fo['Wingspan']-fo['wingspan1']
fo['reach_diff']=fo['Standing.Reach']-fo['standing.reach1']
fo['weight_diff']=fo['Weight']-fo['weight1']
fo['bodyF_diff']=fo['Body.Fat..']-fo['body.fat1']
fo['handL_diff']=fo['Hand.Length']-fo['hand.length1']
fo['orb_diff']=fo['ORB']-fo['orb1']
fo['drb_diff']=fo['DRB']-fo['drb1']
fo['blk_diff']=fo['BLK']-fo['blk1']


fo=fo[["Player","School","Conf","Age","G","MP","FG","FGA","FG.","X2P","X2PA","X2P.","X3P",
"X3PA","X2P.","X3P","X3PA","X3P","FT","FTA","FT.","AST","STL","height_diff",
"wingspan_diff","reach_diff","weight_diff","bodyF_diff","handL_diff","TOV","PF","orb_diff",
"drb_diff","blk_diff"]]

#guards
tr_guard=te[te.pos_name=="guard"]
tr_guard.shape #32 guards 
tr_guard_pos=te_pos.iloc[2,]
tr_guard_pos=pd.DataFrame(tr_guard_pos)
tr_guard_pos=tr_guard_pos.T 
tr_guard_pos.reset_index(level=0,inplace=True)
tr_g=tr_guard_pos
tr_g=tr_g.drop('index',1)
tr_g.reset_index(level=0,inplace=True)
tr_g=pd.concat([tr_g]*32)
tr_g.reset_index(level=0,inplace=True)
tr_g=tr_g.iloc[:,1:13]
tr_guard.reset_index(level=0,inplace=True)

gu=pd.concat([tr_g,tr_guard],axis=1) 
gu['height_diff']=gu['Height.w.o.Shoes']-gu['height_no_shoes1']
gu['wingspan_diff']=gu['Wingspan']-gu['wingspan1']
gu['reach_diff']=gu['Standing.Reach']-gu['standing.reach1']
gu['weight_diff']=gu['Weight']-gu['weight1']
gu['bodyF_diff']=gu['Body.Fat..']-gu['body.fat1']
gu['handL_diff']=gu['Hand.Length']-gu['hand.length1']
gu['orb_diff']=gu['ORB']-gu['orb1']
gu['drb_diff']=gu['DRB']-gu['drb1']
gu['blk_diff']=gu['BLK']-gu['blk1']


gu=gu[["Player","School","Conf","Age","G","MP","FG","FGA","FG.","X2P","X2PA","X2P.","X3P",
"X3PA","X2P.","X3P","X3PA","X3P","FT","FTA","FT.","AST","STL","height_diff",
"wingspan_diff","reach_diff","weight_diff","bodyF_diff","handL_diff","TOV","PF","orb_diff",
"drb_diff","blk_diff"]]

today_names=pd.concat([gu,fo,ca1],axis=0)
today_names=today_names.dropna()
today_names.to_csv("today_names.csv") #export to csv 