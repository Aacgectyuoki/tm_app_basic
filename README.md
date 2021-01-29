This is going to turn into an app that uses buttons and gives people the total time they have left.

Blueprint:
- Calculate how much free time you have
    - 24 hrs a day (starting 
    - If total hours > 24: print Error message(“Not enough time”)
    - Factors:
        - Work(Num jobs: 0, 1000)
            - How many hours and minutes each job?(0, 23) (0, 60)
        - Travel(Ask user to predict how much time to travel by inputting hour and minutes
        - Exercise # sessions a day(0, 1000)
                - Hours (0, 23) minutes (0, 60) each session
        - Meals
            - Breakfast(0, 1)
                - Hours (0, 23) minutes (0, 60)
            - Lunch(0, 1)
                - Hours (0, 23) minutes (0, 60)
            - Dinner(0, 1)
                - Hours (0, 23) minutes (0, 60)
            - Snacks(0, 1)
                - How many(0, 1000)
                    - Hours (0, 23) minutes (0, 60) each snack
        - Other commitments (allow user input)
            - How many hours and minutes each other commitment? (0, 23) (0, 60)
- Print the remaining time left
