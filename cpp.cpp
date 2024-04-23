#include <iostream>
#include <windows.h>
#include <cstring>
#include <cctype>
#include <conio.h>
using namespace std;
char Menu();
void Add();
void Delete();
void Update();
void Search();
void insert(int);
void Display_all();
const int N = 100;
struct Student
{
  int id;
  char fname[30];
  char lname[30];
  char college[30];
} s[N];
int main()
{
  cin.clear();
  char choice;
  for (;;)
  {
      fflush(stdin);
    system("cls");
    choice = tolower(Menu());
    switch (choice)
    {
      case 'a':
        Add();
        break;
      case 'd':
        Delete();
        break;
      case 'u':
        Update();
        break;
      case 's':
        Search();
        break;
      case 'p':
        Display_all();
        break;
      case 'e':
        exit(0);
      default:
        cout << "Press any key to continue";
       _getch();
    }
  }
  return 0;
}
char Menu()
{
  char n;
  do
  {
    cout << "\t\t\t\t\t\t\tMenu" << endl;
    cout << "A : Add Student" << endl;
    cout << "D : Delete Student" << endl;
    cout << "U : Update The Infos" << endl;
    cout << "S : Search id" << endl;
    cout << "P : Display infos" << endl;
    cout << "E:  exit " << endl;
    cout << "Select your choice:";
    cin >> n;
  } while (!strchr("aduspe", tolower(n)));
  return n;
}
void Add()
{
 int i;
  for (i = 0; i < N; i++)
  {
    if (s[i].fname[0] == '\0')
      break;
  }
  insert(i);
}
void insert(int i)
{
  cout << "Enter The id:";
  cin >> s[i].id;
  fflush(stdin);
  cout << "Enter The First Name:";
  cin >> s[i].fname;
  cout << "Enter The Last Name :";
  cin >> s[i].lname;
  cout << "Enter The college :";
  cin >> s[i].college;
}
void Delete()
{
 bool flag = false;
  int ID;
  cout << "Enter The ID :";
  cin >> ID;
  for (int i = 0; i < N; i++) {
      if (ID == s[i].id) {
          s[i].fname[0] = '\0';
          cout << "Deleted.";
          flag = true;
          break;
      }
  }
    if (!flag)
 {
    cout << "Not Exists.";
  }
  cout<<"Press any key to continue...";
  _getch();
}
void Update()
{
  bool flag = false;
  int ID;
  cout << "Enter The ID :";
  cin >> ID;
  for (int i = 0; i < N; i++)
  {
    if (ID == s[i].id)
   {
     insert(i);
      flag = true;
      break;
   }
  }
  if (!flag) {
    cout << "Not Exists.";
  }
}
void Search()
{
    bool flag = false;
    int ID;
    cout << "Enter The ID :";
    cin >> ID;
    for(int i = 0; i < N; i++)
    {
        if (ID == s[i].id)
        {
            cout<<s[i].fname<<endl;
            cout<<s[i].lname<<endl;
            cout<<s[i].college<<endl;
            flag = true;
            break;
        }

    }
    if (!flag)
    {
        cout << "This Id doesn't Exists";
   }
    cout << "Press any key to continue";
    _getch();

}
void Display_all()
{
  int i, flag = false;
  for (i = 0; i < N; i++)
  {
    if (s[i].fname[0] != '\0')
    {
      flag = true;
      cout << "id:" << s[i].id << endl;
      cout << "first name:" << s[i].fname << endl;
      cout << "last name:" << s[i].lname << endl;
      cout << "college:" << s[i].college << endl;
      cout << "==================================\n" << endl;
    }
  }
  if (!flag)
  {
    cout << "\n\t\t\t\t\t list is empty";
  }
  cout << "Press any key to continue";
  _getch();
}
