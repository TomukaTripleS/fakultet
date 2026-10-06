from django.db import migrations


def forwards(apps, schema_editor):
    Program = apps.get_model("exchange", "ExchangeProgram")

    Program.objects.filter(places="2 місця").update(places="2")
    Program.objects.filter(places="до 4").update(places="4")
    Program.objects.filter(places="1 місце").update(places="1")


def backwards(apps, schema_editor):
    Program = apps.get_model("exchange", "ExchangeProgram")

    Program.objects.filter(
        university="KU Leuven", places="2"
    ).update(places="2 місця")

    Program.objects.filter(
        university="Vilnius University", places="4"
    ).update(places="до 4")

    Program.objects.filter(
        university="Masaryk University", places="1"
    ).update(places="1 місце")


class Migration(migrations.Migration):
    dependencies = [
        ("exchange", "0004_split_university_country"),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]