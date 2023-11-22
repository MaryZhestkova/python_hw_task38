// Задача 66: Задайте значения M и N. 
// Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.
// M = 1; N = 15 -> 120
// M = 4; N = 8. -> 30


int ReadInt(string msg)
{
    System.Console.Write(msg);
    return Convert.ToInt32(Console.ReadLine());
}

int SumNaturalNumbers(int m, int n)
{
    if (m > n)
    {
        return 0;
    }
    if (m <= 0)
    {
        return SumNaturalNumbers(m + 1, n);
    }
    return m + SumNaturalNumbers(m + 1, n);
}

int m = ReadInt("Введите первое число: ");
int n = ReadInt("Введите второе число: ");


Console.WriteLine(SumNaturalNumbers(m, n));