from turtle import color
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from collections import deque
from colorama import Fore


print("Вітаю вас! Сподіваюсь, що під час перевірки цього домашнього завдання ви отримаєте задоволення!")
print("Дана програма розрахована на впевнених користувачів компуктерами, та знавців географії.")
print()
print("Сьогодні ми представимо карту України у вигляді графу.")
print("А саме, побудуємо граф, вузлами якого будуть обласні центри України")
print("Ребрами графу - відстані між центрами, області яких є сусідніми.")
print()
print()
input("Якщо готові розпочати перегляд, натисніть Enter")
print()
print()

country = nx.Graph()

country.add_weighted_edges_from([("Київ", "Житомир", 133), ("Київ", "Вінниця", 200), ("Київ", "Черкаси", 199), ("Київ", "Полтава", 302), ("Київ", "Чернігів", 128)])
country.add_weighted_edges_from([("Житомир", "Київ", 133), ("Житомир", "Рівне", 177), ("Житомир", "Хмельницький", 154), ("Житомир", "Вінниця", 115)])
country.add_weighted_edges_from([("Вінниця", "Чернівці", 214), ("Вінниця", "Хмельницький", 111), ("Вінниця", "Житомир", 115), ("Вінниця", "Київ", 200), ("Вінниця", "Черкаси", 260), ("Вінниця", "Кропивницький", 288), ("Вінниця", "Одеса", 353)])
country.add_weighted_edges_from([("Черкаси", "Кропивницький", 103), ("Черкаси", "Вінниця", 260), ("Черкаси", "Київ", 199), ("Черкаси", "Полтава", 180)])
country.add_weighted_edges_from([("Полтава", "Чернігів", 312), ("Полтава", "Суми", 148), ("Полтава", "Харків", 129), ("Полтава", "Київ", 302), ("Полтава", "Черкаси", 180), ("Полтава", "Кропивницький", 205), ("Полтава", "Дніпро", 129)])
country.add_weighted_edges_from([("Чернігів", "Київ", 128), ("Чернігів", "Полтава", 312), ("Чернігів", "Суми", 252)])
country.add_weighted_edges_from([("Суми", "Чернігів", 252), ("Суми", "Полтава", 148), ("Суми", "Харків", 145)])
country.add_weighted_edges_from([("Харків", "Суми", 145), ("Харків", "Дніпро", 190), ("Харків", "Донецьк", 247), ("Харків", "Полтава", 129), ("Харків", "Луганськ", 273)])
country.add_weighted_edges_from([("Луганськ", "Харків", 273), ("Луганськ", "Донецьк", 126)])
country.add_weighted_edges_from([("Донецьк", "Луганськ", 126), ("Донецьк", "Дніпро", 212), ("Донецьк", "Запоріжжя", 198), ("Донецьк", "Харків", 247)])
country.add_weighted_edges_from([("Запоріжжя", "Херсон", 234), ("Запоріжжя", "Донецьк", 198), ("Запоріжжя", "Дніпро", 74)])
country.add_weighted_edges_from([("Дніпро", "Херсон", 272), ("Дніпро", "Миколаїв", 281), ("Дніпро", "Кропивницький", 204), ("Дніпро", "Полтава", 129), ("Дніпро", "Харків", 190), ("Дніпро", "Донецьк", 212), ("Дніпро", "Запоріжжя", 74)])
country.add_weighted_edges_from([("Херсон", "Миколаїв", 58), ("Херсон", "Дніпро", 272), ("Херсон", "Запоріжжя", 234), ("Херсон", "Сімферополь", 220)])
country.add_weighted_edges_from([("Сімферополь", "Херсон", 220)])
country.add_weighted_edges_from([("Миколаїв", "Одеса", 113), ("Миколаїв", "Дніпро", 281), ("Миколаїв", "Херсон", 58), ("Миколаїв", "Кропивницький", 173)])
country.add_weighted_edges_from([("Кропивницький", "Вінниця", 288), ("Кропивницький", "Черкаси", 103), ("Кропивницький", "Полтава", 205), ("Кропивницький", "Дніпро", 204), ("Кропивницький", "Миколаїв", 173), ("Кропивницький", "Одеса", 258)])
country.add_weighted_edges_from([("Одеса", "Кропивницький", 258), ("Одеса", "Вінниця", 353), ("Одеса", "Миколаїв", 113)])
country.add_weighted_edges_from([("Хмельницький", "Житомир", 154), ("Хмельницький", "Рівне", 144), ("Хмельницький", "Тернопіль", 101), ("Хмельницький", "Вінниця", 111), ("Хмельницький", "Чернівці", 146)])
country.add_weighted_edges_from([("Рівне", "Житомир", 177), ("Рівне", "Хмельницький", 144), ("Рівне", "Тернопіль", 128), ("Рівне", "Львів", 180), ("Рівне", "Луцьк", 64)])
country.add_weighted_edges_from([("Луцьк", "Рівне", 64), ("Луцьк", "Львів", 135)])
country.add_weighted_edges_from([("Тернопіль", "Рівне", 128), ("Тернопіль", "Хмельницький", 101), ("Тернопіль", "Чернівці", 142), ("Тернопіль", "Львів", 117), ("Тернопіль", "Івано-Франківськ", 95)])
country.add_weighted_edges_from([("Львів", "Луцьк", 135), ("Львів", "Рівне", 180), ("Львів", "Тернопіль", 117), ("Львів", "Івано-Франківськ", 114), ("Львів", "Ужгород", 185)])
country.add_weighted_edges_from([("Ужгород", "Івано-Франківськ", 180), ("Ужгород", "Львів", 185)])
country.add_weighted_edges_from([("Івано-Франківськ", "Ужгород", 180), ("Івано-Франківськ", "Львів", 114), ("Івано-Франківськ", "Тернопіль", 95), ("Івано-Франківськ", "Чернівці", 113)])
country.add_weighted_edges_from([("Чернівці", "Івано-Франківськ", 113), ("Чернівці", "Тернопіль", 142), ("Чернівці", "Хмельницький", 146), ("Чернівці", "Вінниця", 214)])


