def hello_world(world="World"):
    """
Возврат строки приветсвия
    :param world:  Кого приветствуем
    :return:      строка приветствия

    """

    return f"Hello,{world}!"

print(hello_world())
print(hello_world("Home"))
