def calculate_food(num_small_dogs, num_med_dogs, num_large_dogs, food_remaining):
    total_dogs = num_small_dogs + num_med_dogs + num_large_dogs
    if num_small_dogs < 0 or num_med_dogs < 0 or num_large_dogs < 0:  # return an error if any number of dogs is
        # negative
        error = "Cannot have a negative amount of dogs"
        return error
    if total_dogs > 30:  # return an error if there are more than the maximum number of dogs
        error = "Only 30 dogs allowed in the shelter at one time"
        return error
    if food_remaining < 0:  # return an error if a negative amount of food is given
        error = "Cannot have a negative amount of food"
        return error
    min_food_required = abs((10 * num_small_dogs + 20 * num_med_dogs + 30 * num_large_dogs) - food_remaining)
    # calculate the amount of food required for the dogs in the shelter given the amount of dog food currently in the
    # shelter
    if min_food_required == 0:  # when exactly enough order 20% more
        min_food_required = food_remaining
        food_required = .2 * min_food_required
    else:
        food_required = round(.2 * min_food_required + min_food_required, 2)
        food_difference = food_remaining - food_required
        if food_difference > 10:  # when more food remaining than required and that difference is significant set
            # required to 0
            food_required = 0
    return food_required
