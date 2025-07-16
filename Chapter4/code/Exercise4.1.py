#You may need to install the pingouin library using pip install pingouin
import pandas as pd
from pingouin import cronbach_alpha

# Create the dataset
data = pd.DataFrame({
    'item1': [2,3,1,0,2,3,2,1,3,2],
    'item2': [1,2,1,0,2,3,1,0,2,1],
    'item3': [1,2,1,0,1,2,1,1,2,1],
    'item4': [0,2,0,0,1,2,1,0,2,1],
    'item5': [1,3,1,0,2,2,1,0,3,1]
})

# Calculate Cronbach's alpha
alpha, _ = cronbach_alpha(data)
print(f"Cronbach's alpha: {alpha:.2f}")
