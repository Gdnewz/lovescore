print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
names_lover = name1+name2
X_score = names_lover.lower()
#Count_Name1 = (print(len(new_name1.count('t','r', 'u', 'e', 'l','o','v'
#'e'))))
#print(Count_Name1)
Love_Score = str(X_score.count("t") + X_score.count ("r") +
X_score.count("u")+ X_score.count("e"))

True_Score = str(X_score.count("l") + X_score.count ("o") +
X_score.count("v")+ X_score.count("e"))

All_score = Love_Score + True_Score
All_score = int(All_score)

if All_score < 10 or All_score > 90:
    print(f"Your score is {All_score}, you go together like coke and mentos")
elif All_score > 40 and All_score < 50:
    print(f"Your score is {All_score}, you are alright together")
else:
    print(f"Your score is {All_score}")
    

