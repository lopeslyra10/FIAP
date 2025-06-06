package br.com.fiap.biblioteca.dominio;

import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class RelacaoDeAlunosMutuariosTest {

    private RelacaoDeAlunosMutuarios relacaoDeMutuarios;

    @Test
    void lerEEscreverMutuarios() throws IOException {
        File relatorio = new File("src/test/resources/relatorio.txt");
        relatorio.delete();
        relacaoDeMutuarios = new RelacaoDeAlunosMutuarios(relatorio);

        Aluno fernandaSantos = new Aluno("Fernanda Santos", "550123", "1TDSPY");
        Aluno gustavoFerreira = new Aluno("Gustavo Ferreira", "555444", "1TDSPY");
        relacaoDeMutuarios.adicionar(fernandaSantos);
        relacaoDeMutuarios.adicionar(gustavoFerreira);

        List<String> todosAlunos = relacaoDeMutuarios.listarTodos();

        List<String> alunosEsperados = new ArrayList<>();
        alunosEsperados.add("550123");
        alunosEsperados.add("555444");
        assertTrue(todosAlunos.containsAll(alunosEsperados));
    }
}