REFERENCES = [
('Arnett, T., & Young, K. (2024, July 26).','Taking K-12 education transformation from pipe dream to pipeline.','Christensen Institute.','https://www.christenseninstitute.org/blog/taking-k-12-education-transformation-from-pipe-dream-to-pipeline/'),
('Christensen Institute. (n.d.).','Disruptive innovation theory.','','https://www.christenseninstitute.org/theory/disruptive-innovation/'),
('Christensen Institute. (2025, September 24).','What is disruptive innovation? [Video].','','https://www.christenseninstitute.org/video/what-is-disruptive-innovation/'),
('Hogg, A. S. (2026, March 18).',"No, disruption isn't a strategy.",'Christensen Institute.','https://www.christenseninstitute.org/blog/no-disruption-isnt-a-strategy/'),
('Netflix, Inc. (2002a, May 22).','Netflix announces initial public offering.','','https://ir.netflix.net/investor-news-and-events/financial-releases/press-release-details/2002/Netflix-Announces-Initial-Public-Offering/default.aspx'),
('Netflix, Inc. (2002b, June 20).','Netflix announces opening of 10 regional distribution centers.','','https://ir.netflix.net/investor-news-and-events/financial-releases/press-release-details/2002/Netflix-Announces-Opening-of-10-Regional-Distribution-Centers/default.aspx'),
('Netflix, Inc. (2002c, March 6).','Netflix files registration statement for initial public offering.','','https://ir.netflix.net/investor-news-and-events/financial-releases/press-release-details/2002/Netflix-Files-Registration-Statement-for-Initial-Public-Offering/default.aspx'),
('Netflix, Inc. (2003).','Annual report on Form 10-K for the fiscal year ended December 31, 2002.','U.S. Securities and Exchange Commission.','https://www.sec.gov/Archives/edgar/data/1065280/000095016803001155/d10k.htm'),
('Netflix, Inc. (2019).','Annual report on Form 10-K for the fiscal year ended December 31, 2018.','','https://s22.q4cdn.com/959853165/files/doc_financials/annual_reports/2018/Form-10K_Q418_Filed.pdf'),
('Sarandos, T. (2023, April 18).','Netflix DVD - The final season.','Netflix.','https://about.netflix.com/en/news/netflix-dvd-the-final-season'),
]

MODEL = [
('Scope and model', 'This report examines Netflix\'s original online DVD-by-mail service relative to physical video-rental stores, especially Blockbuster. The question is how a service that initially required waiting could attract customers and become a wider competitive alternative. Christensen\'s disruptive innovation model is appropriate because the explanation follows a changing competitive process, rather than treating a new technology as automatically disruptive (Hogg, 2026).'),
('Foothold and customers', 'The relevant early foothold includes people outside convenient rental-store locations who accepted postal delivery in return for access to a broad catalogue (Christensen Institute, n.d.). This project interprets those preferences as a trade-off between immediacy and access. It does not assume that every early customer was a low-income consumer, a nonconsumer or uninterested in film quality. The claim is specific to the customer needs and performance dimension being compared.'),
('Performance and customer mapping', 'The poster uses immediacy of film access as its conventional performance indicator. Higher on the vertical axis means less waiting before viewing. Store rental offered same-day pickup when the film was available; early mail rental required delivery. The early customer label identifies people willing to accept a delay, while the mainstream label identifies viewers seeking same-day access. The lines are a qualitative schematic, not measured scores or a statistical market forecast. They illustrate the performance trade-off and later improvement without implying that catalogue breadth, price and viewing experience are identical.'),
('Technological and commercial enablers', 'Disruptive innovation depends on enabling technology, a business model and a supporting value network (Christensen Institute, 2025). Applied here, the web catalogue, postal service and distribution facilities supported a subscription alternative to a retail-store network. The interpretation concerns how the service was delivered and sustained, alongside the technology used.'),
]

