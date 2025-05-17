from patterns.facade.smart_home import SmartHomeFacade, SmartHomeSubSystem

if __name__ == "__main__":
    smart_home = SmartHomeSubSystem()
    smart_home_facade = SmartHomeFacade(smart_home)

    smart_home_facade.set_movie_mode()
    print("Movie mode:\n", smart_home, sep="")

    print("#" * 75)

    smart_home_facade.set_focus_mode()
    print("Focus mode:\n", smart_home, sep="")
