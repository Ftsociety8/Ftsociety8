#include <iostream>
#include <vector>
#include <random>
#include <ctime>
#include "minesweeper.h"

using namespace std;

// Define the dimensions of the minefield
const int width = 10;
const int height = 10;

// Define the number of mines
const int numMines = 10;

// Create a 2D vector to represent the minefield
vector<vector<char>> minefield(height, vector<char>(width, '.'));

// Function to generate the minefield
void generateMinefield() {
    // Set all cells to be empty
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            minefield[i][j] = '.';
        }
    }

    // Generate the mines
    srand(time(NULL));
    for (int i = 0; i < numMines; i++) {
        int x = rand() % width;
        int y = rand() % height;

        // Make sure the cell is empty
        while (minefield[y][x] == 'M') {
            x = rand() % width;
            y = rand() % height;
        }

        // Place the mine
        minefield[y][x] = 'M';
    }
}

// Function to print the minefield
void printMinefield() {
    // Print the column numbers
    cout << "  ";
    for (int i = 0; i < width; i++) {
        cout << i << " ";
    }
    cout << endl;

    // Print the minefield
    for (int i = 0; i < height; i++) {
        // Print the row number
        cout << i << " ";

        // Print the cells
        for (int j = 0; j < width; j++) {
            cout << minefield[i][j] << " ";
        }

        // Print a newline
        cout << endl;
    }
}

// Function to get the number of mines adjacent to a cell
int getAdjacentMines(int x, int y) {
    // Initialize the number of adjacent mines to 0
    int numAdjacentMines = 0;

    // Check the cells adjacent to the given cell
    for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
            // Make sure the cell is within the bounds of the minefield
            if (x + i >= 0 && x + i < width && y + j >= 0 && y + j < height) {
                // Check if the cell is a mine
                if (minefield[y + j][x + i] == 'M') {
                    // Increment the number of adjacent mines
                    numAdjacentMines++;
                }
            }
        }
    }

    // Return the number of adjacent mines
    return numAdjacentMines;
}

// Function to play the game
void playGame() {
    // Generate the minefield
    generateMinefield();

    // Print the minefield
    printMinefield();

    // Get the player's move
    int x, y;
    cout << "Enter your move (row, column): ";
    cin >> x >> y;

    // Check if the player hit a mine
    if (minefield[y][x] == 'M') {
        // Print a message indicating that the player lost
        cout << "You hit a mine! Game over." << endl;
    } else {
        // Get the number of adjacent mines
        int numAdjacentMines = getAdjacentMines(x, y);

        // Update the minefield to show the number of adjacent mines
        minefield[y][x] = numAdjacentMines + '0';

        // Print the updated minefield
        printMinefield();

        // Check if the player has won
        bool won = true;
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if (minefield[i][j] == '.') {
                    won = false;
                    break;
                }
            }
        }

        // Print a message indicating that the player won
        if (won) {
            cout << "You win!" << endl;
        }
    }
}

// Main function
int main()
{
    // Play the game
    playGame();
    return 0;
}