   #  Лабораторная работа №9: Практическая работа с Git


##  Цель работы

Познакомиться с основными возможностями системы управления версиями Git, изучить базовые операции работы с репозиториями, научиться выполнять commit'ы, работать с удаленными репозиториями и понять принципы version control.

---

##  Задачи

1. Установка и настройка Git
2. Создание репозитория на GitHub/GitLab
3. Клонирование удаленного репозитория
4. Работа с файлами и коммитами
5. Синхронизация локального и удаленного репозиториев

---

##  Задание 1: Установка Git

### Установка в WSL (Ubuntu)

```bash
# Обновление списка пакетов
sudo apt update

# Установка Git
sudo apt-get install git -y

# Проверка установки
git --version
```

**Результат:**
```
git version 2.34.1
```

✅ **Git успешно установлен**

### Глобальная настройка Git

После установки необходимо настроить имя пользователя и email:

```bash
# Настройка имени
git config --global user.name "Ваше Имя"

# Настройка email
git config --global user.email "your.email@example.com"

# Настройка редактора по умолчанию (опционально)
git config --global core.editor "nano"

# Цветной вывод для удобства
git config --global color.ui auto


---

##  Задание 2: Создание репозитория на GitHub

### Шаг 1: Регистрация/Вход на GitHub

1. Перешла на [github.com](https://github.com)
2. Вошла в существующий аккаунт (или создал новый)

### Шаг 2: Создание нового репозитория

**Параметры создания:**

| Параметр | Значение |
|----------|----------|
| Repository name | `lab9-git-practice` |
| Description | `Лабораторная работа №9: Практика работы с Git` |
| Visibility | Public |
| Initialize with README |  Да |
| .gitignore template | Python |
| License | MIT |

**Процесс создания:**

1. Нажала кнопку **"New"** (или **"Create repository"**)
2. Заполнила название: `lab9-git-practice`
3. Добавила описание
4. Выбрала **Public** для открытого доступа
5. Отметила **"Add a README file"**
6. Выбрала `.gitignore` шаблон для Python
7. Добавила лицензию MIT
8. Нажала **"Create repository"**



 **Репозиторий успешно создан**

##  Задание 3: Клонирование репозитория

### Получение URL репозитория

На странице репозитория нажала зеленую кнопку **"Code"** и скопировал HTTPS URL:


### Клонирование на локальный компьютер

```bash
# Переход в директорию для проектов
cd ~/projects

# Клонирование репозитория
git clone https://github.com/username/lab9-git-practice.git

# Переход в склонированный репозиторий
cd lab9-git-practice
```

**Вывод при клонировании:**
```
Cloning into 'lab9-git-practice'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
```


### Проверка удаленного репозитория

```bash
# Просмотр информации об удаленном репозитории
git remote -v
```

 **Репозиторий успешно склонирован**

---

##  Задание 4: Создание нового файла

### Создание файла new_file.txt

```bash
# Для Unix-систем
touch new_file.txt

echo "Это мой первый файл в Git!" > new_file.txt
echo "Лабораторная работа №9" >> new_file.txt
echo "Дата: $(date)" >> new_file.txt
```

### Просмотр содержимого

```bash
cat new_file.txt
```

**Результат:**
```
Это мой первый файл в Git!
Лабораторная работа №9
Дата: Fri Dec 20 11:15:23 UTC 2024
```

### Проверка статуса Git

```bash
git status
```

##  Задание 5: Добавление файла в индекс и коммит

### Добавление файла в staging area

```bash
# Добавление файла
git add new_file.txt

# Альтернатива - добавить все измененные файлы
# git add .
```

### Проверка статуса после добавления

```bash
git status
```

**Результат:**
```
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   new_file.txt
```

### Создание коммита

```bash
git commit -m "Create new_file.txt"

[main a1b2c3d] Добавлен новый файл new_file.txt с описанием работы
 1 file changed, 3 insertions(+)
 create mode 100644 new_file.txt
```

**Расшифровка вывода:**
- `[main a1b2c3d]` - ветка и хеш коммита
- `1 file changed` - изменен 1 файл
- `3 insertions(+)` - добавлено 3 строки
- `create mode 100644` - создан обычный файл

### Просмотр истории коммитов

```bash
git log
```

### Краткий формат истории

```bash
git log --oneline --graph --decorate
```

 **Файл успешно добавлен и закоммичен**

---

##  Отправка изменений на GitHub

### Push изменений на удаленный репозиторий

```bash
git push origin main
```

### Проверка на GitHub

После push'а изменения видны на GitHub:

✅ **Изменения успешно отправлены на GitHub**

---



### Изменение существующего файла

```bash
# Редактирование README.md
echo "## Описание проекта" >> README.md
echo "Это учебный проект для изучения Git" >> README.md

# Проверка
git diff README.md

# Добавление и коммит
git add README.md
git commit -m "Обновлено описание в README"
git push origin main
```

### Просмотр изменений

```bash
# Разница между рабочей директорией и staging area
git diff

# Разница между staging area и последним коммитом
git diff --staged

# Разница между коммитами
git diff HEAD~1 HEAD
```

---

##  Полезные команды Git

### Основные команды

```bash
# Инициализация нового репозитория
git init

# Клонирование репозитория
git clone <url>

# Статус файлов
git status

# Добавление файлов
git add <file>
git add .                    # Все файлы

# Коммит изменений
git commit -m "сообщение"
git commit -am "сообщение"   # add + commit для отслеживаемых файлов

# История коммитов
git log
git log --oneline
git log --graph --all

# Отправка на удаленный репозиторий
git push origin <branch>

# Получение изменений
git pull origin <branch>
```

### Работа с ветками

```bash
# Просмотр веток
git branch

# Создание новой ветки
git branch <branch-name>

# Переключение на ветку
git checkout <branch-name>

# Создание и переключение (одна команда)
git checkout -b <branch-name>

# Слияние веток
git merge <branch-name>

# Удаление ветки
git branch -d <branch-name>
```

### Откат изменений

```bash
# Откат изменений в файле (не в staging)
git checkout -- <file>

# Удаление файла из staging
git reset HEAD <file>

# Откат последнего коммита (сохранив изменения)
git reset --soft HEAD~1

# Откат последнего коммита (удалив изменения)
git reset --hard HEAD~1
```

**Типы коммитов:**
- `feat:` - новая функциональность
- `fix:` - исправление ошибки
- `docs:` - изменения в документации
- `style:` - форматирование кода
- `refactor:` - рефакторинг кода
- `test:` - добавление тестов
- `chore:` - обновление зависимостей и т.д.

### .gitignore - игнорирование файлов

Создание файла `.gitignore`:

```bash
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.env

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Temporary files
*.tmp
temp/
```

---

##  Workflow для типичной задачи

### Пример рабочего процесса

```bash

git pull origin main

git checkout -b feature/new-login-page

git status
git diff

git add .

git commit -m "feat: добавлена страница логина с валидацией"

git push origin feature/new-login-page

git checkout main
git pull origin main

git branch -d feature/new-login-page
```