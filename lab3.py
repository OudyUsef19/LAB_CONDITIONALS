movie = "outside"
rating = 3
popularity = 72.65

print("The movie: ",movie)
if rating >= 4 and popularity > 80:
    print("Highly recommended")
elif rating >= 3 and popularity > 70:
    print("I recommended it . It is good")
elif rating <= 2 and popularity > 70:
    print("You should check it out!")
elif rating <= 2 and popularity < 50:
    print("Don't watch it. It is a waste of time")
