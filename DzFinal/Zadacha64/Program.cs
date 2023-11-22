// Задача 64: Задайте значения M и N. Напишите программу, которая выведет все чётные натуральные числа 
// в промежутке от M до N с помощью рекурсии.
// M = 1; N = 5 -> "2, 4"
// M = 4; N = 8 -> "4, 6, 8"

int ReadInt(string msg)
{
    System.Console.Write(msg);
    return Convert.ToInt32(Console.ReadLine());
}

void EvenNumbers(int m, int n)
{
    if (m > n)
    {
        return;
    }
    if (m % 2 == 0 && m > 0)
    {
        Console.Write($"{m} ");
    }
    EvenNumbers(m + 1, n);
}

int m = ReadInt("Введите начало диапазона: ");
int n = ReadInt("Введите конец диапазона: ");
EvenNumbers(m, n);
System.Console.WriteLine();