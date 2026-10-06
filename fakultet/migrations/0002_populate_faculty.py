from django.db import migrations

def populate_faculty(apps, schema_editor):
    Department = apps.get_model("fakultet", "Department")
    Discipline = apps.get_model("fakultet", "Discipline")
    Program = apps.get_model("fakultet", "Program")
    Teacher = apps.get_model("fakultet", "Teacher")
    FacultyInfo = apps.get_model("fakultet", "FacultyInfo")
    database = schema_editor.connection.alias

    Department.objects.using(database).create(
        id=1,
        name="Кафедра міжнародних відносин",
        head="Яковлєв Максим Володимирович",
    )
    Department.objects.using(database).create(
        id=2,
        name="Києво-Могилянська школа врядування імені Андрія Мелешевича",
        head="Малиш Наталія Андріївна",
    )

    disciplines = [
        (1, "Дипломатія: теорія і практика"),
        (2, "Аналіз зовнішньої політики"),
        (3, "Основи міжнародного публічного права"),
        (4, "Дипломатичний протокол та етикет"),
        (5, "Якісні методи досліджень у міжнародних відносинах"),
        (6, "Статистика та кількісні методи досліджень"),
        (7, "Основи державної служби та роботи з персоналом"),
        (8, "Багаторівневе врядування та євроінтеграція"),
        (9, "Національна економіка та антикризове управління"),
        (10, "Вироблення та аналіз суспільної політики"),
    ]
    for discipline_id, name in disciplines:
        Discipline.objects.using(database).create(id=discipline_id, name=name)

    international_relations = Program.objects.using(database).create(
        id=1,
        name="Міжнародні відносини",
        code="C3",
        description=(
            "Бакалаврська освітня програма «Міжнародні відносини, суспільні "
            "комунікації та регіональні студії» поєднує вивчення міжнародної "
            "політики, економіки, права та комунікацій. Студенти розвивають "
            "уміння аналізувати міжнародні події, оцінювати політичні ризики, "
            "працювати з джерелами інформації та обґрунтовувати власні висновки. "
            "Навчання охоплює дипломатію, зовнішню політику, дослідницькі методи "
            "та іноземні мови. Отримані знання можуть бути використані в "
            "аналітичній роботі, міжнародних організаціях, державних установах "
            "і громадському секторі. Нижче наведено добірку дисциплін програми; "
            "повний навчальний план доступний на офіційному сайті НаУКМА."
        ),
        coordinator_name="Метельський Данило Олександрович",
        coordinator_contact=(
            "+38 (067) 722-09-61; danylo.metelskyi@ukma.edu.ua"
        ),
        department_id=1,
    )
    international_relations.disciplines.set([1, 2, 3, 4, 5])

    governance = Program.objects.using(database).create(
        id=2,
        name="Публічне управління та адміністрування",
        code="D4",
        description=(
            "Бакалаврська освітня програма «Суспільне і приватне врядування» "
            "присвячена управлінню в публічному та приватному секторах. "
            "Студенти знайомляться з українськими та європейськими підходами "
            "до врядування, аналізують суспільні проблеми й управлінські рішення. "
            "Навчання передбачає роботу з практичними ситуаціями, опанування "
            "методів дослідження, вивчення державної служби та європейської "
            "інтеграції. Програма допомагає підготуватися до роботи в органах "
            "влади, місцевому самоврядуванні, громадських організаціях та інших "
            "установах. Нижче наведено добірку дисциплін; повний навчальний "
            "план оприлюднено на офіційному сайті НаУКМА."
        ),
        coordinator_name="Третьяков-Гродзевич Олексій Дмитрович",
        coordinator_contact=(
            "+38 (098) 648-27-29; o.tretiakov-hrodzevych@ukma.edu.ua"
        ),
        department_id=2,
    )
    governance.disciplines.set([6, 7, 8, 9, 10])

    teachers = [
        (
            1, "Яковлєв Максим Володимирович", "Завідувач кафедри, доцент",
            "Кандидат політичних наук", 1,
        ),
        (
            2, "Гриценко Олена Миколаївна", "Професор",
            "Доктор політичних наук", 1,
        ),
        (
            3, "Дем’янчук Олександр Петрович", "Професор",
            "Доктор політичних наук", 1,
        ),
        (
            4, "Малиш Наталія Андріївна", "Завідувачка кафедри",
            "Доктор наук з державного управління", 2,
        ),
        (
            5, "Ільченко-Сюйва Леся Василівна", "Доцент",
            "Кандидат наук з державного управління", 2,
        ),
    ]
    for teacher_id, name, position, degree, department_id in teachers:
        Teacher.objects.using(database).create(
            id=teacher_id,
            name=name,
            position=position,
            degree=degree,
            department_id=department_id,
        )

    FacultyInfo.objects.using(database).create(
        id=1,
        name="Факультет міжнародних відносин та врядування",
        description=(
            "Факультет міжнародних відносин та врядування Національного "
            "університету «Києво-Могилянська академія» пропонує бакалаврську "
            "підготовку з міжнародних відносин та публічного управління. "
            "Освітні програми охоплюють міжнародну політику, дипломатію, "
            "суспільні комунікації та врядування. На цьому навчальному сайті "
            "зібрано відомості про дві бакалаврські програми, їхні випускові "
            "кафедри та добірку викладачів і дисциплін. "
            "Наведені нижче адреса, телефон та електронна пошта належать "
            "приймальній комісії НаУКМА, а не деканату факультету."
        ),
        dean="Яковлєв Максим Володимирович",
        deputy_dean="Інформацію не підтверджено",
        address="Приймальна комісія: вул. Волоська, 12/4, Київ, 04070",
        phone="+38 (044) 425-60-22",
        email="vstup@ukma.edu.ua",
    )


def remove_faculty_data(apps, schema_editor):
    Department = apps.get_model("fakultet", "Department")
    Discipline = apps.get_model("fakultet", "Discipline")
    Program = apps.get_model("fakultet", "Program")
    Teacher = apps.get_model("fakultet", "Teacher")
    FacultyInfo = apps.get_model("fakultet", "FacultyInfo")
    database = schema_editor.connection.alias

    extra_programs = Program.objects.using(database).filter(
        department_id__in=[1, 2]
    ).exclude(pk__in=[1, 2])
    extra_teachers = Teacher.objects.using(database).filter(
        department_id__in=[1, 2]
    ).exclude(pk__in=[1, 2, 3, 4, 5])
    shared_disciplines = Program.objects.using(database).filter(
        disciplines__pk__in=range(1, 11)
    ).exclude(pk__in=[1, 2])
    if extra_programs.exists() or extra_teachers.exists() or shared_disciplines.exists():
        raise RuntimeError(
            "Cannot remove seed data: later records reference its departments "
            "or disciplines. Reassign those references before rollback."
        )

    Teacher.objects.using(database).filter(pk__in=[1, 2, 3, 4, 5]).delete()
    Program.objects.using(database).filter(pk__in=[1, 2]).delete()
    Discipline.objects.using(database).filter(pk__in=range(1, 11)).delete()
    Department.objects.using(database).filter(pk__in=[1, 2]).delete()
    FacultyInfo.objects.using(database).filter(pk=1).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("fakultet", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(populate_faculty, remove_faculty_data),
    ]
