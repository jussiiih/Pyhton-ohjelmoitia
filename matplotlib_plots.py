import matplotlib.pyplot as plt
from matplotlib import colormaps 
import pandas as pd

# To test this code, change these filepaths to 
# the correspond filepaths of rain2015.csv, rain2014.csv, and umbrella.jpg files

rain2015 = pd.read_csv("C:\\Users\\Jussi\\OneDrive - Brights\\Documents\\Checkpointit\\Checkpoint9\\Task2\\rain_2015.csv")
rain2014 = pd.read_csv("C:\\Users\\Jussi\\OneDrive - Brights\\Documents\\Checkpointit\\Checkpoint9\\Task2\\rain_2014.csv")
image_filepath = "C:\\Users\\Jussi\\OneDrive - Brights\\Documents\\Checkpointit\\Checkpoint9\\Task2\\umbrella.jpg"

# The rest of the code does not require any adjustments for testing

rain2015_sum =rain2015.sum(axis='rows')
x2015 = rain2015_sum.index
x2015 = x2015[1:]
y2015 = rain2015_sum.values
y2015 = y2015[1:]

rain2014_sum =rain2014.sum(axis='rows')
x2014 = rain2014_sum.index
x2014 = x2014[1:]
y2014 = rain2014_sum.values
y2014 = y2014[1:]

plt.figure(figsize=(10,6))

plt.subplot(2,2,1)
plt.plot(x2015,y2015, color = 'blue')
plt.gca().set_title('Rainfall per month in 2015')

plt.subplot(2,2,2)
explode = (0, 0, 0, 0,0,0,0.2,0,0,0,0,0)
plt.pie(y2015, labels=x2015, explode=explode, colors=list(plt.get_cmap('Paired').colors))
plt.gca().set_title('Rainfall distribution 2015')

plt.subplot(2,2,3)
plt.bar(x2014, y2014, color='blue')
plt.bar(x2014, y2015, bottom=y2014, color='orange')
plt.gca().set_title('Rainfall Comparison 2015 and 2014')

plt.subplot(2,2,4)
image = plt.imread(image_filepath)
plt.imshow(image)
plt.tick_params(left = False, right = False , labelleft = False, labelbottom = False, bottom = False)
for pos in ['right', 'top', 'bottom', 'left']: 
    plt.gca().spines[pos].set_visible(False)

plt.tight_layout()
plt.show()