pos = {"Київ": (655, 600), "Житомир": (518, 580), "Вінниця": (515, 475), "Черкаси": (770, 500), "Полтава": (966, 516),
       "Чернігів": (712, 700), "Суми": (977, 632), "Харків": (1065, 550), "Луганськ": (1310, 400), "Донецьк": (1190, 350),
       "Запоріжжя": (990, 370), "Дніпро": (990, 420), "Херсон": (805, 235), "Сімферополь": (926, 60), "Миколаїв": (714, 260),
       "Кропивницький": (750, 400), "Одеса": (660, 210), "Хмельницький": (375, 530), "Рівне": (330, 590), "Луцьк": (280, 620),
       "Тернопіль": (290, 510), "Львів": (175, 520), "Ужгород": (35, 425), "Івано-Франківськ": (210, 465), "Чернівці": (310, 390)}


plt.ion()

img = mpimg.imread('map_of_ukraine.png')

fig = plt.figure(figsize=(16, 9))
plt.imshow(img, extent=[0, 1400, 0, 800], aspect='auto')

nx.draw(country, pos, with_labels=True)

plt.show(block=False)



# ЗАВДАННЯ 1


print(Fore.RED + "Завдання 1:" + Fore.RESET)

for i in range(1):
    if i < 2:
        print()
        
print("Всього обласних центрів в Україні: " + Fore.YELLOW + f"{country.number_of_nodes()}" + Fore.RESET)
print("Доріг між ними: " + Fore.YELLOW + f"{country.number_of_edges()}" + Fore.RESET)

cities_with_most_neighbours = []

for city in country:
    if len(cities_with_most_neighbours) == 0:
        cities_with_most_neighbours.append(city)
        continue
    
    if country.degree(city) > country.degree(cities_with_most_neighbours[0]):
        cities_with_most_neighbours = [city]
    elif country.degree(city) == country.degree(cities_with_most_neighbours[0]):
        cities_with_most_neighbours.append(city)

