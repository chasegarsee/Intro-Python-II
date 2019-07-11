from player import Player
from room import Room

# Declare all the rooms


room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

player = Player("Garsee", room["outside"])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


print(f"\n------------------------------")
print(f"\n{player.current_room.title}")
print(f"\n   {player.current_room.description}\n")


def print_room(room):
    print(f"\n------------------------------")
    print(f"\n{room.title}")
    print(f"\n   {room.description}\n")


current_room = player.current_room
print_room(current_room)

valid_directions = ["n", "s", "e", "w"]

while True:
    # Print the current room title and description
    current_room = player.current_room
    # Wait for user input
    cmd = input("-> ")
    # Parse User Inputs (n, s, e, w, q)
    if cmd in valid_directions:
        direction = cmd
        if getattr(player.current_room, f"{direction}_to") == None:
            print("Sorry, No Room Here!", "\n")
        else:
            player.current_room = getattr(
                player.current_room, f"{direction}_to")
            print_room(player.current_room)

    elif cmd == "q":
        print("GOODBYE!")
        exit()
    else:
        print("Invalid Command")


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# * If the user enters a cardinal direction, attempt to move to the room there.
