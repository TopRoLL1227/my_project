# Cursor - це об'єкт, який використовується для виконання SQL-запитів до бази даних і обробки результатів цих запитів. 
# У більшості баз даних, таких як PostgreSQL, MySQL, SQLite і т. д., використовується поняття курсора.

# Основні функції курсора включають в себе:

# Виконання запитів: Курсор використовується для виконання SQL-запитів до бази даних. Це можуть бути запити на вибірку даних (SELECT), 
# оновлення даних (UPDATE), видалення даних (DELETE), вставка нових даних (INSERT), а також інші види запитів.

# Отримання результатів: Курсор може отримувати результати виконання запитів. Наприклад, результати вибірки даних, 
# які потім можуть бути оброблені в коді програми.

# Навігація по результатам: Курсор дозволяє переміщатися вперед та назад по результатам запиту, щоб обробляти кожен рядок результатів по черзі.

# Керування транзакціями: Курсор також може виконувати операції керування транзакціями, такі як підтвердження (commit) або відміна (rollback) транзакцій.

# У контексті коду, який ви навели, об'єкт курсора використовується для виконання SQL-запиту до бази даних PostgreSQL. 
# Після виконання запиту результати отримуються за допомогою методу fetchone(), щоб перевірити, чи існує користувач з вказаним ім'ям користувача і паролем. 
# Після завершення роботи з курсором його слід закрити методом close()