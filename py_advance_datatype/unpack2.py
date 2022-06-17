def f(*args, **kwargs):
    # print("Positional:", args)
    print("Named:", kwargs)

# f("Goat me", 200, 25)
f(Galleons=500, Sickels=250, Knuts=125)