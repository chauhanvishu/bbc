import cx_Freeze



executables = [cx_Freeze.Executable("pygame_car.py")]

cx_Freeze.setup(

    name="car_game",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["car.png"]}},
    executables = executables

    )
