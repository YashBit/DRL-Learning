#include <iostream>
using namespace std;

int main(){
    string personName;
    personName = "John";
    int characterAge;
    characterAge = 35;
    cout << "His age is: " << characterAge << endl;
    char grade = 's';
    // String: Bunch of different characters
    string phrase = "Giraffe Academy";
    // Float vs Double: Double can store more decimal points than a float
    bool isMale;
    cout << phrase.find("Academy", 0) << endl;
    /*

        Numbers: Double - More specific decimal points

    */
    int age;
    cout << pow(2, 5) << endl;
    cout << ceil(3.2) << endl;
    cout << round(4.6) << endl;
    cout << fmax(2, 3) << endl;
    cout << "Enter your age" << endl;
    cin >> age;
    return 0;
}