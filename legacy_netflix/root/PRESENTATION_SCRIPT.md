# Group 13 Presentation Script

LDCW6123 Fundamentals of Digital Competence for Programmer, Trimester 2620.

Topic: Netflix Innovation Life Cycle and Movie Discovery Assistant.

This is a suggested six-person allocation, not a statement of completed contributions. Rehearse before recording. Aim for 14-16 minutes including the live programme demonstration, and keep the actual recording at or below 18 minutes. Stage directions in square brackets are not spoken. Use the final report, A3 poster, terminal and source code on screen. Speak the scripts in your own natural voice after understanding them.

## 1 Aziel Tan Zheng Chuan — Introduction — about 1 minute 30 seconds

[Show the report title and member names.]

Good day, Mr. Segaran. We are Group 13. I am Aziel Tan Zheng Chuan, the group leader. Our members are See Wing Kit, Soo Kian Rong, Vincent Lock Chun Kit, Wong Kee Yuan and Ho Ming Hao.

Our project is about Netflix and the development of its movie-rental service. There are two connected parts. Part 1 uses Christensen's disruptive innovation model to examine Netflix in relation to physical video-rental stores, especially Blockbuster. Part 2 is a simple interactive movie discovery programme written in C++.

We focus first on Netflix's DVD-by-mail service. This is important because Netflix did not enter the market as the streaming platform we know today. Customers originally selected DVDs online and waited for delivery. Streaming was introduced later.

Our main question is how a service with a disadvantage in immediate access could still attract customers and eventually compete more widely. The poster maps the change over time. The programme demonstrates a related customer benefit: helping someone find a title using their preferences.

The programme has a small fictional catalogue, so it can run without an account or internet connection. It is a learning demonstration rather than Netflix's real recommendation system.

I will now pass to See Wing Kit to explain the model and the performance graph.

## 2 See Wing Kit — Model and customer mapping — about 2 minutes

