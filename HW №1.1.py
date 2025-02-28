#Бой с врагом
ar1=20
hp1=100
dam1=50
hit=(dam1 * (1 - ar1 / 100))
hit_point=(hp1 - hit)
print("Нанесенный ущерб:", hit, "Остаток хитпоинтов:", hit_point)
