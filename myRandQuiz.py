import random
import pygame
# import time

quizArr =[{1: ["What is the full meaning of Amazon SNS? ","simple notification service"]},
{2: ["What does EC2 stand for? ", "elastic compute cloud"]}, 
{3: ["What does IAM stand for? ", "identity and access management"]}, 
{4: ["What is the full meaning of ECR? ", "elastic container registry"]},
{5: ["What is the full meaning of AMI? ", "amazon machine image"]}, 
{6: ["What does ECS stand for? ", "elastic container service"]}, 
{7: ["What does AZ stand for? ","availability zone" ]}, 
{8: ["What does DMS stand for? ", "database migration service"]}, 
{9: ["What does EKS stand for? ", "elastic kubernetes service"]}, 
{10: ["What does EBS stand for? ", "elastic block store"]}, 
{11: ["What does CLI stand for? ", "command line interface"]},
{12: ["What does CIDR stand for? ", "classless inter-domain routing"]}, 
{13: ["What does DDoS stand for? ","distributed denial of service"]},
{14: ["What does SWF stand for? ", "simple workflow service"]}, 
{15: ["What does RDS stand for? ", "relational database service"]},
{16: ["What does JSON stand for? ", "javascript object notation"]}]
pygame.mixer.init()
pygame.init()
game_sound = pygame.mixer.Sound("game.wav")

score= 0
# Exit with Pressing CTRL+C to quit
while True:
    game_sound.play()
    num = random.randint(0, 15)

    for key in quizArr[num].keys():
        print(key, ". ", sep="", end=" ")
        print(quizArr[num][key][0])
        userInput = input("Enter your answer: ").lower()
        arrQuiz = [*quizArr[num][key]]
        if userInput in arrQuiz:
            score+= 1
            print("correct!!!😎", "Current Score:", score)
        else:
             print("incorrect😌", "Current Score:", score)
# for ques in quizArr:
#     # print(ques.keys())
#     for key in ques.keys():
#         # print(ques[key][0])
#         # print(ques[key][1])
#         break

