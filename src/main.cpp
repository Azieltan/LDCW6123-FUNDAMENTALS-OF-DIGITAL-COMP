#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

struct Track {
    std::string title;
    std::string artist;
    std::string genre;
    std::string mood;
    int minutes;
    std::string description;
};

// All tracks and artists are fictional; no music service or network is used.
const std::vector<Track> catalogue = {
    {"City Lanterns", "Mira Vale", "Pop", "Calm", 3, "Soft vocals for a quiet evening."},
    {"Bright Avenue", "The North Lights", "Pop", "Energetic", 5, "A lively chorus built for a long drive."},
    {"Letters in Rain", "Elio Park", "Pop", "Calm", 6, "An unhurried song about finding home."},
    {"Daybreak Run", "Nova Finch", "Pop", "Energetic", 3, "A quick beat to start the morning."},
    {"Blue Circuit", "Kite Sequence", "Electronic", "Calm", 3, "Gentle synthesisers and a steady pulse."},
    {"Night Current", "Vela Static", "Electronic", "Energetic", 5, "Bright layers rise across the dance floor."},
    {"Slow Orbit", "Rin Echo", "Electronic", "Calm", 6, "A spacious instrumental with patient textures."},
    {"Pulse Arcade", "Luma Phase", "Electronic", "Energetic", 3, "Playful rhythms in a compact track."},
    {"Paper Harbour", "June Rowan", "Acoustic", "Reflective", 3, "An intimate guitar song about old letters."},
    {"Homeward Lines", "Ari Fern", "Acoustic", "Reflective", 5, "A winding folk story about a return journey."},
    {"Quiet Crossing", "Nell Rivers", "Acoustic", "Calm", 3, "Warm strings accompany a peaceful walk."},
    {"Storm Window", "Theo Lark", "Acoustic", "Energetic", 5, "Brisk strumming through a change of season."}
};

// Whole-line parsing rejects entries such as 1abc, decimals and huge integers.
int readChoice(const std::string& prompt, int minimum, int maximum) {
    while (true) {
        std::cout << prompt;
        std::string line;
        if (!std::getline(std::cin, line)) {
            std::cout << "\nInput ended. Goodbye.\n";
            std::exit(0);
        }
        std::istringstream input(line);
        int choice = 0;
        char extra = '\0';
        if (input >> choice && !(input >> extra)
            && choice >= minimum && choice <= maximum) {
            return choice;
        }
        std::cout << "Please enter a whole number from " << minimum
                  << " to " << maximum << ".\n";
    }
}

int main() {
    std::cout << "MUSIC DISCOVERY ASSISTANT\n"
              << "An offline, rule-based demonstration of digital music discovery.\n"
              << "Every track and artist is fictional; no account or internet is needed.\n";
    bool again = true;
    while (again) {
        std::cout << "\nGenre: 1 Pop  2 Electronic  3 Acoustic\n";
        int genre = readChoice("Choose genre (1-3): ", 1, 3);
        std::cout << "Mood: 1 Calm  2 Energetic  3 Reflective\n";
        int mood = readChoice("Choose mood (1-3): ", 1, 3);
        int length = readChoice("Length: 1 Up to 4 min  2 Over 4 min: ", 1, 2);
        const std::string genres[] = {"Pop", "Electronic", "Acoustic"};
        const std::string moods[] = {"Calm", "Energetic", "Reflective"};
        // A matching genre is required; mood outranks the length preference.
        int bestScore = -1;
        const Track* best = nullptr;
        for (const Track& track : catalogue) {
            if (track.genre != genres[genre - 1]) continue;
            int score = 0;
            if (track.mood == moods[mood - 1]) score += 2;
            if ((track.minutes <= 4) == (length == 1)) score += 1;
            // On equal scores retain the first track in catalogue order.
            if (score > bestScore) {
                best = &track;
                bestScore = score;
            }
        }
        // Guard against a future catalogue without the requested genre.
        if (best == nullptr) {
            std::cout << "No tracks are available in this genre.\n";
            again = readChoice("Find another? 1 Yes  2 No: ", 1, 2) == 1;
            continue;
        }
        std::cout << "\nRecommendation: " << best->title << " by " << best->artist
                  << " (" << best->minutes << " min)\n"
                  << best->description << "\n"
                  << "Why: It matches your " << genres[genre - 1] << " choice";
        if (best->mood == moods[mood - 1]) std::cout << ", " << moods[mood - 1] << " mood";
        if ((best->minutes <= 4) == (length == 1)) std::cout << ", and length preference";
        std::cout << ".\n";
        again = readChoice("Find another? 1 Yes  2 No: ", 1, 2) == 1;
    }
    std::cout << "Thanks for exploring.\n";
}
