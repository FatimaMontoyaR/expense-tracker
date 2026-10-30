"""
Expense Tracker
Proyecto académico para registrar y consultar gastos personales.
No requiere librerías externas.
"""

import csv
import os
from datetime import date, datetime

FILE_NAME = "expenses.csv"
CATEGORIES = ["Comida", "Transporte", "Escuela", "Entretenimiento", "Salud", "Otros"]


def load_expenses():
    """Carga los gastos guardados en el archivo CSV."""
    expenses = []

    if not os.path.exists(FILE_NAME):
        return expenses

    with open(FILE_NAME, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                row["amount"] = float(row["amount"])
                expenses.append(row)
            except (ValueError, KeyError):
                continue

    return expenses


def save_expenses(expenses):
    """Guarda los gastos en un archivo CSV."""
    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as file:
        fields = ["description", "category", "amount", "expense_date"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(expenses)


def show_categories():
    print("\nCategorías:")
    for number, category in enumerate(CATEGORIES, start=1):
        print(f"{number}. {category}")


def add_expense(expenses):
    description = input("Descripción del gasto: ").strip()
    if not description:
        print("La descripción no puede estar vacía.")
        return

    show_categories()
    try:
        option = int(input("Selecciona una categoría: "))
        if option < 1 or option > len(CATEGORIES):
            print("Opción no válida.")
            return
    except ValueError:
        print("Debes escribir un número.")
        return

    try:
        amount = float(input("Monto: $"))
        if amount <= 0:
            print("El monto debe ser mayor que cero.")
            return
    except ValueError:
        print("Escribe un monto válido.")
        return

    expense_date = input(
        f"Fecha (AAAA-MM-DD) o Enter para hoy [{date.today()}]: "
    ).strip()

    if not expense_date:
        expense_date = str(date.today())
    else:
        try:
            datetime.strptime(expense_date, "%Y-%m-%d")
        except ValueError:
            print("Formato de fecha incorrecto.")
            return

    expenses.append({
        "description": description,
        "category": CATEGORIES[option - 1],
        "amount": amount,
        "expense_date": expense_date
    })
    save_expenses(expenses)
    print("Gasto guardado correctamente.")


def show_expenses(expenses):
    if not expenses:
        print("\nTodavía no hay gastos registrados.")
        return

    print("\n--- LISTA DE GASTOS ---")
    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['expense_date']} | "
            f"{expense['description']} | {expense['category']} | "
            f"${expense['amount']:.2f}"
        )


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal gastado: ${total:.2f}")


def show_category_totals(expenses):
    if not expenses:
        print("\nTodavía no hay gastos registrados.")
        return

    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    print("\n--- GASTOS POR CATEGORÍA ---")
    for category, amount in sorted(totals.items()):
        print(f"{category}: ${amount:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n====== EXPENSE TRACKER ======")
        print("1. Agregar gasto")
        print("2. Mostrar gastos")
        print("3. Ver total gastado")
        print("4. Ver gastos por categoría")
        print("5. Salir")

        option = input("Selecciona una opción: ").strip()

        if option == "1":
            add_expense(expenses)
        elif option == "2":
            show_expenses(expenses)
        elif option == "3":
            show_total(expenses)
        elif option == "4":
            show_category_totals(expenses)
        elif option == "5":
            print("Gracias por usar Expense Tracker.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
