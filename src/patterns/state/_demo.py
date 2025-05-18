from patterns.state.traffic import TrafficLight

if __name__ == "__main__":
    light_system = TrafficLight()

    light_system.change()  # Red - Stop!
    light_system.change()  # Yellow (from Red to Green) - caution!
    light_system.change()  # Green - go!
    light_system.change()  # Yellow (from Green to Red) - caution!
    light_system.change()  # Red - Stop!
    light_system.change()  # Yellow (from Red to Green) - caution!
    light_system.change()  # Green - go!
