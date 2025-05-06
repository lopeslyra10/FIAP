package br.com.fiap.first_spring_app.service;

import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;

@Service
public class HelloWorldService {
    @GetMapping
    public String helloWorld(String name){
        return "Hello World! "+ name;
    }
}
