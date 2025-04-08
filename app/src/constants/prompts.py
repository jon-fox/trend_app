DAILY_NEWS_PROMPT = """
### **Daily News Brief - Balanced and Unbiased Overview**

Please provide a summary of today's most important news stories with the goal of remaining as unbiased as possible. For each topic:

- Present **both a supportive and opposing perspective**.
- Focus on the topics of market, business, technology, finance, and political news. Attempt to provide news for each of these listed topics.
- Ensure international stories are covered as well when appropriate. An international story is relevant if it has a major impact on world events or is a worldwide story.
- Include **no more than 2 sources**, unless otherwise requested.
- Prioritize source diversity: avoid using two sources with the same known political or ideological leaning.
- If a source with a known bias is included, actively balance it with a credible source from the opposite viewpoint, even if it is less mainstream.
- You may include reputable independent or non-mainstream outlets if they adhere to journalistic standards (fact-based, non-sensational, attributable).
- If a source is known to have bias, **balance it** by including one from the opposite side of the spectrum.
- Ensure diversity in topics. Refrain from including multiple stories that revolve around a similar theme, unless each offers a truly distinct development or perspective.
- Technology Coverage Requirement:
-- Ensure at least one topic is focused solely on technology itself, not just the tech sector. This could include:
-- Scientific or engineering breakthroughs (e.g., quantum computing, AI models, semiconductors)
-- Emerging tech (e.g., robotics, space tech, biotech)
-- Venture capital trends, new startups, or tech founder initiatives
-- Unique applications of technology shaping industries or society
-- Business or political impacts of tech-related issues may be included in other topics, but one story must highlight technology as the core subject, independent of its financial or political implications.
- Avoid citing two sources from the same side of the political spectrum unless no alternatives are available; if necessary, explain the reason.
- Include clickable URLs for each source in markdown format. Do not leave links as placeholders.
- Format each topic as follows:

---

**Topic**
**One sentence summary of Topic**
------------------------------  

**Supportive View**  
------------------------------  
*Brief summary of the positive or supportive viewpoint.*

**Opposing View**  
------------------------------  
*Brief summary of the critical or opposing viewpoint.*

**Sources Table**  
------------------------------  
| Source | Link |  
|--------|------|  
| Outlet 1 | URL |  
| Outlet 2 | URL |  

---
"""
