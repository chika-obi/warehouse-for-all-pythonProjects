#note pip install cx_Freeze
from cx_Freeze import setup,Executable,sys
includefiles = ['icon.ico']
excludes=[]
packages=[]
base=None

if sys.platform == "win32":
    base="Win32GUI"

shortcut_table = [
    ("DesktopShortcut",
     "DesktopFolder",
     "Billing System",
     "TARGETDIR",
     "[TARGETDIR]\main.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data = {"Shortcut":shortcut_table}
bdist_msi_options={'data':msi_data}
setup(
    version = "0.1",
    description="Billing System",
    author ="Kpanuku Chika-Obi",
    name="Billing System",
    options={'build.exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables =[
        Executable(
            script = "main.py",
            base=base,
            icon='icon.ico',
            )
        ]
    )
#on terminal to run type
#python setup.py bdist_msi to run the code
#when completed two addition folder will be in the main folder (dist) and (build)
#right click on the dist and open in explorer
#open the folder and run your raw file or send to recipient
