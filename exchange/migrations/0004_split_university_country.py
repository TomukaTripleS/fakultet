from django.db import migrations


UNIVERSITIES = [
    ("Uniwersytet Warszawski, Польща", "Uniwersytet Warszawski", "Польща"),
    ("KU Leuven (Бельгія)", "KU Leuven", "Бельгія"),
    ("Vilnius University, Литва", "Vilnius University", "Литва"),
    ("Uniwersytet Jagielloński, Польща", "Uniwersytet Jagielloński", "Польща"),
    ("University of Tartu - Естонія", "University of Tartu", "Естонія"),
    ("Masaryk University, Чехія", "Masaryk University", "Чехія"),
]


def forwards(apps, schema_editor):
    Program = apps.get_model("exchange", "ExchangeProgram")
    programs = Program.objects.using(schema_editor.connection.alias)

    for original, name, country in UNIVERSITIES:
        programs.filter(university=original).update(
            university=name,
            country=country,
        )


def backwards(apps, schema_editor):
    Program = apps.get_model("exchange", "ExchangeProgram")
    programs = Program.objects.using(schema_editor.connection.alias)

    for original, name, country in UNIVERSITIES:
        programs.filter(university=name, country=country).update(
            university=original,
            country="",
        )


class Migration(migrations.Migration):
    dependencies = [
        ("exchange", "0003_add_country"),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]