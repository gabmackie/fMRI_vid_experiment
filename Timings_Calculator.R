library(tidyverse)

file = "20210917_1210_P1.csv"

# Load in data
data <- read_csv(file)

# Calculate the timings
data <- data %>%
  mutate(
    adjusted_timing = lag(timing, default = 0) # Add a variable with the timings shifted forwards
  ) %>%
  mutate(
    difference = timing - adjusted_timing # Calculate the difference to show time elapsed since the last timestamp
  )
# Print it
data

# Write it back to the file
write_csv(data, file)
