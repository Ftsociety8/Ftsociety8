#include <iostream>
#include <windows.h>
using namespace std;
int Menu();
void Add();
void Delete();
void Update();
void Search();
void insert();
const int N = 100;
struct Student
{
  int id;
  char fname[30];
  char lname[30];
  char college[30];
}s[N];
int main()
{
  int choice;
  for (;;)
  {
    system("cls");
    choice = Menu();
    switch (choice)
    {
      case 1:
        Add();
        break;
      case 2:
        Delete();
        break;
      case 3:
        Update();
        break;
      case 4:
        Search();
        break;
      case 5:
        break;
      default:
        cout << "...................." << endl;
    }
  }
  return 0;
}
int Menu()
{
  int n;
  cout << "\t\t\t\t\t\t\tMenu" << endl;
  cout << "1 : Add Student" << endl;
  cout << "2 : Delete Student" << endl;
  cout << "3 : Update The Infos" << endl;
  cout << "4 : Search id" << endl;
  cout << "5 : Exit" << endl;
  cout << "Select your choice:";
  cin >> n;
  return n;
}
void Add()
{
  int i;
  for (int i = 0; i < N; i++)
  {
    s[i].fname[0] = '\0';
    break;
  }
  insert(i);
}
void insert(int i)
{
  int a;
  char b, c;
  cout << "Enter The id:";
  cin >> a;
  s[i].id = a;
  cout << "Enter The First Name:";
  cin >> b;
  s[i].fname = b;
  cout << "Enter The Last Name :";
  cin >> c;
  s[i].lname = c;
  cout << s[i].fname;
}
void Delete()
{
}
void Update()
{
}
void Search()
{
}