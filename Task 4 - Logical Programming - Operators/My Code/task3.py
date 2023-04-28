# Triathlon events and times (in MINUTES) taken to complete each
swimming = 0
cycling = 10
running = 20

# Calculate the total time taken to complete triathlon
total_time = swimming + cycling + running

# Determine which which award participant will receive
# The qualifying time for awards is 100 minutes
# Within qualifying time: Provincial Colours
# Within 5 minutes of qualifying time: Provincial Half Colours
# Within 10 minutes of qualifying time: Provincial Scroll
# More than 10 minutes of qualifying time: No Award
"""
I was very confused here to understand the criteria for awards as task says the qualifying time for award is 100 minutes. That points as if there is no award if over 100 minutes.

The only way I could make sense was this:
    total_time <= 100 **Provincial Colours**
    total_time <= 105 **Provincial Half Colours**
    total_time <= 110 **Provicial Scroll**
    total_time > 110 **No award**

I asked for help purely about the citeria here on "The Coding Den" discord server (https://discord.gg/code). I turned out to be right or at least others feel same way.
"""

if total_time <= 100:
    award = "Provincial Colours"
elif total_time <= 105:
    award = "Provincial Half Colours"
elif total_time <= 110:
    award = "Provicial Scroll"
else:     # total_time > 110
    award = "No award"

# Print the total time taken to complete triathlon and the award that the participant will receive
print(f"Total time to complete triathlon: {total_time} minutes \nAward: {award}")