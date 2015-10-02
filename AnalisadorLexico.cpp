#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main (){
    char token[10];
    char c;
    ifstream reading;
    reading.open ("TesteArquivo.txt", ios::in);
    if (reading.is_open()){
        while (reading.get(c)){
            //cout << c << '\n';
            if(ispunct(c)){  // fazer os automatos de simbolos especiais/comentarios/identificadores 
                // automato dos identificadores         
                if (c == '@'){
                    cout << c; 
                    reading.get(c);// fazer arquivo de saida (log de token)
                    if(isalpha(c)){
                        cout << c;
                        reading.get(c);
                        if (c == '_'){
                            cout << c;
                            reading.get(c);
                        }
                        if (isalpha(c) || isdigit(c)){
                            cout << c;
                            reading.get(c);
                        }
                        while(isalpha(c) || isdigit(c)){
                            cout << c;
                            reading.get(c);
                        }
                        cout << " - Identificador" << '\n';
                    }
                }
                // automato de comentarios
                if (c == '@'){
                    cout << c; 
                    reading.get(c);
                    if (c == '@'){
                        cout << c; 
                        reading.get(c);
                        while(c != '\n'){
                            cout << c; 
                            reading.get(c);
                        }
                    }
                    cout << " - Comentario Tipo 1" << '\n';
                }
                if (c == '/'){
                    cout << c; 
                    reading.get(c);
                    if (c == '+'){
                        cout << c; 
                        reading.get(c);
                        do{
                            while(c != '+'){
                                cout << c; 
                                reading.get(c);
                            }
                        }while(c == '/');
                        cout << " - Comentario Tipo 2" << '\n';
                    }
                    if (c == '/'){
                        cout << c; 
                        reading.get(c);
                        do{
                            while(c != '/'){
                                cout << c; 
                                reading.get(c);
                            }
                        }while(c == '/');
                        cout << " - Comentario Tipo 3" << '\n';
                    }
                }
                // automato de simbolos especiais
                if (c == ';' || c == ',' || c == '.' || c == '+' || c == '-' || c == '*' || c == '(' || c == ')' || c == '=' || c == '{' || c == '}' || c == '/' || c == '@'){
                   cout << c;
                   cout << " - Simbolo Especial" << '\n'; 
                }
                if (c == ':' || c == '>'){
                    cout << c;
                    reading.get(c);
                    if (c == '=' || c == '/'){
                        cout << c;
                    }
                    cout << " - Simbolo Especial" << '\n';
                }
                if (c == '<'){
                    cout << c;
                    reading.get(c);
                    if (c == '>' || c == '=' || c == '*'){
                        cout << c;
                    }
                    cout << " - Simbolo Especial" << '\n';
                }
            } 
            if(isalpha(c)){  // fazer o automato de palavras reservadas          
                cout << c;
                reading.get(c);
                while(isalpha(c)){
                    cout << c;
                    reading.get(c);
                }
                if (c == '_'){
                    cout << c;
                    reading.get(c);
                }
                do{
                    if (isalpha(c)){
                        cout << c;
                        reading.get(c);
                    }
                }while(reading.eof());
                cout << " - Palavra Reservada" << '\n';
            } 
            /*if(isdigit(c)){  // fazer o automato de digitos          
                cout << c << " - Digito"<< endl;            
            }*/
        }
        reading.close();
    }
    else{ 
    	cout << "Erro ao abrir o arquivo!!"; 
    }
}