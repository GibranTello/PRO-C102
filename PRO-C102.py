list_of_files = os.listdir(from_dir)
print(list_of_files)

if os.path.exists(path2):
    print("Movineg " + file_name + ".....")

    shutil.move(path1, path3)

else:
    os.makedirs(path2)
    print("Moving " + file_name + ".....")
    shutil.move(path1, path3)