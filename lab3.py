import numpy as np
import matplotlib.pyplot as plt

# Зчитування датасету з файлу
file_path = r'C:\lab 2\DS2.txt'
data = np.loadtxt(file_path)

# Визначення параметрів афінного перетворення
angle = np.radians(10)  # Кут у радіанах
rotation_point = np.array([480, 480])  # Точка обертання

# Створення матриці для обертання
rotation_matrix = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle), np.cos(angle)]
])

# Виконання афінного перетворення на всі точки датасету
transformed_data = np.dot(data - rotation_point, rotation_matrix) + rotation_point

# Встановлення розмірів вікна
plt.figure(figsize=(8, 8))

# Відображення датасету після афінного перетворення
plt.scatter(transformed_data[:, 0], transformed_data[:, 1], color='blue')

# Налаштування вигляду графіку
plt.xlim(0, 960)
plt.ylim(0, 960)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Transformed Dataset')

# Збереження результату у файлі графічного формату (наприклад, PNG)
output_file_path = 'transformed_dataset.png'
plt.savefig(output_file_path)

# Відображення графіку
plt.show()