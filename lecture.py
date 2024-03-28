place = input("Choose a place: forest or cave?")
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    action = input("Do you want to light a torch or proceed in the dark?")
    if action == "light a torch":
        print("Light the torch!")
    elif action == "proceed in the dark":
        print("You found a boat!")



attendees = input("Enter number of attendees")

if int(attendees) > 100:
    venue = "large hall"
    print("We recommend an audio system")
else:
    venue = "conference room"    
    print("We recommend a projector")
print(venue)

user_input = input("Would you like vegetarin food")
if user_input == "yes":
    print("Veggie delight caterers")
else:
    print("Gourmet meal catererrs")

      