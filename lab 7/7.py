class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_info(self):
        return f"Имя сотрудника: {self.name}, ID: {self.emp_id}"


class Manager(Employee):  # Применяем наследственность для все сотрудников
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)
        self.department = department

    def manage_project(self):
        return f"Менеджер {self.name} управляет проектом в {self.department} департаменте."


class Technician(Employee):
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Тех специалист {self.name} выполняет тех обслуживание в области {self.specialization}."


class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Manager.__init__(self, name, emp_id, department)
        Technician.__init__(self, name, emp_id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        if not self.team:
            return "Нету сотрудников команды"
        return "\n".join([emp.get_info() for emp in self.team])


emp1 = Employee("Майкл", 1)
manager = Manager("Даниил", 2, "Продаж")
technician = Technician("Михаил", 3, "Техник")
tech_manager = TechManager("Александр", 4, "IT", "разработчик ПО")

# Демонстрация функциональности каждого класса
print(emp1.get_info())  # Вывод базовой информации о сотруднике
print(manager.get_info())  # Информация о менеджере
print(manager.manage_project())  # Управление проектами

print(technician.get_info())  # Информация о технике
print(technician.perform_maintenance())  # Выполнение обслуживания

# TechManager может управлять проектами и выполнять технические задачи
print(tech_manager.get_info())  # Информация о TechManager
print(tech_manager.manage_project())  # Управление проектами
print(tech_manager.perform_maintenance())  # Выполнение обслуживания

# Добавляем сотрудников в команду TechManager
tech_manager.add_employee(emp1)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)
tech_manager.add_employee(tech_manager)

# Получаем информацию о команде
print("Информация о команде:")
print(tech_manager.get_team_info())