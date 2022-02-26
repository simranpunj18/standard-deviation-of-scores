import pandas as pd
import statistics
import csv
df = pd.read_csv("student-scores.csv")
height_list = df["Scores(students)"].to_list()
weight_list = df["Scores(students)"].to_list()
#Mean for height and Weight
height_mean = statistics.mean(student_scores)
weight_mean = statistics.mean(student-scores)
#Median for height and weight
height_median = statistics.median(student-scores)
weight_median = statistics.median(student-scores)
#Mode for height and weight
height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)
#Printing mean, median and mode to validate
print("Mean, Median and Mode of height is {}, {} and {} respectively".format(scores_mean, scores_median, scores_mode))
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(student_mean, student_median, student_mode))
#Standard deviation for height and weight
height_std_deviation = statistics.stdev(scores_list)
weight_std_deviation = statistics.stdev(scores_list)
#1, 2 and 3 Standard Deviations for height  
scores_first_std_deviation_start, students_first_std_deviation_end = students_mean-students_std_deviation, students_mean+students_std_deviation
scores_second_std_deviation_start, students_second_std_deviation_end = students_mean-(2*students_std_deviation), students_mean+(2*students_std_deviation)
scores_third_std_deviation_start, students_third_std_deviation_end = students_mean-(3*students_std_deviation), students_mean+(3*students_std_deviation)
#1, 2 and 3 Standard Deviations for weight
scores_first_std_deviation_start, scores_first_std_deviation_end = scores_mean-scores_std_deviation, scores_mean+scores_std_deviation
scores_second_std_deviation_start, scores_second_std_deviation_end = scores_mean-(2*scores_std_deviation), scores_mean+(2*scores_std_deviation)
scores_third_std_deviation_start, scores_third_std_deviation_end = scores_mean-(3*scores_std_deviation), scores_mean+(3*scores_std_deviation)
#Percentage of data within 1, 2 and 3 Standard Deviations for Height
height_list_of_data_within_1_std_deviation = [result for result in students_list if result > students_first_std_deviation_start and result < students_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in students_list if result > students_second_std_deviation_start and result < students_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in students_list if result > students_third_std_deviation_start and result < students_third_std_deviation_end]
#Percentage of data within 1, 2 and 3 Standard Deviations for Weight
scores_list_of_data_within_1_std_deviation = [result for result in students_list if result > students_first_std_deviation_start and result < students_first_std_deviation_end]
scores_list_of_data_within_2_std_deviation = [result for result in students_list if result > students_second_std_deviation_start and result < students_second_std_deviation_end]
scores_list_of_data_within_3_std_deviation = [result for result in students_list if result > students_third_std_deviation_start and result < students_third_std_deviation_end]
#Printing data for height and weight (Standard Deviation)
print("{}% of data for scores lies within 1 standard deviation".format(len(scores_list_of_data_within_1_std_deviation)*100.0/len(scores_list)))
print("{}% of data for scores lies within 2 standard deviations".format(len(scores_list_of_data_within_2_std_deviation)*100.0/len(scores_list)))
print("{}% of data for scores lies within 3 standard deviations".format(len(scores_list_of_data_within_3_std_deviation)*100.0/len(scores_list)))
print("{}% of data for scores lies within 1 standard deviation".format(len(scores_list_of_data_within_1_std_deviation)*100.0/len(students_list)))
print("{}% of data for scores lies within 2 standard deviations".format(len(scores_list_of_data_within_2_std_deviation)*100.0/len(students_list)))
print("{}% of data for scores lies within 3 standard deviations".format(len(studets_list_of_data_within_3_std_deviation)*100.0/len(students_list)))
