# Replace with you path to make copy of file
# (don't forget to place it later in app folder to get values from day file)
DESKTOP_PATH = None
PATH_TO_FOLDER = None

# MVP
my_values_preset = {
    "weight": 66.6,      # Kg, input your ideal weight (goal to achieve)
    "muscle": 28.5,      # Kg, input your ideal muscle mass
    "fat":    12.5,      #  %, input your ideal fat procent
    "water":  55.0,      #  %, input your ideal water procent
    "IMT":     0.0,      # deprecated
}


# celebration swing dates
celebrations = {
    # input desirable celebrations to swing diet (+50% to carbonates, +100% to fats)
    # format is a dict:
    # day_number: "Name of Day"
    # day_number is day counter from 1/1/1 ac
    # so, 1 jan 2020 is 737425
    # or you can use "your_date.toordinal()" to get that value
    737384: "My Celebration", # 21 nov 2019
}


# complex swing dates
fetes = {
    # input desirable fetes to swing diet (+25% to carbonates, +50% to fats, +15% to proteins)
    737387: "My Complex Swing", # 24 nov 2019
}


# sugar swing dates
holidays = {
    # input desirable holidays to swing diet (+25% to carbonates, +20% to fats)
    737399: "My Holiday", # 6 dec 2019
}


# balance swing dates
rituals = {
    # input desirable fasting days to swing diet (-30% to carbonates, -50% to fats, -10% to proteins)
    737405: "My Fasting Day", # 12 dec 2019
}
