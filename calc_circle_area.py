# calc_circle_area

def calc_circle_area(circle_diameter):
    pi_val = math.pi

    circle_radius = circle_diameter / 2.0
    circle_area = pi_val * circle_radius *
            circle_radius

    return circle_area


pizza_diameter_1 = 12.0
pizza_diameter_2 = 14.0

total_pizza_area =
  calc_circle_area(pizza_diameter_1) +
  calc_circle_area(pizza_diameter_2)

print('A 12 and 14 inch pizza has', end=' ')
print(f'{total_pizza_area:.2f}', end=' ')
print('square inches combined.')



