"""Fact-checked report text and full human-readable references."""

REFERENCES = [
('Christensen Institute. (n.d.).', 'Disruptive innovation theory.', '', 'https://www.christenseninstitute.org/theory/disruptive-innovation/'),
('International Federation of the Phonographic Industry. (2018).', 'IFPI global music report 2018.', '', 'https://www.ifpi.org/ifpi-global-music-report-2018/'),
('International Federation of the Phonographic Industry. (2026, March 18).', 'Global music report 2026: Global recorded music revenues grow 6.4% as record companies drive innovation.', '', 'https://www.ifpi.org/global-music-report-2026-global-recorded-music-revenues-grow-6-4-as-record-companies-drive-innovation/'),
('Multimedia University. (n.d.).', 'Digital convergence and emerging innovative problem solving through: Topic 6A [Lecture slides].', 'LDCW6123.', ''),
('Sony. (n.d.).', 'A quick guide in understanding digital audio.', '', 'https://www.sony.com/electronics/support/articles/00165079'),
('Spotify. (2019, May 24).', 'How to download and listen to music and podcasts - offline and on the go.', '', 'https://newsroom.spotify.com/2019-05-24/how-to-download-and-listen-to-music-and-podcasts-offline-and-on-the-go/'),
('Spotify. (2025, September 10).', 'Lossless listening arrives on Spotify Premium with a richer, more detailed listening experience.', '', 'https://newsroom.spotify.com/2025-09-10/lossless-listening-arrives-on-spotify-premium-with-a-richer-more-detailed-listening-experience/'),
('Spotify. (n.d.).', 'Spotify: A visual history.', '', 'https://newsroom.spotify.com/spotify-timeline/'),
]

MODEL = [
('Scope and model', 'The incumbent is purchased compact discs (CDs) within the physical recorded-music market. The entrant is Spotify’s licensed on-demand streaming service, launched in six European countries in October 2008 (Spotify, n.d.). Christensen’s model asks whether an entrant first satisfies less demanding or overlooked users on a conventional performance dimension while offering another form of value, then becomes more capable over time (Christensen Institute, n.d.). This poster applies that test to streaming; it does not equate any new digital service with a proven low-end disruption.'),
('Foothold and customers', 'A CD listener seeking an owned, lossless digital recording has a higher fidelity requirement. A less demanding listener may accept compressed streaming when convenient search and access to many licensed tracks matter more than ownership or maximum fidelity. “Low-end” here refers to the tolerance for a lower level on this particular metric, not to a person’s income. Spotify’s free and subscription options illustrate a different way to access music, although the early market also included other digital alternatives.'),
('Performance and customer mapping', 'The graph’s single vertical metric is the fidelity of the delivered digital music signal relative to a lossless source under suitable playback conditions. Sony identifies standard CD audio as 16-bit/44.1 kHz. Earlier Spotify streaming used compressed audio; Spotify announced a Premium lossless option with up to 24-bit/44.1 kHz FLAC in September 2025 (Sony, n.d.; Spotify, 2025). The yellow CD path is almost level because the CD format did not continuously gain bit depth. The green path begins lower, crosses a conceptual good-enough threshold for compression-tolerant listeners and ends at a supported lossless option. Arrow slopes and threshold crossings are schematic, not measured scores or dated parity observations.'),
('A second, distinct value', 'The template’s blue curved callout is not another vertical scale. It denotes Spotify’s alternative attraction: on-demand catalogue access, instant search and later discovery tools such as Discover Weekly, which Spotify dates to 2015 (Spotify, n.d.). Listening without owning each disc reduced a purchase and storage barrier. This benefit explains why a user might choose an entrant whose conventional audio fidelity was initially lower.'),
('Technology and business model', 'Licensing and digital distribution allowed one service to supply on-demand tracks across devices; mobile access followed in 2009, according to Spotify’s chronology. The free tier and paid Premium offered different access and quality options. The commercial arrangement differs from selling a permanently owned CD. These differences connect the technology, the business model and the audience’s trade-off (Spotify, n.d.; Christensen Institute, n.d.).'),
]

