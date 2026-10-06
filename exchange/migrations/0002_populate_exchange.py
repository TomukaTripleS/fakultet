from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("exchange", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                INSERT INTO exchange_exchangeprogram
                    (id, university, languages, places, deadline, description)
                VALUES
                    (
                        1,
                        'Uniwersytet Warszawski, Польща',
                        'польська, англійська',
                        '5',
                        '2026-11-15',
                        'Навчальний обмін у Варшаві. Можливість познайомитися з академічним середовищем Польщі.'
                    ),
                    (
                        2,
                        'KU Leuven (Бельгія)',
                        'English',
                        '2 місця',
                        '2026-12-01',
                        'Навчальний обмін у Бельгії. Програма передбачає навчання англійською мовою.'
                    ),
                    (
                        3,
                        'Vilnius University, Литва',
                        'англійська',
                        'до 4',
                        '2026-10-20',
                        'Навчальний обмін у Вільнюсі. Можливість здобути досвід навчання в міжнародному середовищі.'
                    ),
                    (
                        4,
                        'Uniwersytet Jagielloński, Польща',
                        'Польська, Англійська',
                        '3',
                        '2026-11-15',
                        'Навчальний обмін у Кракові. Навчання доступне польською та англійською мовами.'
                    ),
                    (
                        5,
                        'University of Tartu - Естонія',
                        'англійська, естонська',
                        '2',
                        '2027-01-10',
                        'Навчальний обмін у Тарту. Можливість познайомитися з академічним середовищем Естонії.'
                    ),
                    (
                        6,
                        'Masaryk University, Чехія',
                        'англійська',
                        '1 місце',
                        '2026-09-30',
                        'Навчальний обмін у Чехії. Програма передбачає навчання англійською мовою.'
                    );
            """,
            reverse_sql="""
                DELETE FROM exchange_exchangeprogram
                WHERE id IN (1, 2, 3, 4, 5, 6);
            """,
        ),
    ]