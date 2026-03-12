## question 1
# load both datasets
alpha <- read.csv("vineyard_alpha.csv")
beta <- read.csv("vineyard_beta.csv")

# id assignemnt
alpha$Batch_ID <- 0
beta$Batch_ID <- 1

merged_data <- rbind(alpha, beta) # merge


## question 2
# all correlations, without the batchid, if I dont do this then for positive it does correlate which doesnt make sense #nolint
cor_matrix <- cor(merged_data[, !names(merged_data) %in% "Batch_ID"])

score_cor <- cor_matrix[, "Var12"] # getting correlations with Var12 label


# sorting the correlations then picking the top values for negative andpositives
pos_cor <- sort(score_cor[-which(names(score_cor) == "Var12")], decreasing = TRUE) # all positive correlations ordered # nolint
strongest_pos <- names(pos_cor)[1:2] # picking top two # nolint
neg_cor <- sort(score_cor[-which(names(score_cor) == "Var12")]) # all negative correlations, ordered # nolint
strongest_neg <- names(neg_cor)[1] # strongest negative # nolint

print("Stronges Two positive (a):")
print(strongest_pos)
print("Strongest negative (b):")
print(strongest_neg)

## question 3

set.seed(20242913) # random seed
train_idx <- sample(seq_len(nrow(merged_data)), size = 0.8 * nrow(merged_data)) # train and test split # nolint
# tran and test assignments
train_data <- merged_data[train_idx, ]
test_data <- merged_data[-train_idx, ]


model <- lm(Var12 ~ . - Batch_ID, data = train_data) # linear regression model without including the IDs # nolint

model_summary <- summary(model) # model summary to use for question c

significant_vars <- rownames(model_summary$coefficients)[
  model_summary$coefficients[, 4] < 0.05] # if p value is less than 0.05 then its significant # nolint

coef_signs <- model_summary$coefficients[significant_vars, 1] # getthing coefficient signs for significant variables # nolint

predictions <- predict(model, newdata = test_data) # testing the model

rmse <- sqrt(mean((test_data$Var12 - predictions)^2)) # rmse calculation

print("Significant variables and coefficient signs (c):")
print(coef_signs)

print("Test RMSE (d):")
print(rmse)

# queston 4

merged_data$Tier <- factor(ifelse(merged_data$Var12 >= 7, "Premium", "Standard")) # tiering the wines based on Var12 # nolint 
merged_data$Var12 <- NULL # then removing the label for dataleakge

# seeding and setting train and test with the new version
set.seed(20242913)
train_idx <- sample(seq_len(nrow(merged_data)), 0.8 * nrow(merged_data))
train_data <- merged_data[train_idx, ]
test_data <- merged_data[-train_idx, ]

library(caret)# caret has the preprocessing for normalization and metrics # nolint
preproc <- preProcess(train_data[, !names(train_data) %in% "Tier"], # where I define how to preprocess this data around "Tier" # nolint
                      method = c("center", "scale")) # center and scale makes it so that mean is 0 and sd is 1, so its normalized # nolint

# normalizing both sets
train_x <- predict(preproc, train_data[, !names(train_data) %in% "Tier"])
test_x <- predict(preproc, test_data[, !names(test_data) %in% "Tier"])

# getting the labes from test and train
train_y <- train_data$Tier
test_y <- test_data$Tier

# loading three models here, with their confusion matrices
library(class)
knn_pred <- knn(train_x, test_x, train_y, k = 5)
knn_cm <- confusionMatrix(knn_pred, test_y, positive = "Premium")

library(e1071)
nb_model <- naiveBayes(train_x, train_y)
nb_pred <- predict(nb_model, test_x)
nb_cm <- confusionMatrix(nb_pred, test_y, positive = "Premium")

library(C50)
c50_model <- C5.0(train_x, train_y)
c50_pred <- predict(c50_model, test_x)
c50_cm <- confusionMatrix(c50_pred, test_y, positive = "Premium")

results <- data.frame( # custom table here for al the models and metrics comparing # nolint
  Model = c("KNN", "Naive Bayes", "C5.0"), # each model name in order with its metrics # nolint
  Accuracy = c(knn_cm$overall["Accuracy"],
               nb_cm$overall["Accuracy"],
               c50_cm$overall["Accuracy"]),
  F1_Score = c(knn_cm$byClass["F1"],
               nb_cm$byClass["F1"],
               c50_cm$byClass["F1"]),
  Sensitivity = c(knn_cm$byClass["Sensitivity"],
                  nb_cm$byClass["Sensitivity"],
                  c50_cm$byClass["Sensitivity"])
)

# these are results provided from the libraries, a lot more detailed since it kind of clutters im commenting it out # nolint
# print(knn_cm) #nolint
# print(nb_cm) #nolint
# print(c50_cm) # nolint
# for question e, KNN handles it the best all the scores are higher than the other models # nolint
print(results) # metrics we care about

## question 5


# Recommendation
# based on the F1 scores of the models, id recommend the KNN for the classification of “Premium” wines. # nolint
# tho the sensitivity value of Naive Bayes was slightly higher, KNN had the highest F1 value of 0.586 # nolint
# which balances precision and recall. This is important because precision can be misleading on its own # nolint
# if most wines are “Standard”, then a model may look good even when it does not correctly pick “Premium” wines. # nolint
# The F1-score makes sure that we consider correctly classifying Premium wines and avoiding incorrectly labeling Standard wines. # nolint

# Secret Sauce
# - In this regard, I would suggest monitoring the highest two positive correlation varialbes # nolint
# as well as highest negative (avoiding high levels of it)
# these three are directly connected and the most influencial part of the Var12 score which leads wine to be premium # nolint