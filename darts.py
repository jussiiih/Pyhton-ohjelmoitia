
folder_path = 'C:\\Users\\Jussi\\OneDrive - Brights\\Documents\\Checkpointit\\Checkpoint9\\Task3'
image_file = '\\targets.png'

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans
import numpy as np

image = mpimg.imread(folder_path + image_file)
plt.imshow(image)
player_A = {'x':[1985,1990,2010,1985,1990,1992],
            'y':[755,680,710,690,730,770]
}

player_B = {'x':[750,680,710,690,730,770],
            'y':[764,683,710,690,730,770]
}

# Throwing darts
# plt.scatter(player_A['x'],player_A['y'], marker='x')
# plt.scatter(player_B['x'],player_B['y'], marker='x')
# plt.show()

player_A_x = np.array(player_A['x']).reshape(-1,1)
player_A_y = np.array(player_A['y']).reshape(-1,1)

player_B_x = np.array(player_B['x']).reshape(-1,1)
player_B_y = np.array(player_B['y']).reshape(-1,1)

# print(player_A_x)
# print(player_A_y)
# print(player_B_x)
# print(player_B_y)

player_A_model = KMeans(n_clusters=1)
player_A_model.fit(player_A_x, player_A_y)
player_B_model = KMeans(n_clusters=1)
player_B_model.fit(player_B_x, player_B_y)


print(player_A_model.inertia_)
print(player_B_model.inertia_)