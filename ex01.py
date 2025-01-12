materials = {
    "Wood": 8,
    "Concrete": 12,
    "Brick": 10,
    "Tiles": 5,
}

length = int(input("\nEnter the length of the room (in m)"))
width = int(input("\nEnter the width of the room (in m)"))
totalarea = length*width

print("The total area of the room is", totalarea, "square feet")

print("Choose material for the floor:")
print("1. Wood (8€/m2)")
print("2. Concrete (12€/m2)")
print("3. Brick (10€/m2)")
print("4. Tiles (5€/m2)")
choice = input("\nEnter your choice (1/2/3/4):")
if choice == "1":
    chosenmaterial = materials['Wood']
    cost=totalarea*chosenmaterial
    print("You chose Wood costing 8€/m2")
    print("The total cost for the floor is:", cost, "€")

elif choice == "2":
    chosenmaterial = materials['Concrete']
    cost=totalarea*chosenmaterial
    print("You chose Concrete costing 12€/m2")
    print("The total cost for the floor is:", cost, "€")

elif choice == "3":
    chosenmaterial = materials['Brick']
    cost=totalarea*chosenmaterial
    print("You chose Brick costing 10€/m2")
    print("The total cost for the floor is:", cost, "€")

elif choice == "4":
    chosenmaterial = materials['Tiles']
    cost=totalarea*chosenmaterial
    print("You chose Tiles costing 5€/m2")
    print("The total cost for the floor is:", cost, "€")

save = input("Do you want to save this project? (y/n)")
if save == "y":
    project_details = (
        f"Room Dimensions: {length}x{width} m\n"
        f"Room area: {totalarea} m2\n"
        f"Flooring material: {list(materials.keys())[int(choice) - 1]} ({chosenmaterial}€/m²)\n"
        f"Total cost: {cost}€\n"
        
    )

    with open("Project_details_Javi_Albo.txt", "a") as file:
        file.write(project_details)
        print("Project saved in: Project_details_Javi_Albo.txt")

print("Project saved successfully!")
print("Thank you for using the estimator!")