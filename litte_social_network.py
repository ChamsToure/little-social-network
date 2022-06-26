# This is another file for the bfs algorithm
# Im trying to create a little social network of my friends
# Search for friendships degrees

from collections import deque

graph = {}
graph["you"] = ["Mert", "Joshua", "Hendrik", "Manaf", "Erkan", "Granit", "Auron", "Elvis","Khalil", "Sascha"]
graph["Mert"] = ["Joshua", "Hendrik", "Manaf", "Erkan", "Granit", "you"]
graph["Joshua"] = ["Mert", "Manaf", "you"]
graph["Hendrik"] = ["Mert", "Erkan", "Granit", "Manaf", "you"]
graph["Manaf"] = ["Mert", "Erkan","Hendrik", "Joshua", "Elvis", "Auron", "you"]
graph["Erkan"] = ["Mert", "Manaf", "Hendrik", "Granit", "you"]
graph["Granit"] = ["Mert", "Hendrik", "you", "Erkan"]
graph["Auron"] = ["Elvis", "Manaf", "you"]
graph["Elvis"] = ["Auron", "Manaf", "you"]
graph["Khalil"] = ["you"]
graph["Sascha"] = ["Lee"]
graph["Lee"] = ["Rocky"]
graph["Rocky"] = ["Balboa"]
graph["Balboa"] = ["Sylvester"]
graph["Sylvester"] = ["Arnold"]

#search_queue = deque()
#search_queue += graph["you"]
#print(search_queue)



def search_degree(start_name, target_name):
    searched = []
    loops = 0
    search_queue = deque()
    degree = 1
    search_queue += graph[start_name]
    last_person = graph[start_name][-1]
    while search_queue:
        print("last person is: ", last_person)
        loops+=1
        person = search_queue.popleft()

        if person not in searched:
            if person == target_name:
                print("We found him!!")
                print("Looped: ", loops)
                print("The degree is: ", degree)
                return {"searched: ": searched, "remaining search queue: ": search_queue}
            else:
                search_queue += graph[person]
                searched.append(person)

        if person == last_person :
            degree += 1
            #print("Last Person updated to: ", last_person)
            if len(search_queue) != 0:
                last_person = graph[person][-1]
    return "The person is not in the network"
        #TODO: Write a function that checks on which degree we are currently

print("Me list: ", graph["you"])
print(search_degree("Erkan", "Sylvester"))





