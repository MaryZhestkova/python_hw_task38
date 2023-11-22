// // Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.
// m = 2, n = 3 -> A(m,n) = 9
// m = 3, n = 2 -> A(m,n) = 29

int ReadInt(string msg)
{
    Console.Write(msg);
    return Convert.ToInt32(Console.ReadLine());
}

int ack(int n, int m){
    if(n==0){
        return m+1;       
    } else if(m==0){
      return ack(n-1,1);
    }
    return ack(n-1, ack(n, m-1));
}
Console.WriteLine(ack(ReadInt("Введите N: "), ReadInt("Введите M: ")));