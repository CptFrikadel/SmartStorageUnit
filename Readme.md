# Smart Storage unit

Storage unit too smart for its own good..
Connects to SmartCuttingBoard over the OOCSI network and keeps track of the progress in a recipe.

# Software architecture

Multiple threads:

1. Main thread
  * Keeps track of the general state of the system, sensors and recipe
  * Handles the OOCSI networking and communication
2. The pressure sensor thread
  * Constantly polls the pressure sensor for a change in weight
  * On change updates the `global_state` which triggers an OOCSI update.
3. The camera / barcode reader thread
  * Keeps track of the camera and calls its `yoBarcodeWasScanned()` function in main

# Recipes

Recipes are saved in json format and loaded in `Recipe` class, see `example_recipe.json` and `recipe.py`.Sensor data from SmartCuttingBoard (and possibly other things) is interpreted to keep track of the current step in the recipe.

# Dimensions of amounts

For all recipes, we follow a standard dimension for multiple types of ingrediënts:

* Cooking_time: time in minutes
* * Liquids: amount in milliliters
* Solid items in packaging: amount in amount of products/packagings of product
* Crystallized or powdered solids like flour or sugar: milligrams
* Sauces: Tablespoons
* Solid items in large amounts like rice or pasta: grams

