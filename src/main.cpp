#include <cstdlib>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

struct Movie {
    std::string title;
    std::string genre;
    std::string mood;
    int minutes;
    std::string description;
};

// Fictional titles keep the demonstration self-contained and easy to review.
const std::vector<Movie> catalogue = {
    {"Orbit Station", "Sci-Fi", "Thoughtful", 96, "A crew solves a mystery aboard a research station."},
    {"Tomorrow's Signal", "Sci-Fi", "Exciting", 114, "A radio message sends friends on a time-bending journey."},
    {"The Last Satellite", "Sci-Fi", "Thoughtful", 128, "An engineer searches for a lost signal beyond Earth."},
    {"Neon Run", "Sci-Fi", "Exciting", 83, "A courier races across a futuristic city."},
    {"Summer Market", "Comedy", "Relaxed", 89, "Neighbours come together to rescue a local market."},
    {"The Accidental Chef", "Comedy", "Exciting", 105, "A cooking contest becomes a series of surprises."},
    {"Coffee and Clouds", "Comedy", "Relaxed", 118, "Old friends meet again in a tiny hillside cafe."},
    {"Weekend Mix-Up", "Comedy", "Exciting", 78, "A switched suitcase changes a family's holiday."},
    {"River Letters", "Drama", "Thoughtful", 94, "Letters reconnect two generations of a family."},
    {"The Long Road Home", "Drama", "Thoughtful", 121, "A musician returns to the town she left behind."},
    {"Crossing Paths", "Drama", "Relaxed", 87, "Two commuters find an unexpected friendship."},
    {"Night Shift", "Drama", "Exciting", 109, "A hospital worker faces a difficult overnight choice."}
};

int readChoice(const std::string& prompt, int minimum, int maximum) {
    while (true) {
        std::cout << prompt;
        int choice;
        if (std::cin >> choice && choice >= minimum && choice <= maximum) {
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            return choice;
        }
        std::cout << "Please enter a number from " << minimum << " to " << maximum << ".\n";
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        if (std::cin.eof()) {
            std::cout << "Input ended. Goodbye.\n";
            std::exit(0);
        }
    }
}

int main() {
    std::cout << "MOVIE DISCOVERY ASSISTANT\n"
              << "A small rule-based demonstration inspired by online movie discovery.\n"
              << "The titles below are fictional; no account or internet is needed.\n";
    bool again = true;
    while (again) {
        std::cout << "\nGenre: 1 Sci-Fi  2 Comedy  3 Drama\n";
        int genre = readChoice("Choose genre (1-3): ", 1, 3);
        std::cout << "Mood: 1 Relaxed  2 Exciting  3 Thoughtful\n";
        int mood = readChoice("Choose mood (1-3): ", 1, 3);
        int length = readChoice("Length: 1 Up to 100 min  2 Over 100 min: ", 1, 2);
        const std::string genres[] = {"Sci-Fi", "Comedy", "Drama"};
        const std::string moods[] = {"Relaxed", "Exciting", "Thoughtful"};
        int bestScore = -1;
        const Movie* best = nullptr;
        for (const Movie& movie : catalogue) {
            if (movie.genre != genres[genre - 1]) continue;
            int score = 0;
            if (movie.mood == moods[mood - 1]) score += 2;
            if ((movie.minutes <= 100) == (length == 1)) score += 1;
            if (score > bestScore) {
                best = &movie;
                bestScore = score;
            }
        }
        // The selected genre always contains titles, even when other preferences conflict.
        std::cout << "\nRecommendation: " << best->title << " (" << best->minutes << " min)\n"
                  << best->description << "\n"
                  << "Why: It matches your " << genres[genre - 1] << " choice";
        if (best->mood == moods[mood - 1]) std::cout << ", " << moods[mood - 1] << " mood";
        if ((best->minutes <= 100) == (length == 1)) std::cout << ", and length preference";
        std::cout << ".\n";
        again = readChoice("Find another? 1 Yes  2 No: ", 1, 2) == 1;
    }
    std::cout << "Thanks for exploring.\n";
}
