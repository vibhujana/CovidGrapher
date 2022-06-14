import urllib.request
import matplotlib.pyplot as plt
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
#['Province_State', 'American Samoa', 'Guam', 'Northern Mariana Islands', 'Puerto Rico', 'Virgin Islands', 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'Diamond Princess', 
#'Grand Princess']
state1 = input("Enter state: (Make sure first letter in each letter is Cap): ")
state2 = input("Enter state: (Make sure first letter in each letter is Cap): ")
state3 = input("Enter state: (Make sure first letter in each letter is Cap): ")
places = [state1,state2,state3]
requestURL = urllib.request.urlopen(url)
8
lines = requestURL.readlines()
names = [str(line).split(",")[6] for line in lines]
states = []
# for state in names:
#     if(state not in states):
#         states.append(state)
# print(states)
indices = []
loc = 0
for i in range(len(places)):
    indices.append([i for i, x in enumerate(names) if x == places[loc]])
    loc = loc + 1
data_sets = []
for i in range(len(indices)):
    data_sets.append([str(lines[index]).split(",")[13:-1] for index in indices[i]])





#data_sets is a list(each state) of list(each region) of strings(data points)
#make method to combine the region data for states


# [[[1,5,6][5,3,2][5]][[][][][]]

def get_state_data_set(data_set):

    state_data = [0 for i in range(len(data_set[0]))]
    for i in range(len(data_set[0])):   #loop over index i in each array
        for j in range(len(data_set)):  
            state_data[i] += int(data_set[j][i])

    return state_data

# print(get_state_data_set([[10,12,13],[1,2,3]]))

def get_avg_from(data_set,start,end):
    avg = (data_set[start] - data_set[end])/ (start - end)
    return avg
def avg_if_following_rules(avg):
    return avg * 0.35



combined_data = [get_state_data_set(data) for data in data_sets]
state_trajectory = [get_avg_from(data,len(data) - 11, len(data) - 1) for data in combined_data]
current_date = len(combined_data[0])

for i in range(len(combined_data)):
    for j in range(100):
        last_loc = len(combined_data[i]) - 1
        combined_data[i].append(int(combined_data[i][last_loc] + state_trajectory[i]))

a = [pow(10, i) for i in range(10)]
fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)
colors = ["g-","r-","b-"]
# num = 0
for num,data in enumerate(combined_data):
    y = [int(val) for val in data]

    plt.plot(y,colors[num % len(colors)],label = places[num])
    # num = num + 1
    plt.legend(loc="upper left")
plt.axvline(x=current_date)
plt.title("COVID-19 Infections")
plt.xlabel("Days Since 1/22/20")
plt.ylabel("Infected")
plt.show()