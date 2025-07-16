# Install and load the psych package if not already installed
install.packages("psych")
library(psych)

# Create the dataset
data <- data.frame(
  item1 = c(2,3,1,0,2,3,2,1,3,2),
  item2 = c(1,2,1,0,2,3,1,0,2,1),
  item3 = c(1,2,1,0,1,2,1,1,2,1),
  item4 = c(0,2,0,0,1,2,1,0,2,1),
  item5 = c(1,3,1,0,2,2,1,0,3,1)
)

# Calculate Cronbach's alpha
alpha(data)
