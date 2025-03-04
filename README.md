# Sentiment Analysis Report: Yelp Reviews

---

## 1. Introduction

This report presents the findings from a sentiment analysis conducted on a dataset of Yelp reviews. The dataset contains customer reviews collected over several years, including star ratings, review text, and review dates.

### Objective

The aim of this analysis is to understand the overall sentiment expressed by customers and track weekly sentiment trends over time. This analysis helps businesses identify periods of high customer dissatisfaction, spot seasonal patterns, and derive actionable insights to enhance customer satisfaction.

---

## 2. Data Overview

- **Total Reviews:** 10,000
- **Date Range Covered:** 2005-04-18 to 2013-01-05

### Star Rating Distribution

| Stars | Count |
|---|---|
| 1 | 840 |
| 2 | 836 |
| 3 | 1461 |
| 4 | 2458 |
| 5 | 5405 |

---

## 3. Sentiment Classification

### Classification Logic

| Star Rating | Sentiment |
|---|---|
| 4 - 5 | Positive |
| 3 | Neutral |
| 1 - 2 | Negative |

### Sentiment Summary Table

| Sentiment | Count | Percentage |
|---|---|---|
| Positive | 6863 | 68.63% |
| Negative | 1676 | 16.76% |
| Neutral | 1461 | 14.61% |

---

## 4. Sentiment Trend Analysis

### Trend Methodology

- Reviews are aggregated **weekly** based on the review date.
- A **4-week moving average** is applied to smoothen short-term fluctuations.
- The trend plot visualizes the proportion of each sentiment over time.

### Trend Visualization

The following plot captures the weekly sentiment trend over time:

![Weekly Sentiment Trend](../images/weekly_sentiment_trend.png)

---

## 5. Key Insights

- **Positive Sentiment Dominates:** Approximately 69% of the reviews express positive sentiment, indicating overall customer satisfaction.
- **Noticeable Negative Spikes:** Certain weeks show sudden increases in negative sentiment, which may correspond to service issues or external factors.
- **Neutral Sentiment Consistent:** Neutral reviews hover around 14-15% steadily.
- **Seasonal Variation:** Some dips in positive sentiment are visible around certain time periods, possibly related to seasonal demand fluctuations or operational challenges.

---

## 6. Preprocessing & Exploratory Insights (Appendix)

### Word Cloud

A word cloud was created to visualize the most frequent words in the reviews.

![Word Cloud](../images/word_cloud.png)

### Review Length Distribution

(To be added later if required)

### Common Bigrams

(To be added later if required)

---

## 7. Conclusion & Recommendations

### Summary

- The overall sentiment health of the business is **positive**.
- However, periodic spikes in **negative sentiment** need further investigation to understand root causes.

### Recommendations

- Conduct deeper analysis during periods of high negative reviews to identify specific operational or service issues.
- Implement a **review response strategy** to address negative reviews promptly and improve perception.
- Consider **text topic modeling** to uncover common themes or complaints within negative reviews.
- Explore segmentation analysis (e.g., sentiment by location or time of day) for finer insights.

---

### Future Work

- Extend analysis by incorporating **text sentiment analysis using NLP** rather than just star-based classification.
- Compare sentiment trends with **external factors** like promotions, events, or competitor actions.
- Build an **automated sentiment monitoring dashboard** for real-time insights.

---

## Final Note

This report is part of the comprehensive 'Yelp Sentiment Analysis' project, aimed at equipping businesses with actionable insights from customer feedback.

---

