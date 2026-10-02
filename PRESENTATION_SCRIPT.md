# Spotify and Physical Music Group Presentation

Suggested order and timing: about 14 minutes, including live programme demonstration and transitions. Every speaker should check the facts, adjust the wording to reflect their own understanding, and rehearse. The recording must stay under 18 minutes.

## Aziel Tan Zheng Chuan  Case and thesis  1 minute 40 seconds

Hello. We are Group 13. Our Part 1 asks how Spotify’s on-demand music streaming can be mapped onto Clayton Christensen’s disruptive innovation model when the established option is buying music on CD. The comparison is deliberately narrow: our vertical axis means fidelity of the delivered digital audio signal. It is not a chart of subscribers, music sales, overall convenience or how much people enjoy a song.

A standard CD gives a lossless digital signal. Spotify offered an alternative attraction: a listener could search a licensed catalogue and play music without purchasing a separate disc for each album. Some people were willing to accept compressed audio for that immediate access. We will show how the lecturer’s two technology trajectories and two customer-demand levels represent this trade-off. We also separate historical evidence from our model interpretation. The market shift involved other services and digital formats, so we are not claiming that Spotify alone ended the CD market. Part 2 is a small offline C++ Music Discovery Assistant that illustrates catalogue search with transparent rules, not Spotify’s real recommendation system.

## See Wing Kit  Clayton graph and customers  2 minutes 20 seconds

Please look at the central graph on the A3 poster. It follows the template in our Topic 6A slides. Time, with actual years, runs from left to right. Performance rises vertically, and we have explicitly defined it as delivered digital audio fidelity. The upper yellow arrow represents CDs as the established option. We kept this line almost level because CD’s 16-bit and 44.1-kilohertz format did not keep increasing in resolution. Making it a steep line would look more like the generic diagram but would be historically misleading.

The green Spotify line begins below the yellow one because early streaming used compressed audio. Its later rise ends with the Premium Lossless option introduced in 2025, for supported songs, plans, devices and markets. The red dashed line represents listeners with a high demand for lossless fidelity. The purple line stands for listeners willing to accept a lower conventional signal standard. That description concerns what they value, not whether they have a low income.

The blue curved callout stands for a different source of value: immediate catalogue access and discovery. It is not secretly a second vertical metric. The green line’s crossing of the purple line is only a conceptual good-enough threshold. We have not measured its exact date. The 2017 marker at the bottom is an industry revenue event. It does not say Spotify’s signal equalled CD quality in 2017. The graph therefore makes the lecturer’s model recognisable while keeping its limitations visible.

## Soo Kian Rong  History and market impact  2 minutes 15 seconds

Spotify’s own chronology dates its launch in six European markets to October 2008 and its mobile expansion to September 2009. It added a free mobile experience in 2013 and Discover Weekly in 2015. These are service milestones. For the broader market, IFPI reported that streaming became the largest individual source of global recorded-music revenue in 2017, accounting for 38.4 percent. That number combines streaming services; it is not Spotify’s market share.

In September 2025 Spotify announced a lossless Premium option, up to 24-bit and 44.1-kilohertz FLAC in selected markets. This was long after streaming had become a major commercial format. That timing matters: many users chose digital access despite a conventional fidelity trade-off. They valued discovery, portability or not having to buy individual CDs.

The change affected distribution and payment too. Recorded music increasingly reached listeners through licensed platforms and subscription or advertising income. But physical formats did not disappear. IFPI reports that physical-format revenue grew by eight percent in 2025, with vinyl helping drive the result. A purchased CD also gives a form of possession that a streaming account does not. Our conclusion is that the model helps explain one competitive path; the evidence does not isolate Spotify as the only cause of the industry’s change.

## Vincent Lock Chun Kit  Programme design  2 minutes 25 seconds

For Part 2, we built a Music Discovery Assistant in C++17. Its purpose is to show a modest catalogue-discovery feature connected to the poster’s alternative value. It works offline and uses 12 fictional tracks and artists, so it needs no Spotify account, API, internet access or proprietary algorithm.

The user enters three choices: Pop, Electronic or Acoustic; Calm, Energetic or Reflective; and a track lasting up to four minutes or longer. The programme first filters by genre. Within that genre a mood match receives two points and a length match receives one point. The highest score wins, while an equal score keeps the earlier track in catalogue order. This deterministic tie rule means repeated inputs give the same recommendation.

The title, artist, minutes and description are shown with a reason listing only preferences actually matched. If no track matches the requested mood, the programme will not falsely say that it did. The readChoice function accepts one whole line and rejects text, decimals, blank lines, numbers outside the menu and trailing characters such as 1abc. It also exits cleanly at end-of-file. If someone later edits the catalogue and accidentally removes a genre, the missing-result guard prints a safe message instead of using a null pointer. These are simple, explainable classroom rules, not a claim to recreate Spotify.

## Wong Kee Yuan  Live demonstration  3 minutes

I will run the compiled programme. I choose Electronic, Calm and over four minutes. The result is the fictional track Slow Orbit by Rin Echo, six minutes long. Its explanation correctly lists the Electronic genre, Calm mood and length preference. I then choose to search again, enter Pop, Reflective and up to four minutes, and receive City Lanterns by Mira Vale. Notice that the reason includes Pop and length but does not pretend the Calm track matches the requested Reflective mood.

Now I enter 1abc in the genre menu. The programme does not accept the numeric prefix: it asks for a whole number from one to three. A decimal such as 1.5 is rejected for the same reason. After a valid entry it continues without losing track of the next question. I can finish by choosing No, or an ended input stream exits cleanly.

These are real terminal captures from the compiled C++ source. The report includes the source extract for validation and scoring, the interactive output screenshot and a separate invalid-input screenshot. Because the data are invented, no listener history or external songs are accessed. The demonstration illustrates how a searchable digital catalogue can help someone find music, while the Clayton analysis concerns the broader historical market.

## Ho Ming Hao  Testing, limitations and closing  2 minutes 30 seconds

We compiled with the C++17 standard and warning flags. The Python test driver then launched the compiled programme 35 times with explicit inputs and expected outputs: all 18 preference combinations, eight invalid entries, four end-of-input positions, plus repeat, whitespace, menu bounds, fallback and mood-priority scenarios. All 35 passed. The full CSV is generated by the test script after actual executions, rather than being a manually marked table. These tests check whether the rule behaves as designed; they do not establish that its recommendations are useful to real listeners.

The Git screenshot and portable bundle preserve genuine development history. The prior Netflix work remains visible because this project changed case studies. Later revisions are marked as AI-assisted, and the history does not claim that a particular student made a commit they did not make. Each group member still needs to review, contribute and declare their own real work before submission.

Our model also has limits. A CD’s technical digital format is fixed, so the yellow trajectory is nearly level. The good-enough threshold is conceptual, and consumer choices involve more than audio fidelity. Streaming’s 2017 revenue lead preceded Spotify’s 2025 lossless option, which makes the different value proposition central to our interpretation. Other services and business decisions affected the market, and physical music survives. Thank you.
