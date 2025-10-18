import json
import subprocess
import sys
from typing import Dict, Any


def get_matplotlib_info():
    """Анализ пакета matplotlib (Python)"""
    print("=" * 70)
    print("АНАЛИЗ ПАКЕТА MATPLOTLIB (PYTHON)")
    print("=" * 70)

    try:
        # Получаем информацию о пакете
        result = subprocess.run([
            sys.executable, '-m', 'pip', 'show', 'matplotlib'
        ], capture_output=True, text=True)

        if result.returncode == 0:
            print(" Служебная информация о пакете:")
            print(result.stdout)

            # Парсим информацию
            package_info = {}
            for line in result.stdout.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    package_info[key.strip()] = value.strip()

            print("\n Ключевые элементы:")
            print(f"  • Name: {package_info.get('Name', 'N/A')}")
            print(f"  • Version: {package_info.get('Version', 'N/A')}")
            print(f"  • Summary: {package_info.get('Summary', 'N/A')}")
            print(f"  • Requires: {package_info.get('Requires', 'N/A')}")
            print(f"  • Location: {package_info.get('Location', 'N/A')}")

        else:
            print(" Matplotlib не установлен")

    except Exception as e:
        print(f" Ошибка: {e}")


def get_express_info():
    """Анализ пакета express (JavaScript) - эмуляция"""
    print("\n" + "=" * 70)
    print("АНАЛИЗ ПАКЕТА EXPRESS (JAVASCRIPT)")
    print("=" * 70)

    # Эмуляция package.json для express
    express_package = {
        "name": "express",
        "description": "Fast, unopinionated, minimalist web framework for Node.js",
        "version": "4.18.2",
        "author": "TJ Holowaychuk <tj@vision-media.ca>",
        "license": "MIT",
        "repository": {
            "type": "git",
            "url": "git+https://github.com/expressjs/express.git"
        },
        "homepage": "https://expressjs.com/",
        "keywords": ["express", "framework", "sinatra", "web", "rest", "restful", "router", "app", "api"],
        "dependencies": {
            "accepts": "~1.3.8",
            "array-flatten": "1.1.1",
            "body-parser": "1.20.1",
            "content-disposition": "0.5.4",
            "content-type": "~1.0.4",
            "cookie": "0.5.0",
            "cookie-signature": "1.0.6",
            "debug": "2.6.9",
            "depd": "2.0.0",
            "encodeurl": "~1.0.2",
            "escape-html": "~1.0.3",
            "etag": "~1.8.1",
            "finalhandler": "1.2.0",
            "fresh": "0.5.2",
            "merge-descriptors": "1.0.1",
            "methods": "~1.1.2",
            "on-finished": "2.4.1",
            "parseurl": "~1.3.3",
            "path-to-regexp": "0.1.7",
            "proxy-addr": "~2.0.7",
            "qs": "6.11.0",
            "range-parser": "~1.2.1",
            "safe-buffer": "5.2.1",
            "send": "0.18.0",
            "serve-static": "1.15.0",
            "setprototypeof": "1.2.0",
            "statuses": "2.0.1",
            "type-is": "~1.6.18",
            "utils-merge": "1.0.1",
            "vary": "~1.1.2"
        },
        "engines": {
            "node": ">= 0.10.0"
        }
    }

    print("Служебная информация (package.json):")
    print(json.dumps(express_package, indent=2, ensure_ascii=False))

    print("\nКлючевые элементы:")
    print(f"  • Name: {express_package['name']}")
    print(f"  • Version: {express_package['version']}")
    print(f"  • Description: {express_package['description']}")
    print(f"  • License: {express_package['license']}")
    print(f"  • Dependencies: {len(express_package['dependencies'])} пакетов")
    print(f"  • Repository: {express_package['repository']['url']}")


def explain_semver():
    """Объяснение семантического версионирования"""
    print("\n" + "=" * 70)
    print("СЕМАНТИЧЕСКОЕ ВЕРСИОНИРОВАНИЕ (SEMVER)")
    print("=" * 70)

    print("""
SemVer (Semantic Versioning) - стандарт нумерации версий: MAJOR.MINOR.PATCH

• MAJOR версия (первое число):
  - Обратно НЕсовместимые изменения API
  - Пример: 1.x.x → 2.x.x

• MINOR версия (второе число):
  - Новая функциональность с обратной совместимостью
  - Пример: 1.1.x → 1.2.x

• PATCH версия (третье число):
  - Исправления ошибок с обратной совместимостью
  - Пример: 1.0.1 → 1.0.2

Специальные символы в зависимостях:
• ~1.2.3  - обновления PATCH (1.2.x)
• ^1.2.3  - обновления MINOR и PATCH (1.x.x)
• 1.2.3   - точная версия
• *       - любая версия
    """)


def get_packages_without_manager():
    """Как получить пакеты без менеджера пакетов"""
    print("\n" + "=" * 70)
    print("ПОЛУЧЕНИЕ ПАКЕТОВ БЕЗ МЕНЕДЖЕРА ПАКЕТОВ")
    print("=" * 70)

    print("MATPLOTLIB (Python):")
    print("  1. Прямо из репозитория GitHub:")
    print("     git clone https://github.com/matplotlib/matplotlib")
    print("  2. Скачать архив с PyPI:")
    print("     https://pypi.org/project/matplotlib/#files")
    print("  3. Установка вручную:")
    print("     python setup.py install")

    print("\nEXPRESS (JavaScript):")
    print("  1. Прямо из репозитория GitHub:")
    print("     git clone https://github.com/expressjs/express")
    print("  2. Скачать архив с npm:")
    print("     https://www.npmjs.com/package/express")
    print("  3. Ручная установка:")
    print("     npm install ./express-directory")


def main():
    """Основная функция анализа пакетов"""
    print("АНАЛИЗ ПАКЕТОВ: MATPLOTLIB И EXPRESS")
    print("=" * 70)

    get_matplotlib_info()
    get_express_info()
    explain_semver()
    get_packages_without_manager()


if __name__ == "__main__":
    main()