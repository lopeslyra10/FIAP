import { Veiculo } from "../Veiculo";
 
export class GerenciadorVeiculos {
  private veiculos: Veiculo[] = [];
 
  adicionarVeiculo(veiculo: Veiculo): void {
    this.veiculos.push(veiculo);
  }
 
  listarVeiculos(): void {
    this.veiculos.forEach((veiculo, index) => {
      console.log(`${index + 1}. ${veiculo.modelo} - ${veiculo.ano}`);
    });
  }
 
  removerVeiculo(indice: number): void {
    if (indice >= 0 && indice < this.veiculos.length) {
      this.veiculos.splice(indice, 1);
    } else {
      console.log("Índice inválido.");
    }
  }
}