[Show the poster's graph and customer labels.]

Christensen's model explains a competitive process. A new service can begin outside an incumbent's main priorities, gain an initial foothold, and improve until it becomes attractive to a wider market. A successful new product is not automatically disruptive. We need to identify the incumbent, the early customers, the original trade-off and the process of improvement.

In this project, the incumbent is the physical video-rental store. The entrant is Netflix's online DVD-by-mail service. The market being examined is home video rental, rather than the whole entertainment industry.

The performance indicator on our vertical axis is convenience of film access. Here, convenience means less waiting and effort to obtain a film. Historical years appear on the horizontal axis. The arrows form a conceptual comparison, without measured performance scores or market-share data.

The established store service offered same-day pickup if a title was available. Netflix's early postal service involved waiting. Its offer could still appeal to people who accepted the delay in exchange for home ordering and access to a broad catalogue. People outside convenient store locations were another relevant customer group.

The yellow arrow represents the established store-rental trajectory. The green arrow represents Netflix's emerging trajectory. The blue callout identifies the new competitive path based on home ordering and postal delivery. Netflix later added streaming. The two dashed lines show customer-demand levels, rather than company performance.

The high-end label identifies mainstream customers seeking immediate access. The low-end label identifies customers willing to wait, including those outside convenient store locations. These labels concern demand for immediate access. We make no claim about their income or film knowledge.

Netflix's delivery improvements and streaming reduced the waiting disadvantage and supported wider appeal. The slopes and crossings are illustrative. They do not identify an exact takeover date. Catalogue availability and internet access still affected the viewing experience.

The main interpretation is that the delivery system and business model changed together. Soo Kian Rong will now explain the evidence behind the timeline.

## 3 Soo Kian Rong — Historical milestones and impact — about 2 minutes

[Point to each milestone on the poster.]

The timeline begins in 1998, when Netflix launched its online DVD rental service. In September 1999, it introduced the subscription service. These are separate milestones. We should not place the subscription launch in 1998.

In 2002, Netflix announced ten regional distribution centres. The purpose was to shorten delivery times. Company records from that period also describe recommendation support, including CineMatch. These developments helped people receive and discover titles, although customers still depended on postal delivery.

Netflix introduced streaming in 2007. This allowed online viewing instead of waiting for a DVD, when the viewer had the necessary internet connection and the title was available. We treat this as a later development in the Netflix case, rather than its original entry.

Blockbuster filed for bankruptcy in 2010. This is an important industry outcome, but our report does not claim that one Netflix feature alone caused it. Netflix's DVD service ended in 2023; its announced final shipment date was September 29. That last event marks the end of the postal service and is not, by itself, evidence of the original disruption.

The social impact concerns convenience and access. Home ordering offered an alternative to travelling to a rental store. A broad catalogue could help viewers find titles beyond the selection in a nearby shop. Later, streaming changed the delivery experience again.

There were also trade-offs. Postal users waited for delivery. Streaming depended on a reliable internet connection and available content. Some people valued the experience of browsing a store. These differences make the impact more complex than saying every customer benefited equally.

The references include Netflix company announcements, annual reports and explanations from the Christensen Institute. Full details are in the report and on the poster. Vincent will now explain how Part 2 connects to this case.

## 4 Vincent Lock Chun Kit — Programme design and logic — about 2 minutes 30 seconds

[Show src/main.cpp, the Movie structure, catalogue and scoring loop.]

Part 2 is called the Movie Discovery Assistant. Its purpose is to help a user choose a fictional film from a small catalogue. The connection with Netflix is online catalogue discovery. We use this one feature as inspiration, rather than trying to copy the full Netflix platform.

The programme asks for three inputs: genre, mood and preferred duration. Genre options are science fiction, comedy and drama. Mood options are relaxed, exciting and thoughtful. Duration can be up to one hundred minutes, or over one hundred minutes.

Each movie record stores a title, genre, mood, running time and description. These records are held in a vector. The programme first considers only movies in the selected genre, so genre is a required match.

It then applies a simple score. A matching mood adds two points. A matching duration adds one point. Therefore mood has priority over duration. The movie with the highest score becomes the recommendation. If two titles have the same score, the first one in catalogue order is selected. That makes the result predictable.

The output displays the title, running time, a short description and a reason. The reason only mentions preferences that the selected movie actually matches. If there is no exact match for mood or duration, the programme still recommends a title in the selected genre.

For example, choosing drama, exciting and a short duration returns Night Shift. It matches the genre and mood, but its running time is over one hundred minutes. The programme explains the mood match without claiming that the duration preference was met.

There is also a check for an empty result if a genre is removed from a future catalogue. After each search, the user can choose another recommendation or exit.

This is a rule-based programme. It does not learn from ratings, viewing history or other subscribers. Wong Kee Yuan will now demonstrate the inputs and the improved validation.

## 5 Wong Kee Yuan — Live demonstration and validation — about 3 minutes

[Open a terminal in the project directory. Compile and run. Keep the typed inputs visible.]

I will first compile the programme using C++17. The command also enables compiler warnings.

[Run: g++ -std=c++17 -Wall -Wextra -pedantic src/main.cpp -o movie_assistant. Then run ./movie_assistant. On Windows use the README's .exe command.]

For the first example, I choose comedy, relaxed and over one hundred minutes.

[Enter 2, then 1, then 2. Pause to show the result.]

The result is Coffee and Clouds, with a running time of one hundred and eighteen minutes. It matches the selected genre, mood and duration. The reason shown by the programme confirms those matches.

I choose to search again. This time I will demonstrate invalid input.

[Enter 1 at Find another. At the genre menu enter 1abc, then 1.5, then 1.]

Both entries are rejected. The programme asks for a whole number. An earlier version accepted the numeric beginning of entries such as these. The revised version reads the complete input line and checks that there is no extra non-whitespace character after the number.

For the valid second example, I choose science fiction, thoughtful and up to one hundred minutes.

[After genre 1, enter mood 3 and duration 1.]

The result is Orbit Station, at ninety-six minutes. I will now exit.

[Enter 2 at Find another. Restart the programme.]

The final example demonstrates the priority rule. I choose drama, exciting and up to one hundred minutes.

[Enter 3, then 2, then 1.]

The result is Night Shift at one hundred and nine minutes. It matches mood and genre, but the duration is longer than requested. The output does not falsely claim a duration match. This is expected because the mood score is higher than the duration score.

[Enter 2 to exit. Show readChoice in the source file.]

The input function also rejects blank entries and numbers outside the menu range. If the input stream ends, the programme prints a goodbye message and stops. These behaviours help a user recover from an error without restarting the programme. Ho Ming Hao will now explain the tests, Git record and limitations.

## 6 Ho Ming Hao — Testing, Git and conclusion — about 2 minutes 30 seconds

[Run sh test.sh, or the Windows test commands. Show test_results.csv and the current Git log.]

The supplied automated test run passed thirty-five checks. Eighteen checks cover every genre, mood and duration combination. Eight checks cover invalid entries, including text, decimals, trailing letters, blank input and a very large number. Four checks cover input ending at different menus.

The remaining checks cover repeated recommendations, surrounding spaces, invalid entries at the duration and repeat menus, fallback explanations and the priority of mood over duration. The CSV records the input, expected result, actual result and pass status. We can run the same tests again after making a change.

The programme-output screenshots and transcript were regenerated from the compiled version. The code evidence includes both input validation and the main scoring logic, so the report shows more than the catalogue alone.

Git is used to keep the actual preparation history. The command is git log with the oneline and graph options. The report also explains an important limitation: the existing commits identify AI-assisted preparation and revision. They must not be presented as proof that a named student wrote those changes. Group contributions should be recorded through genuine review, changes and commits.

Our analysis has limitations too. The performance graph is conceptual, and the case does not prove that Netflix alone caused every change in the rental market. For the programme, the catalogue is small and fictional. The scoring weights were chosen for a simple demonstration. We have not measured whether users find these recommendations useful, and the programme has no learning algorithm, account system or persistent storage.

The project connects a historical innovation case with an interactive digital example. The poster shows the relationship between early customer needs, performance trade-offs and later improvement. The programme shows how preference inputs can help someone discover a title, while making its decision rules clear.

Thank you for watching our presentation.

## Recording checks

- Replace this suggested allocation if the group agrees on different speaking roles.
- Each speaker should review their section and describe only work or demonstrations they can explain.
- Re-run the programme and tests during rehearsal. Do not claim that the group completed a review before doing it.
- Show a real current Git log after the group adds any genuine contributions.
- Check audio, readable screen sharing and total runtime before uploading the real MP4/MOV/MPEG recording to OneDrive.
- Add an accessible video link and source/Git link to the report. No recording is included in the supplied package.
