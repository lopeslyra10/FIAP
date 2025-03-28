package br.com.fiap.biblioteca.dominio;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.StandardOpenOption;
import java.util.List;

public class RelacaoDeAlunosMutuarios {

    private File relatorio;

    public RelacaoDeAlunosMutuarios(File relatorio) throws IOException {
        this.relatorio = relatorio;
        this.relatorio.createNewFile();
    }

    public void adicionar(Aluno mutuario) throws IOException {
        String linha = mutuario.getChamada() + "\n";
        Files.write(relatorio.toPath(), linha.getBytes(), StandardOpenOption.APPEND);
    }

    public List<String> listarTodos() throws IOException {
        return Files.readAllLines(relatorio.toPath());
    }
}
