# Course
- IST 340: Knowledge Discovery and Data Mining (Claremont Graduate University)
# Data Mining Project 
- A Data-Driven Approach to Evaluating Risk Factors of Student Loan Borrowers
## Project Statement
- In an effort to fulfill the expressly desired outcomes of maximizing financial gain from student loan borrowers and improving related decision-making, an effective predictive model must be developed as a data-driven solution to continuously pinpoint and differentiate between students who are good or bad loan risks based on their given characteristics and histories.
## Target Event
- '*NoPaymentDue*' = 'pos'
- The target variable classifies whether or not a given student is behind on their loan payments after one calendar year that they were supposed to start paying, in which 'pos' represents the latter.
## Data Mining Project Team Members
- Mark Villamayor
- Shengyu Zhang
## Tentative Evaluation Matrix
- Average Profit/Accuracy
    - Weight: 45%
    - Threshold: >(0.60)
- Simplicity
    - Maximum Range: 3-9 Rules
        - Ideal Range: 4-6 Rules
    - Weight: 30%
    - Threshold: >(0)
- Lift
    - Weight: 15%
    - Threshold: >(0.30)
- Stability
    - Weight: 10%
    - Threshold: >(0)
- Overall Score = 0.45xScore_AverageProfit/Accuracy + 0.30xScore_Simplicity + 0.15xScore_Lift + 0.10xScore_Stability