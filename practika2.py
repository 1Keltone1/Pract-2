import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def create_matplotlib_graph():
    """Создание графа зависимостей matplotlib"""
    G = nx.DiGraph()

    # Основные узлы matplotlib
    nodes = {
        'matplotlib': {'color': '#ff6b6b', 'size': 4000},
        'pyplot': {'color': '#4ecdc4', 'size': 2500},
        'numpy': {'color': '#45b7d1', 'size': 2200},
        'PIL': {'color': '#45b7d1', 'size': 1800},
        'cycler': {'color': '#45b7d1', 'size': 1500},
        'dateutil': {'color': '#45b7d1', 'size': 1500},
        'kiwisolver': {'color': '#45b7d1', 'size': 1500},
        'pyparsing': {'color': '#45b7d1', 'size': 1500},
        'fonttools': {'color': '#45b7d1', 'size': 1500},
        'backend_agg': {'color': '#f9c74f', 'size': 1200},
        'backend_tk': {'color': '#f9c74f', 'size': 1200},
        'backend_qt': {'color': '#f9c74f', 'size': 1200}
    }

    # Добавляем узлы
    for node, attrs in nodes.items():
        G.add_node(node, **attrs)

    # Добавляем связи
    edges = [
        ('matplotlib', 'pyplot'),
        ('matplotlib', 'numpy'), ('matplotlib', 'PIL'),
        ('matplotlib', 'cycler'), ('matplotlib', 'dateutil'),
        ('matplotlib', 'kiwisolver'), ('matplotlib', 'pyparsing'),
        ('matplotlib', 'fonttools'),
        ('pyplot', 'backend_agg'), ('pyplot', 'backend_tk'),
        ('pyplot', 'backend_qt')
    ]

    for edge in edges:
        G.add_edge(*edge)

    return G, nodes


def create_express_graph():
    """Создание графа зависимостей express"""
    G = nx.DiGraph()

    # Основные узлы express
    nodes = {
        'express': {'color': '#ff6b6b', 'size': 4000},
        'body-parser': {'color': '#4ecdc4', 'size': 2000},
        'cookie': {'color': '#4ecdc4', 'size': 1800},
        'debug': {'color': '#4ecdc4', 'size': 1800},
        'send': {'color': '#4ecdc4', 'size': 1800},
        'serve-static': {'color': '#4ecdc4', 'size': 1800},
        'path-to-regexp': {'color': '#4ecdc4', 'size': 1600},
        'accepts': {'color': '#45b7d1', 'size': 1400},
        'methods': {'color': '#45b7d1', 'size': 1400},
        'qs': {'color': '#45b7d1', 'size': 1400},
        'http': {'color': '#f9c74f', 'size': 1500},
        'path': {'color': '#f9c74f', 'size': 1300},
        'fs': {'color': '#f9c74f', 'size': 1300}
    }

    # Добавляем узлы
    for node, attrs in nodes.items():
        G.add_node(node, **attrs)

    # Добавляем связи
    edges = [
        ('express', 'body-parser'), ('express', 'cookie'),
        ('express', 'debug'), ('express', 'send'),
        ('express', 'serve-static'), ('express', 'path-to-regexp'),
        ('express', 'accepts'), ('express', 'methods'),
        ('express', 'qs'),
        ('body-parser', 'http'), ('send', 'fs'),
        ('send', 'path'), ('serve-static', 'fs')
    ]

    for edge in edges:
        G.add_edge(*edge)

    return G, nodes


def visualize_graph(G, node_attrs, title, filename):
    """Визуализация графа зависимостей"""
    plt.figure(figsize=(16, 12))

    # Создаем layout
    pos = nx.spring_layout(G, k=2, iterations=100, seed=42)

    # Рисуем узлы
    node_colors = [node_attrs[node]['color'] for node in G.nodes()]
    node_sizes = [node_attrs[node]['size'] for node in G.nodes()]

    nx.draw_networkx_nodes(G, pos, node_color=node_colors,
                           node_size=node_sizes, alpha=0.9,
                           edgecolors='black', linewidths=1)

    # Рисуем ребра
    nx.draw_networkx_edges(G, pos, edge_color='gray',
                           arrows=True, arrowsize=25,
                           arrowstyle='->', width=2, alpha=0.7)

    # Рисуем метки
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold',
                            font_family='sans-serif')

    plt.title(title, fontsize=20, fontweight='bold', pad=30)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()


