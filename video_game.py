#imports pandas 
import pandas as pd

#makes a dataframe from the csv file and reads it into the program
video_data = pd.read_csv("HW\\video_games_raw.csv")

print("VIDEO GAME CATALOG MANAGER\n")

#Creates a loop that gets a valid input from the user, or a number that is associated with one of the games in
#the file. If invalid tells the user that it is an invalid input
while True:
    try:
        chosen_game = int(input("Enter a row number to inspect: "))
    except ValueError:
        print("Invalid input. Enter a whole-number from 0-14")
        continue
    if 0 <= chosen_game < len(video_data):
        break
    print("Invalid input.")

#Prints the information for the game that the user chooses
print(video_data.iloc[chosen_game])

#Allows the user to input a valid status for the game that they previously chose
#Will check to make sure the status is one of the four given statuses.
valid_statuses = {"backlog", "playing", "completed", "dropped"}
while True:
    new_status = input("Enter a new status: ").lower()
    if new_status in valid_statuses:
        new_status = new_status.capitalize()
        break
    print("Invalid. Please enter Backlog, Playing, Completed, or Dropped.")

video_data.at[chosen_game, "Status"] = new_status

#Creates a new recommended column and sets it automatically to "No". Then it looks and finds the games that have
#a rating of 8 or higher and that cost $40 or lower and will swap the recommended column to "Yes"
video_data["Recommended"] = "No"
video_data.loc[(video_data["Rating"] >= 8) & (video_data["Price"] <= 40),
    "Recommended",] = "Yes"

#Will print out all the games that have "Yes" in the recommended column.
#It will print title, platform, price, and rating for the recommended games
print("Recommended Games: ")
print(video_data.query("Recommended == 'Yes'")[["Title", "Platform", "Price", "Rating"]])

#Commits the data to a new csv file named videos_game_cleaned and makes it so there will be no
#first column with numbers
video_data.to_csv("HW\\videos_games_cleaned.csv", index=False)

#informs the user that the catalog has been updated and is saved in the new csv file
print("The catalog has been updated.")
print("Saved as video_games_cleaned.csv.")