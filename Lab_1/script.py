
import random
import time

print("=" * 60)
print("🔮 КВЕСТ: МАГИЧЕСКИЙ МНОЖИТЕЛЬ 🔮")
print("=" * 60)
print("\nДревний волшебник зашифровал код от своего сундука!")
print("Код состоит из числа z, при котором сумма 5z и 15z")
print("равна 840 магическим кристаллам.\n")
print("У тебя есть 3 попытки, чтобы найти значение z!")
print("=" * 60)

# Правильный ответ
correct_answer = 42

# Счетчики
attempts = 0
max_attempts = 3
points = 100

# Игровой цикл
while attempts < max_attempts:
    attempts += 1
    print(f"\n🎯 Попытка {attempts} из {max_attempts}")
    print(f"⭐ Текущие очки: {points}")
    
    try:
        user_answer = int(input("\n🔢 Введи значение z: "))
        
        # Проверка ответа
        if user_answer == correct_answer:
            print("\n" + "=" * 60)
            print("✨ ПОЗДРАВЛЯЮ! ТЫ НАШЁЛ ПРАВИЛЬНЫЙ ОТВЕТ! ✨")
            print(f"z = {correct_answer}")
            print(f"Проверка: 5 × {correct_answer} + 15 × {correct_answer} = {5*correct_answer + 15*correct_answer}")
            print("\n🎁 Сундук открылся! Твоя награда:")
            print(f"   💎 {points} магических очков")
            print(f"   🏆 Ранг: ", end="")
            if points == 100:
                print("ЛЕГЕНДАРНЫЙ ВОЛШЕБНИК!")
            elif points >= 70:
                print("ОПЫТНЫЙ МАГ!")
            else:
                print("НАЧИНАЮЩИЙ ЧАРОДЕЙ!")
            print("=" * 60)
            break
            
        else:
            # Неправильный ответ
            result = 5 * user_answer + 15 * user_answer
            print(f"\n❌ Неправильно! При z = {user_answer} получается:")
            print(f"   5 × {user_answer} + 15 × {user_answer} = {result}")
            print(f"   А нужно: 840")
            
            points -= 15  # Штраф за ошибку
            
            # Подсказки
            if attempts == 1:
                print("\n💡 Подсказка 1:")
                print("   Попробуй сложить коэффициенты при z!")
                print("   5z + 15z = (5 + 15)z = 20z")
                print("   Теперь реши: 20z = 840")
                
            elif attempts == 2:
                print("\n💡 Подсказка 2:")
                print("   20z = 840")
                print("   Раздели обе части на 20: z = 840 ÷ 20")
                print("   Осталась последняя попытка!")
    
    except ValueError:
        print("\n⚠️ Ошибка! Введи целое число.")
        attempts -= 1  # Не считаем неправильный ввод за попытку
        continue

# Если закончились попытки
if attempts >= max_attempts and user_answer != correct_answer:
    print("\n" + "=" * 60)
    print("💀 ИГРА ОКОНЧЕНА 💀")
    print(f"\nПравильный ответ был: z = {correct_answer}")
    print(f"Проверка: 5 × {correct_answer} + 15 × {correct_answer} = {5*correct_answer + 15*correct_answer}")
    print("\n🔮 Волшебник говорит:")
    print("   'Не расстраивайся! Попробуй ещё раз и ты обязательно справишься!'")
    print("=" * 60)

print("\n\n📊 СТАТИСТИКА ИГРЫ:")
print(f"   Использовано попыток: {attempts}")
print(f"   Финальные очки: {max(0, points)}")
print("\nСпасибо за игру! 🎮")
