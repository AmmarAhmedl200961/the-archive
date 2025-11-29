# include <iostream>
using namespace std;

int main()
{

	system("Pause");
	return 0;
}

int main_5()
{ 
	 // This program averages 3 test scores.
    // It uses the variable perfectScore as a flag.
	cout << "Enter your 3 test scores and I will "<< "average them:";
int score1, score2, score3;
score1=score2=score3=0;
cin >> score1 >> score2 >> score3;
float average;
average = (score1 + score2 + score3) / 3.0;
float perfectScore;
if (average == 100)
{
	perfectScore = true; // Set the flag variable

}
cout<<"Your average is  "<<average;

if (average == 100)
{
cout << "Congratulations!\n";
cout << "That's a perfect score.\n";
cout << "You deserve a pat on the back!\n";
system("Pause");

return 0;
}

}


int main_4()
{
// This program uses an if/else if statement to assign a
// letter grade (A, B, C, D, or F) to a numeric test score.

int testScore;
cout << "Enter your test score and I will tell you\n";
cout << "the letter grade you earned: ";
cin >> testScore;
if (testScore < 60)
cout << "Your grade is F.\n";
else if (testScore < 70)
cout << "Your grade is D.\n";
else if (testScore < 80)
cout << "Your grade is C.\n";
else if (testScore < 90)
cout << "Your grade is B.\n";
else if (testScore > 100)
cout << "That is not a valid score.\n";
else if (testScore <= 100)
cout << "Your grade is A.\n";
system("Pause");

return 0;
}

int main_3()
{
	// This program divides a user-supplied number by another
   // user-supplied number. It checks for division by zero

double num1, num2, quotient;
cout << "Enter a number: ";
cin >> num1;
cout << "Enter another number: ";
cin >> num2;
if (num2 == 0)
{
	cout << "Division by zero is not possible.\n";
cout << "Please run the program again ";
cout << "and enter a number besides zero.\n";

}

else 
{
	quotient = num1 / num2;
cout << "The quotient of " << num1 << " divided by " << num2 << " is ";
cout << quotient << endl;
}
system("Pause");

return 0;
}

int main_2()
{
	int f, s, area;
	f=s=area=0;
	cout<<endl<<"Flavour of your choice (1), (2) & (3):  "<<endl<<"(1) Tikka"<<endl<<"(2) Fajita"<<endl<<"(3) Supreme";
	cin>>f;
	cout<<endl<<"Your pizza size radius  ";
	cin>>s;
	area=3.14*(s*s);
	cout<<endl<<"Price of your pizza:  "<<area<<endl;
	
	system("Pause");

	return 0;
}

int main_1()
{
	int a;
	cout<<endl<<"Enter the colour value:  ";
	cin>>a;
	if(a>=1 && a<=5)
		cout<<"Blue"<<endl;
	if(a>=6 && a<=10)
		cout<<"Red"<<endl;
	if(a>=11 && a<=15)
		cout<<"Green"<<endl;
	if(a>=15)
		cout<<"Not a correct colour option"<<endl;

	system("Pause");
	return 0;
}