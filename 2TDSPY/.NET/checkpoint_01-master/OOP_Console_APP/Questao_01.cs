namespace OOP_Console_APP;

// Crie um programa em C# que pergunte ao usuário 3 informações:
// 1.	Nome
// 2.	Idade
// 3.	Se possui CNH (Carteira de Habilitação) – deve responder com “sim” ou “não”

// O programa deve verificar se a pessoa pode dirigir legalmente no Brasil, considerando:
//     •	Ter 18 anos ou mais E
//     •	Possuir CNH

// Use operadores lógicos e if para fazer essa verificação. Ao final, exiba uma mensagem usando interpolação de string.

//Mensagens esperadas (saídas) no console

// Se a pessoa tiver 18 anos ou mais e responder "sim" para CNH:
//R: "Olá {nome}, você pode dirigir legalmente!"

//Se a pessoa tiver 18 anos ou mais e responder "não" para CNH:
//R: "Olá {nome}, você tem idade para dirigir, mas precisa tirar a CNH."

//Se a pessoa tiver menos de 18 anos e responder "sim" para CNH:
//R: "Olá {nome}, você tem CNH, mas ainda não tem idade legal para dirigir!"

//Se a pessoa tiver menos de 18 anos e responder "não" para CNH:
//R: "Olá {nome}, você não pode dirigir ainda."



public class Questao_01
{
    public Questao_01()
    {
        // Solicita as informações do usuário
        Console.Write("Digite seu nome: ");
        string nome = Console.ReadLine();

        Console.Write("Digite sua idade: ");
        int idade = int.Parse(Console.ReadLine());

        Console.Write("Você possui CNH? (sim/não): ");
        string possuiCnh = Console.ReadLine().Trim().ToLower();

        // Verifica a condição para dirigir legalmente no Brasil
        if (idade >= 18 && possuiCnh == "sim")
        {
            Console.WriteLine($"Olá {nome}, você pode dirigir legalmente!");
        }
        else if (idade >= 18 && possuiCnh == "não")
        {
            Console.WriteLine($"Olá {nome}, você tem idade para dirigir, mas precisa tirar a CNH.");
        }
        else if (idade < 18 && possuiCnh == "sim")
        {
            Console.WriteLine($"Olá {nome}, você tem CNH, mas ainda não tem idade legal para dirigir!");
        }
        else
        {
            Console.WriteLine($"Olá {nome}, você não pode dirigir ainda.");
        }
    }
}