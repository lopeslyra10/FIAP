using Microsoft.AspNetCore.Mvc;

namespace OOP_API.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class EmpresaController : ControllerBase
    {
    
        [HttpGet]
        public IActionResult Get()
        {
            return Ok("GET: Informações da empresa");
        }

        [HttpPost]
        public IActionResult Post()
        {
            return Ok("POST: Empresa criada com sucesso");
        }

        [HttpPut]
        public IActionResult Put()
        {
            return Ok("PUT: Empresa atualizada com sucesso");
        }

        [HttpDelete]
        public IActionResult Delete()
        {
            return Ok("DELETE: Empresa removida com sucesso");
        }
    }
}

