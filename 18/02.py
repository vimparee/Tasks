def letter(name, date, email, place="Нефтекамск"):
    print(f"To:", email)
    print(f"Здравствуйте,", name)
    print(f"Были бы рады видеть вас на встрече начинающих программистов в {place}, которая пройдет {date}.")


letter("Evgeniy", "25.06.2022", "test@mail.ru")