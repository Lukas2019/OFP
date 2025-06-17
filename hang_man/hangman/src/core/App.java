package core;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        String loesung = "Hello World";

        String erraten = "____________";
        int hangman = 6;

        while (hangman>=0 || erraten == loesung) {
            String buchstabe = input("Buchstabe:");
            Boolean buchstabe_erraten = false;
            for(int i =0; i < loesung.length(); i++){
                if(loesung.charAt(i) == buchstabe.charAt(0)){
                    buchstabe_erraten = true;
                    if (loesung.length()==i){
                        erraten = erraten.substring(0,i-1)+loesung.charAt(i);
                    }else if (i==0){
                        erraten = loesung.charAt(0)+erraten.substring(i+1,erraten.length());
                    }else{
                    erraten = erraten.substring(0,i-1) + loesung.charAt(i) + erraten.substring(i+1, loesung.length());
                    }
                }
        }
        if (buchstabe_erraten) {
            System.out.println("Richtig "+erraten);
            if(erraten==loesung){
                System.out.println("Gewonnen"+erraten);
            }
        }else {
            hangman--;
            System.out.println("Falsch "+erraten);
        }

        }
        if (hangman == 0) {
            System.out.println("Du hast verloren.");
        }
        }

    private static String input(String prompt) {
        System.out.print(prompt);
        class ScannerHolder {
            static final java.util.Scanner scanner = new java.util.Scanner(System.in);
        }
        return ScannerHolder.scanner.nextLine();
}
}