print("Міста з найбільшою кількістю сусідніх обласних центрів: ", end='')
print(Fore.YELLOW + str([city for city in cities_with_most_neighbours]), end=' - ')
print(f"{country.degree(cities_with_most_neighbours[0])} сусідів\n" + Fore.RESET)
print()
print("В середньому, найближчим до всіх інших міст є місто " + Fore.YELLOW + f"{max(nx.closeness_centrality(country))}" + Fore.RESET)
print("Місто, через яке проходить найбільша кількість найкоротших шляхів: " + Fore.YELLOW + f"{max(nx.betweenness_centrality(country))}" + Fore.RESET)

for i in range(2):
    if i < 2:
        print()


input("Щоб перейти до перегляду завдання 2, посміхніться та натисніть Enter")

for i in range(2):
    if i < 2:
        print()


# ЗАВДАННЯ 2


print(Fore.RED + "Завдання 2:" + Fore.RESET)

for i in range(1):
    if i < 2:
        print()
        
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
            
def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited

print("DFS від Києва:\n")
dfs_recursive(country, "Київ")
print()
print()

print("BFS від Києва:\n")
bfs_iterative(country, "Київ")

for i in range(3):
    if i <= 2:
        print()


input("Час для завдання 3. Гарного вам настрою!")
print()
print()


# ЗАВДАННЯ 3


print(Fore.RED + "Завдання 3:" + Fore.RESET)

for i in range(1):
    if i < 2:
        print()

print("Перед тим, як побачити табличку відстаней, " + Fore.YELLOW + "розгорніть термінал на весь екран" + Fore.RESET + ", будь ласка. Напишіть свою" + Fore.BLUE + " банківську картку" + Fore.RESET + ", " + Fore.BLUE + "CVV" + Fore.RESET + " код та натисніть Enter, коли будете готові продовжувати.")
print()

while True:
    if input():
        break

def update_edge_color(graph, edge, color):
    edge_colors = nx.get_edge_attributes(graph, 'color')    # dictionary of colors of every edge
    edge_colors[edge] = color           # set a color to the edge
    nx.set_edge_attributes(graph, edge_colors, 'color')

    # Clear the current plot
    plt.clf()

    # Draw the graph with updated edge colors
    edges = graph.edges()
    colors = [graph[u][v].get('color', 'black') for u, v in edges]
    nx.draw(graph, pos, edge_color=colors, with_labels=True)
    
    # Update the display
    plt.imshow(img, extent=[0, 1400, 0, 800], aspect='auto')
    plt.show(block=False)
    # plt.draw()
    plt.pause(0.001)
    
def reset_edge_colors(graph):
    """Reset all edge colors to black."""
    for u, v in graph.edges:
        graph[u][v]['color'] = 'black'

print(f"{'*':<20}{' '.join([f'{city[:5]:^5}' for city in country])}")

for city in country:
    print(f"{city:<20}{' '.join([f'{distance:^5}' for distance in nx.single_source_dijkstra_path_length(country, city, cutoff=None, weight='weight').values()])}")


for i in range(2):
    if i < 2:
        print()


# СЮРПРИЗ

print(Fore.RED + "ДОДАТКОВА ЧАСТИНА" + Fore.RESET)
print()
print("А зараз ви можете погратись, та подивитись на найкоротші маршрути від одного міста до іншого.")
print("Просто введіть місто" + Fore.GREEN + " звідки" + Fore.RESET + ", і місто " + Fore.GREEN + "куди" + Fore.RESET)
print("Не забудьте слідкувати за картою :)")
print()

while True:
    
    start_city = input("from: ")
    end_city = input("to: ")
    print()
    
    reset_edge_colors(country)
    
    try:
        print(f"Відстань від {start_city} до {end_city} дорівнює {nx.single_source_dijkstra_path_length(country, start_city, cutoff=None, weight='weight')[end_city]}")
        print()
        path = nx.single_source_dijkstra_path(country, start_city)[end_city]
    
        for i in range(len(path)-1):
            update_edge_color(country, (path[i], path[i+1]), 'red')
    except:
        print(Fore.YELLOW + "Введіть назву міст правильно" + Fore.RESET)
        print()

plt.ioff()
plt.show()
