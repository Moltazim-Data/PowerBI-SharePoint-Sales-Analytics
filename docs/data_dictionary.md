# Data dictionary

One row represents one synthetic sales opportunity.

| Field | Type | Meaning | Notes |
|---|---|---|---|
| OpportunityID | Text | Unique opportunity identifier | Expected unique and nonblank |
| CreatedDate | Date | Date opportunity entered the pipeline | Used for cohort/trend analysis |
| CloseDate | Date / blank | Date opportunity closed | Blank for open deals |
| Stage | Text | Current or final sales stage | Closed Won and Closed Lost count as closed |
| Segment | Text | Customer-size segment | SMB, Mid-Market, Enterprise |
| LeadSource | Text | Channel that sourced the opportunity | Synthetic categories |
| Region | Text | Sales territory | Synthetic regions |
| SalesRep | Text | Opportunity owner | Fictional names |
| AmountEUR | Decimal | Opportunity amount in euros | Won amount is a proxy, not accounting revenue |
| DealType | Text | New Business, Expansion, or Renewal | Synthetic categories |

## Data quality expectations
- `OpportunityID` should be unique and nonblank.
- `CreatedDate` should be populated.
- `CloseDate` should be populated only for closed opportunities in this sample.
- `AmountEUR` should be numeric and nonnegative.
- All data is fictional, created for demonstration and practice.