IMPACT = [
('Verified timeline', 'Spotify launched in October 2008, went mobile in September 2009, introduced a free mobile experience in 2013 and launched Discover Weekly in 2015 (Spotify, n.d.). IFPI reported that streaming became the largest single source of global recorded-music revenue in 2017, accounting for 38.4% of the total. That figure combines streaming services and is not a Spotify market-share statistic (IFPI, 2018). Spotify began rolling out Premium Lossless in September 2025 in selected markets (Spotify, 2025).'),
('Interpreting the performance path', 'Early compressed playback was below a CD’s lossless digital format on this narrowly defined metric. The conceptual lower demand line denotes listeners for whom streaming quality was adequate even before lossless parity. By 2017, streaming as a format led global recorded-music revenue despite the absence of a Spotify lossless tier; therefore its market success cannot be explained by audio parity alone. The green endpoint marks a later improvement available to eligible Premium listeners, not a claim that every stream, device or track is lossless (IFPI, 2018; Spotify, 2025).'),
('Access, revenue and social impact', 'Digital access shifted listening from purchasing specific physical albums towards searching a licensed catalogue and paying through subscriptions or advertising. Portability, recommendations and immediate discovery could benefit listeners with little storage or an inconvenient retail option. IFPI reported total streaming at 69.6% of global recorded-music revenue in 2025, while physical formats also grew by 8.0%. These are industry-wide format outcomes, not evidence that Spotify alone caused CD decline or that physical media vanished (IFPI, 2026).'),
('Costs and limits', 'A purchased CD can be kept and played with compatible equipment without renewing a streaming subscription; licensed streaming is tied to available tracks, devices and service terms. Spotify Premium offers downloads for offline listening, but this still differs from owning a disc (Spotify, 2019). The quality comparison depends on encoding, plan, device and output path; Spotify specifically cautions that Bluetooth transmission may compress a lossless source (Spotify, 2025). Vinyl collectors and other physical-music buyers remain part of the market (IFPI, 2026).'),
('Critical interpretation', 'Spotify is a useful illustration of a lower conventional performance trade-off and a new access value, but a strict Christensen classification is contestable. The incumbent record companies also licensed streaming, earlier digital downloads and other services played roles, and 2017 streaming revenue does not prove the model’s mechanism. The graph is a reasoned schematic, not causal identification, fidelity test results or a market-share plot. The CD line is nearly level to preserve the real format ceiling while retaining the lecturer’s upper incumbent trajectory.'),
('Connection to Part 2', 'The offline C++ Music Discovery Assistant illustrates just one part of the new value proposition: searching a small catalogue by stated preferences. It uses fictional artists and transparent rules. It neither uses Spotify accounts or data nor reproduces Spotify’s recommendation algorithms.'),
]

DESIGN = [
('Purpose and integration', 'The Music Discovery Assistant lets a user browse 12 fictional tracks by genre, mood and preferred duration. It demonstrates the catalogue-discovery aspect of access-based music services without connecting to Spotify or an external API.'),
('Inputs and outputs', 'Genres are Pop, Electronic and Acoustic. Moods are Calm, Energetic and Reflective. A length option asks for up to four minutes or over four minutes. Output shows the fictional track title, artist, duration, description and the matched preferences. A repeat prompt allows another search.'),
('Transparent selection rule', 'Genre is a required filter. A matching mood contributes two points, and a matching length contributes one. The first track in catalogue order wins an equal score. Mood therefore outranks length. The explanation prints only matches actually achieved; an absent genre in a future edited catalogue has a safe fallback.'),
('Implementation and validation', 'C++17 uses a Track struct, a vector catalogue, loops and conditional scoring. readChoice consumes the entire line and uses istringstream to accept only one bounded integer with optional surrounding whitespace. It rejects text, decimals, trailing characters, blank input, overflow and out-of-range choices. End-of-input exits cleanly. Thirty-five black-box checks exercise 18 preference combinations and the key invalid-input, EOF, repeat and fallback cases.'),
('Limits', 'Tracks and artists are invented, the catalogue is small, and weights were chosen for a classroom demonstration. No machine learning, personalised history, account, persistence, streaming, or usability study is implemented. Tests establish deterministic behaviour, not satisfaction with the selected music.'),
]

TOC = [
('Assessment coversheet and six declarations','1–7'),
('Contents','8'),
('Part 1 Clayton model poster (A3 landscape)','9'),
('Part 1 Model application','10'),
('Part 1 History and impact','11'),
('Part 1 Tradeoffs and critical interpretation','12'),
('Part 1 References','13–14'),
('Part 2 Programme design','15'),
('Part 2 Source-code captures','16–17'),
('Part 2 Programme output and validation','18'),
('Part 2 Tests','19'),
('Part 2 Git record','20'),
('Presentation links and declaration notes','21'),
]
