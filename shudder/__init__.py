if __name__ == "__main__":
    from shudder.session import ShudderSession

    shudder = ShudderSession()
    shudder.login()

    for feature in shudder.my_list():
        print("%(title)s [%(year)s]" % feature)
        print("%(short)s\n" % feature["description"])
