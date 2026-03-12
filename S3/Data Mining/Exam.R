# Task 1 
data <- read.csv("data.csv", stringsAsFactors = FALSE, header = TRUE)

str(data) # data type and structure
summary(data)
# There are 3 NA's on all numeric columns except X3P where it is 45. I will deal with them after the exploration # nolint

total_missing <- sum(is.na(data))
cat("Total missing values in dataset:", total_missing, "\n", "Duplicated rows:", sum(duplicated(data)), "\n") # nolint
# number of unique vals in each column, it is kind of useful regarding the team counts and years # nolint
sapply(data, function(x) length(unique(x)))


# this part is to see outlier investigation
numeric_cols <- sapply(data, is.numeric)

# to see any logical inconsistency since all the numbers should be above 0
for (col in names(data)[numeric_cols]) {
  cat("Number of negatives:", sum(data$col < 0, na.rm = TRUE), "\n") # checking if any numeric value is negative # nolint
}


# Task 2 Data Cleaning
missing_per_row <- rowSums(is.na(data))
cat("Number of rows with missing values:", sum(missing_per_row > 0), "\n") # how many rows have missing values # nolint

# Explanation:
# Most variables have at most 3 missing values overall, so missing data is rare
# An observation with 3 or more missing values (across columns) is going to be unreliable. # nolint
# so, ive defined my "high number" as 3 or more missing values in one row.
high_missing_threshold <- 3

rows_high_missing <- which(missing_per_row >= high_missing_threshold) # rows that has more than 3 missing values # nolint
length(rows_high_missing) # there are only 3 rows with high freq of missing since the number is low I am just going to get rid of them # nolint

clean_data <- data[-rows_high_missing, ] # removing them

# for verification
cat("Original number of observations:", nrow(data), "\n")
cat("Number of observations removed:", length(rows_high_missing), "\n")
cat("Remaining observations:", nrow(clean_data), "\n")

colSums(is.na(clean_data)) # final sanity check to make sure that all the high missing rows are gone except X3P # nolint

# Task 3 Team Comparison
filtered_data <- subset(clean_data, Min > 10) # players who played more than 10mins # nolint

team_avg_pts <- aggregate(Pts ~ Team, # grouping pts with team - also using aggregate instead of tapply since I need the result later on # nolint
                          data = filtered_data, FUN = mean) # applying mean to pts # nolint
team_avg_pts <- team_avg_pts[order(-team_avg_pts$Pts), ] # ordering it in descending order # nolint
print(team_avg_pts) # avg points by team

barplot( # comparing it with barplot
  height = team_avg_pts$Pts,
  names.arg = team_avg_pts$Team,
  main = "Performance by Team ",
  ylab = "avg points p/game",
  col = "red"
)

# Task 4 Career Longevity
player_years <- aggregate(Year ~ Name + Team, # grouping years with name and team # nolint
       data = data, # nolint
        FUN = function(x) length(unique(x))) # counting each unique year of players with their team # nolint
colnames(player_years)[3] <- "Seasons_Played" # then adding this column name # nolint

# sorting it by team first then how many years they played in descending order
player_years <- player_years[order(player_years$Team, -player_years$Seasons_Played), ] # makes it easier to find the top two # nolint

teams_split <- split(player_years, player_years$Team) # split the data by team

top2_by_team <- lapply(teams_split, function(df) head(df, 2)) # getting top 2 for each team # nolint
top2_players <- do.call(rbind, top2_by_team) # merging the dataframes

#  felipe reyes and ergio llull from Real madrid with 7 years
#  paulius jankunas and arturas milaknis wfrom zalgiris with 6 and 5 years respectively # nolint
print(top2_players)

# Task 5 Derived Variables

