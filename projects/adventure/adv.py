from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

# Player starts in Room 0
player = Player(world.starting_room)

# List will fill with directions to walk
traversal_path = []

# Inverse directions N/S/E/W
inverse = {"n": "s", "s": "n", "e": "w", "w": "e"}

# Keep track of visited rooms 
visited = set()
# Keep track of exits explored 
exits = {} # player.current_room.get_exits()


# # While all room have not been visited
# while len(visited) < len(room_graph):
#     # Current room
#     room = player.current_room
#     # Get room exits
#     if room.id not in exits:
#         # add exits
#         exits[room.id] = room.get_exits()
#         # mark as visited 
#         visited.add(room.id)

room = player.current_room
exits[room.id] = room.get_exits()
visited.add(room.id)

print(visited)
print(exits)



# # TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
