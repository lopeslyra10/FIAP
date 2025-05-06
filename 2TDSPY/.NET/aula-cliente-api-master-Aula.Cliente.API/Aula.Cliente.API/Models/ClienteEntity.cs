using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Aula.Cliente.API.Models
{
    [Table("tb_cliente")]
    public class ClienteEntity
    {
        [Key]
        public int Id { get; set; }
        [Required]
        [StringLength(150)]
        public string Nome { get; set; } = string.Empty;
        [Required]
        public int Idade { get; set; }
        public string Email { get; set; } = string.Empty;
    }
}