data$FG_percent <- ifelse(
  is.na(data$FG) | is.na(data$FGA) | data$FGA == 0, # if missing or zero
  NA,                                 # then NA
  round((data$FG / data$FGA) * 100, 2)  # otherwise calculate percentage
)
head(data[, c("Name", "FG", "FGA", "FG_percent")])
summary(data$FG_percent) # checking the distribution of it and max is 100 meaning it is logically okay # nolint

# Task 6 Defensive Performance
zalgiris_players <- subset(clean_data, Team == "Zalgiris") # zalgiris players # nolint
top_blocker <- zalgiris_players[which.max(zalgiris_players$Blks), c("Name", "Team", "Blks")] # top blocker # nolint
print(top_blocker) # mirza begic with 2.3

# Task 7 Visualization
teams <- unique(clean_data$Team)
team_colors <- rainbow(length(teams)) # assign a distinct color to each team

color_map <- setNames(team_colors, teams) # assigning colors to teams

plot(
  clean_data$Min, clean_data$Pts, # x and y axis
  col = color_map[clean_data$Team], # color for the teams
  pch = 20,                # fill the circles
  main = "Relationship Between Points Scored and Minutes Played", # title
  xlab = "Minutes Played",
  ylab = "Points Scored"
)
legend(
  "topleft",
  legend = teams,
  col = team_colors,
  pch = 20,
  title = "Teams",
)

# Task 8 Normalization

normalize_minmax <- function(x) {
  (x - min(x, na.rm = TRUE)) / (max(x, na.rm = TRUE) - min(x, na.rm = TRUE))
}
standardize_zscore <- function(x) {
  (x - mean(x, na.rm = TRUE)) / sd(x, na.rm = TRUE)
}
subset_data <- clean_data[, c("Pts", "Min", "FG")]

# applying the functions to each column
normalized_subset <- as.data.frame(lapply(subset_data, normalize_minmax))
standardized_subset <- as.data.frame(lapply(subset_data, standardize_zscore))

head(standardized_subset)

# Task 9 Score Distribution

# real madrid shows slightly higher and more varying performance probably would mean there are multiple different high performing players # nolint
# zalgiris is more consistent with its performance but they have an outlier player with very high points # nolint
boxplot(
  Pts ~ Team,
  data = clean_data,
  main = "Score Distribution by Team",
  xlab = "Team",
  ylab = "Points Scored",
  col = "purple",
  border = "black",
  las = 1
)

# Task 10 Outlier Investigation
team_data <- subset(clean_data, Team == "Real Madrid")
outlier_counts <- data.frame(Variable = character(), Outlier_Count = numeric())

for (col in names(team_data)[numeric_cols]) {
  x <- team_data[[col]]
  q1 <- quantile(x, 0.25, na.rm = TRUE) # 25% range without NA
  q3 <- quantile(x, 0.75, na.rm = TRUE) # 75% range without NA
  iqr <- q3 - q1 # 75% - 25%
  lower <- q1 - 1.5 * iqr # getting the lower end
  upper <- q3 + 1.5 * iqr # and higher end
  # counting the outliers
  outlier_count <- sum(x < lower | x > upper, na.rm = TRUE) # comparing it to find outliers # nolint
  # saving the results
  outlier_counts <- rbind(outlier_counts, data.frame(Variable = col, Outlier_Count = outlier_count)) # nolint
}

outlier_counts <- outlier_counts[order(-outlier_counts$Outlier_Count), ] # sorting the data with possible outliers # nolint

print(outlier_counts)
# I just want to let you know professors my basketball knowledge is not that high # nolint
# Asts has the most outliers - 9 - maybe different play styles
# Stls - 8 if we think stealing the ball as defensive we could tie this with asists since it would indicate the defender stole the ball and immediately made an assist
# X3P - 7 - since landing 3 point shots are hard maybe not many players are doing it
# Off - 6 - probably because the amount of defensiveplayers and offensive players vary
# Blks - 6 I am almost certain this is the same reason as Off
# PFs - 4  maybe these players are too aggressive or they are a bit softer on the play depending on where they lay
