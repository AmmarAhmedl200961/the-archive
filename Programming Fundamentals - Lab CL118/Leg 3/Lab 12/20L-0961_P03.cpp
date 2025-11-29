#include <iostream>
using namespace std;

struct Item
{
	string menu;
	double price;
};
Item menuList[11];
int n[11] = { 0 };

void getData()
{
    menuList[1].menu = "Egg (cooked to order)";
    menuList[1].price = 1.99;
    menuList[2].menu = "Golden-Brown Pancake";
    menuList[2].price = 1.99;
    menuList[3].menu = "French Toast";
    menuList[3].price = 2.99;
    menuList[4].menu = "Muffin";
    menuList[4].price = 0.99;
    menuList[5].menu = "Bagel w/ Spread";
    menuList[5].price = 1.20;
    menuList[6].menu = "Fresh Fruit";
    menuList[6].price = 3.49;
    menuList[7].menu = "Steel-Cut Irish Oatmeal";
    menuList[7].price = 4.69;
    menuList[8].menu = "Coffee";
    menuList[8].price = 1.50;
    menuList[9].menu = "Pot of Assorted Tea";
    menuList[9].price = 1.75;
    menuList[10].menu = "Hot Chocolate";
    menuList[10].price = 1.75;

}

void showMenu()
{
	cout << endl <<"-----------Today's Menu-----------" << endl;
    for (int i = 1; i <= 10; i++)
    {
        cout << i << "\t" << menuList[i].menu << "  \t\t" << "$ " << menuList[i].price << endl;
    }

    int choice, quantity;
    char con;

    cout << "Do you want to place an order? (y/n) ";
    cin >> con;

    if (con == 'y')
        do {
            con = 0; // initialising continue variable

            cout << "Enter item number: ";
            cin >> choice; 
            if (choice >= 1 && choice <= 10)
            {
                cout << "Enter Item Quantity :";
                cin >> quantity;
                switch (choice)
                {
                case 1:
                {
                    n[1] = n[1] + quantity;
                    cout << "You have Selected :" << menuList[1].menu << endl;

                    break;
                }
                case 2:
                {
                    n[2] = n[2] + quantity;
                    cout << "You have Selected :" << menuList[2].menu << endl;

                    break;
                }
                case 3:
                {
                    n[3] = n[3] + quantity;
                    cout << "You have Selected :" << menuList[3].menu << endl;

                    break;
                }
                case 4:
                {
                    n[4] = n[4] + quantity;
                    cout << "You have Selected :" << menuList[4].menu << endl;

                    break;
                }
                case 5:
                {
                    n[5] = n[5] + quantity;
                    cout << "You have Selected :" << menuList[5].menu << endl;

                    break;
                }
                case 6:
                {
                    n[6] = n[6] + quantity;
                    cout << "You have Selected :" << menuList[6].menu << endl;

                    break;
                }
                case 7:
                {
                    n[7] = n[7] + quantity;
                    cout << "You have Selected :" << menuList[7].menu << endl;


                    break;
                }

                case 8:
                {
                    n[8] = n[8] + quantity;
                    cout << "You have Selected :" << menuList[8].menu << endl;


                    break;
                }

                case 9:
                {
                    n[9] = n[9] + quantity;
                    cout << "You have Selected :" << menuList[7].menu << endl;


                    break;
                }

                case 10:
                {
                    n[10] = n[10] + quantity;
                    cout << "You have Selected :" << menuList[10].menu << endl;


                    break;
                }
                default:
                    cout << "Invalid Input" << endl;
                }
                cout << "Select another item? (y/n):" << endl;
                cin >> con;
            }
            else
                cout << "Enter item number between 1 and 10 ";
                continue;

        } while (con != 'n');
    cout << endl;
}

void printCheck()
{
    double total = 0, tax, due;
    cout << endl <<" Thank you for eating at the FAST`S Cafe" << endl;

    cout << "------------------------------------" << endl;
    cout << "Receipt \tQty \tAmount" << endl;
    cout << "------------------------------------" << endl;
    for (int i = 1; i <= 10; i++)
    {
        if (n[i] > 0)
        {
            cout << menuList[i].menu << "\t " << n[i] << "   $ " << menuList[i].price * n[i] << endl;
            total = total + (menuList[i].price * n[i]);
        }

    }
    tax = (total * 1.05) - total;
    due = total + tax; 
    cout << "Tax " << "\t" << tax << endl;
    cout << "Amount due      $ " << due << endl;
}

int main()
{
    cout << "\t\t\tWelcome to the FAST'S Cafe" << endl;
    getData();
    showMenu();
    printCheck();


	return 0;
}