IMPACT = [
('Historical development', 'Netflix launched its online DVD-rental service in 1998 (Netflix, Inc., 2002a). Its subscription service began in September 1999 (Netflix, Inc., 2003). In June 2002, it announced ten regional distribution centres intended to reduce delivery times (Netflix, Inc., 2002b). A March 2002 company announcement describes CineMatch support for title selection (Netflix, Inc., 2002c). Netflix introduced streaming in 2007 (Netflix, Inc., 2019). Blockbuster\'s 2010 bankruptcy marks an important incumbent outcome (Christensen Institute, n.d.). In April 2023, Netflix announced that its last DVD shipments would be on September 29, 2023 (Sarandos, 2023).'),
('Improvement and mainstream competition', 'Faster delivery reduced the initial waiting disadvantage. Streaming later changed the access method for supported titles and connected viewers. These developments help explain the move toward broader competition on convenience. The graph treats 2007 as a change in delivery capability, not proof that all customers switched immediately or that every Netflix feature was separately disruptive.'),
('Social impact and trade-offs', 'Home ordering offered an alternative to travelling to a store. A larger accessible catalogue could serve viewers with fewer convenient local options (Christensen Institute, n.d.). The benefit depended on what the viewer valued. Postal delivery still required waiting, while streaming introduced dependence on connectivity and available content. Early streaming also had catalogue limitations; some customers valued the social experience of visiting stores (Arnett & Young, 2024).'),
('Critical interpretation', 'The case supports a model of changing customer access and competition. It does not establish that Netflix alone caused Blockbuster\'s bankruptcy or that the conceptual graph measures market share. Using one performance indicator makes the trade-off clear but cannot represent every dimension of a rental service. Historical outcome and model interpretation should therefore remain distinct.'),
('Connection to Part 2', 'Netflix\'s early service included title-selection assistance (Netflix, Inc., 2002c). The C++ programme illustrates this catalogue-discovery benefit through explicit preference rules. Its fictional catalogue and fixed weights make the decision process explainable. It does not recreate CineMatch, operate a streaming service or use Netflix data.'),
]

DESIGN = [
('Purpose and integration', 'The Movie Discovery Assistant recommends a fictional film based on genre, mood and preferred duration. It illustrates one customer-facing function associated with a searchable online catalogue: finding a title suited to a user\'s preferences. It runs offline without login or subscriber information.'),
('Inputs and outputs', 'Genre choices are Sci-Fi, Comedy and Drama. Mood choices are Relaxed, Exciting and Thoughtful. Duration choices are up to 100 minutes and over 100 minutes. The output contains the selected film\'s title, duration, description and the preferences it actually matches. A repeat menu lets the user search again or exit.'),
('Selection rule', 'Genre is a required filter. Within that genre, a mood match adds two points and a duration match adds one point. The highest-scoring film wins; equal scores retain the first title in catalogue order. Mood therefore has priority over duration. A fallback stays within the selected genre and never claims an unmatched preference. A guard handles the absence of titles if the catalogue is later changed.'),
('Input handling and implementation', 'C++17 is used with a Movie structure, a vector of records and a reusable readChoice function. getline reads the entire input. An istringstream parses a bounded integer and checks for trailing non-whitespace characters. Text, decimals, blank input, overflow and out-of-range entries are rejected. End-of-input exits cleanly. The programme uses conditional statements and loops to produce its recommendation.'),
('Limitations', 'The catalogue contains 12 fictional titles. Weights are manually chosen and do not learn from preferences or ratings. No user-effectiveness evaluation, account features, persistence or external catalogue integration is included. The automated tests verify expected programme behaviour, rather than the real-world usefulness of recommendations.'),
]

TOC = [
('Assessment coversheet and six member declarations','1-7'),
('Part 1 Innovation life cycle poster','9'),
('Part 1 Model application','10'),
('Part 1 History impact and critical analysis','11'),
('Part 1 APA references','12-13'),
('Part 2 Programme design','14'),
('Part 2 Code captures','15-16'),
('Part 2 Actual programme runs','17'),
('Part 2 Testing and results','18'),
('Part 2 Git development record','19'),
('Presentation links and assistance disclosure','20'),
]
