# Adding a comment to this file
# Add a second comment to this file

print("Welcome to our AWS Acronym Quiz!")

playing = input("Are you ready to play? ")

if playing.lower() != "yes":
    print("Cool, come back when you want to play")
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is the full meaning of Amazon SNS? ")
if answer.lower() == "simple notification service":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does EC2 stand for? ")
if answer.lower() == "elastic compute cloud":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does IAM stand for? ")
if answer.lower() == "identity and access management":
    print("Correct! You are on roll!")
    score += 1
else:
    print("Incorrect! Don't worry you can still get the next one")

answer = input("What is the full meaning of ECR? ")
if answer.lower() == "elastic container registry":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ECS stand for? ")
if answer.lower() == "ec2 container service":
    print("Correct! whoo! let's do this!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does AMI stand for? ")
if answer.lower() == "amazon machine image":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does AZ stand for? ")
if answer.lower() == "availability zone":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does DMS stand for? ")
if answer.lower() == "database migration service":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does EKS stand for? ")
if answer.lower() == "elastic kubernetes service":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does EBS stand for? ")
if answer.lower() == "elastic block store":
    print("Correct! You are simply a genius!")
    score += 1
else:
    print("Incorrect!")
    
    answer = input("What does CLI stand for? ")
if answer.lower() == "command line interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    answer = input("What does CIDR stand for? ")
if answer.lower() == "classless inter-domain routing":
    print("Correct! Great job!")
    score += 1
else:
    print("Incorrect!")
    
    answer = input("What does DDoS stand for? ")
if answer.lower() == "distributed denial of service":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Oh no, better luck next time!")
    
    answer = input("What does SWF stand for? ")
if answer.lower() == "simple workflow service":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does RDS stand for? ")
if answer.lower() == "relational database service":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does JSON stand for? ")
if answer.lower() == "javascript object notation":
    print("Correct! Woohoo, way to go!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("That is " + str((score / 16) * 100) + "%.")
print("We hope that was fun! Do come back again! :)")
