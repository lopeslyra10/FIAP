using Aula.Cliente.API.Models;
using Aula.Cliente.API.Utils;
using Microsoft.AspNetCore.Mvc;
using Swashbuckle.AspNetCore.Annotations;
using System.Net;

namespace Aula.Cliente.API.Controllers
{
    [Route("api/v1/[controller]")]
    [ApiController]
    public class AulaController : ControllerBase
    {
        private List<AulaModel> _aulaModels;

        public AulaController()
        {
            _aulaModels = new List<AulaModel> 
            {
                new AulaModel { Id = 1, Nome = "Humberto", Email = "humberto@fiap.com" },
                new AulaModel { Id = 2, Nome = "Joao", Email = "joao@fiap.com" },
                new AulaModel { Id = 3, Nome = "Carlos", Email = "carlos@fiap.com" },
            };
        }

        [HttpGet]
        [SwaggerOperation(
            Summary = ApiDoc.AulaSummary,
            Description = ApiDoc.AulaDescription
        )]
        [SwaggerResponse(200, "Dados da aula retornou com sucesso", typeof(List<AulaModel>))]
        [SwaggerResponse(StatusCodes.Status204NoContent, "Nenhum dado foi encontrato")]
        [SwaggerResponse((int)HttpStatusCode.BadRequest, "Ocorreu uma falha ao buscar as informações")]
        public IActionResult Get()
        {
            try
            {
                var aulas = _aulaModels.ToList();

                if(aulas.Count == 0)
                    return NoContent();

                return Ok(aulas);
            }
            catch (Exception)
            {
                return BadRequest("Ocorreu um erro");
            }
        }

        [HttpGet("obter/{id}")]
        public IActionResult GetId(int id)
        {
            var aula = _aulaModels.FirstOrDefault(x => x.Id == id);

            return Ok(aula);
        }


        [HttpPost]
        public IActionResult Post(AulaModel model)
        {
            _aulaModels.Add(model);

            return Ok(_aulaModels.ToList());
        }

        [HttpPost("gravando/dados")]
        public IActionResult PostGravandoDados(AulaModel model)
        {
            _aulaModels.Add(model);

            return Ok(_aulaModels.ToList());
        }


        [HttpPut]
        public IActionResult Put(AulaModel model)
        {
            var aula = _aulaModels.FirstOrDefault(x => x.Id == model.Id);

            aula.Nome = model.Nome;

            return Ok(aula);
        }

        [HttpPut("{id}")]
        public IActionResult PutComParametros(int id, AulaModel model)
        {
            var aula = _aulaModels.FirstOrDefault(x => x.Id == id);

            aula.Nome = model.Nome;

            return Ok(aula);
        }


        [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            var aula = _aulaModels.FirstOrDefault(x => x.Id == id);

            _aulaModels.Remove(aula);

            return Ok(_aulaModels);
        }
    }
}
