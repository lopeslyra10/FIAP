namespace Aula.Cliente.API.Models
{
    public record AulaModel
    {
        public int Id { get; set; }
        public string Nome { get; set; }
        public string Email { get; set; }
    }
}