def create_comparison_visualization():
    """Создание сравнительной визуализации"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(20, 15))

    # 1. Количество зависимостей
    categories = ['Основные', 'Дополнительные', 'Встроенные']
    mpl_counts = [7, 5, 2]
    exp_counts = [6, 10, 4]

    x = np.arange(len(categories))
    width = 0.35

    ax1.bar(x - width / 2, mpl_counts, width, label='Matplotlib',
            color='#4ecdc4', alpha=0.8)
    ax1.bar(x + width / 2, exp_counts, width, label='Express.js',
            color='#ff6b6b', alpha=0.8)

    ax1.set_xlabel('Типы зависимостей', fontsize=12)
    ax1.set_ylabel('Количество', fontsize=12)
    ax1.set_title('Сравнение количества зависимостей', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # 2. Круговая диаграмма для matplotlib
    mpl_labels = ['Внешние пакеты', 'Бэкенды', 'Встроенные']
    mpl_sizes = [12, 3, 2]

    ax2.pie(mpl_sizes, labels=mpl_labels, autopct='%1.1f%%',
            colors=['#45b7d1', '#f9c74f', '#90be6d'],
            startangle=90)
    ax2.set_title('Matplotlib: типы зависимостей', fontsize=14, fontweight='bold')

    # 3. Круговая диаграмма для express
    exp_labels = ['Middleware', 'Утилиты', 'Node.js core']
    exp_sizes = [10, 6, 4]

    ax3.pie(exp_sizes, labels=exp_labels, autopct='%1.1f%%',
            colors=['#4ecdc4', '#45b7d1', '#f9c74f'],
            startangle=90)
    ax3.set_title('Express.js: типы зависимостей', fontsize=14, fontweight='bold')

    # 4. Общая статистика
    stats_data = [
        ['Общее количество', '12+', '20+'],
        ['Основные зависимости', '7', '6'],
        ['Встроенные модули', '2', '4'],
        ['Архитектура', 'Монолитная', 'Микросервисная']
    ]

    ax4.axis('off')
    table = ax4.table(cellText=stats_data,
                      colLabels=['Параметр', 'Matplotlib', 'Express.js'],
                      cellLoc='center',
                      loc='center',
                      bbox=[0.1, 0.1, 0.8, 0.8])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 2)
    ax4.set_title('Сравнительная статистика', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('dependencies_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()


def main():
    """Основная функция визуализации"""
    print("СОЗДАНИЕ ВИЗУАЛИЗАЦИЙ ЗАВИСИМОСТЕЙ")
    print("=" * 70)

    try:
        # Matplotlib dependencies
        print("1. Создание графа зависимостей Matplotlib...")
        G_mpl, nodes_mpl = create_matplotlib_graph()
        visualize_graph(G_mpl, nodes_mpl,
                        'Зависимости Matplotlib\n(Python пакет для визуализации)',
                        'matplotlib_dependencies.png')

        # Express dependencies
        print("2. Создание графа зависимостей Express.js...")
        G_exp, nodes_exp = create_express_graph()
        visualize_graph(G_exp, nodes_exp,
                        'Зависимости Express.js\n(JavaScript веб-фреймворк)',
                        'express_dependencies.png')

        # Comparison visualization
        print("3. Создание сравнительной визуализации...")
        create_comparison_visualization()

        print("Все визуализации успешно созданы!")
        print("\nСозданные файлы:")
        print("   • matplotlib_dependencies.png")
        print("   • express_dependencies.png")
        print("   • dependencies_comparison.png")

    except ImportError as e:
        print(f"Ошибка импорта: {e}")
        print("\nУстановите необходимые пакеты:")
        print("   pip install matplotlib networkx numpy")

    print("\n" + "=" * 70)
    print("ВИЗУАЛИЗАЦИЯ ЗАВЕРШЕНА")


if __name__ == "__main__":
    main()