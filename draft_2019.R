library(randomForest)
library(ggplot2)

#import draft data 
train=read.csv("all_past.csv")
test=read.csv("today_names.csv")

train1=train[c("Age","G","MP_G","FG","FGA","FG", 
               "X2P","X2PA","X2P","X3P",
               "X3PA","FT","FTA","FT",
               "AST","STL",
               "TOV","PF")]

#train ----------------
#scaling data
train1=scale(train1)
colMeans(train1)

train2=subset(train,select=c("height_diff",
                             "wingspan_diff","reach_diff","weight_diff",
                             "bodyF_diff","handL_diff","orb_diff","drb_diff","blk_diff","VORP_score"))
train2$VORP_score=as.factor(train2$VORP_score)
train_final=cbind(train1,train2)


#test -------------
#scaling data 
test1=test[c("Age","G","MP","FG","FGA","FG", 
             "X2P","X2PA","X2P","X3P",
             "X3PA","FT","FTA","FT",
             "AST","STL",
             "TOV","PF")]

names(test1)[3]="MP_G"
test1=scale(test1)
colMeans(test1)

test2=subset(test,select=c("height_diff",
                           "wingspan_diff","reach_diff","weight_diff",
                           "bodyF_diff","handL_diff","orb_diff","drb_diff","blk_diff"))
test_final=cbind(test1,test2)


#random forest model 
set.seed(355)
rf=randomForest(VORP_score~.,data=train_final)
pred_vorp2=predict(rf,test_final,type="prob")
pred_vorp2=as.data.frame(pred_vorp2)
pred_vorp2=pred_vorp2[1:74,]
names(pred_vorp2)[1]="below_replacement"
names(pred_vorp2)[2]="bench/role player"
names(pred_vorp2)[3]="starter"
names(pred_vorp2)[4]="all-star"
names(pred_vorp2)[5]="elite"

coll_names=test[c("Player","School")][1:74,]
coll_names=as.data.frame(coll_names)

merge=cbind(coll_names,pred_vorp2)
merge$sum_good=rowSums(merge[,c("starter", "all_star","elite")])
merge$all_elite=rowSums(merge[,c("all_star","elite")])
names(merge)[6]="all_star"
names(merge)[7]="elite"
names(merge)[4]="bench"
median(merge$below_replacement)

