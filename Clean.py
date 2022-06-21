
import pathlib;
import shutil; 

for dir in pathlib.Path('.').rglob("__pycache__") :
    shutil.rmtree(dir);
    print("remove " + str(dir));
print("clean done!");
