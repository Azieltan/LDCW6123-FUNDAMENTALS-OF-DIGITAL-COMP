#include <cstdlib>
#include <iostream>
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

int main() {
    std::cout << "MUSIC DISCOVERY ASSISTANT\n"
              << "An offline, rule-based demonstration of digital music discovery.\n"
              << "Every track and artist is fictional; no account or internet is needed.\n";

    std::cout << "\nGenre: 1 Pop  2 Electronic  3 Acoustic\n";
    std::cout << "Choose genre (1-3): ";
    int genre = 1;
    std::cin >> genre;

    std::cout << "Mood: 1 Calm  2 Energetic  3 Reflective\n";
    std::cout << "Choose mood (1-3): ";
    int mood = 1;
    std::cin >> mood;

    std::cout << "Length: 1 Up to 4 min  2 Over 4 min: ";
    int length = 1;
    std::cin >> length;

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

    if (best == nullptr) {
        std::cout << "No tracks are available in this genre.\n";
        return 0;
    }

    std::cout << "\nRecommendation: " << best->title << " by " << best->artist
              << " (" << best->minutes << " min)\n"
              << best->description << "\n"
              << "Why: It matches your " << genres[genre - 1] << " choice";
    if (best->mood == moods[mood - 1]) std::cout << ", " << moods[mood - 1] << " mood";
    if ((best->minutes <= 4) == (length == 1)) std::cout << ", and length preference";
    std::cout << ".\n";

    std::cout << "Thanks for exploring.\n";
    return 0;
}
