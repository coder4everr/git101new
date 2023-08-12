# def square_area(length, width):
#     return length*width

# square1=square_area(7,4)
# square2=square_area(3,5)
# sum=square1+square2
# print("The area of square1 is",square1)
# print("The area of square2 is",square2)
# print("The sum of both areas is",sum)

# def ranking(points, matches):
#     return points/matches
# pakistan=ranking(2316,20)
# australia=ranking(2714,23)
# india=ranking(3807,33)
# print("Pakistan's rankking is",pakistan)
# print("Australia's rankking is",australia)
# print("India's rankking is",india)
# print(pakistan)

# def convert_seconds(seconds):
#     hours=seconds//3600
#     minutes=(seconds-hours*3600)//60
#     remaining_seconds=seconds-hours*3600-minutes*60
#     return hours, minutes, remaining_seconds
# hours,minutes,seconds=convert_seconds(86000)
# print(hours,":",minutes,":",seconds)


# name="Hamid"
# number=len(name)*2
# print("Hello",name,"your shirt number is",number)
# name="Ali"
# number=len(name)*2
# print("Hello",name,"your shirt number is",number)
# name="Mariam"
# number=len(name)*2
# print("Hello",name,"your shirt number is",number)
# name="M. Wasiq"
# number=len(name)*2
# print("Hello",name,"your shirt number is",number)

# def shirt_num(name):
#     number=len(name)*2
#     print("Hello",name,"your shirt number is",number)
# shirt_num("Hamid")
# shirt_num("Mariam")
# shirt_num("John Smith")
# shirt_num("Pakistan")

# def ranking(opposition_points,team_rating,matches):
#     return(opposition_points+team_rating+50)/(matches+1)
# pak=ranking(3200,116,20)
# print(pak)

# def future(age):
#     current_age=20
#     new_age=age+current_age
#     return new_age
# new_age=future(15)
# print(new_age)

# def user(username):
#     if len(username)<3:
#         print("Please enter a valid username")
#     else:
#         print("Thank you for logging in!")


# user("h")

# x=0
# while x<=5:
#     print(str(x),"people are present today")
#     x += 2
# print("All present")   

# friends=("Hamid"," Mariam", "Wasiq")
# for friend in friends:
#     print("Hello", friend)

# sum=0
# for n in range(1,10):
#     sum=sum+n
# print(sum)

# group_a=["Pakistan","Bangladesh","India", "South Africa","New Zealand"]
# group_b=["Australia","West Indies","England","Sri Lanka","Afghanistan"]
# for home_teams in group_a:
#     for away_teams in group_a:
#         # for home_teams in group_b:
#         #     for away_teams in group_b:
#                 if home_teams!=away_teams:
#                     print(home_teams,"vs",away_teams)


# for n in range(19):
#     if n%2==0:
#         print(n)

# def count_numbers(first, last):
#   # Loop through the numbers from first to last 
#   x = first
#   while x <= last:
#     print(x)
#     x=x+1
# count_numbers(2,6)

# group_a=["Pakistan","Sri Lanka","New Zealand","South Africa","Ireland"]
# group_b=["Australia","India","West Indies","Bangladesh","England"]
# for x in group_a:
#     for y in group_a:
#         for x in group_b:
#             for y in group_b:

#              if x!=y and y!=x:
#                  print(x, "vs", y)


# a="I am conffsed"
# # b=a[0:9]+"u"+a[10:]
# print(a.index("f"))
# print("I" in a)


# def replace_email(emails,old_domain,new_domain):
#     emails="hamidwasif9ar@gmail.com"
#     new_domain="yahoo.com"
#     if "@"+ old_domain in emails:
#         index=emails.index("@"+old_domain)
#         new_email=emails[:index]+("@"+new_domain)
#         return new_email
#     return emails

# price=10
# tax=2.32

# print("Base price: ${:.2f}, Tax: ${}, Total Price: ${}".format(price, tax, (price+tax)))

# def to_celcius(x):
#     return(x-32)*5/9
# for x in range(0,101,10):
#     print ("{:>3} F | {:>6.2f} C".format(x, to_celcius(x)))

# def usd_to_pkr(x):
#     return (x*287.27)
# for x in range(0,501,25):
#     print("${:>3} | PKR {:>5}".format(x,usd_to_pkr(x)))
# multiples=[]
# for x in range(1,6):
#     multiples.append(x*5)
# print(multiples)
# multiple=[x*10 for x in range(1,11)]
# print(multiple)



