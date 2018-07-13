from cx_Freeze import setup,Executable


setup(name='Racing game Vishu',version='0.1',description='parse stuff',
      executables=[Executable("pygame_car.py")])