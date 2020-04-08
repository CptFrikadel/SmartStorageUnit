# Smart Storage unit

Storage unit too smart for its own good..
Connects to SmartCuttingBoard over the OOCSI network and keeps track of the progress in a recipe.

# OOCSI data channels

| Type	 | Channel name	 | key | range |
| --- 	 | :---: 		 | --- | --- |
| Value of the pressure sensor | `storagePressureChannel` | `pressure_val` | Bool (0-1) |
| Scanned barcode | `barCodeChannel` | `scanned_barcode` | EAN code of scanned products |
| Items currently in storage | `itemListChannel` | `item_list` | python dict (list of key-value pairs) |
| Recipe information | `recipeChannel` | `step` | integer (0 - nrof steps) |
| Recipe finish | `recipeChannel` | `done` | value is arbitrary |
| Recipe commands 	| `recipeChannel` | `next_step` / `prev_step` | value is ignored |	

> Currently itemListChannel is a conventional oocsi channel that fires an event every time something gets added or removed. Upon request, an oocsi variable can be made available.

# Commands for simulation

For simulation and debugging purposes there are some commands available. Commands are followed by one or more arguments separated by spaces.

| Command | Arguments | function | 
| --- | --- | --- |
| `add_item` | `item name` `amount` | simulates adding of one item of `name` to the storage unit |
| `remove_item` | `item name` `amount` | same as add, but remove |
| `scan_code` | `EAN number` or `defX` | simulates scanning barcode of a product. `defX` is a shortcut for pre-programmed codes |
| `exit` | - | Exits..

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