# points_table={"Pakistan":10, "India":8, "Srilanka":6, "Bangladesh":6}
# for team,points in points_table.items():
#     print("{} have got {} points.".format(team, points))
# print(points_table.keys())
# print(points_table.values())

# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)
# print(wardrobe)
# def year(first, last):
#     return[year for year in range(first, last+1)]
# print(year(2000,2023))
# def odds(first, last):
#     return[odds for odds in range(first, last+1) if odds%2!=0]
# print(odds(16,60))
# class Piglet:
#     years=0
#     def pig_years(self):
#         return self.years *18
# piggy=Piglet()
# piggy.years=2
# print(piggy.pig_years())

# class Jungle:
#     years=0
#     def chirya_years(self):
#         return self.years*4
# chirya=Jungle()
# chirya.years=3
# print(chirya.chirya_years())


# class Gold:
#     weight=""
#     color=""
# x=Gold()
# x.color="golden"
# x.weight="20g"
# print("The color of gold is",x.color, "and its weight is", x.weight)
# class Apple:
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor
#     def __str__(self):
#         return "This apple is {} and {}.".format(self.color, self.flavor)
    
# sweet=Apple("red","tasty")
# print(sweet)

# class Apple:
#      def __init__(self, color, flavor):
#          self.color = color
#          self.flavor = flavor
#      def __str__(self):
#          return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
# jonagold = Apple("red", "sweet")
# print(jonagold)
# import random
# print(random.randint(1,5))

# def calculate_rating(points, matches):
#     return points / matches

# def predict_ratings(team1_matches, team1_points, team1_rating,
#                     team2_matches, team2_points, team2_rating):
#     # Calculate initial ratings for both teams
#     team1_initial_rating = calculate_rating(team1_points, team1_matches)
#     team2_initial_rating = calculate_rating(team2_points, team2_matches)

#     # Simulate the match and update points and matches played accordingly
#     team1_matches += 1
#     team2_matches += 1

#     team1_winning_points = (team1_points + team2_initial_rating + 50) / team1_matches
#     team1_points = round(team1_points + team1_winning_points)

#     team2_losing_points = (team2_points + team1_initial_rating - 50) / team2_matches
#     team2_points = round(team2_points + team2_losing_points)

#     # Calculate updated ratings for both teams
#     team1_updated_rating = calculate_rating(team1_points, team1_matches)
#     team2_updated_rating = calculate_rating(team2_points, team2_matches)

#     return team1_updated_rating, team2_updated_rating

# # Given data for Pakistan and Afghanistan
# pakistan_matches = 20
# pakistan_points = 2320
# pakistan_rating = 116

# afghanistan_matches = 15
# afghanistan_points = 1410
# afghanistan_rating = 94

# # Predict the ratings after the match
# pakistan_updated_rating, afghanistan_updated_rating = predict_ratings(
#     pakistan_matches, pakistan_points, pakistan_rating,
#     afghanistan_matches, afghanistan_points, afghanistan_rating
# )

# # Print the predicted ratings
# print("Predicted Ratings:")
# print(f"Pakistan: {pakistan_updated_rating}")
# print(f"Afghanistan: {afghanistan_updated_rating}")

def get_event_date(event):
    return event.date
def current_users(events):
    events.sort(key=get_event_date)
    machines={}
    for event in events:
        if event.machine not in machines:
            machines[event.machine]=set()
        if event.type =="login":
            machines[event.machine].add(event.user)
        elif event.type=="logout":
            machines[event.machine].remove(event.user)
    return machines
def generate_report(machines):
    for machine, users, in machines.items():
        if len(users)>0:
            user_list=", ".join(users)
            print("{}: {}".format(machine, user_list))
class Event:
    def __init__(self, event_date, event_type,
                 machine_name, user):
        self.date=event_date
        self.type=event_type
        self.machine=machine_name
        self.user=user
events=[Event('2023-08-08 12:12:54','login','myworkstation.local', 'Hamid'),
        Event('2023-08-08 14:13:58','login','webserver.local', 'Hamid'),
        Event('2023-08-08 15:12:54','login','localnetwork.local', 'Saqib'),
        Event('2023-08-08 12:12:54','logout','myworkstation.local', 'Hamid'),
        Event('2023-08-08 13:12:54','login','mywork.local', 'Ahmer'),
        Event('2023-08-08 16:12:54','logout','localnetwork.local', 'Saqib'),
        Event('2023-08-08 10:12:54','login','myworkstation.local', 'Ahmer')]  
users=current_users(events)
print(users)