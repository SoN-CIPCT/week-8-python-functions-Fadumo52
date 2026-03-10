def Ordered_Sandwich(*Ingredients):
    print(f" You Ordered a Sandwich with the following ingredients:")
    for Ingredient in Ingredients:
        print(f"{Ingredient}")
    print("Your sandwich is being prepared!")
        
        
Ordered_Sandwich("Egg","cheese","turkey bacon")
Ordered_Sandwich("Chicken","Pico di gallo","Lettuce","Mayo","Pepper")