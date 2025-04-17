using Aula.Cliente.API.Data.AppData;
using Aula.Cliente.API.Models;
using Microsoft.AspNetCore.Mvc;

namespace Aula.Cliente.API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ClienteController : ControllerBase
    {
        private readonly ApplicationContext _context;

        public ClienteController(ApplicationContext context)
        {
            _context = context;
        }


        [HttpGet]
        public IActionResult Get()
        {
            try
            {
                var clientes = _context.Cliente.ToList();

                if (clientes.Count == 0)
                    return NoContent();

                return Ok(clientes);
            }
            catch (Exception)
            {
                return BadRequest("Ocorreu uma falha");
            }
        }

        [HttpGet("{id}")]
        public IActionResult GetPorId(int id)
        {
            try
            {
                var clientes = _context.Cliente.Find(id);

                if (clientes is null)
                    return NoContent();

                return Ok(clientes);
            }
            catch (Exception)
            {
                return BadRequest("Ocorreu uma falha");
            }
        }

        [HttpPost]
        public IActionResult Post(ClienteEntity entity)
        {
            try
            {
                _context.Cliente.Add(entity);
                _context.SaveChanges();

                return Ok(entity);
            }
            catch (Exception)
            {
                return BadRequest("Ocorreu uma falha");
            }
        }

        [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            try
            {
                var cliente = _context.Cliente.Find(id);

                if (cliente is not null)
                {
                    _context.Cliente.Remove(cliente);
                    _context.SaveChanges();

                    return Ok(cliente);
                }

                return NoContent();
            }
            catch (Exception)
            {
                return BadRequest("Ocorreu uma falha");
            }
        }
    }
}
